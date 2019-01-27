#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
#
# git-rebase-autotags                                                                  
#
# git post-receive hook which will be called after a commit has been modified 
# by git amend or rebase command to move tags from old commit to new one

__author__ = "Benjamin Brabant"
__copyright__ = "Copyright 2017"

__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Benjamin Brabant"
__email__ = "brabant.benjamin@gmail.com"

import sys                                                                               
import subprocess                                                                        

args = sys.stdin.read().split()
commits = zip(*[iter(args)]*2)
rewrite_cmd = sys.argv[1]

try:
	stdoutput = subprocess.check_output(['git', 'config', '--get', '--bool', 'rewrite.autotags.enabled'])
	autotags = stdoutput.splitlines()[0].upper() == 'TRUE'
except subprocess.CalledProcessError:
	autotags = False

try:
	stdoutput = subprocess.check_output(['git', 'config', '--get', '--bool', 'rewrite.autotags.warnings'])
	warnings = stdoutput.splitlines()[0].upper() == 'TRUE'
except subprocess.CalledProcessError:
	warnings = True

if not autotags and warnings:
	print "\033[33mWARNING: rewrite.autotags hook configure in this repository has not been activated\033[0m"
	print "configure rewrite.autotags by running the following commands in the repository"
	print "    git config --local --add rewrite.autotags.enabled true"
	print "    git config --local push.followTags true"
	print ""
	print "to disable rewrite.autotags warning, apply the following configuration"
	print "    git config --local --add rewrite.autotags.warnings false"
	print ""



if autotags:
	print "\033[33mWARNING: rewrite.autotags activated, tags will be moved between commits during %(cmd)s\033[0m" % {"cmd": rewrite_cmd}
	print ""

	for (old, new) in commits:
		stdoutput = subprocess.check_output(['git', 'tag', '--points-at', old])
		tags = stdoutput.splitlines()

		for tag in tags:
			subprocess.call(['git', 'tag', '-f', tag, new])

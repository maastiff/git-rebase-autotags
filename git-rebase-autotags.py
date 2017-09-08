#!/usr/bin/env python                                                                    
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
 
try:
	rewrite_cmd = sys.argv[1]
	stdoutput = subprocess.check_output(['git', 'config', '--get', '--bool', 'rewrite.autotags'])
	autotags = stdoutput.splitlines()[0].upper() == 'TRUE'
except subprocess.CalledProcessError:
	autotags = False

if autotags:
	print "rewrite.autotags activated, tags will be moved between commits during %(cmd)s" % {"cmd": rewrite_cmd}

	for (old, new) in commits:
		stdoutput = subprocess.check_output(['git', 'tag', '--points-at', old])
		tags = stdoutput.splitlines()

		for tag in tags:
			subprocess.call(['git', 'tag', '-f', tag, new])

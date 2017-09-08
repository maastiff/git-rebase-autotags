git rebase autotags
===================

As explained in this [old thread](http://git.661346.n2.nabble.com/Rebase-with-tags-td5582971.html), 
git does not provide a way to move tags between commits during **amend** or **rebase**.

The provided `git-rebase-autotags.py` script is a simple **post-rewrite** git hook which will be called after a commit has been 
modified by git amend or rebase command to move tags from old commit to new one.

INSTALL
-------

### Locally in repository
You can easily install this hook in your git repository following these steps:

1. Copy `git-rebase-autotags.py` inside `.git/hooks` directory of your repository
2. Rename `git-rebase-autotags.py` as `post-rewrite` in order to be automatically executed by git
3. Make sure the hook is executable

```shell
chmod a+x .git/hooks/post-rewrite
```

### Globally on computer

You can use the git template functionnality to provide git-rebase-autotags hooks accross all your repositories.

1. Configure git templates

```
git config --global init.templatedir '~/.git-templates'
mkdir -p ~/.git-templates/hooks
```

2. Copy `git-rebase-autotags.py` inside `~/.git-templates/hooks` directory
3. Rename `git-rebase-autotags.py` as `post-rewrite`

4. Make sure the hook is executable

```shell
chmod a+x ~/.git-templates/hooks/post-rewrite
```

5. Re-initialize git in each existing repo you'd like to use this in

```shell
git init
```

> WARNING: if you already have a hook defined in your local git repo, this will not overwrite it.

CONFIGURE
---------

The autotags functionnality is disabled by default. You can easily enable it adding `rewrite.autotags = true` 
in your local or global configuration.

```shell
git config [--global] --add rewrite.autotags true
```


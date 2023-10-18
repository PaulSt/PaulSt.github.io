---
layout: post
title:  "git dark magic"
categories: debug
---

So, your git history is messed up, or you are thinking about messing it up. 
To use the dark magic of git, you pay the price of breaking the repo history, but hopefully fix something else.

My choice of book of dark spells was [git-filter-repo](https://github.com/newren/git-filter-repo)
Assume you have committed a large file. To identify the problem run
```
git filter-repo --analyze
```
which will give you a nice run down of large files in your history.
To erase a file from history run
```
  git filter-repo --invert-paths --path filename
```

In my case, I really wanted to unify the formatting of all my c++ files. 
[git-filter-repo cheat sheet](https://github.com/newren/git-filter-repo/blob/main/Documentation/converting-from-filter-branch.md#cheat-sheet-conversion-of-examples-from-the-filter-branch-manpage) to the rescue! Simply running 
```
lint-history --relevant 'return (filename.endswith(b".cpp") or filename.endswith(b".hpp"))' clang-format -style=file:.clang-format -i
```
with a .clang-format file in the root of the git repo worked like a charm (or maybe more like a hex..)

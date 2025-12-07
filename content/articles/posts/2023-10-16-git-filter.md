Title: git dark magic
Date:  2023-10-16

So, your git history is messed up, or you are thinking about messing it up. 
To use the dark magic of git, you pay the price of breaking the repo history, but hopefully fix something else.

My choice of book of dark spells was [git-filter-repo](https://github.com/newren/git-filter-repo)
Assume you have committed a large file. To identify the problem run
```bash
git filter-repo --analyze
```
which will give you a nice run down of large files in your history.
To erase a file from history run
```bash
  git filter-repo --invert-paths --path filename
```

In my case, I really wanted to unify the formatting of all my c++ files. 
[git-filter-repo cheat sheet](https://github.com/newren/git-filter-repo/blob/main/Documentation/converting-from-filter-branch.md#cheat-sheet-conversion-of-examples-from-the-filter-branch-manpage) to the rescue! Simply running 
```bash
lint-history --relevant 'return (filename.endswith(b".cpp") or filename.endswith(b".hpp"))' clang-format -style=file:.clang-format -i
```
with a .clang-format file in the root of the git repo worked like a charm (or maybe more like a hex..)


To change things from a few commits ago,
```bash
git rebase --interactive <commit ID>~
```
Please note the tilde ~ at the end of the command. In the editor change `pick` to `edit` from the commit in question.
Close the file, make the changes and then commit using
```bash
git commit --all --amend --no-edit
```
After that, return back to the previous HEAD commit using:
```bash
git rebase --continue
```
This will change the SHA-1 of that commit as well as all children, so again: it break everything!

# Notes
1. `git init` to initialize a git repository in the current directory.
2. `git status` to check what files are staged and those that aren't.
3. `git add <files>` to add the files to the staging area (`<files>` can be `.` to add all files at the current directory and subdirectories). 
4. `git commit -m <message>` to create a new commit with the currently staged files with a `message` as description.
5. `git diff <file>` to check the difference between the actual version and the latest commited version of the same file.
6. `git log` to see a list of commits in the local repository's current branch. 
7. `git remote add origin <url_to_remote.git>` to link current local git repository with a remote repository. `origin` is the name of the remote repository.
8. `git push -u origin <branch>` to push `<branch>` to remote repository and link it with the current branch in local repository.
9. `git push` to push commits to remote repository on the current branch.
10. `git rm --cached -r .` to recursively remove all the files from the current directory from the staging area's index.
11. `.gitignore` is a file with rules to determine what files to ignore when adding files to the staging area.
12. The rules in `.gitignore` can be filenames or directories and use wildcards like `*.exe`.
13. `git clone <url>` to clone the git remote repository from `<url>` into a new directory in the working directory.
14. `git merge <branch>` to merge the commits from `<branch>` into the current branch, creating a new commit with all those changes.
15. `git branch <name>` to create a branch with `<name>`
16. `git branch` to show all branches that exist in the local repository. An `*` marks the current branch.
17. `git checkout <branch>` to change to the `<branch>` and make it the current branch.
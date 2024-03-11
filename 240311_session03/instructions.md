### 1. Git commands

This week's git session is on branching.
This one of the most powerful features of git that is used for collaborations to avoid conflicts when several people work on the same document.
The idea is that there is one main branch that contains the latest fully functional code. When you clone code, like for example the if_analysis package and you want to experiment with it and add features its generally a good idea to generate your own local branch that you work with. Once you have established a new function or chaged a function to improve its features you can merge these changes back to main, once you are sure they work.
Today you wil generate a branch of the if_analysis package that you will use for your own work.
cd into the if_analysis folder
the most common commands for working with git branches:

- **git branch**

gives you a lits of the current branches in the repo

- **git switch -c new-branch-name**

This checks you out of the main branch and into a new branch with the new name. You will see this in the terminal header

- **git switch branch-name**

Use this to switch between excisting branches

- **git stash**

When you have already made some changes in your main branch and then decide to switch to a new branch with these changes you cant do that without

commitring the changes first. To avoid this you can stash them. This reverts the original branch back to the last commit and keeps the changes in memory

- **git stash pop**

Once you are in the new branch you can get the stahsed changes back and keep working with them...

So lets try and do this with the if_analysis repo. Its probably a good diea that you keep your own branch that you can change as you see fit.

Once you have something useful you can share it back to the mian branch that everyone is connected to.

To do this we will use git merge, but this is for next time.

### 2. First steps with object oriented programming:

Understanding classes is useful even if you dont need them for the type of coding you do.

Switch to the jupyter notebook to follow along the next steps

### 3. if_analysis code

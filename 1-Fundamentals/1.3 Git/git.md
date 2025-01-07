# Git 

- Installing Git
- Using Git with the Command Line
- Configure Git
- Create a **local** repository

## Installing Git

- It's available for free to download

```shell
sudo apt install git
```

> [https://git-scm.com/](https://git-scm.com/)

## Git Command Line and Configuring Git

1. Check if git is install

    ```shell
    git --version
    ```

2. Configure Git user info

    - This information will be used for each commit.
    - Use the same info that you have on GitHub

    ```shell
    # Configure the Git username
    git config --global user.name "<Your GitHub Username>"

    # Configure the Git email
    git config --global user.email "<Your GitHub email>"
    ```

    > We use `global` to set the username and email for every repository on the machine.
    > If you want to set the username/email for just the current repo you can remove `global`

## Initialize a Local Git Repository

1. Create a project folder and navigate into it:

    ```shell
    mkdir example_project

    cd example_project
    ```

2. Initialize the Git repository:

    ```shell
    git init
    ```

    > This command allows you to attach a path to it and will create a repository at the given path.
    > Git creates a hidden folder to track all the changes.


## Local Git Workflow

- We can check the status of our repo and whether there any untracked files

```shell
git status
```

Files in a Git repository can have 1 of 2 states:

1. Tracked - files that Git knows about and are added to the repository
2. Untracked - files that are in your working directory, but not added to the repository.

> You can use the .gitignore file to keep files untracked and out of the repository.
> By default files are not tracked by Git. In order to track files, you need to add them to a staging environment.

### Git Staging Environment

- One of the main functions of Git is the Staging Environment and the Commit
- When you hit a milestone or finish part of the work, you should add files to the staging environment.
- Staged files are files that are ready to be committed to the repo.

1. Adding file(s) to the staging environment

    ```shell
    git add <filename>
    ```

    - You can add all files in the directory:

        ```shell
        git add --all

        #OR

        git add -A

        #OR

        git add .
        ```

### Git Commit

- Adding commits keeps track of changes as we work. 
- Git considers each commit as a save point.
- Each point serves as as milestone you can go back to if you find any bugs or want revert to a previous change.

> When we commit we should always add a commit message. Commit messages help to give a glimpse of what has changed.

1. Making a commit to the local repo:

    ```shell
    git commit -m "<Commit message>"
    ```

    > `-m` stands for message

    > Use `git log` to check the history of commits on your repo. 

## Branching

- Branches allow you to work on different parts of a project without impacting the main branch.
- When work is complete, a branch can be merged with the main project.
- You can switch between branches and work on different parts of the project without them interfering with each other.

> **NOTE: When creating a new branch, it will use the latest version of the branch you are currently in.**

1. Create a new branch:

    ```shell
    git branch <name of the branch>
    ```

2. List all branches:

    ```shell
    git branch
    ```

    > The branch you are currently on is specified by a `*` (asterisk)

3. Switch to a different branch:

    ```shell
    git checkout <name of the branch>
    ```

    > `git checkout -b <name of branch>` can be used to create a new branch and immediately switch to it.

## Branch Merging

- When merging you need to be in the branch that is going to be merged into.

1. Switch to the `master` branch:

    ```shell
    git checkout master
    ```

2. Merge the feature branch into master:

    ```shell
    git merge <name of the branch>
    ```

3. Delete the feature branch:

    ```shell
    git branch -d <name of the branch>
    ```

## Merge Conflicts

- Merge conflicts need to be resolved and committed to the branch being merged into.
- VS Code provides a nice GUI to track and resolve merge conflicts.

> List currently tracked files in branch using `git ls-tree -r <branch-name>`
# Git & GitHub

- Create remote repositories
- Cloning repos into the local environment
- Pushing a Local Repo to GitHub
- Push/Pull System
    - Fetch and Merge vs Pull
    - Push changes
- Branching on Github
- Ignoring files using `.gitignore`
- Forking

> [https://github.com/](https://github.com/)

## Creating a remote repository

- Owner should be the account/organization you want to create the repository under.
- Repository name: It has to be unique to the owner

## Clone the remote Repo

```shell
git clone <URL of the repo>
```

## Push local to GitHub

```shell
# Add files to staging
git add <filename(s)>

# Commit staged files
git commit -m "<Commit-message>"

# Push changes to GitHub
git push
```

> Note: Since its the first time connecting to GitHub, you will be asked to authenticate.

## Link a local repo to GitHub

1. Initialize a repo locally:

    ```shell
    # Create a folder
    mkdir <folder-name>

    # Navigate into the folder
    cd <folder-name>

    # Initialize the Git repository
    git init
    ```

2. Create a repo on GitHub
    - should have the same name as the locally created repo

3. Link the local to the remote:

    ```shell
    # Setup remote origin of repo
    git remote add origin https://github.com/masonk16/funky-repo.git

    # setup default branch
    git branch -M main

    # Push the default branch to remote
    git push -u origin main
    ```

## Creating your own .gitignore file

1. Create an empty .gitignore file at the root/base of the repo

2. In your browser navigate to [https://www.toptal.com/developers/gitignore](https://www.toptal.com/developers/gitignore) and select the languages/technologies you want to create a .gitignore for.

3. Copy the output into the .gitignore file you created

## Push/Pull System

- Any time you are working on a project you should get the most recent changes to your local copy.
- You can use the `pull` command with Git.

**Git Fetch**

- Fetches updates to see what has changed.

```shell
git fetch origin
```

**Check differences**

```shell
git diff origin/main
```

**Merge**

```shell
git merge origin/main
```

**OR**

- Use `git pull` to combine `fetch` and `merge`

```shell
git pull
```


**Push**

- Updating the local changes into the remote repository.

```shell
git push
```

## Branching

- Locally created branches are not automatically uploaded to github.
- You have to set the remote origin manually.

```shell
# Switch to the newly created branch
git checkout <branch-name>

# Upload the branch to GitHub
git push --set-upstream origin <branchname>
```

- Check for all remote branches

    ```shell
    git ls-remote
    ```

- To get an remote branch into your local repo

1. Fetch any remote changes:

    ```shell
    git fetch
    ```

2. Switch to the newly created branch:

    ```shell
    git checkout <branch-name>
    ```
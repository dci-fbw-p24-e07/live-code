# Linux Terminal

- man

## File/Folder Navigation

- pwd
- ls
- ls -al
- cd

## Manipulation

- mkdir
- rmdir
- touch
- mv
- cp
- open

- gzip
    - will delete the file
    - `-c` option
    - `-d` option

- gunzip
    - `-c` option
- tail
    - `-f` option
    - -n option
Exercise

- cat
- nano
- less

## Updating your Linux Packages

- Check for available updates

    ```shell
    sudo apt list -–upgradable
    ```

- Simulate what would happen if you ran an upgrade

    ```shell
    sudo apt-get --simulate upgrade
    ```

- Run updates

    ```shell
    sudo apt upgrade

    # Or

    sudo apt-get upgrade
    ```
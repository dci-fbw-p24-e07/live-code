# Setting up Django with Postgres, Nginx and Gunicorn on Ubuntu

- We will configure and install some components on an Ubuntu platform to support and serve our Django application 
- We will setup a PostgreSQL database instead of using SQLite 
- The Gunicorn application server with be configured to interface with out application
- The Nginx Web Server will be configured to reverse proxy to Gunicorn

## Setup an Ubuntu VM (virtual machine) - Droplet

1. From the console of your project navigate to the `Droplets` page
2. From the `Droplets` page click on `Create Droplet`
3. Pick a region and select a datacenter if the option is available
        ![](example_imgs/1.3.png)
    - As a general rule of thumb you want to deploy to a region that is closer to your targeted users.
4. Under `OS` select Ubuntu and pick your preferred version from the dropwdown
        ![](example_imgs/1.4.png)
    - The latest with `LTS` (Long Term Support) is usually the best one to use as it is more stable.
5. Under the `Choose Size` section:
   1. Pick the `Basic` Droplet Type
   2. Under `CPU Options` select `Regular`
   3. Select the lowest plan possible
        ![](example_imgs/1.5.png)
6. Under `Choose An Authentication Method` select `SSH Key` then click the `Add SSH Key` button
    ![](example_imgs/1.6.2.png)
    - Create a new SSH Key:
        1. In your terminal use the following command:
            ```shell
            ssh-keygen -t rsa
            ```
            - `-t` allows you to specify the type of key
        2. You will be prompted to save and name the key.

            ```shell
            Generating public/private rsa key pair. Enter file in which to save the key (/Users/USER/.ssh/id_rsa):
            ```
        3. Next you will be asked to create and confirm a passphrase for the key (highly recommended):
            ```shell
            Enter passphrase (empty for no passphrase):
            Enter same passphrase again:
            ```
        4. Copy and paste the contents of the `.pub` file, typically `id_rsa.pub`, into the SSH key content field
            ```shell
            cat ~/.ssh/id_rsa.pub
            ```
        5. Give your key an appropriate name and click `Add  SSH Key` to confirm
    ![](example_imgs/1.6.3.png)
7. Under `Finalize Details` give your droplet an easily identifiable hostname and select the project you want to create in under
   ![](example_imgs/1.7.png)
8. Confirm that all configurations are correct and click on `Create Droplet`

**Connect to Droplet via SSH:**

To do so, you need to have an SSH client, like OpenSSH or PuTTY, and the following three pieces of information:

1. The Droplet’s IP address.
    - After your Droplet is created, its IP address displayed in the DigitalOcean Control Panel.

2. The username on the server that you want to connect as.
    - The default username on initial creation is root on most operating systems, like Ubuntu and CentOS. If you add another user, you can use that username instead.

3. The authentication method for that user.
    - If you add SSH keys to your Droplet, you can connect using those keys, which we strongly recommend for its additional security. Otherwise, if you use password authentication, use the password you chose.

- Once you have your Droplet’s IP address, username, and password or SSH keys, follow the instructions for your SSH client. OpenSSH is included on Linux, macOS, and Windows Subsystem for Linux. Windows users with Bash also have access to OpenSSH. Windows users without Bash can use PuTTY.

- How to Connect via SSH: [https://docs.digitalocean.com/products/droplets/how-to/connect-with-ssh/](https://docs.digitalocean.com/products/droplets/how-to/connect-with-ssh/)

## Install the Packages from the Ubuntu Repositories

- We will download and install all of the necessary packages from the Ubuntu repositories
- We will need to install Python, PostgreSQL, cURL and a few other components

```shell
sudo apt update
sudo apt install python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl
```

## Creating the PostgreSQL Database and User

1. Login to `psql`:
    ```shell
    sudo -u postgres psql
    ```

2. Create the Database for the project:
    ```sql
    CREATE DATABASE <database-name>;
    ```

3. Create the database user for our project:
    ```sql
    CREATE USER <username> WITH PASSWORD '<password>';
    ```

4. Modify connection parameters for the database user:
    - Set the default character encoding to `utf-8` which Django expects
    - Set a default transaction isolation scheme to `read committed`, which blocks reads from uncommitted transactions.
    - Set the default timezone to `UTC` which is normally the default on Django projects.

    ```sql
    ALTER ROLE <username> SET client_encoding TO 'utf-8';
    ALTER ROLE <username> SET default_transaction_isolation TO 'read committed';
    ALTER ROLE <username> SET timezone TO 'UTC';
    ```

    - These are recommendations made by the Django project itself

5. Give the new user acces to administer the database:
    ```sql
    GRANT ALL PRIVILEGES ON DATABASE <database-name> TO <username>;
    ```

## Create a Python Virtual Environment for Project
## Create and Configure New Django Project
## Complete Django Project Setup
## Test Gunicorn’s Ability to Serve the Project
## Creating Gunicorn systemd Socket and Service Files
## Check Gunicorn Socket File
## Testing Socket Activation
## Configure Nginx to Proxy Pass to Gunicorn
## Troubleshooting Nginx and Gunicorn

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
        **Using `ssh-keygen`:**
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

        **Using PuTTYgen:**
        1. In PuTTYgen, under Parameters, choose:
            - Type of key to generate: Usually `RSA` (2048 or 4096 bits).

        2. Click `Generate`.

        3. Move your mouse randomly in the blank area to create entropy.

        4. Once complete, PuTTYgen will display your public key.

        5. (Optional) Enter a Key passphrase to protect the private key.

        6. Click Save private key → save as `.ppk` file (e.g., `mykey.ppk`).

        7. Copy the public key text 
   
    - Give your key an appropriate name and click `Add  SSH Key` to confirm
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

**Connect using the terminal:**

1. Connect to Your Server

    - Use the ssh command:
        ```shell
        ssh username@server_ip
        ```

    - Example:
        ```shell
        ssh ubuntu@203.0.113.10
        ```

2. (Optional) Specify a Private Key

    - If your server uses a key pair (common for cloud servers):
        ```shell
        ssh -i /path/to/private_key.pem username@server_ip
        ```

    - Example:
        ```shell
        ssh -i ~/.ssh/id_rsa ubuntu@203.0.113.10
        ```

        💡 **Tip: Make sure your key has the right permissions:**
        ```shell
        chmod 600 ~/.ssh/id_rsa
        ```

3. Accept the Host Key

- The first time you connect, you’ll see:
    ```shell
    The authenticity of host '203.0.113.10' can't be established.
    Are you sure you want to continue connecting (yes/no)?
    ```

Type *yes* and press `Enter`.

4. Enter Your Password (If Required)

- Type your password (nothing will show as you type — this is normal).

- Press `Enter`.


**Connect using PuTTY:**

1. Open PuTTY & Configure Session

    1. Open PuTTY (you’ll see the PuTTY Configuration window).

    2. Under Session:

        - In Host Name (or IP address) → enter your server’s IP.

        - Ensure Port = 22 (unless specified otherwise).

        - Set Connection type = SSH.

    3. (Optional) Under Saved Sessions → type a name and click Save
    This saves the settings for future use.

2. Load a Private Key

- If you’re using a private key:

    1. In the left sidebar, go to Connection → SSH → Auth.

    2. Click Browse and select your .ppk file (PuTTY private key).

        - If you have an OpenSSH key, use PuTTYgen (installed with PuTTY) to convert it to .ppk.

3. Connect to the Server

    1. Click Open.

    2. A terminal window appears. The first time, PuTTY will ask to trust the server’s host key — click Yes.

    3. Enter your username and press Enter.

    4. Enter your password (you won’t see it while typing) and press Enter.


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

5. Give the new user access to administer the database:
    ```sql
    GRANT ALL PRIVILEGES ON DATABASE <database-name> TO <username>;
    GRANT ALL PRIVILEGES ON SCHEMA public TO <username>;
    ```

## Create a Python Virtual Environment for Project

1. Create a project directory:
    ```shell
    mkdir first_project
    cd first_project
    ```

2. Create and activate python virtual environment:
    ```shell
    python3 -m venv .venv --prompt=first-venv

    source .venv/bin/activate
    ```

4. Install required packages:
    - `django`: The Web Framework we want to utilize
    - `gunicorn`: The application server that will connect to Nginx
    - `psycopg2`: Database connector for PostgreSQL
    - `python-dotenv`: To abstract environment variables
    ```shell
    pip install django gunicorn psycopg2-binary python-dotenv
    ```

## Create and Configure New Django Project

1. Create the django project directory:
    ```shell
    django-admin startproject config .
    ```
    

**Configure environment variables:**

1. Open the `settings.py` and copy the Django Secret Key:
    ```shell
    nano config/settings.py
    ```

2. Create the `.env` and add the variables to it:

    ```shell
    nano .env
    ```

    ```
    SECRET_KEY=<your-django-secret-key>

    # Database Settings
    DB_NAME=<your-database-name>
    DB_USER=<your-dtabase-username>
    DB_PASSWORD=<your-database-password>
    DB_HOST=<your-database-host>
    DB_PORT=<your-database-port>
    ```

    - In order to save the chnages and exit from nano: `Ctrl + X` -> `Shift + Y` -> `Enter`

**Configuring the settings.py for deployment:**

1. Open the `settings.py` file:
    ```shell
    nano config/settings.py
    ```

2. Add the import for the `os` module:
    ```python 
    import os
    ```

3. Add the import for the `load_dotenv` function and call it:
    ```python
    from dotenv import load_dotenv

    load_dotenv()
    ```

4. Set the `DEBUG` setting to `False`:

    ```python
    DEBUG = False
    ```

5. Edit the `SECRET_KEY` setting to use environment variables:
    ```python
    SECRET_KEY = os.getenv("SECRET_KEY")
    ```

6. Add the IP addresses and domains for the `ALLOWED_HOSTS`:
    - Because the database will be connected from the `localhost` we need to the `localhost` or `127.0.0.1` to the the setting
    - Add the Public IP Address for your virtual machine
    - (Optional) add any domains configured for the project
    ```python
    ALLOWED_HOSTS = ["localhost", "<your-droplet-public-ip>"]
    ```

7. Add the Database settings to connect to PostgreSQL:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv("DB_NAME"),
            'USER': os.getenv("DB_USER"),
            'PASSWORD': os.getenv("DB_PASSWORD"),
            'HOST': os.getenv("DB_HOST"),
            'PORT': os.getenv("DB_PORT")
            
        }
    }
    ```

8. Add the `STATIC_ROOT` path:

    ```python
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
    ```

- In order to save the changes and exit from nano: `Ctrl + X` -> `Shift + Y` -> `Enter`

## Complete Django Project Setup

1. Generate the migration files and apply migrations to our database:
    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```

2. Create a superuser:
    ```shell
    python manage.py createsuperuser
    ```

3. Collect all static content into the configured directory:
    ```shell
    python manage.py collectstatic
    ```

4. Allow access to port `8000`:
   - UFW firewall will be protecting the server and it normally blocks access to ports that have not publicly exposed.
   - We will use the port `8000` to initally test our deployment
    ```shell
    sudo ufw allow 8000
    ```

5. Test the Django Development server:
    ```shell
    python manage.py runserver 0.0.0.0:8000
    ```

    - The `0.0.0.0` IP Address exposes the network/server to the Public internet allowing you to access the server via it's public IP address.

6. In your browser navigate to:
    ```
    http://<your-droplet-public-ip>:8000
    ```

## Test Gunicorn’s Ability to Serve the Project

- We will need to test Gunicon to make sure it can serve our application well
- This will be done by loading the projects `WSGI` module through `gunicorn`

```shell
gunicorn --bind 0.0.0.0:8000 config.wsgi
```

- this will start `gunicorn` on the same interface that the Django Development server was running on.
> The admin interface will not have styling(CSS) applied since Gunicorn does not know how to find the static CSS responsible for this
- The `wsgi.py` file is the main entry point to your application. Inside of this file you will find a function called `application` is defined which is used to communicate with the application.

- Exit the virtual environment:
```shell
deactivate
cd ..
```

## Creating Gunicorn systemd Socket and Service Files

- In order to implement a more robust way of starting and stopping the application server we need to configure `systemd` `service` and `socket` files
- Gunicorn socket will be created at boot and will listen for connections. When a connection occurs, systemd will automatically start the Gunicorn process to handle the connection.

1. Create the systemd `socket` file for Gunicorn:
    ```shell
    sudo nano /etc/systemd/system/gunicorn.socket
    ```

    ```
    [Unit]
    Description=gunicorn socket

    [Socket]
    ListenStream=/run/gunicorn.sock

    [Install]
    WantedBy=sockets.target
    ```

    - `[Unit]`: describes a socket
    - `[Socket]`: defines the socket location
    - `[Install]`: makes sure the socket is created at the right time

    > In order to save the chnages and exit from nano: `Ctrl + X` -> `Shift + Y` -> `Enter`

2. Create the systemd `service` file for Gunicorn:
    ```shell
    sudo nano /etc/systemd/system/gunicorn.service
    ```

    ```
    [Unit]
    Description=gunicorn daemon
    Requires=gunicorn.socket
    After=network.target

    [Service]
    User=root
    Group=www-data
    WorkingDirectory=/root/first_project
    ExecStart=/root/first_project/.venv/bin/gunicorn \
                --access-logfile - \
                --workers 3 \
                --bind unix:/run/gunicorn.sock \
                config.wsgi:application

    [Install]
    WantedBy=multi-user.target
    ```

    > In order to save the chnages and exit from nano: `Ctrl + X` -> `Shift + Y` -> `Enter`

3. Start and enable the gunicorn socket:
    - It will create the socket file at `/run/gunicorn.sock`
    - When a connection is made to that socket, systemd will automatically start the `gunicorn.service`
  
    ```shell
    sudo systemctl start gunicorn.socket
    sudo systemctl enable gunicorn.socket
    ```

## Check Gunicorn Socket File

- Check the status of the process to find out whether it was able to start:

```shell
sudo systemctl status gunicorn.socket
```

- Check the existence of the`gunicorn.sock` file:
```shell
file /run/gunicorn.sock
```

- If the `systemctl status` command indicated an error or if you do not find the `gunicorn.sock` file then the Gunicorn socket was not able to be created successfully
- Check the sockets error logs:
```shell
sudo journalctl -u gunicorn.socket
```
- Take another look at your `/etc/systemd/system/gunicorn.socket` file to fix any problems before continuing.

## Testing Socket Activation

- If you have only started the `gunicorn.socket` unit, the `gunicorn.service` unit will not be active since it has not receieved any connections yet.

```shell
sudo systemctl status gunicorn
```

- To test the socket activation mechanism, you can send a connection through `curl`
```shell
curl --unix-socket /run/gunicorn.sock localhost
```

- If the output from `curl` or the output from `systemctl status` indivates a problem, check the logs:
```shell
sudo journalctl -u gunicorn
```

- If you make changes to your `gunicorn.service` file, reload the daemon and restart the Gunicorn service:
```shell
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
```

## Configure Nginx to Proxy Pass to Gunicorn

1. Create and open a new server block in Nginx's `sites-available` directory:
    ```shell
    sudo nano /etc/nginx/sites-available/first_project
    ```

2. Specify the port that Nginx should listen on and that it should respond to your servers domain or IP address:
    ```
    server {
        listen 80;
        server_name <IP address Or Domain>;
    }
    ```

3. Configure Nginx to ignore the `favicon.ico` and tell it where to find the static files:
    ```
    server {
        listen 80;
        server_name <IP address Or Domain>;

        location = /favicon.ico { access_log off; log_not_found off; }
        location /static/ {
            root /root/first_project;
        }
    }
    ```

4. Configure Nginx to match all other requests and `proxy_pass` to Gunicorn:
    ```
    server {
        listen 80;
        server_name <IP address Or Domain>;

        location = /favicon.ico { access_log off; log_not_found off; }
        location /static/ {
            root /root/first_project;
        }

        location / {
            include proxy_params;
            proxy_pass http://unix:/run/gunicorn.sock;
        }
    }
    ```
    > In order to save the chnages and exit from nano: `Ctrl + X` -> `Shift + Y` -> `Enter`

5. Enable the file by linking it to the `sites-enabled` directory:
    ```shell
    sudo ln -s /etc/nginx/sites-available/first_project /etc/nginx/sites-enabled
    ```

6. Test your Nginx configuration:
    ```shell
    sudo nginx -t
    ```

7. If no errors are reported, restart the Nginx:
    ```shell
    sudo systemctl restart nginx
    ```

8. Configure your firewall to allow normal traffic on port 80 and disable port 8000 since it will no longer be used:
    ```shell
    sudo ufw delete allow 8000
    sudo ufw allow 'Nginx Full'
    ```

## Troubleshooting Nginx and Gunicorn

If this last step does not show your application, you will need to troubleshoot your installation.

**Nginx Is Showing the Default Page Instead of the Django Application**
- If Nginx displays the default page instead of proxying to your application, it usually means that you need to adjust the `server_name` within the `/etc/nginx/sites-available/first_project` file to point to your server’s IP address or domain name.

- Nginx uses the `server_name` to determine which server block to use to respond to requests. If you receive the default Nginx page, it is a sign that Nginx wasn’t able to match the request to a sever block explicitly, so it’s falling back on the default block defined in `/etc/nginx/sites-available/default`.

- The `server_name` in your project’s server block must be more specific than the one in the default server block to be selected.

**Nginx Is Displaying a 502 Bad Gateway Error Instead of the Django Application**
- A 502 error indicates that Nginx is unable to successfully proxy the request. A wide range of configuration problems express themselves with a 502 error, so more information is required to troubleshoot properly.

- The primary place to look for more information is in Nginx’s error logs. Generally, this will tell you what conditions caused problems during the proxying event. Follow the Nginx error logs by typing:
```
sudo tail -F /var/log/nginx/error.log
```
- Now, make another request in your browser to generate a fresh error (try refreshing the page). You should receive a fresh error message written to the log. If you look at the message, it should help you narrow down the problem.

- You might receive the following message:
```
connect() to unix:/run/gunicorn.sock failed (2: No such file or directory)
```
- This indicates that Nginx was unable to find the `gunicorn.sock` file at the given location. You should compare the `proxy_pass` location defined within `/etc/nginx/sites-available/first_project` file to the actual location of the gunicorn.sock file generated by the gunicorn.socket systemd unit.

- If you cannot find a `gunicorn.sock` file within the `/run` directory, it generally means that the systemd socket file was unable to create it. Go back to the section on checking for the Gunicorn socket file to step through the troubleshooting steps for Gunicorn.
```
connect() to unix:/run/gunicorn.sock failed (13: Permission denied)
```
- This indicates that Nginx was unable to connect to the Gunicorn socket because of permissions problems. This can happen when the procedure is followed using the root user instead of a `sudo` user. While systemd is able to create the Gunicorn socket file, Nginx is unable to access it.

- This can happen if there are limited permissions at any point between the root directory (`/`) the `gunicorn.sock` file. You can review the permissions and ownership values of the socket file and each of its parent directories by passing the absolute path to your socket file to the `namei` command:
```shell
namei -l /run/gunicorn.sock
```
```shell
Output
f: /run/gunicorn.sock
drwxr-xr-x root root /
drwxr-xr-x root root run
srw-rw-rw- root root gunicorn.sock
```
- The output displays the permissions of each of the directory components. By looking at the permissions (first column), owner (second column) and group owner (third column), you can figure out what type of access is allowed to the socket file.

- In the above example, the socket file and each of the directories leading up to the socket file have world read and execute permissions (the permissions column for the directories end with `r-x` instead of `---`). The Nginx process should be able to access the socket successfully.

- If any of the directories leading up to the socket do not have world read and execute permission, Nginx will not be able to access the socket without allowing world read and execute permissions or making sure group ownership is given to a group that Nginx is a part of.

**Django Is Displaying: “could not connect to server: Connection refused”**
- One message that you may receive from Django when attempting to access parts of the application in the web browser is:
```shell
OperationalError at /admin/login/
could not connect to server: Connection refused
    Is the server running on host "localhost" (127.0.0.1) and accepting
    TCP/IP connections on port 5432?
```
- This indicates that Django is unable to connect to the Postgres database. Make sure that the Postgres instance is running by typing:
```shell
sudo systemctl status postgresql
```
- If it is not, you can start it and enable it to start automatically at boot (if it is not already configured to do so) by typing:
```shell
sudo systemctl start postgresql
sudo systemctl enable postgresql
```
- If you are still having issues, make sure the database settings defined in the `~/first_project/config/settings.py` file are correct.

**Further Troubleshooting**
For additional troubleshooting, the logs can help narrow down root causes. Check each of them in turn and look for messages indicating problem areas.

The following logs may be helpful:

- Check the Nginx process logs by typing: sudo journalctl -u nginx
- Check the Nginx access logs by typing: `sudo less /var/log/nginx/access.log`
- Check the Nginx error logs by typing: `sudo less /var/log/nginx/error.log`
- Check the Gunicorn application logs by typing: `sudo journalctl -u gunicorn`
- Check the Gunicorn socket logs by typing: `sudo journalctl -u gunicorn.socket`

As you update your configuration or application, you will likely need to restart the processes to adjust to your changes.

If you update your Django application, you can restart the Gunicorn process to pick up the changes by typing:
```shell
sudo systemctl restart gunicorn
```

If you change Gunicorn socket or service files, reload the daemon and restart the process by typing:
```shell
sudo systemctl daemon-reload
sudo systemctl restart gunicorn.socket gunicorn.service
```

If you change the Nginx server block configuration, test the configuration and then Nginx by typing:
```shell
sudo nginx -t && sudo systemctl restart nginx
```
These commands are helpful for picking up changes as you adjust your configuration.

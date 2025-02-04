# Virtual Environments

- a way to separate one project environment from the other
- it allows us to switch on or off any environment as desired.
- you cannot switch on an environment for different to use on another

## Create a virtual environment

1. Create a project folder and navigate into it

    ```shell
    mkdir <project-name>

    cd <project-name>
    ```

2. Use venv command to create and name your virtual environment:

    ```shell
    # python3 -m venv <name-of-environment> --prompt=<name-to-be-displayed-in-terminal>
    python3 -m venv .venv --prompt="collections-example"
    ```

    > if it doesn't work or produces an error run `sudo apt install python3.12-venv`

3. Activate the virtual environment

    ```shell
    # source <path-to-activate-script>

    # Linux
    source .venv/bin/activate

    # windows
    .\venv\Scripts\activate
    ```

4. To deactivate the virtual environment

    ```shell
    deactivate
    ```

> find out more at: [https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html](https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html)
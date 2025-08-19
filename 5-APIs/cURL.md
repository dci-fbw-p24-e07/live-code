# cURL

- cURL (Clientside URL) is a command-line utility for transferring data across the internet.
- It supports about 22 protocols including HTTP
- It can be used to test REST API endpoints, download data, upload data, etc

## Installation

- It usually comes pre-installed on Linux and MacOS
- However, you can find download instructions at: [https://curl.se/download.html](https://curl.se/download.html)

- To check if curl is installed:

    ```shell
    curl --version
    ```

## Usage

- cURL supports over 200 commmand-line options.
- By default cURL uses the GET method

**Syntax:**

```shell
curl [options] <URL>
# curl -v https://p24.com/
```

1. Verbose

- This is used to give detailed information about the request. Such as IP addresses, ports and headers.

```shell
curl -v https://example.com
```

2. Output (saving to a file)

```shell
curl -o example.json https://example.com
```

### HTTP methods

1. GET

- this is the default method that cURL uses

```shell
curl -v https://example.com
```

2. POST

- It requires data to be sent to the API
- We use the -X option to specify the method to be used
- Use the -H (headers) to specify the type of data that will be sent
- It supports 2 options for sending data to the API

    1. Using the `-d` (data) option
    
        - Direct injection of JSON

        ```shell
        curl -X POST 'https://fakestoreapi.com/users' -H 'Content-Type: application/json' -d '{"username": "john_doe", "email": "john@example.com", "password": "pass123"}'
        ```

        - When using the `Content-Type` header the data should match the format specified by the header

    2. Using the `-d` option to attach data from a file

        - This uses an existing file to send data

        ```shell
        curl -X POST 'https://fakestoreapi.com/users' -H 'Content-Type: application/json' -d @newuser.json
        ```

3. PUT

- This is very similar to a POST request
- Only that it is used to edit an existing resources

    ```shell
    curl -X PUT -H 'Content-Type: application/json' -d @edit.json h
    ```

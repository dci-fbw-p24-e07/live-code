# Python `requests` library

- What is the `requests` library?
- Usage
- Examples:
    - GET
    - POST
    - PUT
    - DELETE
    - Headers

## What is the `requests` library?

- This is go-to package for making HTTP requests in Python
- It is available on the [Python Package Index(PyPI)](pypi.org)
- It abstracts complexities of making requests behind an intuitive API
- We can use it perform actions GET, POST, PUT and more

**Installation:**

```shell
pip install requests
```

## Usage

- Import the requests library into you Python file

```python
import requests
```

- We specify the HTTP method by using dot notation to access the corresponding requests library method

    ```python
    # To make a GET request
    response = requests.get("https://example.com/")
    ```

- These methods offer extra parameters to use when sending your requests e.g `headers`, `params`, `data`

1. GET

    ```python
    response = requests.get("<url>", params={}, headers={})
    ```

    1. Without parameters

        ```python
        import requests

        # Get request without parameters
        response = requests.get("https://fakerapi.it/api/v2/persons")

        print(response.json())
        ```

    2. With parameters

        ```python
        import requests

        # Get request with parameters
        parameters = {
            "_quantity": 15,
            "_gender": "female",
            "_birthday_start": "1986-07-01",
            "birthday_end": "2005-09-30"
        }
        response = requests.get("https://fakerapi.it/api/v2/persons", params=parameters)

        print(response.json())
        ```

2. POST

    ```python
    import requests

    response = requests.post("<url>", data=<payload>)
    ```

    1. Using a dictionary

        ```python
        # Post with a dictionary
        product_dict = {
            "title": "Softcare",
            "price": 56.89,
            "description": "This is a brand new product on the market",
            "category": "Tools",
            "image": "https://www.google.com/search"
        }

        response = requests.post("https://fakestoreapi.com/products", data=product_dict)

        print(response.json())
        ```

    2. Using a list of tuples

        ```python
        import requests

        # Post with a list of tuples
        prod_tuples = [
            ("title", "Timeshare"),
            ("price", 54.32),
            ("description", "This is just a random product"),
            ("category", "Tools"),
            ("image", "https://example.com/image")
        ]

        response4 = requests.post("https://fakestoreapi.com/products", data=prod_tuples)

        print(response4.json())
        ```

3. PUT

- This more or less follows the same rules as post
- We need to identify the resource to be edited through some sort of filtering or primary key

    ```python 
    import requests

    # PUT request
    new_data = {
        "title": "The new product",
        "price": 33.75,
        "description": "Some random product",
        "category": "Headphones",
        "image": "example.com/images/8434568765"
    }

    response = requests.put("https://fakestoreapi.com/products/3", data=new_data)

    print(response.json())
    ```

    - Just like the post request you can also use a list of tuples to create the data object.

4. DELETE

```python
import requests

# DELETE request 
response = requests.delete("https://fakestoreapi.com/products/3")

print(response.json())
```

5. Adding custom headers

- All methods in the requests library have a headers parameter that allows you to add custom headers for your HTTP request.

```python
# Adding custom headers
url = "https://jsearch.p.rapidapi.com/search"

querystring = {
    "query":"developer jobs in chicago",
    "page":"1",
    "num_pages":"1",
    "country":"us",
    "date_posted":"all"
}

# Create headers dictionary
headers = {
	"x-rapidapi-key": "YOUR API KEY",
	"x-rapidapi-host": "jsearch.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
```

6. Authentication

- All methods of the requests library have an optional `auth` parameter that allows you to define the authentication mechanism and credentials

```python
import requests
from requests.auth import HTTPBasicAuth

# Basic Authentication
response = requests.get("https://example.com/", auth=HTTPBasicAuth("<username>", "<password>"))

# Token Authentication
response = requests.get("https://example.com/", auth=("", "<token>"))
```

## Error handling and asynchronous functions

- Different exceptions in the `requests` module
- Handling HTTP request exceptions
- Using `asyncio` to run asynchronous functions

**General Syntax:**

    ```python
    import requests

    try:
        res = requests.get("http://example.com/some-endpoint")

        # Raise any errors that occurs for unsuccessful HTTP status codes
        res.raise_for_status()
    except requests.exceptions.<Expected-Exception>:
        print(<exception>)
    ```

### HTTP Errors

```python
try:
    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error: {errh}")
```

### Timeout Errors

- A timeout is a prescribed time limit for the requested connection to respond
- If the connection does not respond within the time limit then the request is deemed to have been timed out

```python
try:
    response7 = requests.get(url, headers=headers, params=querystring, timeout=1)
    response7.raise_for_status()
except requests.exceptions.ReadTimeout as errh:
    print(f"Timeout Error: {errh}")
```

### Connection Errors

- Connection error occurs when a site does not exist.
- The error occurs because you cannot establish the connection to the specified domain

```python
try:
    response7 = requests.get(url, headers=headers, params=querystring, verify=True)
    response7.raise_for_status()
except requests.exceptions.ConnectionError as errh:
    print(f"Connection Error: {errh}")
```

### General exception handling

- This will handle any exception raised from the request

```python
try:
    response7 = requests.get(url, headers=headers, params=querystring, timeout=1, verify=True)
    response7.raise_for_status()
except requests.exceptions.RequestException as errh:
    print(f"General Error: {errh}")
```

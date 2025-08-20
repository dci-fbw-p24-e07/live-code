import requests

# Get request with parameters
parameters = {
    "_quantity": 15,
    "_gender": "female",
    "_birthday_start": "1986-07-01",
    "birthday_end": "2005-09-30"
}
response = requests.get("https://fakerapi.it/api/v2/persons", params=parameters)

# Get request without parameters
response2 = requests.get("https://fakerapi.it/api/v2/persons")

# Post with a dictionary
product_dict = {
    "title": "Softcare",
    "price": 56.89,
    "description": "This is a brand new product on the market",
    "category": "Tools",
    "image": "https://www.google.com/search?sa=X&sca_esv=a6dae9f26a3c2c64&rlz=1C5CHFA_enZW1175ZW1176&udm=2&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIemkjk18Cn72Gp24fGkjjh6zHcTYmus8TBHCnMOizJiF2sYDUTUN2FhjUrwGEdodZgHLdxlFI0oRXzRVm8Jt11kFkRNZXIp2bUfTBVkR8WGN5rAaAyom8MFE92jzyZE5ZvSv8libDWC7ejSOmjme8RbqV3_vYDNYQA3W2mZFzMI2ldDM5nQ&q=tools&ved=2ahUKEwjXubWE_JiPAxWqXEEAHfy3GhkQtKgLegQIExAB&biw=949&bih=919&dpr=1"
}

response3 = requests.post("https://fakestoreapi.com/products", data=product_dict)

# Post with a list of tuples
prod_tuples = [
    ("title", "Timeshare"),
    ("price", 54.32),
    ("description", "This is just a random product"),
    ("category", "Tools"),
    ("image", "https://example.com/image")
]

response4 = requests.post("https://fakestoreapi.com/products", data=prod_tuples)

# PUT request
new_data = {
    "title": "The new product",
    "price": 33.75,
    "description": "Some random product",
    "category": "Headphones",
    "image": "example.com/images/8434568765"
}

response5 = requests.put("https://fakestoreapi.com/products/3", data=new_data)

# DELETE request 
response6 = requests.delete("https://fakestoreapi.com/products/3")

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

response7 = requests.get(url, headers=headers, params=querystring)

print(response7.json())






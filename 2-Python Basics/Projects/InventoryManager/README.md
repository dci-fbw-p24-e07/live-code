# Inventory Management System

## Topics

- Text
- Dates
- Functions
- Collections
- Statements and Loops
- Logical Thinking
- Algorithmic Thinking
- Debugging
- OOP

### Project Description:

The objective of this project is to develop a simple inventory management system for a store. The system will allow you to add products, remove products, update quantities, retrieve product information, and calculate the total value of the inventory. It involves creating classes to represent products and an inventory manager to handle product operations. 

#### Project structure

To organize our project, we will create multiple files and folders. Follow the steps below to set up the project structure:

Create a new folder for your project. Name it `InventoryManagementSystem`. Inside the `InventoryManagementSystem` folder, create the following sub-folders:

- `inventory/` : This folder will contain the implementation of the inventory-related classes.
- `tests/` : This folder will contain the unit tests for the inventory-related classes.

Create the following files and place them in the corresponding folders:

- `inventory/__init__.py`: The initializer for the inventory module 
- `inventory/product.py` : This file will contain the implementation of the Product class.
- `inventory/inventory_manager.py`: This file will contain the implementation of the InventoryManager class.
- `tests/__init__.py`: The initializer for the tests module
- `tests/test_inventory_manager.py`: This file will contain the unit tests for the InventoryManager class.
- `main.py` - The file that will contain the driver code for our program.
- `gitignore` - To include the names of any files or folders that should not be pushed to github

Your project structure should look something like this:

    
    InventoryManagementSystem/
    ├── inventory/
    │   ├── __init__.py
    │   ├── product.py
    │   └── inventory_manager.py
    ├── tests/
    │   ├── __init__.py
    │   └── test_inventory_manager.py
    └── main.py
    └── .gitignore
    

> Note: this is the simplest structure. You can further organize it into submodules if your project grows.

#### Implementation steps

1. Step 1: Implement the `Product` class in `product.py`
    - Define a class named `Product`
    - Add attributes such as `name`, `price`, `quantity`, etc., to the Product class
    - Implement methods to update product details such as `update_quantity` to update the quantity of the product. You can implement similar methods for updating the price or other attributes.
    - Implement the `get_product_info` method (or call it the way you prefer) to return a string representation of the product's information.

2. Step 2: Implement the `InventoryManager` Class in `inventory_manager.py`:
    - Define a class named `InventoryManager`.
    - Implement methods in the class to add products, remove products, update quantities
    - Create a method to retrieve product information by providing a `product_name` parameter. If the product with the given name exists in the inventory, call the corresponding method of the Product object to retrieve its information; otherwise, return a `"Product not found"` message.
    - Implement a method called `get_total_inventory_value` to calculate the total value of the entire inventory. This method should allow you to determine the total worth of the inventory by summing up the individual values of each product based on its price and quantity.

3. Step 3: Remember to create the `main.py` file at the root level.
    - It serves as entry point for your application. Typically, the main file is responsible for starting the program, initializing objects, and calling relevant functions.
    - Creates an instance of the `InventoryManager`, adds some sample products to the inventory, and then calculates and prints the total inventory value.

4. Step 4: Add Extra Features:
    - You can extend the project by adding additional functionalities to the Product and InventoryManager classes. For example, you can implement features like searching for products, generating reports or statistics on the inventory, create categories for the inventory, etc.
    
> Note: **We will not be implementing anything in the test module for now as we have not covered it but this serves as way to introduce what a typical project structure should look like. We will also talk about the `__init__.py` and why it is important.**

#### Tips & Tricks

> Remember to write clean and readable code, follow best practices, and document your code using comments and docstrings on all classes, functions and files to make it more understandable for yourself and others who may review or maintain it in the future.

> A virtual environment should be created and used. However, it should not be seen on GitHub.

**Pro Tip:** probably best to create the GitHub repository first that has a  `.gitignore` then add each other on as collaborators so that you can clone it to your local machine. 

### Summary of the Fields Covered:

- Software Development: OOP, software design patterns, modularization.
- Business & Enterprise Systems: Inventory management.
- Data Management: Handling and processing product data.

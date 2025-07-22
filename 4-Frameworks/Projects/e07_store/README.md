# Django e-Commerce App

- You will build a modular eCommerce web application with Django. It allows users to browse products, manage a shopping cart, register and log in, and place orders.

## Structure

1. Users
    - Manages user registration, login, and profiles using a custom user model.
    - You can use the built-in authentication url's and view or generate your own

    **Models:**

    - Custom user model (`CustomUser`) extending `AbstractUser`
    - Remove the username field such that Django uses the email as the default

2. Shop

    - Manages the product catalog and categories.

    **Models:**

    ```python
    class Category(TranslatableModel):
        name=models.CharField(max_length=200, db_index=True),
        slug=models.SlugField(max_length=200, unique=True)

        class Meta:
            ordering = ("name",)
            verbose_name = "Category"
            verbose_name_plural = "Categories"

        def __str__(self):
            return self.name

        def get_absolute_url(self):
            return reverse("shop:product_list_by_category", args=[self.slug])


    class Product(TranslatableModel):
        name=models.CharField(max_length=200, db_index=True),
        slug=models.SlugField(max_length=200, db_index=True),
        description=models.TextField(blank=True),
        sku = models.CharField(max_length=20, unique=True, null=True)
        category = models.ForeignKey(
            Category, related_name="products", on_delete=models.CASCADE
        )
        brand = models.CharField(max_length=30, null=True)
        specification = models.TextField(blank=True, null=True)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        available = models.BooleanField(default=True)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)

        class Meta:
            ordering = ("name",)
            index_together = (("id", "slug"),)

        def __str__(self):
            return self.name

        def get_absolute_url(self):
            return reverse("shop:product_detail", args=[self.id, self.slug])

    class ProductImage(models.Model):
        product = models.ForeignKey(Product, related_name='product_images',
                                    on_delete=models.CASCADE,
                                    null=True, blank=True)
        picture = models.ImageField(upload_to='shop/static/product/images/')

        def __str__(self):
            return self.picture.url
    ```

    **Views:**

    1. `product_list` - displays all products that are available, allows for filtering by category. (Hint: you can have 2 URL patterns pointing to the same view)
    2. `product_detail` - displays a specific product, filters by `id` and `slug`

3. Cart

    - Handles the shopping cart functionality using session or user-based storage.
    - You will create a utility class in `cart/cart.py` and implement the following methods:

        ```python
        class Cart(object):  # Request object
            def __init__(self, request):
                """
                Initialize the cart.
                """
                pass

            def add(self, product, quantity=1, override_quantity=False):
                """
                Add a product to the cart or update its quantity.
                """
                pass

            def save(self):
                # mark the session as "modified" to make sure it gets saved
                self.session.modified = True

            def remove(self, product):
                """
                Remove a product from the cart.
                """
                pass

            def __iter__(self):
                """
                Iterate over the items in the cart and get the products
                from the database.
                """
                pass

            def __len__(self):
                """
                Count all items in the cart.
                """
                pass

            def get_total_price(self):
                pass

            def clear(self):
                """Removes cart from the session."""
                pass

            def get_discount(self):
                pass

            def get_total_price_after_discount(self):
                pass
        ```

    **Views:**
    - The following views that make use of the utility class:

        1. `cart_add` - Which adds a product(or updates) to the cart
        2. `cart_remove` - Removes a product from the cart
        3. `cart_detail` - Which displays all products already in the cart
        4. `cart_clear` - Clears the cart completely

4. Orders

    - Manages checkout, order creation, and user order history.

    **Models:**

    ```python
    class Order(models.Model):
        customer = models.ForeignKey(User, related_name="orders", null=True, on_delete=models.CASCADE)
        first_name = models.CharField(_('first name'), max_length=50)
        last_name = models.CharField(_('last name'), max_length=50)
        email = models.EmailField(_('e-mail'))
        phone_number = models.CharField(_('phone number'), max_length=20, null=True)
        address = models.CharField(_('address'), max_length=250)
        postal_code = models.CharField(_('postal code'), max_length=20)
        city = models.CharField(_('city'), max_length=100)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        paid = models.BooleanField(default=False)
        total_items = models.IntegerField(null=True)
        total_price = models.CharField(max_length=10, null=True)
        discount = models.IntegerField(default=0,
                                    validators=[MinValueValidator(0),
                                                MaxValueValidator(100)])

        class Meta:
            ordering = ("-created",)

        def __str__(self):
            return f"Order {self.id}"


    class OrderItem(models.Model):
        order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
        product = models.ForeignKey(
            Product, related_name="order_items", on_delete=models.CASCADE
        )
        price = models.DecimalField(max_digits=10, decimal_places=2)
        quantity = models.PositiveIntegerField(default=1)

        def __str__(self):
            return str(self.id)
    ```

    **Views:**

    - `order_create` - Creates an order using information from the cart and attaches it to the user. (Hint: you will need a form to create orders)

5. Payments

    **Models:**

    ```python
    class Payment(models.Model):
        class PaymentMethod(models.TextChoices):
            CARD = 'card', 'Credit/Debit Card'
            PAYPAL = 'paypal', 'PayPal'
            MANUAL = 'manual', 'Manual Transfer'

        class PaymentStatus(models.TextChoices):
            PENDING = 'pending', 'Pending'
            SUCCESS = 'success', 'Success'
            FAILED = 'failed', 'Failed'

        order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        amount = models.DecimalField(max_digits=10, decimal_places=2)
        method = models.CharField(max_length=20, choices=PaymentMethod.choices, default=PaymentMethod.CARD)
        status = models.CharField(max_length=20, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return f'Payment #{self.id} - {self.status} - {self.amount}'
    ```

    **Views:**

    1. `process_payment` - processes payment for an existing order and redirects to the `payment_complete` view
    2. `payment_complete` - displays payment success message and order details 

### Templates

- You can either generate your own templates(including static files) or use prebuilt templates that are created with Bootstrap or Tailwind CSS
- You will also need to research on how to store media files in Django as the products require it

### Bonus

- Implement order history for each user
- Implement stock management by updating the product quantity whenever an order is completed

### Groups

1. Group 1:
    - Uliana
    - Roman
    - Shafi


2. Group 2:
    - Britta
    - Wimpie
    - Vadim

3. Group 3:
    - Eden
    - Nico
    - Alex

4. Group 4:
    - Padma
    - Thomas
    - Daniel

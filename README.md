coffee-shop-challenge.


A simple object-oriented Python project simulating a coffee shop system, using classes such as `Customer`, `Coffee`, and `Order`. It demonstrates class relationships, data encapsulation, and includes a comprehensive test suite with `unittest

---

##  Project Structure

coffee-shop-challenge.2/
├── customer.py
├── coffee.py
├── order.py
├── tests/
│ ├── init.py
│ ├── customer_test.py
│ ├── coffee_test.py
│ └── order_test.py
├── init.py
└── README.md


---

##  Classes and Relationships

### 1. `Customer`
- Attributes: `name
- Methods: 
  - `orders()
  - `coffees()
  - `create_order()
  - `most_aficionado()

### 2. `Coffee`
- Attributes: `name
- Methods: 
  - `orders()
  - `customers()
  - `num_orders()
  - `average_price()

### 3. `Order`
- Attributes: `customer, coffee, price
- Class-level: Order.all stores all orders

###  Relationships
Customer Order Coffee

---

## Running Tests

All tests are located in the `tests/` directory and use the `unittest` framework.

### To run tests:

python3 -m unittest discover tests
If you're using a virtual environment:
source venv/bin/activate  # or your venv name
python3 -m unittest discover tests
 Setup Instructions
Clone the repo
git clone https://github.com/EDEL-WEB/coffee-shop-challenge.2.git
cd coffee-shop-challenge.2
(Optional) Create a virtual environment


python3 -m venv venv
source venv/bin/activate
Install requirements (if you add any in the future)

pip install -r requirements.txt
Circular Import Handling
To avoid circular imports between customer.py and order.py, some imports (e.g., from order import Order) are done inside methods instead of at the top level.

 Notes
Coffee names must be at least 3 characters long.

Customer names must be between 1–15 characters.

Order price must be a float between 1.0 and 10.0.

Properties are made read-only with @property.

 Author
Developed by EDEL-WEB


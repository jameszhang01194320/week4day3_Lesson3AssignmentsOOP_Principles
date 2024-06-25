<<<<<<< HEAD
def d():
    print("="*25)

=======
>>>>>>> 4096345119d8a0560ca4b644b97e35cf149c3a78
# Lesson 3: Assignments: OOP Principles
# Remember to take your time and work through each question diligently! Test your code, make sure it works, and try to find ways to improve. Once you are happy and satisfied with your code, upload it to Github, then turn in your Github link at the bottom of the page!

# Don't forget. Make sure this assignment is in it's own repository. Not mixed in with others

# 1. Encapsulation in Personal Budget Management
# Objective: The aim of this assignment is to reinforce the understanding of encapsulation in Python, focusing on the use of private attributes and getters and setters. Students will apply these concepts to create a Personal Budget Management system.

# Problem Statement: You are required to build a Personal Budget Management application. The application will manage budget categories like food, entertainment, utilities, etc., ensuring that budget details remain private and are accessed or modified through public methods.

# Task 1: Define Budget Category Class - Create a class `BudgetCategory` with private attributes for category name and allocated budget. - Initialize these attributes in the constructor.

# Expected Outcome: A `BudgetCategory` class capable of storing category details securely.

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
<<<<<<< HEAD
    
    def __str__(self):
        return f"Category: {self.__category_name}, Budget: ${self.__allocated_budget:.2f}"
d()
print(BudgetCategory("Food",100))
d()
=======

    
    # def __str__(self):
    #     return f"Category: {self.__category_name}, Budget: ${self.__allocated_budget:.2f}"

# print(BudgetCategory("Food",100))
>>>>>>> 4096345119d8a0560ca4b644b97e35cf149c3a78
# Task 2: Implement Getters and Setters - Write getter and setter methods for both the category name and the allocated budget. - Ensure that the setter methods include validation (e.g., budget should be a positive number).

# Expected Outcome: Methods that allow controlled access and modification of the private attributes, with validation checks in place.

<<<<<<< HEAD
class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
    
    def __str__(self):
        return f"Category: {self.__category_name}, Budget: ${self.__allocated_budget:.2f}"
=======

>>>>>>> 4096345119d8a0560ca4b644b97e35cf149c3a78
    # Getter for category name
    def get_category_name(self):
        return self.__category_name

    # Setter for category name
    def set_category_name(self, category_name):
        if isinstance(category_name, str) and category_name.strip():
            self.__category_name = category_name
        else:
            raise ValueError("Category name must be a non-empty string.")

    # Getter for allocated budget
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Setter for allocated budget with validation
    def set_allocated_budget(self, new_budget):
        if isinstance(new_budget, (int, float)) and new_budget > 0:
            self.__allocated_budget = new_budget
        else:
            raise ValueError("Allocated budget must be a positive number.")





# Task 3: Add Budget Functionality - Implement a method to add expenses to a category and adjust the budget accordingly. - Validate the expense amount before making deductions from the budget.

# Expected Outcome: Ability to track expenses per category and update the remaining budget safely.
# Getter for total expenses
    def get_total_expenses(self):
        return self.__expenses

    # Method to add expenses
    def add_expense(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            if amount <= self.__allocated_budget - self.__expenses:
                self.__expenses += amount
            else:
                raise ValueError("Expense exceeds the available budget.")
        else:
            raise ValueError("Expense amount must be a positive number.")

    # Method to get remaining budget
    def get_remaining_budget(self):
        return self.__allocated_budget - self.__expenses

    def __str__(self):
        return (f"Category: {self.__category_name}, "
                f"Allocated Budget: ${self.__allocated_budget:.2f}, "
                f"Total Expenses: ${self.__expenses:.2f}, "
                f"Remaining Budget: ${self.get_remaining_budget():.2f}")


# Task 4: Display Budget Details - Create a method to display the details of a budget category, including the name, allocated budget, and remaining budget after expenses.

# Expected Outcome: Users can view a summary of each budget category, showcasing encapsulation in action.

<<<<<<< HEAD
d()
=======

>>>>>>> 4096345119d8a0560ca4b644b97e35cf149c3a78
class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__expenses = 0  # for total expenses

    # Getter for category name
    def get_category_name(self):
        return self.__category_name

    # Setter for category name
    def set_category_name(self, category_name):
        if isinstance(category_name, str) and category_name.strip():
            self.__category_name = category_name
        else:
            raise ValueError("Category name must be a non-empty string.")

    # Getter for allocated budget
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Setter for allocated budget with validation
    def set_allocated_budget(self, new_budget):
        if isinstance(new_budget, (int, float)) and new_budget > 0:
            self.__allocated_budget = new_budget
        else:
            raise ValueError("Allocated budget must be a positive number.")

    # Getter for total expenses
    def get_total_expenses(self):
        return self.__expenses

    # Method to add expenses
    def add_expense(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            if amount <= self.__allocated_budget - self.__expenses:
                self.__expenses += amount
            else:
                raise ValueError("Expense exceeds the available budget.")
        else:
            raise ValueError("Expense amount must be a positive number.")

    # Method to get remaining budget
    def get_remaining_budget(self):
        return self.__allocated_budget - self.__expenses

    # Method to display the budget category summary
    def display_category_summary(self):
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget:.2f}")
        print(f"Total Expenses: ${self.__expenses:.2f}")
        print(f"Remaining Budget: ${self.get_remaining_budget():.2f}")

    def __str__(self):
        return (f"Category: {self.__category_name}, "
                f"Allocated Budget: ${self.__allocated_budget:.2f}, "
                f"Total Expenses: ${self.__expenses:.2f}, "
                f"Remaining Budget: ${self.get_remaining_budget():.2f}")
# Example usage
food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()
food_category = BudgetCategory("Rent", 1000)
food_category.add_expense(730)
food_category.display_category_summary()
<<<<<<< HEAD
d()


# 2. E-commerce Product Catalog System
# Objective: The goal of this assignment is to demonstrate a deep understanding of inheritance and method overriding in Python. Students will apply these concepts to develop an E-commerce Product Catalog System that handles various types of products with both common and unique attributes.

# Problem Statement: An e-commerce platform requires a system to manage different types of products, such as books, electronics, and clothing. Each product type shares some common characteristics but also has unique features. The system should be able to display information about each product appropriately.

# Task 1: Create Base Product Class

# Develop a base class Product with common attributes like product ID, name, price, and a method to display product information.
# Expected Outcome: A Product class that can hold general information about a product and display it.
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")

# Task 2: Implement Subclasses for Specific Products
# (ONLY BOOK SUBCLASS REQUIRED)
# Create subclasses Book, Electronic, and Clothing that inherit from Product.
# Each subclass should have additional attributes relevant to its category (e.g., author for books, specs for electronics, size for clothing).
# Expected Outcome: Each subclass contains both inherited attributes from Product and new attributes specific to the product type.

# Task 3: Override Display Method in Subclasses
# Override the method to display product information in each subclass to include specific attributes.
# For example, the Book class should display the author, Electronic should display specs, etc.
# Expected Outcome: Calling the display method on an instance of any subclass shows both common and specific product details.
class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")

class Electronic(Product):
    def __init__(self, product_id, name, price, specs):
        super().__init__(product_id, name, price)
        self.specs = specs

    def display_info(self):
        super().display_info()
        print(f"Specs: {self.specs}")

class Clothing(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size

    def display_info(self):
        super().display_info()
        print(f"Size: {self.size}")


# Task 4: Test Product Catalog Functionality

# Instantiate objects of each subclass and call their display methods to ensure correct information is shown.
# Expected Outcome: The system should accurately display detailed information for each type of product, demonstrating inheritance and method overriding.

# Test Code
my_book = Book("123", "Python Essentials", 29.99, "J. Doe")
my_book.display_info()
d()
book1 = Book(1, "Python Programming", 50, "John Doe")
electronic1 = Electronic(2, "Laptop", 800, "Intel i7 16GB RAM")
clothing1 = Clothing(3, "T-Shirt", 20, "Medium")

book1.display_info()
d()
electronic1.display_info()
d()
clothing1.display_info()
=======

# # 2. E-commerce Product Catalog System
# # Objective: The goal of this assignment is to demonstrate a deep understanding of inheritance and method overriding in Python. Students will apply these concepts to develop an E-commerce Product Catalog System that handles various types of products with both common and unique attributes.

# # Problem Statement: An e-commerce platform requires a system to manage different types of products, such as books, electronics, and clothing. Each product type shares some common characteristics but also has unique features. The system should be able to display information about each product appropriately.

# # Task 1: Create Base Product Class

# # Develop a base class Product with common attributes like product ID, name, price, and a method to display product information.
# # Expected Outcome: A Product class that can hold general information about a product and display it.
# # Task 2: Implement Subclasses for Specific Products

# # (ONLY BOOK SUBCLASS REQUIRED)

# # Create subclasses Book, Electronic, and Clothing that inherit from Product.
# # Each subclass should have additional attributes relevant to its category (e.g., author for books, specs for electronics, size for clothing).
# # Expected Outcome: Each subclass contains both inherited attributes from Product and new attributes specific to the product type.
# # Task 3: Override Display Method in Subclasses

# # Override the method to display product information in each subclass to include specific attributes.
# # For example, the Book class should display the author, Electronic should display specs, etc.
# # Expected Outcome: Calling the display method on an instance of any subclass shows both common and specific product details.
# # Task 4: Test Product Catalog Functionality

# # Instantiate objects of each subclass and call their display methods to ensure correct information is shown.
# # Expected Outcome: The system should accurately display detailed information for each type of product, demonstrating inheritance and method overriding.
# # Code Examples:

# class Product:
#     # Constructor and common attributes
#     # ...

#     def display_info(self):
#         # General method to display product info
#         pass# ...

# class Book(Product):
#     def __init__(self, product_id, name, price, author):
#         super().__init__(product_id, name, price)
#         self.author = author

#     def display_info(self):
#         # Overridden method for books
#         pass# ...

# # Example usage
# my_book = Book("123", "Python Essentials", 29.99, "J. Doe")
# my_book.display_info()
>>>>>>> 4096345119d8a0560ca4b644b97e35cf149c3a78

### Zegel 2024-2 Python OOP Repository 🐍✨
Welcome to the Zegel 2024-2 Python OOP Repository! This project is an educational resource designed to teach Object-Oriented Programming (OOP) concepts using Python. Perfect for students and professionals who want to master the fundamentals and advanced features of Python's OOP capabilities.
## 🛠️ Project Purpose
This repository is built to guide learners through:
Understanding OOP principles such as encapsulation, inheritance, polymorphism, and abstraction.
Practical implementation of classes, methods, attributes, and exceptions.
Hands-on practice with Python's OOP tools to create robust, reusable code structures.
## 📂 Repository Structure
1. Core Concepts and Classes
The project includes foundational examples of OOP principles:
Encapsulation: Demonstrates how to define private attributes and use getters and setters to control data access.
Inheritance: Explains how child classes can extend functionality from parent classes using the super() function.
Polymorphism: Implements flexible methods to handle multiple types of data seamlessly.
Abstraction: Introduces abstract classes and methods using Python's abc module.
2. Practical Use Cases
This repository brings theoretical concepts to life with real-world scenarios:
Appliance Management: Classes such as Product, Kitchen, Microwave, and WashingMachine demonstrate how to model objects in a modular fashion.
Private methods like _calculate_price_with_tax() ensure secure and accurate computations.
Public methods such as show_details() display formatted information for each object.
## 🚀 Key Functionalities
## 📦 Product Class
A base class that represents generic products with attributes like:
code: A unique identifier for the product.
description: A string that explains the product.
price: The base price before taxes.
Private Methods:
_calculate_igv(): Computes tax (18%) for the product.
_calculate_total_price(): Adds tax to the base price for the total.
Public Methods:
get_code(), get_price(): Retrieve information securely.
set_price(value): Updates the product price.
🍴 Kitchen Class
An extension of the Product class with extra attributes for appliances. Features include:
Overriding the base class's methods for specific appliance use cases.
Future Scope: Adding properties like energy efficiency.
## 🧺 Washing Machine Class
Models washing machines with:
Extended attributes for load capacity and water consumption.
Demonstrates inheritance and method customization.
## 📝 Learning Objectives
By exploring this repository, you will learn to:
Define and structure Python classes effectively.
Apply OOP principles to real-world programming scenarios.
Handle complex relationships between objects using inheritance.
## 🤝 Contributions
Contributions are welcome! If you have additional examples, optimizations, or ideas, feel free to submit a pull request.
## 📩 Contact
For questions, reach out via GitHub Issues or contact the repository maintainer directly.
Enjoy learning Python OOP! 🐍💻
Feel free to adjust this draft to include exact functionality or files if specific details are available in the repository.

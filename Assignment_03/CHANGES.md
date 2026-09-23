# Assignment 03 — CHANGES

**Name:** Ngyein Chan Ko **Student ID:** 6705140061

This is the written part of your submission. Explain **what you changed and why**, then record your **prompt log**. Keep before/after snippets to a line or two.

---

## 1 · What I changed

One row per change. Name the OOP concept and say how you checked the behaviour was unchanged.

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
| --- | --- | --- | --- | --- |
| 1 | Product was stored as a bare tuple like `("Laptop", 1200.0, "electronics")`. | Created a `Product` class with `name`, `price`, and `category`. | Classes / Encapsulation | Ran `python Assignment_03.py` and checked that the self-test passed. |
| 2 | Customer tiers used repeated `if`/`elif` conditions for discounts and points. | Created `Customer`, `SilverCustomer`, `GoldCustomer`, and `PlatinumCustomer` subclasses with their own `discount_rate()` and `points_multiplier()` methods. | Inheritance / Polymorphism | Compared the discount and points rules with the original code and ran the self-test. |
| 3 | Order items were handled using separate product and quantity data. | Created an `OrderItem` class that contains a `Product` object and its quantity, with `line_total()` and `tax()` methods. | Composition / Encapsulation | Checked the item calculations against the original program and ran the self-test. |
| 4 | The original `calc()` function handled many different calculations in one place. | Created an `Order` class with separate methods for `subtotal()`, `discount()`, `tax()`, `total()`, and `points()`. | Encapsulation / Separation of responsibilities | Compared each calculation with the original `calc()` function and checked the final output. |
| 5 | Calculation logic and receipt printing were mixed together. | Added a `receipt()` method to build the receipt separately from the calculation methods and used named constants for repeated values. | Encapsulation / Maintainability | Ran `python Assignment_03.py` and checked that the receipt and grand total matched the original behaviour. |

## 2 · Short reflection (4–6 sentences)

Which change improved the code the most, and why? Where did keeping the behaviour identical force you to be careful?

> _your reflection..._

The biggest change for me was replacing the membership if/elif statements with different customer classes. At first, I was not very familiar with how polymorphism could be used for this, so I used AI to explain it step by step and then added the code myself. I also learned that separating the calculation methods from the receipt printing makes the code easier to follow. I had to be careful because this assignment was a refactoring task, so I could not change the original discounts, tax, points, or receipt output. After each major change, I checked the code and used the self-test to make sure the output stayed the same.

---

## 3 · Prompt log (Level 2 — required)

Record **every** prompt where AI helped. If you wrote a part yourself, say so in one row. AI-shaped code with an empty log does **not** meet the Level-2 policy.

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|
| 1 |Can you help me do this OOP Python assignment one by one? I want to understand how to refactor the code.  | AI explained the main OOP requirements and suggested starting with named constants. |Accepted | I compared the suggested constants with the original code. |
| 2 | For OOP in Python, how should I change the product tuples into a Product class? | AI suggested creating a Product class with attributes such as name, price, and category. | Edited | I checked that the class stored the same product information as the original tuples. |
| 3 | How can I use encapsulation in the Product and OrderItem classes for this assignment? | AI suggested using class attributes and validation in the constructors. | Edited | I checked the validation rules against the assignment requirements. |
| 4 | What is the best way to make an OrderItem class that contains a Product object and quantity? | AI suggested composition, where OrderItem contains a Product object and calculates the line total and tax. | Accepted | I tested the calculations using the original product prices and quantities. |
| 5 | How can I use inheritance and polymorphism for the different customer tiers in Python? | AI suggested a base Customer class with SilverCustomer, GoldCustomer, and PlatinumCustomer subclasses. | Edited | I checked the discount rates and points multipliers against the original code. |
| 6 | Can you explain how the Order class should work using OOP instead of one big calculation function? | AI suggested moving subtotal, discount, tax, total, and points calculations into separate methods in the Order class. | Edited | I compared each method with the calculations in the original program. |
| 7 | How can I separate the calculation logic from printing the receipt in Python? | AI suggested keeping calculations inside the Order class and creating a separate receipt() method for the output. | Edited | I ran the program and checked that the receipt output stayed the same. |
| 8 | How can I create the correct customer subclass without using another long if/elif statement? | AI suggested using a dictionary as a simple customer factory. | Accepted | I checked that each membership tier created the correct customer class. |
| 9 | Can you show me how to put all the OOP classes together in the main function without changing the original behavior? | AI showed how to create products, customers, order items, and orders using the classes. | Edited | I compared the product and order data with the original program. |

**Ownership statement.** *By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.*

---

## 4 · checklist

- [ ] `python Assignment_03.py` prints **PASS**.
- [ ] No tuples / parallel lists left — products, orders, and items are objects.
- [ ] No `if tier == ...` chains — tiers are a class family.
- [ ] Calculation methods **return** values and do not `print`; printing is separate.
- [ ] Constructors validate state; no leftover `global`; magic numbers are named.
- [ ] The change table and reflection above are filled in.
- [ ] The prompt log is complete and the ownership statement is signed.

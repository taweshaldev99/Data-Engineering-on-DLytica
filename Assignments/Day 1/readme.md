Completion of Assignment 1
# Day 1: Python Foundations

## Topics Covered

- Variables
- Data types
- String methods
- Operators
- Conditional statements

## Exercises

1. Sales Summary
2. Data Quality Checker
3. File Validator
4. Customer Record Cleaner
5. Pipeline Health Status
6. Dataset Access Decision

## How to Run

Run each file using:

```bash
python exercise-01-sales-summary.py
What I Learned
Write two or three sentences describing what you learned.

Challenges Faced
Write any problem you encountered and how you solved it.


Do not leave the **What I Learned** and **Challenges Faced** sections empty.

---

## 5. Code structure

Each Python file should include:

```python
"""
Exercise: Sales Summary
Student: Your Name
Day: 1
"""

# Input values
product_name = "Wireless Mouse"
unit_price = 1500
quantity_sold = 12
discount_percentage = 0.10

# Calculations
gross_sales = unit_price * quantity_sold
discount_amount = gross_sales * discount_percentage
final_sales = gross_sales - discount_amount

# Output
print(f"Product: {product_name}")
print(f"Gross sales: NPR {gross_sales:.2f}")
print(f"Discount: NPR {discount_amount:.2f}")
print(f"Final sales: NPR {final_sales:.2f}")
Code should:

Use meaningful variable names.

Include short comments where necessary.

Produce clear output.

Run without errors.

Follow the assignment requirements.

Avoid copying another student’s solution.


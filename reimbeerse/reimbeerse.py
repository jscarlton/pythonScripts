#!/usr/bin/python
# Calculator for subtracting alcohol amounts from reimbursements

total = raw_input("Please enter the total bill: ")
food = raw_input("Please enter the amount spent on food: ")
alcohol = raw_input("Please enter the amount spent on alcohol: ")

total = float(total)
food = float(food)
alcohol = float(alcohol)

tax_tip = total - food - alcohol
food_proportion = food/(food + alcohol)
alcohol_proportion = alcohol/(food + alcohol)

reimburseable_tax_tip = food_proportion * tax_tip

reimbursement = food + reimburseable_tax_tip

print "Your total reimbursement is $%.2f. $%.2f for the food and $%.2f for the tax and tip." % (reimbursement, food, reimburseable_tax_tip)
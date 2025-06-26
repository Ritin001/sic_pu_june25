#level 1
print("level 1")
name=input("Enter your name")
emp_id=input("Enter your employee id")
basic_monthly_salary=int(input("Enter your basic monthly salary"))
special_allowance=int(input("Enter your special allowance"))
bonus_percentage=int(input("Enter your bonus percentage"))
#calculation
gross_monthly_salary=basic_monthly_salary+special_allowance
bonus=bonus_percentage/100 * gross_monthly_salary
annual_gross_salary=12 * gross_monthly_salary + bonus
#output
print("Name:", name)
print("Employee ID:", emp_id)
print("gross monthly salary:", gross_monthly_salary)
print("annual gross salary:", int(annual_gross_salary))
print()




#level 2
print("level 2")
standard_deduction=50000
taxable_income=annual_gross_salary-standard_deduction
#output
print("annual gross salary:", int(annual_gross_salary))
print("Taxable income = ",annual_gross_salary,"-",standard_deduction)
print("Taxable income:", taxable_income)
print()



#level 3
''' ₹0 - ₹3,00,000: 0%
o ₹3,00,001 - ₹6,00,000: 5%
o ₹6,00,001 - ₹9,00,000: 10%
o ₹9,00,001 - ₹12,00,000: 15%
o ₹12,00,001 - ₹15,00,000: 20%
o Above ₹15,00,000: 30%'''
if annual_gross_salary <= 300000:
    tax = 0
elif annual_gross_salary <= 600000:
    tax = 5
elif annual_gross_salary <= 900000:
    tax= 10
elif annual_gross_salary <= 1200000:
    tax = 15
elif annual_gross_salary <= 1500000:
    tax = 20
else:
    tax = 30
#according to  sec 87A
if annual_gross_salary <= 700000:
    tax=0
tax=tax+4 #4% health and education cess
#output
tax_payable = (tax / 100) * annual_gross_salary




#level 4
print("level 4")
print("annual_gross_salary:", int(annual_gross_salary))
print("tax_payable:", int(tax_payable))
print("annual_net_salary:", int(annual_gross_salary - tax_payable))
print()



#level 5
print("level 5")

print("summarized details")
print("employee_name:", name)
print("employee_id:", emp_id)
print("gross_monthly_salary:", int(gross_monthly_salary))
print("annual_gross_salary:", int(annual_gross_salary))
print("taxable_income:", int(taxable_income))
print("tax_payable:", int(tax_payable))
print("annual_net_salary:", int(annual_gross_salary - tax_payable))

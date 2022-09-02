# Myanmar Income Tax Calculation
print('Myanmar Income Tax Calculation')
yearly_income = int(input('What is your yearly income in Myanmar? : '))
# 20% staff relief
staff_relief = 0.2
# total relief after staff deduction
tot_relief = int(float(yearly_income)*staff_relief)
print(tot_relief)
# will include parental, spousal & child relief in next iteration with boolean inputs
# This gives us the assessable income
inc_relief = yearly_income - tot_relief
# these are the tax brackets as per law
tax_b1 = 2000000
tax_b2 = 5000000
tax_b3 = 10000000
tax_b4 = 20000000
tax_b5 = 30000000
# clears the variable whenever the code is rerun
tax_rate = 0.00
a_tax = 0
# tax rate identifier if-else statement
if inc_relief <= tax_b1:
    tax_rate = 0.00
elif tax_b1 < inc_relief <= tax_b2:
    tax_rate = 0.05
    a_tax = (inc_relief - tax_b1) * tax_rate
    print(a_tax / 12)
elif tax_b2 < inc_relief <= tax_b3:
    tax_rate = 0.10
    a_tax = ((tax_b2-tax_b1) * 0.05) + ((inc_relief - tax_b2) * tax_rate)
    print(a_tax / 12)
elif tax_b3 < inc_relief <= tax_b4:
    tax_rate = 0.15
    a_tax = ((tax_b2 - tax_b1) * 0.05) + ((tax_b3 - tax_b2) * 0.1)+((inc_relief - tax_b3) * tax_rate)
    print(a_tax / 12)
elif tax_b4 < inc_relief <= tax_b5:
    tax_rate = 0.20
    a_tax = ((tax_b2 - tax_b1) * 0.05) + ((tax_b3 - tax_b2) * 0.1) + ((tax_b4 - tax_b3) * 0.15) + ((inc_relief - tax_b4) * tax_rate)
    print(a_tax / 12)
else:
    tax_rate = 0.25


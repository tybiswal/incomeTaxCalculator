# Myanmar Income Tax Calculation
print('Myanmar Income Tax Calculation')
yearly_income = int(input('What is your yearly income in Myanmar? : '))

# 20% staff relief
staff_relief = 0.2

# here I will include parental, spousal & child relief in next iteration with boolean inputs later
f_stat = input("Are you supporting your Father through your income? (Y/N): ")
m_stat = input("Are you supporting your Mother through your income? (Y/N): ")
s_stat = input("Are you supporting your Spouse through your income? (Y/N): ")
c_stat = input("Are you supporting your Child(ren) through your income? (Y/N): ")
# total relief after staff deduction
tot_relief = int(float(yearly_income)*staff_relief)
tot_rf = "{:,}".format(tot_relief)
print("\nTotal Relief is: \nKyats " + str(tot_rf))

# This gives us the assessable income
inc_relief = yearly_income - tot_relief
inc_rf = "{:,}".format(inc_relief)
print("Total Assessable Income is: \nKyats " + str(inc_rf))

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
    print("You owe no income tax!")
elif tax_b1 < inc_relief <= tax_b2:
    tax_rate = 0.05
    a_tax = (inc_relief - tax_b1) * tax_rate
elif tax_b2 < inc_relief <= tax_b3:
    tax_rate = 0.10
    a_tax = ((tax_b2-tax_b1) * 0.05) + ((inc_relief - tax_b2) * tax_rate)
elif tax_b3 < inc_relief <= tax_b4:
    tax_rate = 0.15
    a_tax = ((tax_b2 - tax_b1) * 0.05) + ((tax_b3 - tax_b2) * 0.1)+((inc_relief - tax_b3) * tax_rate)
elif tax_b4 < inc_relief <= tax_b5:
    tax_rate = 0.20
    a_tax = ((tax_b2 - tax_b1) * 0.05) + ((tax_b3 - tax_b2) * 0.1) + ((tax_b4 - tax_b3) * 0.15) + ((inc_relief - tax_b4)
                                                                                                   * tax_rate)
else:
    tax_rate = 0.25
    a_tax = ((tax_b2 - tax_b1) * 0.05) + ((tax_b3 - tax_b2) * 0.1) + ((tax_b4 - tax_b3) * 0.15) + ((tax_b5 - tax_b4) *
                                                                                                   0.2) + ((inc_relief -
                                                                                                            tax_b5) *
                                                                                                           tax_rate)

# convert the tax value to integer, to remove the float since currency doesn't support cents and py should round up
a_tax = int(a_tax)
a_taxf = "{:,}".format(a_tax) # formats to include number commas
m_tax = int(a_tax / 12) # monthly value, if we divide by 12
m_taxf = "{:,}".format(m_tax)

# Prints the annual and monthly income tax
print("\nYour Annual Income Tax is: \nKyats " + a_taxf)
print("Your Monthly Income Tax is: \nKyats " + m_taxf)

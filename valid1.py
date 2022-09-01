# PERT Calculator

print('Myanmar Income Tax Calculation')
yearly_income = int(input('What is your yearly income in Myanmar? : '))

staff_rel = 0.2

tot_rel = int(float(yearly_income)*staff_rel)
print(tot_rel)
inc_rel = yearly_income-tot_rel

tax_b1 = 2000000
tax_b2 = 5000000
tax_b3 = 10000000
tax_b4 = 20000000
tax_b5 = 30000000

tax_rate = 0
count = 0

if inc_rel <= tax_b1:
    tax_rate = 0.00
    count += 1
elif tax_b1 < inc_rel <= tax_b2:
    tax_rate = 0.05
    count += 2
elif tax_b2 < inc_rel <= tax_b3:
    tax_rate = 0.10
    count += 3
elif tax_b3 < inc_rel <= tax_b4:
    tax_rate = 0.15
    count += 4
elif tax_b4 < inc_rel <= tax_b5:
    tax_rate = 0.20
    count += 5
else:
    tax_rate = 0.25
    count += 6

if count == 1:
    tax_annual = 0
    tax_monthly = tax_annual / 12
    print("Your annual tax amount is Ks." + str(tax_annual))
    print("Your monthly tax amount is Ks." + str(tax_monthly))
elif count == 2:
    tax_annual = (tax_b2*tax_rate)
    tax_monthly = tax_annual / 12
    print("Your annual tax amount is Ks." + str(tax_annual))
    print("Your monthly tax amount is Ks." + str(tax_monthly))
else:
    print("Bye")




#print(tax_rate, count)


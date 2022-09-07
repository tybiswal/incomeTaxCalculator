# Myanmar Income Tax Calculation
import math


def tax_calc():
    # Staff relief is 20%->
    staff_relief = int(float(yearly_income) * 0.2)
    print("\nStaff Relief is: \nKyats " + str("{:,}".format(staff_relief)))

    # included parental, spousal & child reliefs
    concession = 0
    f_stat = input("\nAre you supporting your Father through your income? (Y/N): ")
    if f_stat == "Y" or f_stat == "y":
        concession += 1000000
    else:
        print("No paternal concession.\n")
    m_stat = input("Are you supporting your Mother through your income? (Y/N): ")
    if m_stat == "Y" or m_stat == "y":
        concession += 1000000
    else:
        print("No maternal concession.\n")
    s_stat = input("Are you supporting your Spouse through your income? (Y/N): ")
    if s_stat == "Y" or s_stat == "y":
        concession += 1000000
    else:
        print("No spousal concession.\n")
    c_stat = input("Are you supporting your Child(ren) through your income? (Y/N): ")
    if c_stat == "Y" or c_stat == "y":
        concession += 500000
    else:
        print("No children concession.\n")

    # This gives us the assessable income
    inc_relief = yearly_income - staff_relief - concession
    print("Total Assessable Income is: \nKyats " + str("{:,}".format(inc_relief)))

    # these are the tax brackets as per law
    tax_b = [2000000, 5000000, 10000000, 20000000, 30000000]

    # clears the variable whenever the code is rerun
    tax_rate = 0.00
    a_tax = 0

    # tax rate identifier if-else statement
    if inc_relief <= tax_b[0]:
        tax_rate = 0.00
        print("You owe no income tax!")
    elif tax_b[0] < inc_relief <= tax_b[1]:
        tax_rate = 0.05
        a_tax = (inc_relief - tax_b[0]) * tax_rate
    elif tax_b[1] < inc_relief <= tax_b[2]:
        tax_rate = 0.10
        a_tax = ((tax_b[1] - tax_b[0]) * 0.05) + ((inc_relief - tax_b[1]) * tax_rate)
    elif tax_b[2] < inc_relief <= tax_b[3]:
        tax_rate = 0.15
        a_tax = ((tax_b[1] - tax_b[0]) * 0.05) + ((tax_b[2] - tax_b[1]) * 0.1) + ((inc_relief - tax_b[2]) * tax_rate)
    elif tax_b[3] < inc_relief <= tax_b[4]:
        tax_rate = 0.20
        a_tax = ((tax_b[1] - tax_b[0]) * 0.05) + ((tax_b[2] - tax_b[1]) * 0.1) + ((tax_b[3] - tax_b[2]) * 0.15) + (
                (inc_relief - tax_b[3])
                * tax_rate)
    else:
        tax_rate = 0.25
        a_tax = ((tax_b[1] - tax_b[0]) * 0.05) + ((tax_b[2] - tax_b[1]) * 0.1) + ((tax_b[3] - tax_b[2]) * 0.15) + (
                (tax_b[4] - tax_b[3]) *
                0.2) + ((inc_relief -
                         tax_b[4]) *
                        tax_rate)

    # convert the tax value to integer, to remove the float and round up since currency doesn't support cents
    a_tax = int(math.ceil(a_tax))
    a_tax_f = "{:,}".format(a_tax)  # formats to include number commas
    m_tax = int(math.ceil(a_tax / 12))  # monthly value, if we divide by 12
    m_tax_f = "{:,}".format(m_tax)

    # Prints the annual and monthly income tax
    print("\nYour Annual Income Tax is: \nKyats " + a_tax_f)
    print("Your Monthly Income Tax is: \nKyats " + m_tax_f)


print('\nMyanmar Income Tax Calculation')
yearly_income = int(input('What is your yearly income in Myanmar? (Kyats): '))
if yearly_income == 0:
    print('You owe no income tax!')
else:
    tax_calc()


X = input("\n--------------------\nPress Enter to Close")

bal = float(raw_input('Enter the outstanding balance on your credit card: '))
ann = float(raw_input('Enter the annual credit card interest rate as a decimal: ')) 
pay = float(raw_input('Enter the minimum monthly payment rate as a decimal: '))
per = ann / 12
result = 0
for i in range(1,13):
    mon = round((bal * pay), 2)
    interest = round((bal * per), 2)
    principal = mon - interest
    bal = bal - principal
    print 'Month: ' + str(i)
    print 'Minimum monthly payment: $' + str(mon)
    print 'Principle paid: $' + str(principal)
    print 'Remaining balance: $' + str(bal)
    result += mon
print 'RESULT'
print 'Total amount paid: $' + str(result)
print 'Remaining balance: $' + str(bal)

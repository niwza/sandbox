##balance = float(raw_input('Enter the outstanding balance on your credit card: '))
##annual = float(raw_input('Enter the annual credit card interest rate as a decimal: '))
##interest = annual / 12
##pay = 0
##result = balance
##while result > 0:
##    pay += 10
##    result = balance
##    mon = 0
##    while mon < 12 and result > 0:
##        mon += 1
##        due = result*interest
##        result -= pay
##        result += due
##result = round(result, 2)
##print 'RESULT'
##print 'Monthly payment to pay off debt in 1 year: ' + str(pay)
##print 'Number of months needed: ' + str(mon)
##print 'Balance: ' + str(result)


balance = float(raw_input('Enter the outstanding balance on your credit card: '))
annual = float(raw_input('Enter the annual credit card interest rate as a decimal: '))
interest = annual / 12
result = balance
low = balance / 12
high = (balance *(1 + interest)**12.0)/12.0
diff = high - low
while result > 0 or diff > 0.01001:
    result = balance
    mon = 0
    while mon < 12:
        pay = round((high + low)/2 + 0.004999, 2)
        mon += 1
        due = result*interest
        result -= pay
        result += due
    if result > 0:
        low = pay
    else:
        high = pay
    diff = high - low
result = round(result, 2)
print 'RESULT'
print 'Monthly payment to pay off debt in 1 year: ' + str(pay)
print 'Number of months needed: ' + str(mon)
print 'Balance: ' + str(result)



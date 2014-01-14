bal = float(raw_input('Enter the outstanding balance on your credit card: '))
ann = float(raw_input('Enter the annual credit card interest rate as a decimal: '))
interest = ann / 12
pay = 0.0
out = 0.0
low = round((bal/12),2)
high = round((bal*(1+interest)**12.0)/12.0,2)
pay = round((high + low)/2.0,2) 
while pay <= round((bal*(1+interest)**12.0)/12.0,2):
    out = bal
    for i in range(1,13):
        out = round((out*(1+interest)-pay), 2)
    if out >= 0:
        low = pay
    else:
        if out >= -0.13:
            break
        high = pay
    pay = round((high + low)/2.0,2)
    
print 'RESULT'
print 'Monthly payment to pay off debt in 1 year: ' + str(round(pay,2))
print 'Number of months needed: ' + str(i)
print 'Balance: ' + str(out)



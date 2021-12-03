x = float(input('vvedite chislo')) 
a = float(input('vvedite ewe chislo'))       
if x > 0:
    if a>=0:
        y=a*x
        print('y=',y)
    else:
        y=2*a*x
        print('y=',y)
else:
    y=2
    print('y=',y)

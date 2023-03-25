#Nested Ifs
x = 15

if x > 10:
    print("x is greater than 10")
    
    if x > 20:
        print("x is also greater than 20")
    else:
        print("x is less than or equal to 20")
else:
    print("x is less than or equal to 10")
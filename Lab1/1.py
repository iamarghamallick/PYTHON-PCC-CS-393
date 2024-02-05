def f(x):
    if x <= 10:
        return (3*x*x)+5
    elif x > 10 and x <= 20:
        return 5*x
    elif x > 20:
        return (2*x*x)-x+9


x = int(input("Enter value of x: "))
print(f(x))

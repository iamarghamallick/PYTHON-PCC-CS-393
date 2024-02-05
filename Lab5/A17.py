# A17. Write a recursive function to find HCF of two numbers. Use the function to find the LCM of set of numbers.

def hcf(a, b):
    if b == 0:
        return a
    return hcf(b, a % b)

def lcm(a, b):
    return (a * b) // hcf(a, b)

n1, n2 = 12, 18
print("HCF:", hcf(n1, n2))
print("LCM:", lcm(n1, n2))

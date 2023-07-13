def herons_formula():
    h=int(input("hight:"))
    b = int(input("base:"))
    formula = h*b/2
    return formula
print(f" heron's formula {herons_formula()}")
print("\n")

def square():
    a=int(input("side:"))
    formula = a**2
    return formula
print(f"area of square {square()}")
print("\n")

def rectangle():
    w=int(input("weight"))
    l=int(input("length"))
    formula=w*l
    return formula
print(f"area of rectangle {rectangle()}")
print("\n")

def circle():
    r=int(input("radius"))
    formula=(3.14)*r**2
    return formula
print(f"radius of circle {circle()}")
print("\n")

def trapezium():
    a = int(input("base"))
    b= int(input("base"))
    h=int(input("height"))
    formula = ((a+b/2)/2)*h
    return formula
print(f" area of trapezium {trapezium()}")









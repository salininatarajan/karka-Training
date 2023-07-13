h= float(input(" your height in m :"))
w = int(input(" your weight in kg :"))
def bmi_calculator(h,w):
    return w/(h**2)
result=(bmi_calculator(h,w))
print(f"your BMI is{result}")











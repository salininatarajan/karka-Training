def find_bmi():
    h= float(input(" your height in m :"))
    w = int(input(" your weight in kg :"))
    bmi = (w/(h**2))

    if bmi<(18.5):
        ans=(f"under weight")
    elif 18.5<=bmi<=24.9:
        ans=("normal weight")
    elif 25.0<=bmi<=29.9:
        ans=("over weight")
    elif 30.0<=bmi:
        ans=("obese")
    print(f"your BMI is:{bmi}")
    print(f"BMI Category:{ans} ")
find_bmi()







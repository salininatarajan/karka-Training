weekday=(int(input("enter your days")))
def find_weekdays(weekday):
    if weekday ==1:
           return("sunday")
    elif weekday ==2:
            return("Monday")
    elif weekday==3:
            return("Tuesday")
    elif weekday ==4:
            return("Wednesday")
    elif  weekday==5:
            return("Thursday")
    elif weekday==6:
            return("Friday")
    elif weekday==7:
            return("Saturday")
    elif weekday==0:
            return("Saturday")
    else :
           return ("error")
print("Today is a ",find_weekdays(weekday))















































        

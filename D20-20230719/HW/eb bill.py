consumer_data={"consumer_name":"shalu",
               "eb_reading":[1100,1200,1350,1650,2050]}
eb_units=consumer_data["eb_reading"]
total_amount=0
bill_detail=[]
for unit in range(len(eb_units)-1):
    # range(1,len(eb_units))
    # eb_units[unit]-eb_units[unit-1]
    unit1 = eb_units[unit]
    unit2 = eb_units[unit + 1]
    units_per_month = unit2 - unit1
    month=unit+1
    if units_per_month<100:
        per =units_per_month*0
        total_amount=total_amount+per
    elif units_per_month>=100 and units_per_month<200:
        per =units_per_month*2
        total_amount=total_amount+per
    elif units_per_month>=200 and units_per_month<500:
        per =units_per_month*5
        total_amount=total_amount+per
    elif units_per_month>=500 and units_per_month>1000:
        per =units_per_month*10
        total_amount=total_amount+per
    elif units_per_month>=1000:
        month=unit+1
        per =units_per_month*14
        total_amount=total_amount+per
    dic={}
    dic["month"]=month
    dic["units_consumed"]=units_per_month
    dic["bill_amount"]=per
    bill_detail.append(dic)
# print(bill_detail)
# print(f"total_amount:{total_amount}")

for data in bill_detail:

    shalu=open("/home/salininatarajan/Documents/shalu.txt","a")
    output=f"for the month {data['month']} unit consumed  is {data['units_consumed']} so the bill amount is {data['bill_amount']}\n"
    string= shalu.write(output)
    shalu.close()
    file=open("/home/salininatarajan/Documents/shalu.txt","r")
    final=file.read()
print(final)

















    






















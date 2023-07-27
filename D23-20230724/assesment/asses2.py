monthly_gold_rate=[{"name":"jan",
                    "rate":2500},
                   {"name":"feb",
                    "rate":1200}, 
                    {"name":"march",
                    "rate":3000},
                    {"name":"april",
                    "rate":2000},]
max=0
min=monthly_gold_rate[0]["rate"]

for i in monthly_gold_rate:
    if i["rate"]>max:
        max=i["rate"]
        month1=i["name"]
    if i["rate"]<min:
        min=i["rate"]
        month2=i["name"]
print(f"""maximum rate :{max}
month_name:{month1}""")
print(f"""minimum rate :{min}
month_name:{month2}""")




















      
      
      
      
      
    






      


















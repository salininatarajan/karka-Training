monthly_gold_rate=[{"month":"jan",
                    "rate":2500,
                    "jewel-list":[{"name":"chain",
                                   "making_cost":12},
                                   {"name":"ring",
                                   "making_cost":14},]},
                   {"month":"feb",
                    "rate":1200,
                     "jewel-list":[{"name":"chain",
                                   "making_cost":12},
                                   {"name":"ring",
                                   "making_cost":14},]},
                    {"month":"march",
                    "rate":3000,
                    "jewel-list":[{"name":"chain",
                                   "making_cost":12},
                                   {"name":"ring",
                                   "making_cost":14}]},
                    {"month":"april",
                    "rate":2000,
                    "jewel-list":[{"name":"chain",
                                   "making_cost":12},
                                   {"name":"ring",
                                   "making_cost":14}]}]
List=[]
jewel=monthly_gold_rate[0]["jewel-list"]
for i in monthly_gold_rate:
    dic={}
    month=i["month"]
    cost=i["rate"]
    dic[month]={}
    dic[month]["gold_rate"] = cost
    for detail in jewel:
        name=detail["name"]
        amount=cost*detail["making_cost"]/100
        total_cost =cost+amount
        # print(f"""
        # month :{month}
        # rate : {cost}
        # {name}:{total_cost}""")
        dic[month][name]=total_cost
    List.append(dic)
print(List)






















    
        









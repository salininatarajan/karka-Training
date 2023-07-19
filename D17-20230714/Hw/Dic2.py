list=[{"name":"shalu",
                "age":22,
                "place":"vadasery"},
                {"name":"gayu",
                "age":20,
                "place":"kottar"},
                {"name":"vinu",
                "age":21,
                "place":"ethamozhy"},
                {"name":"vj",
                "age":20,
                "place":"marthandam"},
                {"name":"abishek",
                "age":22,
                "place":"kottar"}]
def age_details(list):
    for i in list:
        if i["age"]>21:
            data1=i["name"]
            data2=i["place"]
            print(f" i am {data1} my place is {data2}")
age_details(list)





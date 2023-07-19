name_list=[{"name":"shalu",
            "place":"ngl",
            "hobbie's":["songs","drawing","friend"],
            "sslc":{"maths":99,
                    "english":95,
                    "tamil":92,
                    "science":90,
                    "social":95}},
            {"name":"gayu",
            "place":"kottar",
            "hobbie's":["drawing","dance","music"],
             "sslc":{"maths":80,
                    "english":94,
                    "tamil":86,
                    "science":80,
                    "social":100}},
            {"name":"vinu",
              "place":"ethamozhy",
            "hobbie's":["song","movie","playing"],
             "sslc":{"maths":83,
                    "english":96,
                    "tamil":84,
                    "science":88,
                    "social":92}},
            {"name":"abisheck",
             "place":"kottar,",
            "hobbie's":["music","movie","browsing"],
             "sslc":{"maths":100,
                    "english":89,
                    "tamil":79,
                    "science":88,
                    "social":95}},
            {"name":"vj",
             "place":"marthandam",
            "hobbie's":["music","movie","cricket",],
             "sslc":{"maths":87,
                    "english":97,
                    "tamil":93,
                    "science":60,
                    "social":80}},]
for i in name_list:
    dic = i["sslc"]
    maths =dic["maths"]
    eng=dic["english"]
    tamil=dic["tamil"]
    sci=dic["science"]
    social=dic["social"]
    total=maths+eng+tamil+sci+social
    per=total/500*100
    name=i["name"]
    print(f" i am {name} my sslc percentage is {per}")

    if per>90:
        print("eligible to maths-bio" )
    elif per>80:
        print("eligible to computer science")
    elif per>75 and i["maths"]>98:
        print(" eligible to maths-bio")
    elif per<70 and i["maths"]>98:
        print("eligible to computer science")
    
        














    

    








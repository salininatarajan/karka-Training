my_resume={"name":"salini N",
            "E-mail":"salininatarajan06@gmail.com",
            "mobile-no":7695853511,
            "soft skills":["communication","creativity","problem solving"],
            "hard skills":["critical thinking","project management"],
            "educational qualification":[{"qualification":"sslc",
                                            "institude":"govt school vadasery",
                                            "percentage":85,
                                            "passed-out-year":2016},
                                          {"qualification":"hsc",
                                            "institude":"govt school vadasery",
                                            "percentage":80,
                                            "passed-out-year":2018},
                                           {"qualification":"bsc maths",
                                            "institude":"udhaya clg of arts and science",
                                            "percentage":86,
                                            "passed-out-year":2020},
                                            {"qualification":"msc maths",
                                            "institude":"govt clg of arts and science",
                                            "percentage":90,
                                            "passed-out-year":2023}],
            "projects":{"sub":"algebra",
                        "title":"gama semigroup"},
            "Experience":[{"company name":"google",
                           "role":"frontend developer",
                           "duration":1},
                           {"company name":"amazon",
                           "role":"fullstack",
                           "duration":1.5},
                           {"company name":"flipcart",
                           "role":"backend developer",
                           "duration":1.2}],
            "hobbies":["spending time with friends,listen music,dance,cooking,drawing"],
            "personal details":{"Father's name":"Natarajan B",
                                "Father's occupation":"cooli",
                                "languages known":["tamil","english"],
                                "DOB":"06-10-2000",
                                "Gender":"female",
                                "Martial status":"single",
                                "Address":{"door No":32,
                                           "street":"vellalar south street vadasery",
                                           "city":"nagercoil",
                                           "district":"kanyakumari",
                                           "state":"tamilnadu",
                                           "pincode":"629001"}}}
# print(my_resume["personal details"]["languages known"][1])
# level = (my_resume["educational qualification"])
# for i in level:
#     print(i["qualification"])

level = my_resume["personal details"]
# for key in level:
#     print(level[key])

add = level["Address"]
for key in add:
    print(key)
    print(add[key])
# for key,value in my_resume.items():
#     detail=(key)
#     detail2=(value)
#     print(f"{detail} : {detail2}")
# for value in my_resume.values():
#     print(value)
# for i in level:
#     if i=="pincode":
#         print(level[i])

#     if i=="district":
#         print(level[i])

# for i in level:
#     print(i["percentage"])






        




















































                                        



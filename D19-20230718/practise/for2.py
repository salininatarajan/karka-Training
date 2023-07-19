education_details=[{"study":"bsc maths",
                    "institute":"udhaya",
                    "semester_marks":[{"sem_name":1,
                                       "subjects":["algebra","statistic","topology","OR"],
                                       "sem_grade":"o+"},
                                       {"sem_name":2,
                                       "subjects":["algebra_2","statistic_2","topology_2","OR_2"],
                                       "sem_grade":"A+"}]},
                                       
                    {"study":"msc maths",
                    "institute":"govt arts and science",
                    "semester_marks":[{"sem_name":1,
                                       "subjects":["algebra","statistic","topology","OR"],
                                       "sem_grade":"o+"},
                                       {"sem_name":2,
                                       "subjects":["algebra_2","statistic_2","topology_2","OR_2"],
                                       "sem_grade":"A+"}]}]
marks=education_details[0]["semester_marks"]
for i in marks:
    # print(i)
    for grade in marks:
        print(grade["sem_grade"])
        #print(grade["sem_name"])
        
         



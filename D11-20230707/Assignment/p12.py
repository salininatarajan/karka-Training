def quizzz ():
    score = 0
    quiz = input("Are you ready for a quiz?")
    if quiz=="y":
       print(" Okay , here it comes!")
    else:
        return("thank you")
  
    qsn1 = input(f"""
    Q1)  What is the capital of alaska?
             1) melbourne
             2) Anchorage
             3) Juneau 
                Ans = """)
    if qsn1=="3":
        print("That's right ! ")
        score = score+1
    else:
        print("wrong")

    qsn2= input (f""" 
    Q2)  Can you store the value "cat" 
             1) yes
              2) no
                Ans = """)
    if qsn2=="1":
        print(" Sorry, 'cat' is a string. ints can only store nubers")
    else:
        print("wrong")    
        score = score+1


    qsn3 = input (f"""
    Q3) What is the result of 9+6/3? 
              1) 5
              2) 11
              3) 15/3
                Ans = """)
    if qsn3=="2":
        print(" That's correct")
        score=score+1
    print(f"""Overall , you got {score} out of 3 correct.
      Thanks for playing!""")
    
(quizzz())










    
    


    
    
    

    
    





    
    


def living():
    qsn1 = str(input(f"""
    TWO MORE QUESTIONS, BABY! 

    Think of something and I'll try to guess it !
                   
    Question 1) Does it stay inside or outside or both?
        """))
    qsn2= str(input(f"""is it a living thing?
        """))
    if qsn1=="inside" and qsn2=="yes":
        print("houseplant")
    if qsn1=="inside" and qsn2=="no":
        print("shower cutain")
    if qsn1=="outside" and qsn2=="yes":
        print("bison")
    if qsn1=="outside" and qsn2=="no":
        print("bill board")
    if qsn1=="both" and qsn2=="yes":
        print("dog")
    if qsn1=="both" and qsn2=="yes":
        print("cell phone")
living()






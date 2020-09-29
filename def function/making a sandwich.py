def sandwich():

    eatable={}
    
    bread_name1=input("enter name of bread: ")
    
    vorn1=input(" u veg or non veg: ")
    
    sandwich_name1=input("what would u like to call ur sandwich: ")
    
    eatable["bread_name"]=bread_name1

    eatable["vorn"]=vorn1
    
    eatable["sandwich_name"]=sandwich_name1

    feedback={}


    while True:

        feedbackfill=input("do u want to enter a feedback ? (yes or no):")
        
        if feedbackfill=="no":
            break
        
        if feedbackfill=="yes":
            valuename=input("enter your feedback: ")

            number=len(feedback)
            number+=1
            number=str(number)

            feedback_name=("feedback "+number)

            feedback.update({feedback_name:valuename})
            eatable.update(feedback)
            
    
    for d,e in eatable.items():    
        print(d+" : "+e)
    
sandwich()
    

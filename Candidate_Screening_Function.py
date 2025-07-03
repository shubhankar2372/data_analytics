#compute
def screeningResult(age,weight):
    if (age>=25 and age<=35):                       #A
        if (weight>=65 and weight<=85):
            if (age<30):
                if (weight<75):                     #B
                    eligible=True
                else:                               #C
                    eligible=False
            else:
                if (weight>=75):
                    eligible=True
                else:
                    eligible=False
        else:
            eligible=False
    else:
        eligible=False
    return eligible
      

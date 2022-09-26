inputAge = float(input("Enter person's age: "))



if (inputAge > -1 and inputAge <= 1 ) :

    print ("Person is an infant.")

 

elif ( inputAge > 1 and inputAge < 13 ) :

    print ("Person is a child.")

 

elif ( inputAge >= 13 and inputAge < 20 ) :

    print ("Person is a teenager.")

 

elif(inputAge >= 20):

    print ("Person is an adult.")

 
else:

    print("Invalid Age!!")

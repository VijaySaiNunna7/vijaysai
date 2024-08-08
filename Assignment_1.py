def main():
    first_name = input("Enter the first name ")    
    second_name = input("Enter the second name ")
    
    if first_name.isalpha() and second_name.isalpha():
        try: 
           age=int(input("Enter the age "))
        except ValueError:
           print("please enter valid age ")
           return
        full_name=(first_name+second_name)
        if age <= 0:
            print(f"your full name is {full_name} and please enter a valid age" )
        elif age < 18 :
            print(f"your full name is {full_name} and you are a minor" )
        elif age >= 18 and age<69:
            print(f"your full name is {full_name} and you are a major" )  
        else :
           print(f"your full name is {full_name} and you are a senior citizen" )
    else:
        print("please enter valid name")


     
if __name__ == "__main__":
    print("Glad to see you here ")
    main()
    print("Thank you")

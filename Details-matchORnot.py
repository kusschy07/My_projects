
try:
    full_name = str(input("Enter your Name: "))

    valid_name = ["kush chaudhary", "Ram chaudhary", "shyam", "Hari"]

    age = int(input("Enter your Age: "))


    position = str(input("Enter your Position: "))

    if full_name not in valid_name or age != 18:
        raise ValueError
    

    employee_details = f'Name: {full_name} | Age: {age} | Position: {position}'
    print("This employee details is:", employee_details)

except ValueError:
    print("The details you enter is not match, Please try again!")




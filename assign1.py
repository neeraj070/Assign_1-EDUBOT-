import re
import sys
import os
import logging

# Configure logging
logging.basicConfig(filename='app_logs.txt',level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s');

#Valid age checking
def validAge(age):
    age = age.strip();
    agepattern = r'^-?\d+$';
    if not re.match(agepattern, age):
        return False;
    age = int(age);
    if age <= 0:
        return False;
    
    return True;

#Getting Age category
def get_age_category(age):
    if age < 18:
        return "Underaged";
    elif age>=18 and age <= 60:
        return "Adult";
    else:
        return "Senior";

#Valid user check
def ValidUser(name,email,age):
    namepattern = r'^[a-zA-Z\s]+$';
    emailpattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$';
    if not re.match(namepattern,name):
        logging.warning(f"Invalid name entered: {name}");
        return False;
    if not re.match(emailpattern,email):
        logging.warning(f"Invalid email entered: {email}");
        return False;
    if not validAge(age):
        logging.warning(f"Invalid age entered: {age}");
        return False;
    
    return True;

#Adding users
def addUser():
    name = input("Enter the name: ");
    email = input("Enter the email: ");
    age = input("Enter your age: ");
    print("\n");
    if(ValidUser(name,email,age)):
        logging.info(f"Valid user entered: Name={name}, Email={email}, Age={age}");
        return True, name, email, age;

    logging.warning(f"User data invalid: Name={name}, Email={email}, Age={age}");
    return False, name, email, age;

#Saving entered users
def save_data(name,email,age,category):
    try:
        with open("user_data.txt",'a') as f:
            f.write(f"Name: {name}, Email: {email}, Age: {age}, Category: {category}\n");
        logging.info(f"Saved user data: Name={name}, Email={email}, Age={age}, Category={category}");
    except Exception as e:
        logging.error(f"Error while saving data: {e}");
        print("Error while saving data:", e);

#Viewing available users
def view_users():
    filename = 'user_data.txt';
    
    if not os.path.exists(filename):
        print("\nNo user data file found.\n");
        logging.info("No user data file found to view.");
        return False;

    try:
        with open(filename, 'r') as file:
            lines = file.readlines();

            if not lines:
                print("\nUser data file is empty.");
                logging.info("User data file is empty.");
                return True;

            print("\n----- Saved User Data -----\n");
            for idx, line in enumerate(lines, start=1):
                print(f"{idx}. {line.strip()}\n");
    except Exception as e:
        logging.error(f"Error reading user data file: {e}");
        print("Error reading user data file:", e);
        return False;

# Main function starts
while True:
    print("\n----------------VISA MOCK INTERVIEW SYSTEM UTILITY--------------\n");
    print("1)Add Users\n");
    print("2)View Users\n");
    print("3)Exit the program\n");

    try:
        choice = int(input("Enter your choice(1-3): "));
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.\n");
        logging.warning("Non-integer input for menu choice.");
        continue;

    if choice==1:
        success, name, email, age = addUser();
        if(success):
            print("User entered succesfully\n");
            category = get_age_category(int(age));
            save_data(name,email,age,category);
        else:
            print("Entered data is not valid!(Please enter valid Details)\n");
            addUser();
            
    elif choice==2:
        if(view_users()):
            print("No Data is available to view.\n");
            
    elif choice==3:
        print("Exiting the program...");
        logging.info("Program exited by user.");
        sys.exit();
    else:
        print("Invalid Choice.");
        logging.warning(f"Invalid menu choice entered: {choice}");

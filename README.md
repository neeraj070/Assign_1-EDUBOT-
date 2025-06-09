# Building_LLM_powered_apps_using_APIs_Short_Term_Module_1

# -------VISA MOCK INTERVIEW SYSTEM--------

# -----OVERVIEW-------
This project is a basic utility script developed for the Visa Mock Interview System (VMIS). It collects users data such as name, email, age and validate it, and based on the validation it classifies users based on age, and stores the data for future use.

# ------REQUIRMENTS-----
1)Python 3.6 or higher

# -----FILES---------
1)code.py - Contains main python script and excecution with the required functionality.
2)app_logs.txt - This helps to keep a track on the loggings automatically.
3)user_data.txt - This helps in storing the entered users data.
4)test_cases.txt - These are some test cases with inputs and their respective outputs.
5)README.md(This File) - This file has a detailed explaination on how the script works and how the respective files have been created, used.

# --------PROGRAM FLOW----------
Asks the user to choose their choice based on the given menu as,
1)Add Users
2)View Users
3)Exit the program

# -----IF CHOICE = 1-----
Provides some questions and ask user to enter the details as,
name:
email:
age:

# -----VALIDATION CHECKING-----
For every respective inputs we have different functions to check whether the entered data is valid or not. In, the script this validation is achieved by the pattern matching concept or import of "re" module. With this the respective data is getting validated and the respective error messages are getting printed(if errors exists).

# -------AGE_CATEGORY--------
Defined the age categories as,
Age < 18 - "Underaged"
Age >=18 && Age <= 60 - "Adult"
Age > 60 - "Senior"

# ------IF CHOICE = 2-----
Just by making our choice as "2", the script has the defined function to print the available users. If the users are not available then prints as "Data file is empty", if any data is available then it directly print it.

# -------IF CHOICE = 3------
By making choice "3", this means the user is trying to exit the program. So, the script has the module "sys" imported which here it uses to exit the program as soon as user make the choice as "3".

# -------- IF CHOICE <= 0 OR > 3--------
If choice is entered as number other than (1,2,3), then this shows an "Invalid choice message", and again it asks the user to input the choice again.

# ---------FILE FUNCTIONALITIES-----------
1) Entered Valid data will be saved to "user_data.txt".
2) After each & every choice or data we enter the respective message such as errors,info,messages will be stored in the 
"app_logs.txt".

# ---------Menu-Driven Interface----------
Allows adding users, viewing data, or exiting.

# ---------Notes---------
1) The menu-based system is designed to be user-friendly, with clear error messages and logging.
2) The program adds the data to "user_data.txt", without overwriting the already existed data.
3) Logs are saved to "app_logs.txt".

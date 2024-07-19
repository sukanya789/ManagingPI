# ManagingPI
Overview:

This project is a Personal Information Manager that allows you to add and retrieve personal information such as names and dates of birth (DOB). The data is persisted using Python's pickle module, ensuring the information is saved between sessions.

Features:

Add Personal Information: Add names and dates of birth, with the option to mark some DOBs as secret.
Retrieve Personal Information: Retrieve the DOB of a person, with the option to hide secret DOBs.
Data Persistence: Information is saved to a file (problem1_data_file.pickle) and loaded on startup.
Input Validation: Proper validation and error handling for user inputs, with retry attempts for incorrect inputs.
Logging: Logs actions and errors for debugging and tracking purposes.
Prerequisites
Python 3.x


Data Structure:

The data is stored in a dictionary format, where each key is a person's name, and the value is another dictionary containing their DOB and a flag indicating if the DOB is secret. Here is an example: {
    "John Doe": {"dob": "1990-01-01", "secret": False},
    "Jane Doe": {"dob": "1992-02-02", "secret": True}
}




Code Explanation:


PersonalInfoManager Class
__init__(self, data_file='problem1_data_file.pickle'):
Initializes the manager with a data file and loads existing data.

load_data(self):
Loads data from the pickle file. If the file is not found or is empty, it starts with an empty dictionary.

save_data(self):
Saves the current state of data to the pickle file.

add_person(self, name, dob, is_secret=False):
Adds a person's information to the data dictionary and saves it.

get_dob(self, name):
Retrieves the DOB of a person. Returns "secret" if the DOB is marked as such, or "Person not found" if the person does not exist.

input_with_retries(self, prompt, validation_func, error_message, max_retries=3):
Prompts the user for input with validation and retries up to three times if the input is invalid.

exit_application(self):
Saves the data and exits the application.

run(self):
The main loop that provides options to add a person, get a DOB, or exit the program.

validate_dob(dob):
A static method that validates the DOB format (YYYY-MM-DD).

import pickle
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PersonalInfoManager:
    def __init__(self, data_file='problem1_data_file.pickle'):
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, 'rb') as f:
                logging.info(f"Loading data from {self.data_file}")
                return pickle.load(f)
        except FileNotFoundError:
            logging.warning(f"{self.data_file} not found. Starting with an empty database.")
            return {}
        except EOFError:
            logging.warning(f"{self.data_file} is empty. Starting with an empty database.")
            return {}
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            return {}

    def save_data(self):
        try:
            with open(self.data_file, 'wb') as f:
                pickle.dump(self.data, f)
                logging.info(f"Data saved to {self.data_file}")
        except Exception as e:
            logging.error(f"Error saving data: {e}")

    def add_person(self, name, dob, is_secret=False):
        self.data[name] = {'dob': dob, 'secret': is_secret}
        self.save_data()

    def get_dob(self, name):
        person = self.data.get(name)
        if person:
            if person['secret']:
                logging.info(f"DOB for {name} is secret")
                return "secret"
            else:
                logging.info(f"DOB for {name} retrieved")
                return person['dob']
        logging.warning(f"Person {name} not found")
        return "Person not found"

    def input_with_retries(self, prompt, validation_func, error_message, max_retries=3):
        for attempt in range(max_retries):
            value = input(prompt)
            if validation_func(value):
                return value
            print(error_message)
            logging.warning(f"Invalid input: {value} (attempt {attempt + 1} of {max_retries})")
        print("Max retries reached. Exiting.")
        logging.error("Max retries reached for input")
        return None

    def exit_application(self):
        self.save_data()
        print("Data saved. Exiting application.")

    def run(self):
        while True:
            print("\nOptions: 1. Add Person 2. Get DOB 3. Exit")
            option = input("Enter option number: ")

            if option == '1':
                name = self.input_with_retries("Enter name: ", lambda x: bool(x.strip()), "Invalid name.")
                if not name:
                    continue
                dob = self.input_with_retries("Enter DOB (YYYY-MM-DD): ", self.validate_dob, "Invalid DOB format.")
                if not dob:
                    continue
                is_secret_input = self.input_with_retries("Is this DOB secret? (yes/no): ", lambda x: x in ['yes', 'no'], "Enter 'yes' or 'no'.")
                if not is_secret_input:
                    continue
                is_secret = is_secret_input == 'yes'
                self.add_person(name, dob, is_secret)
                print(f"Added: {name}")

            elif option == '2':
                name = input("Enter name to retrieve DOB: ")
                dob = self.get_dob(name)
                print(f"DOB of {name}: {dob}")

            elif option == '3':
                self.exit_application()
                break

            else:
                print("Invalid option. Try again.")

    @staticmethod
    def validate_dob(dob):
        try:
            datetime.strptime(dob, '%Y-%m-%d')
            return True
        except ValueError:
            return False

if __name__ == "__main__":
    manager = PersonalInfoManager()
    manager.run()










# PROJECT: FILE OPERATOR


import os
from datetime import datetime



class JournalManager:

    def __init__(self):
        self.filename = "journal.txt"


    def add_entry(self):

        print("\nEnter your journal entry:")
        entry = input()


        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:

            if not os.path.exists(self.filename):

                with open(self.filename, "x") as file:
                    file.write(f"[{current_time}]\n")
                    file.write(entry + "\n\n")

            else:

                with open(self.filename, "a") as file:
                    file.write(f"[{current_time}]\n")
                    file.write(entry + "\n\n")

            print("\nEntry added successfully!")

        except PermissionError:
            print("\nError: Permission denied. Cannot write to the journal file.")

        except Exception as e:
            print("\nError:", e)



    def view_entries(self):

        try:

            with open(self.filename, "r") as file:
                content = file.read()


            if content.strip() == "":
                print("\nNo journal entries found. Start by adding a new entry!")
                return

            print("\nYour Journal Entries:")
            print("------------------------------")
            print(content, end="")

        except FileNotFoundError:
            print("\nNo journal entries found. Start by adding a new entry!")

        except PermissionError:
            print("\nError: Permission denied. Cannot read the journal file.")

        except Exception as e:
            print("\nError:", e)



    def search_entry(self):

        keyword = input("\nEnter a keyword or date to search: ")

        try:

            with open(self.filename, "r") as file:
                content = file.read()


            entries = content.strip().split("\n\n")

            found = False

            print("\nMatching Entries:")
            print("------------------------------")

            for entry in entries:

                if keyword.lower() in entry.lower():
                    print(entry)
                    print()
                    found = True

            if not found:
                print(f"No entries were found for the keyword: {keyword}.")

        except FileNotFoundError:
            print(
                "\nError: The journal file does not exist. "
                "Please add a new entry first."
            )

        except PermissionError:
            print("\nError: Permission denied. Cannot read the journal file.")

        except Exception as e:
            print("\nError:", e)



    def delete_entries(self):

        try:

            if not os.path.exists(self.filename):
                print("\nNo journal entries to delete.")
                return

            confirmation = input(
                "\nAre you sure you want to delete all entries? (yes/no): "
            )

            if confirmation.lower() == "yes":


                with open(self.filename, "w") as file:
                    file.write("")


                os.remove(self.filename)

                print("\nAll journal entries have been deleted.")

            elif confirmation.lower() == "no":
                print("\nDeletion cancelled.")

            else:
                print("\nInvalid input. Please enter yes or no.")

        except PermissionError:
            print("\nError: Permission denied. Cannot delete the journal file.")

        except Exception as e:
            print("\nError:", e)



    def run(self):

        while True:

            print("\n===================================")
            print("Welcome to Personal Journal Manager!")
            print("===================================")

            print("\nPlease select an option:\n")

            print("1. Add a New Entry")
            print("2. View All Entries")
            print("3. Search for an Entry")
            print("4. Delete All Entries")
            print("5. Exit")

            choice = input("\nEnter your choice: ")



            if choice == "1":
                self.add_entry()



            elif choice == "2":
                self.view_entries()



            elif choice == "3":
                self.search_entry()


            elif choice == "4":
                self.delete_entries()



            elif choice == "5":
                print("\nThank you for using Personal Journal Manager. Goodbye!")
                break


            else:
                print("\nInvalid option. Please select a valid option from the menu.")




journal = JournalManager()

journal.run()
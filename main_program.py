"""
Vincent Nguyen
Class: CS 521 - Summer 2
Date: August 18
Term Project
Description of Problem (1-2 sentence summary in your own words):
Budget tracker transaction, can either using existing data or create new data.
Get output report file after transactions.
"""
import glob
import budget_function
from budget_function import Budget

if __name__ == "__main__":

    name = input("What is your name: ")
    print(f"Hi {name}!. Welcome to Budget App. \n")
    msg = True
    while msg:
        # choose the option.
        option = budget_function.option()
        if option == "1":
            # option 1 for create budget list from scratch.
            budget_l = budget_function.budget_set()
        elif option == "2":
            # option 2 for add new category to existing file.
            add_cate = budget_function.add_cate_budget()
        else:
            # this option will use to make transactions and get output report file.
            while True:
                try:
                    # get list all of existing text files in folder.
                    text_files = [file for file in glob.glob("*.txt")]
                    print(f"\nHere are list existing budget files {text_files}")

                    # Enter file name which you want to make transactions.
                    file_name_input = input(f"\nEnter budget file' name '.txt': ")
                    print(f"Your budget details in '{file_name_input}':\n")

                    # Open file name in read mode and print out contents in it.
                    with open(file_name_input, "r") as file:
                        print(next(file))
                        for line in file:
                            line_cl = Budget.from_file(line) 
                            print(f"Your budget on '{line_cl.category_name()}': {line_cl.budget_s():,} USD")
                
                except FileNotFoundError:
                    print(f"Unfortunately, '{file_name_input}' file not exist. Try again.")
                
                else:
                    # Make transaction and create report after transactions.
                    file_report = budget_function.budget_after(file_name_input)  
                    print(f"Your latest budget report' name:'{file_report}'")
                    break
                
        # Ask user whether exit or re-run program.            
        inp2 = input("\nEnter M to main options or any key to exit: ")
        if inp2.upper() != "M":
            msg = False       
    print("\nGoodbye!. Thanks for using Budget App.\n")


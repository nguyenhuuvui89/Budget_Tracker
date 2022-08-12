import sys
import budget_function
from budget_function import Budget
def main():
    name = input("What is your name: ")
    print(f"Hi {name}!. Welcome to Budget App. \n")
    inp = input("Would you like to set up your budget? Y/N: ")
    if inp.upper() == "Y":
        budget_function.budget_set()
    else:
        print("Goodbye!")
        sys.exit()
    while True:
        inp2 = input("\nDo you want to make transactions:Y/N: ")
        if inp2.upper() == "Y":
            while True:
                try:
                    file_name_input = input(f"\nEnter your budget file '.txt': ")
                    print(f"Your budget details in '{file_name_input}':\n")
                    with open(file_name_input, "r") as file:
                        for line in file:
                            line_cl = Budget.from_file(line) 
                            print(f"Your budget on '{line_cl.category_name()}': ${line_cl.budget_s():,} USD")
                except FileNotFoundError:
                    print(f"Unfortunately, '{file_name_input}' file not exist. Try again.")
                else:
                    file_report = budget_function.budget_after(file_name_input)  
                    print(f"Your latest budget report name after transactions:'{file_report}'")
                    break
        else:
            print("\nGoodbye!. Thanks for using Budget App.\n")
            sys.exit()

if __name__ == "__main__":
    main()

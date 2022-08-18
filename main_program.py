import budget_function
from budget_function import Budget

if __name__ == "__main__":
    msg = True
    while msg:
        option = budget_function.introduction()
        if option == "1":
            budget_function.budget_set()
        else:
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
                    print(f"Your latest budget report' name:'{file_report}'")
                    break
  
        inp2 = input("\nDo you want re-run program (Y to cont): ")
        if inp2.upper() != "Y":
            msg = False       
    print("\nGoodbye!. Thanks for using Budget App.\n")


import budget_cls as bd
import sys

def budget_set (): # Create categories and budget.
    budget_dict = {}
    categories = set()
    while True:
        inp_categories  = input("Add new category: ")
        while True:
            try:
                category_budget = int(input(f"Set your budget (as int in USD) for '{inp_categories}': "))
                break
            except:
                print("Invalid value. Try again")
        budget_dict[inp_categories] = category_budget
        categories.add(inp_categories)
        completed_budget_add = input("\nEnter Y if completed add or press any key to continue: ")
        if completed_budget_add.upper() == "Y":
            break

    print(f"\nHere are your expenses's categories: {categories}")
    print("As detail below:")

    budget_dict_s = sorted(budget_dict.items())
    for key, value in budget_dict_s:
        print('Budget for "{}": {:,} USD'.format(key,value))
    file_name = input('Name your budget file in ".txt": ')
    with open(file_name,"w") as wf:
        for k, v in budget_dict_s:
            wf.write('{} : {:,} USD\n'.format(k,v))
    return (budget_dict_s, categories, file_name)
    
def budget_after (file_inp):   
    '''Create function to calculate budget after transactions
    read and write file before and after transactions'''
    
    with open(file_inp, "r") as rf:
        file_name_output = input("\nName your budget file after transactions in '.txt': ")
        with open(file_name_output, "w") as wf:
            for line in rf:
                cate = bd.Budget.from_file(line)
                while True:
                    inp = input(f"How much did you spend on '{cate.category_name()}' (as int in USD): ")
                    if inp.isnumeric():
                        inp = int(inp)
                        break
                    else:
                        print("Invalid value. Try again.")
                budget_aft_trans = cate.transaction(inp)
                print(f"Your budget on '{cate.category_name()}': ${cate.budget_s()} - ${inp} = {budget_aft_trans:,} USD\n")
                wf.write('{} : {:,} USD\n'.format(cate.category_name(),budget_aft_trans))
    return file_name_output

def main():
    name = input("What is your name: ")
    print(f"Hi {name}!. Welcome to Budget App. \n")
    inp = input("Would you like to set up your budget? Y/N: ")
    if inp.upper() == "Y":
        budget_set()
    else:
        print("Goodbye!")
        sys.exit()
    while True:
        inp2 = input("\nDo you want to make transactions:Y/N: ")
        if inp2.upper() == "Y":
            while True:
                try:
                    file_name_input = input(f"\nEnter your budget file '.txt': ")
                    print(f"Confirmed your budget file input is '{file_name_input}'.")
                    file_report = budget_after(file_name_input)    
                except FileNotFoundError:
                    print(f"'{file_name_input}' not exist. Try again.")
                else:
                    print(f"Your latest budget report' name after transactions:'{file_report}'")
                    break
        else:
            print("Goodbye!")
            sys.exit()

if __name__ == "__main__":
    main()
    
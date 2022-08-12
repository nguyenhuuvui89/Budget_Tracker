def budget_set (): # Create categories and budget.
    budget_dict = {}
    categories_lst = []
    while True:
        inp_categories  = input("Add new category: ")
        while True:
            try:
                category_budget = int(input(f"Set your budget (as int in USD) for '{inp_categories}': "))
                break
            except:
                print("Invalid value. Try again")
        budget_dict[inp_categories] = category_budget
        categories_lst.append(inp_categories)
        completed_budget_add = input("Enter Y if completed add or press any key to continue: ")
        if completed_budget_add.upper() == "Y":
            break
    
    print(f"Here are the list of your expenses's categories: {sorted(categories_lst)}")
    print("As detail below:")
    for key, value in sorted(budget_dict.items()):
        categories_lst.append(key)
        print('Budget for "{}": {:,} USD'.format(key,value))
    file_name = input('Name your budget file in ".txt": ')
    with open(file_name,"w") as wf:
        for k, v in sorted(budget_dict.items()):
            wf.write('Budget for {}: {:,} USD\n'.format(k,v))

    return budget_dict

def transaction_act (budget_dict): # Calculate budget remaining after transactions.
    budget_aft_trans = {}
    for k, v in sorted(budget_dict.items()):
        while True:
            inp = input(f"How much did you spend on '{k}' (as int in USD): ")
            if inp.isnumeric():
                inp = int(inp)
                break
            else:
                print("Invalid value. Try again.")
        budget_aft_trans[k] = v - inp
    file_name_output = input("Name your budget file after transactions in '.txt': ")
    with open(file_name_output, "w") as wf:
        for k, v in sorted(budget_dict.items()):
            wf.write('Budget for {} after transactions: {:,} USD\n'.format(k,v))

    return budget_aft_trans
if __name__ == '__main__':
    print("Please set your budget categories")
    budget_categories = budget_set ()
    budget_cate_aft_trans = transaction_act (budget_categories)
    for k, v in sorted(budget_cate_aft_trans.items()):
        print(f"The remaining money for '{k}': {v} USD")

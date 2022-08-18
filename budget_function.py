import datetime
class Budget:
    def __init__(self, category, budget_set, budget_dev = None):
        self.category = category
        self.__budget_set = budget_set
        self.budget_after_trans = budget_set
        self.budget_dev = budget_dev

    def category_name(self):
        return self.category

    def budget_s(self):
        return self.__budget_set
        
    def __transaction(self, trans_amount):
        self.budget_after_trans -= trans_amount
        return self.budget_after_trans

    def wf_budget_trans (self, trans_amount):
        return '{} : {:,} USD\n'.format(self.category_name(),self.__transaction(trans_amount))

    def budget_d (self):
        self.budget_dev = self.budget_after_trans
        if self.budget_dev >= 0:
            return f"{self.category_name()}' budget remain {self.budget_dev:,} USD.\n"
        else:
            return f"{self.category_name()}' budget is overdraft ${self.budget_dev:,} USD.\n"

    def transaction_msg (self, trans_amount):
        return f"Your '{self.category_name()}' budget: ${self.budget_s():,} - ${trans_amount:,} = {self.budget_after_trans:,} USD"

    @classmethod
    def from_file(cls, line):
        line_lst = line.rstrip(" USD\n").split(" : ")
        category, budget_from_file = line_lst
        budget_from_file = int(budget_from_file.replace(",",""))
        return cls(category, budget_from_file)

    def __add__(self, other):
        return f"Sum budget '{self.category}' and '{other.category}':\
                 {self.__budget_set + other.__budget_set} USD."
    
    def __len__(self):
        return len(self.category)

    def __str__(self):
        return f"The budget set for {self.category}:\
             {self.__budget_set:,} USD"

# Divide:

def date_inp():
    date_str = input('\nWhen was the transaction? (YYYY-MM-DD): ')
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Incorrect formate. Try again.")
        return date_inp()
    return date_str

def budget_set (): # Create categories and budget.
    budget_dict = {}
    categories = set()
    file_date = date_inp()
    while True:
        inp_categories  = input("Add new category: ")
        print()
        while True:
            try:
                category_budget = int(input(f"Set your budget (int) for '{inp_categories}': $"))
                break
            except:
                print("Invalid value. Try again")
        # Check if new category input exist or not
        if inp_categories in budget_dict: # new category exist, budget will be combine.
            budget_dict[inp_categories] += category_budget
        else: 
            budget_dict[inp_categories] = category_budget
        categories.add(inp_categories)
        completed_budget_add = input("\nY - completed or any key to continue: ")
        if completed_budget_add.upper() == "Y":
            break

    print(f"\nYour expenses's categories on {file_date}: {categories}")
    print("As detail below:")

    budget_dict_s = sorted(budget_dict.items())
    
    for key, value in budget_dict_s:
        print('Budget for "{}": {:,} USD'.format(key,value))

    file_name = input('\nName your budget file in ".txt": ')
    with open(file_name,"w", newline="") as wf: # Write categories and budget into text file.
        wf.write(f"File has been saved on {file_date}.\n")
        for k, v in budget_dict_s:
            wf.write('{} : {:,} USD\n'.format(k,v))
    return (budget_dict_s, categories, file_name)
    
def budget_after (file_inp):   
    '''Create function to calculate budget after transactions
        read and write file before and after transactions'''
    
    with open(file_inp, "r") as rf:
        file_name_output = input("\nEnter report' name after transaction in '.txt': ")
        next(rf)
        with open(file_name_output, "w") as wf:
            file_date = date_inp()
            wf.write(f"File has been saved on {file_date}.\n")
            for line in rf:
                cate = Budget.from_file(line)
                while True:
                    inp = input(f"How much did you spend on '{cate.category_name()}' (int):$ ")
                    if inp.isnumeric():
                        inp = int(inp)
                        break
                    else:
                        print("Invalid value. Try again.")
                wf.write(cate.wf_budget_trans(inp))
                print(cate.transaction_msg(inp))
                print(cate.budget_d())
    return file_name_output

def introduction ():

    name = input("What is your name: ")
    print(f"Hi {name}!. Welcome to Budget App. \n")
    print("Choose options below:\n", 
        "1. Set your own budget's list. \n",
        "2. Use exist budget's list. " )
    while True:
        inp = input("Which option do you choose? 1 or 2: ")
        if inp == "1" or inp == "2":
            return inp
        else:
            print("Please type 1 or 2 only.")

if __name__ == "__main__":
    ca1 = Budget("House", 450)
    ca2 = Budget("Food", 200)
    
    assert ca1.wf_budget_trans(50) == "House : 400 USD\n", "Out put is wrong"
    print("Test 1 is passed.")

    assert ca1.budget_s() == 450, "Value is wrong"
    print("Test 2 is passed.")

    assert ca2.__len__() == 4, "Value is wrong"
    print("Test 3 is passed.")
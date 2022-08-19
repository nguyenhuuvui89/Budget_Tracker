"""
Vincent Nguyen
Class: CS 521 - Summer 2
Date: August 18
Term Project
Description of Problem (1-2 sentence summary in your own words):
Budget tracker transaction, can either using existing data or create new data.
Get output report file after transactions.
"""
import datetime
import glob

class Budget:
    '''This class constructs the Budget Objects and its attributes'''
    def __init__(self, category, budget_set, budget_dev = None):
        '''Initialize constructor.'''
        self.category = category
        self.__budget_set = budget_set
        self.budget_after_trans = None
        self.budget_dev = budget_dev

    def category_name(self):
        '''Return category name.'''
        return self.category

    def budget_s(self):
        '''Return budget amount'''
        return self.__budget_set
        
    def __transaction(self, trans_amount):
        '''Return budget amount after making transactions'''
        self.budget_after_trans = self.__budget_set - trans_amount
        return self.budget_after_trans

    def budget_remain(self):
        "Return budget after transaction."
        return self.budget_after_trans

    def wf_budget_trans (self, trans_amount):
        '''Return message of category after making 
        transactions and use this to write to text file.'''
        return '{} : {:,} USD\n'.format(self.category_name(),self.__transaction(trans_amount))

    def budget_d (self):
        '''Check if budget amount is remain positive or 
        overdraft after transactions and return string for display purpose.'''
        self.budget_dev = self.budget_after_trans
        if self.budget_dev >= 0:
            return f"{self.category_name()}' budget remain {self.budget_dev:,} USD.\n"
        else:
            return f"{self.category_name()}' budget is overdraft {self.budget_dev:,} USD.\n"

    def transaction_msg (self, trans_amount):
        '''Return string to explain the transaction 
        calculation and use it for display purpose.'''
        return (f"{self.category_name()}' budget: ${self.budget_s():,} - ${trans_amount:,} = {self.budget_after_trans:,} USD.")

    @classmethod
    def from_file(cls, line):
        '''This use to exact data from text file (category, budget amount)
        return them and use to create Object.'''
        line_lst = line.rstrip(" USD\n").split(" : ")
        category, budget_from_file = line_lst
        budget_from_file = int(budget_from_file.replace(",",""))
        return cls(category, budget_from_file)

    def __add__(self, other):
        '''Return sum of budget of 2 categories.'''
        return (self.__budget_set + other.__budget_set)
    
    def __len__(self):
        '''Return length of category.'''
        return len(self.category)

    def __str__(self):
        '''Return string to show category and its budget.'''
        return f"The budget set for {self.category}: {self.__budget_set:,} USD"

def date_inp():
    '''Create function to record date of the file create.'''
    date_str = input('\nWhen was the transaction? (YYYY-MM-DD): ')
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Incorrect formate. Try again.")
        return date_inp()
    return date_str

def add_cate_budget ():
    '''This function use to add new category to the existing budget file.'''
    add_category = set()
    # List all existing budget file.
    text_files = [file for file in glob.glob("*.txt")]
    print(f"\nHere are list existing budget files {text_files}")
    while True:
        file_n = input("Enter file name to be added (.txt): ")
        if file_n in text_files:
            break
        else:
            print("Your file does not exist. Try input files in list.")
    # Open file and append new category to file.
    with open (file_n,"a") as af:
        while True:
            add_cate = input("Add new category: ")
            while True:
                    try:
                        add_budget = int(input(f"Add your budget (int) for '{add_cate}': $"))
                        break
                    except:
                        print("Invalid value. Try again")
            af.write('{} : {:,} USD\n'.format(add_cate,add_budget))
            add_category.add(add_cate)
            completed_add = input("\nY - completed or any key to continue: ")
            if completed_add.upper() == "Y":
                break
    print(f"Here are added categories: {add_category}")
    return file_n

def budget_set ():
    '''Create function to create own budget list from scratch.'''
    budget_dict = {}
    categories = set()
    file_date = date_inp()
    while True:
        inp_categories  = input("Add new category: ")
        categories.add(inp_categories)
        print()
        while True:
            try:
                category_budget = int(input(f"Set your budget (int) for '{inp_categories}': $"))
                break
            except:
                print("Invalid value. Try again")
        # Check if new category input exist or not
        # If user input existing category' name, I will let budget combined.
        if inp_categories in budget_dict: 
            print("Category is existing. Budget will be combined.")
            budget_dict[inp_categories] += category_budget
        else: 
            budget_dict[inp_categories] = category_budget
            
        completed_budget_set = input("\nY - completed or any key to continue: ")
        if completed_budget_set.upper() == "Y":
            break

    print(f"\nYour input categories'name: {categories}")
    print("As detail below:")

    budget_dict_s = sorted(budget_dict.items())
    # Print out the message to display category and it's budget.
    for key, value in budget_dict_s:
        print('Budget for "{}": {:,} USD'.format(key,value))

    # Name the output report.
    file_name = input('\nName your budget file in ".txt": ')
    with open(file_name,"w", newline="") as wf: 
        # Open and write categories and budget into text file w/ user input' date.
        wf.write(f"File has been saved on {file_date}.\n")
        for k, v in budget_dict_s:
            wf.write('{} : {:,} USD\n'.format(k,v))

    return (categories, file_name)
    
def budget_after (file_inp):   
    '''Create function to calculate budget after transactions
        read and write file before and after transactions'''
    # open file in read mode.
    with open(file_inp, "r") as rf:
        file_name_output = input("\nEnter report' name after transaction in '.txt': ")
        next(rf)
        # open and write to file.
        with open(file_name_output, "w") as wf:
            budget_aft = set()
            file_date = date_inp()
            # Write date which provided by user.
            wf.write(f"File has been saved on {file_date}.\n")
            for line in rf:
                # loop through line in file.
                cate = Budget.from_file(line)
                # create Objects using Budget class.
                while True:
                    inp = input(f"How much did you spend on '{cate.category_name()}' (int): $")
                    if inp.isnumeric():
                        inp = int(inp)
                        break
                    else:
                        print("Invalid value. Try again.")
                # write to file using Budget method.
                wf.write(cate.wf_budget_trans(inp))
                # print out message to show to user by using Budget methods.
                print(cate.transaction_msg(inp))
                print(cate.budget_d())
                budget_aft.add('{} : {:,} USD'.format(cate.category_name(),cate.budget_remain()))
            print(f"Summary of budget after transaction: {budget_aft}")
    return file_name_output

def option ():
    '''This show options which user can use in program.'''

    print("Choose options below:\n", 
        "1. Set your own budget's list. \n",
        "2. Add new categories to existing budget' list. \n",
        "3. Use exist budget's list to make transactions. ")
    while True:
        inp = input("Which option do you choose? 1 or 2 or 3: ")
        if inp == "1" or inp == "2" or inp == "3":
            return inp
        else:
            print("Please type 1, 2 or 3 only.")

if __name__ == "__main__":
    # create Objects for testing methods purposes.
    ca1 = Budget("House", 450)
    ca2 = Budget("Food", 200)
    sum = ca1 + ca2
    cate_len = ca1.category_name()
    ca2.wf_budget_trans(50)
    print(ca1)

    # Test methods.
    assert ca2.budget_after_trans == 150, "Output is wrong"
    print("Test 1 is passed.")
    assert ca1.__add__(ca2) == sum, "Output value is wrong"
    print("Test 2 is passed.")
    assert ca1.__len__() == len(cate_len), "Value is wrong"
    print("Test 3 is passed.")
    assert ca2.budget_d() == f"{ca2.category_name()}' budget remain {ca2.budget_dev:,} USD.\n", "Value is wrong"
    print("Test 4 is passed.")
    assert ca2.budget_remain() == ca2.budget_after_trans, "Value is wrong"
    print("Test 5 is passed.")

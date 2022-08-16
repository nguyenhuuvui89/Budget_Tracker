import datetime
class Budget:
    def __init__(self, category, budget_set, budget_dev = 0):
        self.category = category
        self.__budget_set = budget_set
        self.budget_after_trans = budget_set
        self.budget_dev = 0
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
        if self.budget_dev> 0:
            return f"{self.category_name()}' budget remain {self.budget_dev}"
        else:
            return f"{self.category_name()}' budget is overdraft ${self.budget_dev}"

    def transaction_msg (self, trans_amount):
        return f"Your '{self.category_name()}' budget: ${self.budget_s():,} - ${trans_amount:,} = {self.budget_after_trans:,} USD\n"

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
    date_str = input('When was the transaction? (YYYY-MM-DD): ')
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Incorrect formate. Try again.")
        return date_inp()
    return date_str

def budget_set (): # Create categories and budget.
    budget_dict = {}
    categories = set()
    while True:
        inp_categories  = input("Add new category: ")
        while True:
            try:
                category_budget = int(input(f"Set your budget (as int in USD) for '{inp_categories}': $"))
                break
            except:
                print("Invalid value. Try again")
        # Check if new category input exist or not
        if inp_categories in budget_dict: # new category exist, budget will be combine.
            budget_dict[inp_categories] += category_budget
        else: 
            budget_dict[inp_categories] = category_budget
        categories.add(inp_categories)
        completed_budget_add = input("\nEnter Y if completed add or press any key to continue: ")
        if completed_budget_add.upper() == "Y":
            break

    print(f"\nYour expenses's categories on {date_inp()}: {categories}")
    print("As detail below:")

    budget_dict_s = sorted(budget_dict.items())
    
    for key, value in budget_dict_s:
        print('Budget for "{}": {:,} USD'.format(key,value))

    file_name = input('\nName your budget file in ".txt": ')
    with open(file_name,"w", newline="") as wf: # Write categories and budget into text file.
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
                cate = Budget.from_file(line)
                while True:
                    inp = input(f"How much did you spend on '{cate.category_name()}' (as int in USD): ")
                    if inp.isnumeric():
                        inp = int(inp)
                        break
                    else:
                        print("Invalid value. Try again.")
                wf.write(cate.wf_budget_trans(inp))
                print(cate.transaction_msg(inp))
                print(cate.budget_d())
    return file_name_output

if __name__ == "__main__":
    ca1 = Budget("House", 450)
    ca2 = Budget("Food", 200)
    
    assert ca1.wf_budget_trans(50) == "House : 400 USD\n", "Out put is wrong"
    print("Test 1 is passed.")

    assert ca1.budget_s() == 450, "Value is wrong"
    print("Test 2 is passed.")

    assert ca2.__len__() == 4, "Value is wrong"
    print("Test 3 is passed.")
import sys

class Budget:

    def __init__(self, category, budget_set):
        self.category = category
        self.__budget_set = budget_set
        self.budget_trans = budget_set

    def category_name(self):
        return self.category

    def __budget_set(self):
        return self.__budget_set

    def budget_s(self):
        return self.__budget_set

    def transaction(self, trans_amount):
        self.budget_trans -= trans_amount
        return self.budget_trans

    def __add__(self, other):
        print(f"Sum budget of '{self.category}' and '{other.category}' is {self.budget_s() + other.budget_s()} USD.")
        
    @classmethod
    def from_file(cls, line):
        line_lst = line.rstrip(" USD\n").split(" : ")
        category, budget_from_file = line_lst
        budget_from_file = int(budget_from_file.replace(",",""))
        return cls(category, budget_from_file)

    def __str__(self):
        return f"The budget set for {self.category}: {self.budget_s():,} USD"

# Divide:

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
        # Check if new category input exist or not
        if inp_categories in budget_dict: # new category exist, budget will be combine.
            budget_dict[inp_categories] += category_budget
        else: 
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
    file_name = input('\nName your budget file in ".txt": ')

    with open(file_name,"w") as wf: # Write categories and budget into text file.
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
                budget_aft_trans = cate.transaction(inp)
                print(f"Your budget on '{cate.category_name()}': ${cate.budget_s()} - ${inp} = {budget_aft_trans:,} USD\n")
                wf.write('{} : {:,} USD\n'.format(cate.category_name(),budget_aft_trans))
    return file_name_output

if __name__ == "__main__":
    ca1 = Budget("House", 450)
    ca2 = Budget("Food", 200)
    assert ca1.category_name() == "House", "Value is wrong"
    print("Test 1 is passed.")
    assert ca1.transaction(50) == 400, "Value is wrong"
    print("Test 2 is passed.")
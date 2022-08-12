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

if __name__ == "__main__":
    ca1 = Budget("House", 450)
    ca2 = Budget("House", 200)
    ca3 = Budget("Misc", 300)
    string_1 = "Car : 5,0000 USD\n"
    ca4 = Budget.from_file(string_1)
    print(f"Budget of {ca4.category} is {ca4.budget_s()}")
    print(ca4)
    # print(ca1.__add__(ca2))
    # print(ca1.transaction(500))
    # print(Budget.number_categories)
    # print(ca1)
    # print(ca1.transaction(200))
    # print(ca1.transaction(100))
   


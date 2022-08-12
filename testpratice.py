class geeks: 
    def __init__(self, name, roll): 
        self.name = name 
        self.roll = roll
   
# creating list       
list = [] 
  
# appending instances to list 
list.append( geeks('Akash', 2) )
list.append( geeks('Deependra', 40) )
list.append( geeks('Reaper', 44) )
print(list)
dict = {}
for obj in list:
    dict[obj.name] = obj.roll

print(dict)
# from budget_cls import Budget as BD

# def get_categories():
#     dict_ob = {}
#     lst = []
#     while True:
#         inp_categories  = input("Add new category: ")
#         while True:
#             try:
#                 category_budget = int(input(f"Set your budget (as int in USD) for '{inp_categories}': "))
#                 break
#             except:
#                 print("Invalid value. Try again")
#         cat = BD(inp_categories, category_budget)
        
#         if inp_categories in dict_ob:
#             dict_ob[cat.category] = dict_ob[cat.category] + cat.budget_s()
#         else:
#             dict_ob[cat.category_name()] = cat.budget_s()
#         completed_budget_add = input("\nEnter Y if completed add or press any key to continue: ")
#         if completed_budget_add.upper() == "Y":
#             break
#     return dict_ob

# print(get_categories())
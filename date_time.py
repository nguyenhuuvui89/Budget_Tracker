# import datetime

# def date_inp():
#     date_str = input('When was the transaction? (YYYY-MM-DD): ')
#     try:
#         datetime.datetime.strptime(date_str, "%Y-%m-%d")
#     except ValueError:
#         print("Incorrect formate. Try again.")
#         return date_inp()
#     return date_str

# budget_dict = {}
# budget_list = []
# categories = set()
# while True:
#     inp_categories  = input("Add new category: ")
#     budget_dict["category"] = inp_categories
#     while True:
#         try:
#             category_budget = int(input(f"Set your budget (as int in USD) for '{inp_categories}': $"))
#             break
#         except:
#             print("Invalid value. Try again")
#         # Check if new category input exist or not
#     if inp_categories in budget_dict: # new category exist, budget will be combine.
#             budget_dict["budget"] += category_budget
#     else: 
#         budget_dict["budget"] = category_budget
#     budget_dict["date"] = date_inp()
#     budget_list.append(budget_dict)
#     budget_dict = {}
#     categories.add(inp_categories)
#     completed_budget_add = input("\nEnter Y if completed add or press any key to continue: ")
#     if completed_budget_add.upper() == "Y":
#         break
# with open("a.txt","w") as wf:
#     for dict in budget_list:
#         wf.write("{} : {} : {}\n".format(dict["category"],dict["budget"],dict["date"]))
# print(budget_list)
# from budget_function import budget_after
# print(budget_after("n.csv"))
# with open("n.csv", "r") as rf:
#     csv_reader = csv.reader(rf, delimiter=" ")
#     with open("a.csv", "w") as wf:
#         csv_writer = csv.writer(wf, delimiter=" ")
#         for line in csv_reader:
#            csv_writer.writerow(line)
# from budget_function import budget_after
# budget_after("anh.txt")
import glob
from budget_function import Budget
my_list = {f for f in glob.glob("*.txt")}
print(my_list)
print(f"Your '{self.category_name()}' budget: ${self.budget_s():,} - ${trans_amount:,} = {self.budget_after_trans:,} USD.")
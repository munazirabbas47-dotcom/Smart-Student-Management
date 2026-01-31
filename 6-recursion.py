# what is recursion :
# when a function calls itself repeatedly is called recursion.
# print n to 1 backwards

# def show(n):
#     if n == 0: #base case
#         return
#     print(n)
#     show(n-1)

# recursive function 
# def one_100(n):
#     if n == 11:
#         return
#     print(n)
#     one_100(n+1)
# one_100(1)
# print("\nrecursion end")

# def reverse(a):
#     if a == 0:
#         return
#     print(a)
#     reverse(a-1)
# reverse(10)

# def fact(n):
#     if n == 1 or n == 0:
#         return 1
#     return n * fact(n-1)
# print(fact(5))

# def cal(n):
#     if n == 0:
#         return 0
#     return cal(n-1) + n
# sum = cal(10)
# print(sum)




# def ress(list,idx=0):
#     if idx == len(list):
#         return
#     print(list[idx])
#     ress(list, idx+1)
# name = ["ali","janan","abbas","amjad"]
# ress(name)

# def sum_list(n):
#     if len(n) == 0:
#         return 0
#     return n[0] + sum_list(n[1:])
# num = [1,2,3,4,5,6,8,9,10]
# print(sum_list(num))

# def greates_num_find(n):
#     if len(n) == 1:
#         return n[0]
#     else:
#         max_list = greates_num_find(n[1:])
#         return n[0] if n[0] > max_list else max_list
# mere_list = [1,2,6,8,9,11,555,67777,999999]
# print(greates_num_find(mere_list))


# def search_contact(contacts, index):
#     if index == len(contacts):
#         print("❌ Contact not found")
#         return
#     if contacts[index] == "Ali":
#         print("✔ Contact found")
#         return
#     search_contact(contacts, index + 1)

# search_contact(["Ahmed", "Usman", "Ali", "Bilal"], 0)


# def emi(balance):
#     if balance <= 0:
#         print("✅ Loan cleared")
#         return
#     print("Remaining balance:", balance)
#     emi(balance - 1000)

# emi(5000)

# aik program likho jo aik banda hai uss ne labarires se 10 books liye hai wo har din aik aik books waps kr ga
def books(bookss):
    if bookss <= 0:
            print("book k adayeeega tum ne clear kr diya")
            return
    print("reamining books is ", bookss)
    books(bookss -  1)
books(10)


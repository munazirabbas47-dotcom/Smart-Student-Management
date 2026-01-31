# wap to print the lenth of list using list
# def list_len():
#     list = [1,2,3,4,5,6,7,8,8]
#     print(len(list))
# list_len()

# second way
# cities = ["orakzai","kurram","kohat","hangu","raisan","chekar kot"]
# tiktoker = ["ilyas","asif orakzay","dada okz","yawaar","aesthetic pakhtoon"]

# def len_list(list):
#     print(len(list))

# len_list(cities)
# len_list(tiktoker)    

# WAF to print the element of a list in single line 

# list = [1,2,3,4,56,7,8,9,0]

# def lst(val):
#     print(val)
# # lst(list)

# # second method
# cities = ["orakzai","kurram","kohat","hangu","raisan","chekar kot"]
# tiktoker = ["ilyas","asif orakzay","dada okz","yawaar","aesthetic pakhtoon"]

# def list_tiktoker(list):
#     for i in list:
#         print(i, end= " , ")
# list_tiktoker(tiktoker)


# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(fact)
    


# calculate the factorial of number n using function
# def cal_fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     print(fact)
# cal_fact(5)
# cal_fact(6)     


# WAP to convert usd into pkr

# def con_uds_pkr(n):
#     usd = n
#     pkr = 279
#     con  = usd * pkr 
#     print(n, "USD", "=", con,"PKR")
# con_uds_pkr(5)
# con_uds_pkr(100)

# def check():
#     user = int(input("Enter a number : "))
#     if user % 2 == 0:
#         print(f"Yes ye number even hai {user}")
#     else:
#         print(f"ye number odd hai {user}")
# check()

# def janwar(animal,name):
#     print(f"i have a {animal}'s and his name is {name} ")
# janwar("dog","janan")

def fun(*args):
    print(type(args))
    print(f"first args is {args[0]}")
    print(f"second argument is {args[1]}")
    print(f"third argument is {args[2]}")
    
fun("ali","ahmad",17)



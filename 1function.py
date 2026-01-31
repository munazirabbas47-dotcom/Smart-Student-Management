# function in python
"""
Block of statment that perform a specific task.
def fun_name(parameter1,parameter2): 
    #some work
    return val

fun_name(argument1,argument2) #function call
"""
# first method
# def sum_val(a,b): #parameter
#     s = a+b #work
#     return s #return value
# print(sum_val(55,5)) #final call of function : arguments


# second method
# def mult_val(a,b):
#     mul = a * b
#     print(mul)
#     return sum

# mult_val(5,4)
# mult_val(2,8)
# mult_val(4,3)


# print some list in function by for loops

# def listt():
#     list = [55,3,2,4,1,8,9,23,6,5,7]
#     list.sort()
#     count = 0
#     for i in list:
#         count += 1
#         print(f"the indx on {count} is {i}")
# listt()
# print("second time")
# listt()


# avarage of 3 num

def cal_avarg(a,b,c):
    sum = a + b + c
    avg = sum // 3
    print(avg)
    return avg
cal_avarg(4,5,9)
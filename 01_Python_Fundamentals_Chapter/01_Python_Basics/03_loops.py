def multiply_1(num_list, num):
    for x in num_list:
        x *= num
    return num_list

def multiply_2(num_list, num):
    for idx in range(len(num_list)):
        num_list[idx] *= num
    return num_list

# num_list = [1,2,3,4,5,6]
#  num = 5

# x = 1 -> x = 5
# x = 2 -> x = 10
#  ...

# idx = 0 -> num_list[0] = 1 -> num_list[0] = 5
# idx = 1 -> num_list[1] = 2 -> num_list[0] = 10

print("*"*50)

# CASE 1
a = [2,4,10,16]
num = 5
print(a, num)
b = multiply_1(a,num)
print(b)

print("*"*50)

# CASE 2
a = [2,4,10,16]
num = 5
print(a, num)
c = multiply_2(a,num)
print(c)

print("*"*50)

# CASE 3
a = [2,4,10,16]
num = 5
print(a, num)
b = multiply_1(a,num) # -> b = [2,4,10,16]
print(b)
c = multiply_2(a,num) # -> c = [10,20,50,80]
                      # -> b = [10,20,50,80]
print(b)
print(c)

print("*"*50)
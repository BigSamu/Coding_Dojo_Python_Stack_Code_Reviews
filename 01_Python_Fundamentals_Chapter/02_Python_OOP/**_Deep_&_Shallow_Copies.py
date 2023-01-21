
class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email


a = 12
b = [1,2,3,4,5,6]
c = "hello"
d = {
    "name":"John Doe",
    "email": "johndoe@gmail.com"
}
e = User("Peter Phillips", "peterphillips@gmail.com")

a_copy = a
b_copy = b
c_copy = c
d_copy = d
e_copy = e


print("\n"+"*"*150)

print("Initial states")
print(f"value of 'a'     : {a} - address in memory of 'a':      {hex(id(a))}")
print(f"value of 'a_copy': {a_copy} - address in memory of 'a_copy': {hex(id(a_copy))}")
print(f"value of 'b'     : {b} - address in memory of 'b':      {hex(id(b))}")
print(f"value of 'b_copy': {b_copy} - address in memory of 'b_copy': {hex(id(b_copy))}")
print(f"value of 'c'     : {c} - address in memory of 'c':      {hex(id(c))}")
print(f"value of 'c_copy': {c_copy} - address in memory of 'c_copy': {hex(id(c_copy))}")
print(f"value of 'd'     : {d} - address in memory of 'd':      {hex(id(d))}")
print(f"value of 'd_copy': {d_copy} - address in memory of 'd_copy': {hex(id(d_copy))}")
print(f"value of 'e'     : {e.name} - {e.email} - address in memory of 'e':      {hex(id(e))}")
print(f"value of 'e_copy': {e_copy.name} - {e_copy.email} - address in memory of 'e_copy': {hex(id(e_copy))}")


print("*"*150+"\n")
print("*"*150)

# Case 1 - int Type
a_copy = 10
print("Case 1 - int type")
print(f"value of 'a'     : {a} - address in memory of 'a':      {hex(id(a))}")
print(f"value of 'a_copy': {a_copy} - address in memory of 'a_copy': {hex(id(a_copy))}")

print("*"*150+"\n")
print("*"*150)

# Case 2 - list type
b_copy.append(7)
print("Case 2 - list type")
print(f"value of 'b'     : {b} - address in memory of 'b':      {hex(id(b))}")
print(f"value of 'b_copy': {b_copy} - address in memory of 'b_copy': {hex(id(b_copy))}")

print("*"*150+"\n")
print("*"*150)

# Case 3 - string type
c_copy = "world"
print("Case 3 - string type")
print(f"value of 'c'     : {c} - address in memory of 'c':      {hex(id(c))}")
print(f"value of 'c_copy': {c_copy} - address in memory of 'c_copy': {hex(id(c_copy))}")

print("*"*150+"\n")
print("*"*150)

# Case 4 - dictionary type
d_copy["age"] = 47
print("Case 4 - dictionary type")
print(f"value of 'd'     : {d} - address in memory of 'd':      {hex(id(d))}")
print(f"value of 'd_copy': {d_copy} - address in memory of 'd_copy': {hex(id(d_copy))}")

print("*"*150+"\n")
print("*"*150)

# Case 4 - class type
e_copy.name = "John Phillips"
e_copy.email = "johnphillips@gmail.com"
print("Case 5 - class type")
print(f"value of 'e'     : {e.name} - {e.email} - address in memory of 'e':      {hex(id(e))}")
print(f"value of 'e_copy': {e_copy.name} - {e_copy.email} - address in memory of 'e_copy': {hex(id(e_copy))}")

print("*"*150)
# Name Error
name = "Name Error"
try:
    print(nam)
except:
    print("This is Name error")

# Overflow Error
i=1
f = 3.0**i
try:
    for i in range(100):
        print (i, f)
        f = f ** 2
except:
    print("This is Overflow Error")

# # Syntax Error
#     print(()

# #Identation Error
#     print("Identation error")

# Value Error
i="string"
try:
    print(int(i))
except:
    print("This is Value Error")

# Type Error
b = 34
try:
    print("Type error" + b)
except:
    print("This is Type Error")

# Unbound Local Error
x = 5
try:
    def local():
        print(x)
        x = 7
    local()
except:
    print("This is Unbound Local Error")

#Zero Division Error
try:
    print(5/0)
except:
    print("This is Zero Division Error")
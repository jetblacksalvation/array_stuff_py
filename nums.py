import random
list_=[random.randint(1,100)for x in range (10)]
def func(var:list):
    num = 0
    for elem in var:
        if elem > num:
            num = elem
            
    return num
print(func(list_))
print("how many numbers do you want?")
num = int(input())
for x in range(num):
    list_.append(int(input()))
print(list_)

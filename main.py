list = []

length_of_list = int(input("Give a number for the length of the list: "))

for i in range(length_of_list):
    x = int(input("Give an integer: "))
    list.append(x)

print(list)

for i in range(length_of_list-1):
    for j in range(length_of_list-1-i):
        if list[j]>list[j+1]:
            c=list[j+1]
            list[j+1]=list[j]
            list[j]=c

print(list)
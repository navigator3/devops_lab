list1 = list(map(int,input("enter 1st list through a space: ").split()))
list2 = list(map(int,input("enter 2st list through a space: ").split()))
q = []
for i in range(len(list1)):
    if list1[i] in list2:
        q.append(list1[i])
q.sort()
answer = set(q)
print("Common elements are: %s" %list(answer))

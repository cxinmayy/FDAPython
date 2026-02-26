import copy
list1=[10,20,[30,40],50]
# list2=list1
list2=copy.copy(list1)
list1[1]=22
list1[2][0]=33
print(list1)
print(list2)

list3=[10,20,[30,40],50]
# list4=list3
list4=copy.deepcopy(list3)
list3[1]=22
list3[2][0]=33
print(list3)
print(list4)

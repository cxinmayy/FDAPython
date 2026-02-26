squares=[0,4,9,16,25]
print(squares)
list1=[10,20,30,"hello",True,2,3]
print(list1)
print(squares[0])
print(squares[-1])
print(squares[-3:])
print(squares[1:4])
print(len(squares))

print(squares+[36,52,64,81,100]) #list concatenation

letters=['a','b','c','d','e','f']
print(letters)
letters[2:5]=['C','D','E'] #replace some variables
print(letters)
letters[2:5]=[] #now remove them
print(letters)
letters[:]=[] #clear all the elements by replacing them with empty list
print(letters)


cube=[1,8,27,65,125] #something is wrong
4**3 #cube of 4is 64 not 65
cube[3]=64 #replace the wrong value list is mutable
print(cube)


list2=['apple','banana','cheery','apple','cheery']
print(list2)
print(type(list2))
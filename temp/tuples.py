t1=(4,6,[2,8],'abc',[3,4])
print(type(t1))
print(t1[0])



t1=("apple","banana","kiwi","mango")
t2 = list(t1)
t2[3]="cherry"
t2.append("grapes")
t2.insert(1,"pineapple")
t1 = tuple(t2)
print(t1)


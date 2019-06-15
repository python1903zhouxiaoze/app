from functools import reduce

list=[7,5,9,3,10]
for i in range(len(list)):
    a=reduce(lambda x,y:x if x<y else y,list)
    print(a,end=' ')
    list.remove(a)
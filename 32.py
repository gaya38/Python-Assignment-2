list1=[10,20,30,40,50,60]
list2=[10,20,30,40]
list3=[50,60,70,80,90]
a=len(list1)
b=len(list2)
c=len(list3)
print "length of list1 is:",a
print "length of list2 is:",b
print "length of list3 is:",c
print "maximum and minimum elements of each list"
print "maximum of list1:",max(list1)
print "minimum of list1:",min(list1)
print "maximum of list2:",max(list2)
print "minimum of list2:",min(list2)
print "maximum of list3:",max(list3)
print "minimum of list3:",min(list3)
list4=[a,b,c]
list4.sort()
print "The smallest list is:"
if (list4[0]==a):
    print "list1"
elif(list4[0]==b):
    print "list2"
else:
    print "list3"
print "The biggest list is:"
if (list4[-1]==a):
    print "list1"
elif(list4[-1]==b):
    print "list2"
else:
    print "list3"
del(list1[0],list1[1])
print "List1 after deleting:",list1
del(list2[0],list2[1])
print "List2 after deleting:",list2
del(list3[0],list3[1])
print "List3 after deleting:",list3





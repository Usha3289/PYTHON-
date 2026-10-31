#LIST:=
#a list is a ordered collection of items which can be of any data type.
# Lists are mutable, meaning that their contents can be changed after they are created. 
# Lists are defined using square brackets [] and can contain duplicate elements.
lst1=[1,2,3,4,5]
print(lst1)
print(lst1[0])
print(lst1[0:1])
print(lst1[2:4])
print(lst1[::-1])
#LIST METHODS
#1.append() method is used to add an element at the end of the list.
lst1.append(6)
print(lst1)
lst1.append([10,20,30])
print(lst1)
print(lst1[6][1])
#2.extend() method is used to add multiple elements at the end of the list.
lst1.extend([7,8,9])
print(lst1)
#3.insert() method is used to add an element at a specific index in the list.
lst1.insert(0,100)
print(lst1)
#4.REMOVING
#a.remove() method is used to remove the first occurrence of a specific element from the list.
lst1.remove(100)
print(lst1)
#if any number is not present in the list then it will give an error.we can use if condition to check whether the number is present in the list or not.
if 100 in lst1:
    lst1.remove(100)
    print(lst1)
lst4=[1,2,3,4,5,6,7,8,9]
#b.pop() method is used to remove an element at a specific index from the list.
lst4.pop(0)
print(lst4)
print(lst4.pop())#removes the last element from the list and returns it.
print(lst4.clear())#removes all the elements from the list.
lst5=[1,2,3,4,5]
del lst5[0]#deletes the element at index 0 from the list.
print(lst5)

#5.sorting:=
lst2=[12,56,73,45,85,23,45,67,89,90]
lst2.sort()#alters the original list and sorts it in ascending order.
print(lst2)
lst2.sort(reverse=True)
print(lst2)#displays the list in descending order.

sorted_lst=sorted(lst2)#sorted() function returns a new sorted list without modifying the original list.
print(sorted_lst)
#6.copying:=
l1=[1,2,3,4,[2,3,6]]
l2=l1.copy()#creates a shallow copy of the list.
print(l2)



#TUPLES:==
# A tuple is an ordered collection of items which can be of any data type.
#creating and accessing tuples:=
tup1=(1,2,3,4,5)
print(tup1)
print(tup1[0])
print(tup1[-3])
print(tup1[0:1])
print(tup1[::-1])

#1.concatenation:=
tup2=(6,7,8,9,10)
tup3=tup1+tup2
print(tup3)

#2.repeating:=
tup4=tup1*3
print(tup4)

#3.looping through tuples:=
for i in tup1:
    print(i)

#4.immutability:=
#tuples are immutable, meaning that their contents cannot be changed after they are created.
tup5=(1,2,3,4,5)
#tup5[0]=100#this will give an error because tuples are immutable.
print(tup5)


array_A = [7,5,10,14,3,9,7]
array_B = [9,10,3,4,2,5,7,1]
print("ARRAY_A :",array_A)
print("ARRAY_B :",array_B)
print()
print("Print both arrays :",end=" ")
array_A.extend(array_B)

print(array_A)
array_Length = len(array_A)
print("Length:",end=" ")
print(array_Length)
print("Find index of 7 in 2 arrays:",end=" ")
#array_A
LocationA = array_A.index(7)
LocationB = array_A.index(2)
print(LocationA,LocationB)

array_A.sort()
print("Sort 3rd Array : ",array_A)

for i in array_A.copy():
    if i is 7:
        array_A.remove(i)
print("Remove 7 ->",array_A)

array_F = array_A.copy()
print("4th Array :",array_F)
array_F.reverse()
print("Reverse : ",array_F)

print("Array 3rd :",array_A,"Array 4th : ",array_F)
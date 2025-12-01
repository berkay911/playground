import copy
num_list = list(range(4,11,2)) #mutable
num_tuple = tuple(range(4,11,2)) #immutable

average_list = sum(num_list) / len(num_list)

x = 5
y=  3

(x, y) = (y, x)  #swap values

#print(num_tuple + num_tuple) # prints (4, 6, 8, 10, 4, 6, 8, 10)

num_list.append(12) # adds 12 to the end of the list
num_list.append([20,30]) # adds [20,30] as a single element to the end of the list

3 in num_list  # False
4 in num_list  # True
20 in num_list # False
[20,30] in num_list # True

num_list.remove(8) # removes the first occurrence of 8 from the list

num_list.index(4) #kaçıncı indekste olduğunu verir

num_list.remove([20,30])
num_list.append(1)

#a = sorted(num_list) # returns a new sorted list without modifying the original list
#num_list.sort()  # sorts the list in place

#num_list_alias = num_list  # both variables point to the same list object
#num_list_shallow = copy.copy(num_list)  # creates a shallow copy of the list
#um_list_deepcopy = copy.deepcopy(num_list) # creates a deep copy of the list

num_list.append([100,200])

num_list_shallow_copy = copy.copy(num_list)
num_list_deep_copy = copy.deepcopy(num_list)    

num_list[0] = 999
num_list[5][0] = 888  # Modifying the nested list

print("Original List:", num_list)
print("Shallow Copy:", num_list_shallow_copy)
print("Deep Copy:", num_list_deep_copy)

my_list = [1,2,3,4,5]
squared_list = [x**2 for x in my_list]  # List comprehension to create a list of squares
print("Squared List:", squared_list)  # Output: [1, 4, 9, 16, 25]


my_string = "123596"

#my_list2 = my_string.split(",")
#print(my_list2)  # Output: ['1', '3', '5', '9', '6']


new_list = [elem for elem in my_string]

print(new_list)  # Output: ['1', '2', '3', '5', '9', '6']

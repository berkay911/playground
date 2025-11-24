def create_list_from_range():
    empty_list = []
    x = 0
    while x < 10:
        empty_list.append(x)
        x += 1
    print(empty_list)    
    return empty_list
    
#create_list_from_range()

def is_triangular_number(n):
    is_triangular = False
    sum = 0
    for j in range(0, n+1):
        sum += j
        if sum == n:
            is_triangular = True
            break
    return is_triangular

def is_triangular_number_v2(n):
    triangular_list = []
    for i in range(0, n+1):
        triangular_number = (i * (i + 1)) // 2
        triangular_list.append(triangular_number)
    if n in triangular_list:
        return True
    else:
        return False
    
#print(is_triangular_number_v2(7))

def square_number(n1, n2):
    return sum([i**2 for i in range(n1, n2+1) if i%2 == 0])
    
#print(square_number(3, 7))       

#L = [1,2,3,4,3,2,1,5]



def remove_duplicates(list,e):
    l_new = list.copy()

    while e in l_new:
        l_new.remove(e)
    return l_new


#print(remove_duplicates(L, 2))
#print(L) 

import copy
L = [1,2,[3,4],5,[6,7],8,9]

L_alias = L
L_shallow_copy_1 = L[:]
L_shallow_copy_2 = copy.copy(L)
L_deep_copy = copy.deepcopy(L)


from speak import talk
talk("Alice", 25)
talk("Bob")
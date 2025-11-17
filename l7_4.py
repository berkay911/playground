def build_tuple(start, end, increment):
    range_input = range(start, end, increment)
    return tuple(range_input)

def split_tuple(input_tuple):
    length_of_tuple = len(input_tuple)
    odd_tuple = build_tuple(1, length_of_tuple, 2)
    even_tuple = build_tuple(0, length_of_tuple, 2)
    return (odd_tuple, even_tuple)

print(split_tuple((1,2,3,4,5,6,7,8,9,10)))
   
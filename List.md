append(): adds an element to the end of a list

fruits = ['apple', 'banana', 'orange']
fruits.append('grape')
print(fruits)  # Output: ['apple', 'banana', 'orange', 'grape']

insert(): inserts an element at a specified position

fruits = ['apple', 'banana', 'orange']
fruits.insert(1, 'grape')
print(fruits)  # Output: ['apple', 'grape', 'banana', 'orange']

extend(): adds elements from another list to the end of a list
 
fruits = ['apple', 'banana', 'orange']
more_fruits = ['grape', 'kiwi', 'mango']
fruits.extend(more_fruits)
print(fruits)  # Output: ['apple', 'banana', 'orange', 'grape', 'kiwi', 'mango']

remove(): removes the first occurrence of an element from a list
 
fruits = ['apple', 'banana', 'orange', 'grape']
fruits.remove('orange')
print(fruits)  # Output: ['apple', 'banana', 'grape']


pop(): removes and returns the element at a specified position (or the last element if no position is specified)
 
fruits = ['apple', 'banana', 'orange']
orange = fruits.pop(2)
print(orange)  # Output: 'orange'
print(fruits)  # Output: ['apple', 'banana']

index(): returns the index of the first occurrence of an element in a list
 
fruits = ['apple', 'banana', 'orange', 'grape']
index_of_orange = fruits.index('orange')
print(index_of_orange)  # Output: 2


count(): returns the number of times an element appears in a list
 
fruits = ['apple', 'banana', 'orange', 'banana', 'grape']
count_of_bananas = fruits.count('banana')
print(count_of_bananas)  # Output: 2


sort(): sorts the elements in a list in ascending order
 
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numbers.sort()
print(numbers)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

reverse(): reverses the order of elements in a list
 
fruits = ['apple', 'banana', 'orange', 'grape']
fruits.reverse()
print(fruits)  # Output: ['grape', 'orange', 'banana', 'apple']

len(): returns the number of elements in a list
 
fruits = ['apple', 'banana', 'orange', 'grape']
num_fruits = len(fruits)
print(num_fruits)  # Output: 4

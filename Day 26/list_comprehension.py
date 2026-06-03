numbers = [1,2,3]
new_list= []

#normal method without list comprehension
for n in numbers:
    add_1 = n+1
    new_list.append(add_1)

# List comprehension structure:
# new_list = [new_item for item in list]

new_list_compr = [n+1 for n in numbers]
print(new_list_compr)

#List comprehension in strings
name = "Marina The Queen"
new_listn = [l for l in name]
print(new_listn)

#list comprehension in range
numbers_range = [r*2 for r in range(1,5)]
print(numbers_range)

#Conditional list comprehension
names = ["luna", "lee", "lyn", "lucy", "leopolda", "lily", "lisa", "leonora"]
#Retrieve names of 4 characters and upper case them
short_names = [n.upper() for n in names if 5 > len(n) > 3]
print(short_names)

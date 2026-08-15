n = int(input("Enter the number of elements: "))

list = []     # define an empty list

# handle with the input stream
for num in input().split():
    list.append(int(num))

# sort the list first, because it's easier to sort on list
list.sort()

# test the correction of the list
# print(list) √

# get a copy of the list to deal with the subtask of counting
dict = {}

for i in range(1, (len(list) + 1)):
    dict[i] = list.count(i)

# test the correction of the dict
print(list)

# switch the list into a set. in order to remove the repeated nums
set = set(list)

# use the length of the set, and set the final output
for i in range(1,(len(set) + 1)):
    print(f"{i}: {dict[i]}")

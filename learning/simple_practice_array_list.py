# simple_practice_array_list
# array = []

# 输入为同一行的情况
# for x in input().split():
#     array.append(int(x))

# 每个输入占一行，以Ctrl+D结束输入
# while True:
#     try:
#         array.append(int(input()))
#     except EOFError:
#         break

# 打印列表的长度
# length = len(array)
# print(length)

# # 打印列表中的元素
# for i in range(length):
#     print(array[i])


# print(array)


# new_array = [('小明',98),('美美',100),('张三',65)]
# print(sorted(new_array , key = lambda x: x[1],reverse = True))
# new_array.sort(key = lambda x : x[1],reverse = True)

# rank_array = ["gold","silver","bronze"]

# print("The results of yesterday's competition:")
# for i in range(len(new_array)):
#     print(f"\tscore: {new_array[i][1]:<8d} price:{rank_array[i]}")

# # 遍历列表
# for item in new_array:
#     print(item[1],end = ';' if (item != new_array[len(new_array) - 1]) else '.')
#     if(item == new_array[len(new_array) - 1]):
#         print()

# tuple_array = [('Samy',98),('Michale',67),('Wincy',92)]
# # tuple_array = ['Smlie','Nancy','JJhony']

# for index,value in enumerate(tuple_array):
#     print(index)

# print(*tuple_array,sep = '/')
# print(max(tuple_array,key = lambda x: len(x[0])))

n = int(input('please enter the row of the matrx: '))

matrix = [[int(x) for x in input().split() ] for _ in range(n)]
print(matrix)

# for row in matrix:
#     for item in row:
#         print(item,end = ' ')
#     print()

for row in matrix:
    print(f"{max(row)}")

# simple test on dict

# build a dict upon tuple_list

tuple_list = [("apple", 1), ("banana", 2), ("cherry", 3)]
dict_1 = dict(tuple_list)
print(dict_1)

print(dict_1.get("apple", 2))
del dict_1["apple"]
print(dict_1.get("apple", 3))

print(dict_1.items())
print(dict_1.keys())
print(dict_1.values())

for k, v in dict_1.items():
    print(k, v, sep='/')


# sorted(d.items(), key=lambda x: (-x[1], x[0]))  # 值降序，键升序

# 构造一个字典，演示“值降序，键升序”排序后的效果
my_dict = {'apple': 20, 'banana': 20,
           'cherry': 20, 'date': 40, 'elderberry': 50}
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: (-x[1], x[0])))
print(sorted_dict)

# 用多行显示的方式分别创建一个列表和一个字典
mul_row_list = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry"
]
mul_row_dict = {
    "apple": 20,
    "banana": 20,
    "cherry": 20,
    "date": 40,
    "elderberry": 50
}
print(mul_row_dict)
print(mul_row_list)

k, v = mul_row_dict.popitem()
print(k, v)
print(mul_row_dict)
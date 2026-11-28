# 用 for 循环挑出数量大于 0 的商品名。
cart = [("苹果", 3), ("香蕉", 0), ("西瓜", 2)]

available_names = []
for name, quantity in cart:
    if quantity > 0:
        available_names.append(name)

# 同一件事可以用列表推导式完成。
# 左边的 name 是要放进新列表的值，末尾的 if 是筛选条件。
available_names_compact = [name for name, quantity in cart if quantity > 0]

print(available_names)          # ['苹果', '西瓜']
print(available_names_compact)  # ['苹果', '西瓜']
# 练习：让这个新列表只保留数量至少为 3 的商品名。

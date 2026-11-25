
# 元组 和列表一样可以按下标取值 但创建后不能替换、增加或删除其中的项。

item = ["苹果",3]

print(item[0])
print(item[1])


name,quantity = item

print(f"{name}买了{quantity}件")
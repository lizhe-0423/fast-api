# 对比列表 和 元组的区别是什么

"""
1. 只管区别 list 和 tuple 按位置取值 而 dict按键取值
2. list 和tuple 创建后不能增删或者替换元素
3. 所以tuple 常用来表示几项固定含义、适合一起传递的值 比如坐标（x，y）图片尺寸（宽，高）
"""

cart = [("苹果", 3), ("香蕉", 2), ("苹果", 1)]
totals = {}

# 美轮取出一个元组并把它拆给两个变量name 和 quantity
for name, quantity in cart:
    totals[name] = totals.get(name, 0) + quantity

print(totals)  # {'苹果': 4, '香蕉': 2}

for name, quantity in totals.items():
    print(f"{name}一共买了{quantity}件")
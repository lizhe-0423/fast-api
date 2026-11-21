# 第一节：创建变量、重新赋值、多变量赋值

# 1. 从右边取值，再把左边的变量名绑定到这个值。
price = 20
old_price = price
price = 25

# 给 price 重新赋值后，old_price 仍然指向整数 20。
print(f"当前价格：{price} 元")      # 25 元
print(f"原来价格：{old_price} 元")  # 20 元

# 2. 多变量赋值：两边按位置对应。
width, height = 1920, 1080
print(f"分辨率：{width} × {height}")

# 3. 交换变量：先取得右边的两个值，再赋给左边的变量。
a, b = 10, 20
print(f"交换前：a = {a}, b = {b}")
a, b = b, a
print(f"交换后：a = {a}, b = {b}")

# 练习：改成 a = b 和 b = a 两行，先猜结果，再运行对照。




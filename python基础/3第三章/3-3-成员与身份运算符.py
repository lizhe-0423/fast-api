# in is

cart = ["苹果", "香蕉", "橙子"]

print("苹果" in cart)
print("蓝莓" in cart)

stock = {"苹果": 3}
# 对字典来说，`in` 默认查的是键
print("苹果" in stock)

# == 值不想等 is 指针想等

a = "苹果"

b = "苹果"
print("========")
print(a==b)
print(a is b)

a = ["苹果"]
b = ["苹果"]

# 相同内容的字符串可能共享一个对象，所以在业务代码里判断字符串内容，用 ==。
print(a == b)  # True，内容相同
print(a is b)  # False，是两个列表对象

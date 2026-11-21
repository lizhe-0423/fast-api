# type() 可以查看数据类型

quantity = 20
price = 20.0
quantity_text = "20"
is_paid = False
is_paid_t = True
tracking_number = None

print(type(quantity))
print(type(price))
print(type(quantity_text))
print(type(is_paid_t))
print(type(tracking_number))


print(quantity == price)
print(quantity == quantity_text)

if "False":
    print("进入了 if 分支")

if tracking_number is None:
    print("还没有物流单号")
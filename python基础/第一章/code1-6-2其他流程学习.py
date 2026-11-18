# 接下来学习其他流程

unit_price = int(20)
quantity = 0

while True:
    text = input("请输入购买数量：")

    try:
        quantity = int(text)
    except ValueError:
        print("请输入整数例如,3")
        continue

    if quantity < 0:
        print("请输入正整数")
        continue

    break

subtotal = unit_price * quantity

if subtotal >= 100:
    shipping_fee = 0
else:
    shipping_fee = 8

print(f"商品价格为{subtotal}元")
print(f"运费为{shipping_fee}元")
print(f"总价为{subtotal + shipping_fee}元")

# 综合练习：用 enumerate 编号，跳过无效记录，再按金额算运费。
# 每条记录依次是商品名、单价和数量，金额都用整数元简化。
cart = [("苹果", 20, 3), ("香蕉", 15, 0), ("西瓜", 25, 2)]
subtotal = 0

for number, (name, unit_price, quantity) in enumerate(cart, start=1):
    if quantity <= 0:
        print(f"{number}. {name}的数量无效，跳过")
        continue

    line_total = unit_price * quantity
    subtotal += line_total
    print(f"{number}. {name} × {quantity}，小计 {line_total} 元")

if subtotal >= 100:
    shipping_fee = 0
elif subtotal > 0:
    shipping_fee = 8
else:
    shipping_fee = 0

print(f"商品合计：{subtotal} 元")
print(f"运费：{shipping_fee} 元")
print(f"应付金额：{subtotal + shipping_fee} 元")
# 练习：改西瓜数量为 1，此时商品合计 85 元，应付 93 元。

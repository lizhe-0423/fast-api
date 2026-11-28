# if / elif / else 从上往下判断，只执行第一个满足条件的分支。
subtotal = 120

if subtotal >= 200:
    shipping_fee = 0
elif subtotal >= 100:
    shipping_fee = 4
else:
    shipping_fee = 8

print(f"商品金额：{subtotal} 元，运费：{shipping_fee} 元")
# 练习：改成 99、100、199、200，观察运费如何变化。

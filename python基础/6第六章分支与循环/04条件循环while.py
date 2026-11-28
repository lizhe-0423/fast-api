# while 在每轮开始前判断条件。
stock = 3

while stock > 0:
    print(f"当前库存：{stock}，售出一件")
    stock -= 1

print(f"循环结束，剩余库存：{stock}")
# 练习：把初始库存改成 0，看看循环体会不会执行。

# continue 跳过当前这一轮；break 结束当前循环。
cart = [("苹果", 3), ("香蕉", 0), ("西瓜", 5), ("橙子", 1)]
total_quantity = 0

for name, quantity in cart:
    if quantity <= 0:
        print(f"{name}数量无效，跳过")
        continue

    total_quantity += quantity
    print(f"已累计{name}，共 {total_quantity} 件")

    if total_quantity >= 6:
        print("已达到至少 6 件，结束统计")
        break

print(f"最终累计：{total_quantity} 件")
# 练习：把目标从 6 改成 9，观察橙子是否会被统计。

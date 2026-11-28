# range(start, stop, step) 包含 start，不包含 stop。
for number in range(1, 4):
    print(f"第 {number} 次检查")

# range(3) 从 0 开始，依次给出 0、1、2。
print(list(range(3)))
# 第三个参数表示每次走几步。
print(list(range(2, 10, 2)))  # [2, 4, 6, 8]

# 练习：用 range 输出 5、4、3、2、1。

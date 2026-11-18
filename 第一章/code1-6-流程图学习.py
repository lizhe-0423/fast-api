# 学习流程 开始结束 判断 处理 输入输出

# 输入年龄 然后并且询问用户 有没有过生日 从而判断其出生日

# 下一步学习while / try catch / for 等 循环 分支

from datetime import datetime

age = input("请输入你的年龄：")

answer = input("请问你有没有过生日？（仅允许输入是/否）").strip()
year = datetime.now().year
if answer == "是":

    int_age_ = year - int(age)

elif answer == "否":
    int_age_ = year - int(age) - 1

else:
    int_age_ = None
print("输入错误")


if int_age_ is not None: print(f"你的出生年份是{int_age_}")

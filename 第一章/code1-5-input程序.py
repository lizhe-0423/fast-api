# 创建变量age 输出年龄

age = input()

print("当前年龄：",age)

# 接下来模拟一个更加真实的企业业务 账号密码
account = input("请输入账号：")
password = input("请输入密码：")

print("当前正在登录账号：", account)
print("...正在检查账号密码...")

if password == "12345678":
    print("登录成功")
else:
    print("登录失败")

# input 企业项目中 函数也不常用吧 不对 一般企业项目 用到的是 fastAPI 这种 web框架 input 这种控制台输入的 确实 不常见

# Mock（模拟）：用事先准备的假数据，练习原本需要数据库才能完成的操作。
# 下面是一个教学例子，不连接真实数据库，也不适用于真实登录。
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(filename)s:%(lineno)d - %(message)s",
    stream=sys.stdout,  # 与 print 使用同一个输出流，方便观察
)
logger = logging.getLogger(__name__)

print("\n--- 模拟企业项目登录 ---")

# 假装这些用户是从数据库查询出来的，账号和密码都只是练习数据。
mock_users = {
    "lizhe": "12345678",
    "xiaoming": "87654321",
}

# 复用前面 input() 输入的账号和密码，不需要再次输入。
# .get(account) 根据账号查找；如果没有这个账号，返回 None。
saved_password = mock_users.get(account)

if saved_password is not None and password == saved_password:
    logger.info("模拟登录成功，账号：%s", account)
    print("模拟结果：登录成功")
else:
    logger.warning("模拟登录失败")
    print("模拟结果：账号或密码错误")

# 测试：lizhe / 12345678 可以成功，输入错误的账号或密码会失败。
# 真实项目通常由 Web 请求提供数据，并通过数据库等服务查询用户。
# 密码不能像这个 Mock 例子一样明文保存，也不要写进日志。

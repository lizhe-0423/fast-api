import logging
import sys


# 一、print 输出格式
print("=== 一、print 输出格式 ===")

# 1. \n 表示换行；print() 本身也会在结尾换行。
print("我是李哲\n你好\n2026 我要从零学 Python")
print("好好学习")

# 2. 日期加引号是字符串；没有引号的 2026-11-17 是减法。
day = "2026-11-17"
up = "天天向上"
print(day, up)  # 多个值之间默认用空格分隔
print(day, up, sep=" | ")  # sep 指定值之间的分隔符

# 3. end 指定结尾；默认是换行符 \n。
print("好好学习", end="，")
print("天天向上")

# 4. f-string 可以把变量和简单计算放进字符串。
name = "李哲"
price = 19.956
print(f"我是{name}，今天是{day}")
print(f"价格：{price:.2f} 元")  # .2f 表示保留两位小数

apple,blueBarry = 10.123,50.456
print(f"苹果加蓝莓的价格是{apple+blueBarry:.2f}")


# 二、logging 日志
print("\n=== 二、logging 日志 ===")

# 程序入口通常统一配置一次；先配置，再输出日志。
logging.basicConfig(
    level=logging.INFO,  # 显示 INFO 及以上；改为 DEBUG 可查看调试信息
    format="%(asctime)s %(levelname)s %(filename)s:%(lineno)d - %(message)s",
    stream=sys.stdout,  # 练习时与 print 使用同一输出流，方便观察顺序
)

# __name__ 是当前模块的名称；直接运行此文件时，它的值是 __main__。
logger = logging.getLogger(__name__)

# 常见日志级别：DEBUG < INFO < WARNING < ERROR < CRITICAL。
logger.debug("这是调试信息，当前 INFO 级别下不会显示")
logger.info("用户服务启动成功")
logger.warning("这是一条警告信息")
logger.error("这是一条错误信息")

# 在日志中用 %s 放变量，logging 会在需要输出时格式化。
user_id = 1001
logger.info("用户登录成功，用户 ID：%s，用户名：%s", user_id, name)

# logger.log 可以直接指定级别，与 logger.info(...) 的作用相同。
logger.log(logging.INFO, "这也是一条正常运行信息")

# 日志可能被保存或共享，不要记录密码、验证码等敏感信息。

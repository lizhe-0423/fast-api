raw_code = "  SKU_0042  "

code = raw_code.strip() # 去掉两端空白
code = code.lower() # 转成小写
code = code.replace("_", "-") # 替换

# repr是自带函数 用于调试看清一个值
print(repr(raw_code))  # '  SKU_0042  '
print(repr(code))      # 'sku-0042'

stock = {"sku-0042": 3}
print(stock.get(code))  # 3



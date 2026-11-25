

raw = "苹果，，橙子"

items = raw.split("，")
print(items)

clean_items = []

for item in items:
    clean_items.append(item.strip())

result = "、".join(clean_items)
# "、".join(clean_items) 用 、 把列表里的字符串连起来
print(result)


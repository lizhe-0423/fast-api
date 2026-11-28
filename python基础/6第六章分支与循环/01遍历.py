cart = [("苹果",3),("香蕉",5),("西瓜",2)]


for number,(name,quantity) in enumerate(cart,start=1):
    print(f"第{number}个商品是{name},数量是{quantity}")

    # enumerate 遍历时顺便给每一项编号
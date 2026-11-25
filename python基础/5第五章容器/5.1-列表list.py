cart = ['apple', 'banana', 'orange']

cart.append('pear')

print(cart)

cart[0] = '苹果'

print(cart)

cart.remove('banana') # 按值删
print(cart)

last_item = cart.pop() # 按下标删除 并返回删除的一项

print(last_item+str(cart))
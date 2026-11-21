from copy import deepcopy  # copy 是 Python 标准库，直接导入即可

cart = [["苹果", 2]]
backup = deepcopy(cart)

cart[0][1] = 3

print(cart)    # [['苹果', 3]]
print(backup)  # [['苹果', 2]]
n = int(input('請輸入一個三位數：'))
a = n // 100
b = (n % 100) // 10
c = (n % 100) % 10
all = a + b + c
print('每位數字的總和：',all)
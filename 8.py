n = int(input('請輸入一個五位數：'))
a = n // 10000
b = (n % 10000) // 1000
c = (n % 1000) // 100
d = (n % 100) // 10
e = n % 10
print('結果：')
print(a)
print(b)
print(c)
print(d)
print(e)
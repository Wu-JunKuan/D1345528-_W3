n = int(input('輸入三位數字：'))
a = n // 100
b = (n % 100) // 10
c = (n % 100) % 10
print('結果：',c,end='')
print(b,end='')
print(a)
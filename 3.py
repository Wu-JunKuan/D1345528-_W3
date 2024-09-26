n = int(input('輸入數字：'))
result = (n % 2 == 0) * "偶數" + (n % 2 == 1) * "奇數"
print(f"{n} 是 {result}")
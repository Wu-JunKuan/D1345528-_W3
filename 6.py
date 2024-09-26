a = float(input('輸入係數 a：'))
b = float(input('輸入係數 b：'))
c = float(input('輸入係數 c：'))
x1 = (-b + (b**2 - 4 * a * c )**0.5) / 2 * a
x2 = (-b - (b**2 - 4 * a * c )**0.5) / 2 * a
print('方程式的根為：','x1 =',x1,'x2 =',x2)
# print('\n', var1 | var2)
# print(5 or 6)
# print(5 | 6)

# short-circuit-evaluation.
# num1 = 10

# print('\n', num1 > 5 or abc)
# print(0 or 6)

# kidsHeight = int(input('\n신장을 입력하세요(cm): '))
# print(120 <= kidsHeight and kidsHeight < 170)

# inputs = []
# inputs.append(input('수입: '))
# inputs.append(input('지출: '))

# income, outcome = [float(i) for i in inputs]
# print('흑자' if income > outcome else '적자')

crtBright = 50
brightThres = 60
print('Turn on' if crtBright < brightThres else 'Turn off')
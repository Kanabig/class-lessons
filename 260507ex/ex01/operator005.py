import random
import operator

# count = 0

# while(True):
#     count += 1
#     result = random.randrange(0,100)

#     if(result == 0):
#         break

# print(count)

a, b = 10, 10
print(operator.add(a, b))
print(operator.sub(a, b))
print(operator.mul(a, b))
print(operator.truediv(a, b))
print(operator.mod(a, b))
print(operator.floordiv(a, b))
print(operator.pow(a, b))

print(operator.eq(a, b))
print(operator.ne(a, b))
print(operator.gt(a, b))
print(operator.ge(a, b))
print(operator.lt(a, b))
print(operator.le(a, b))

a, b = True, False
print(operator.and_(a, b))
print(operator.or_(a, b))
print(operator.not_(a))

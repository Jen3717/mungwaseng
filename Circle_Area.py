# calculate the area of a circle
# print the result the nearest thousandth(셋째자리까지)

import math

r = float(input("반지름길이를 입력하시오 : "))
result = r * r * math.pi

print("반지름이 ",r,"길이인 원의 넓이는 %.3f 입니다." %result)

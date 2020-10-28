from decimal import Decimal


PI = 3.14

print(round(PI, 1))
print(round(PI))  # always get an integer
print(round(PI, 0))
print(round(Decimal(PI), 1))
print(round(Decimal('3.14')))

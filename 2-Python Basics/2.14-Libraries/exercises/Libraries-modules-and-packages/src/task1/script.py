from math_mod import add, sub, mul, div
import string_mod

a = 4
b = 17
c = 33
d = 19
e = 3
f = 23
g = 44

s1 = 'Hello'
s2 = 'DCI'
s3 = string_mod.con(s1 + s2, '007')

print(f"Result of adding {a} and {b} is {add(a, b)}")
print(f"Result of subtracting  {c} and {d}  {sub(c, d)}")
print(f"Result of multiplying  {e} and {f} is {mul(e, f)}")
print(f"Result of dividing  {g} by {e} is {div(g, e)}")

print(f"Result of concatenation of '{s1}'' and '{s2}'' is {string_mod.con(s1, s2)}")
print(f"Result of creating string from list ['{s1}'', '{s2}''] is {string_mod.string_from_list([s1, s2])}")
print(f"Result of checking digits in the string '{s3}' is {string_mod.check_digit(s3)}")

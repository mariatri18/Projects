import math

a1 = float (input ('a1 = '))
a2 = float (input ('a2 = '))
b1 = float (input ('b1 = '))
b2 = float (input ('b2 = '))

a_b = (a1 * b1) + (a2 * b2)


a = math.sqrt(a1 ** 2 + a2 ** 2)
a = math.fabs(a)

b = math.sqrt(b1 ** 2 + b2 ** 2)
b = math.fabs(b)

costh = math.acos (a_b/(a*b))
goniath = math.degrees(costh)

print(costh)
print(goniath)

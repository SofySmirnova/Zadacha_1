import matplotlib.pyplot as plt
from math import *

#Дано
cp = 0.04
cf = 0.0071
cw = 0.0025
alpha = 1.002
P = 0.001
Lel = 0.00001

# Оценка количества ступней
Rf = cf / (1 - cf)
print("Rf =", Rf)
Rw = cw / (1 - cw)
print("Rw =", Rw)
Rp = cp / (1 - cp)
print("Rp =", Rp)
q = pow(alpha, 2)
print("q =", q)
e = q - 1
print('e =', e)
Sw = log(Rf / Rw) * 2 / e
print("Sw =", Sw)
Sp = log(Rp / Rf) * 2 / e
print("Sp =", Sp)
S =int(Sw + Sp) #количство ступеней в каскаде
print("S =", S)
f = int(- log(Rp / Rf) / log(alpha) + S + 1)
print("f =", f)
W = P * (cp - cf) / (cf - cw)
print("W =", W)
F = P + W
print("F =", F)


# Построение графиков C(s) и L/P
cs = [Rf * pow(alpha, i - f) for i in range(S)] #Зависимость концентрации от номера ступени
l = []
l_p = []
d_U = []
U = 0
for i in range(S):
    if i + 1 < f:
        temp = (alpha + 1) * W * (cs[i] - cw) / ((alpha - 1) * cs[i] * (1 - cs[i]))
        temp_p = (alpha + 1) * W * (cs[i] - cw) / (P * (alpha - 1) * cs[i] * (1 - cs[i]))
        l.append(temp)
        l_p.append(temp_p)
    else:
        temp = (alpha + 1) * P * (cp - cs[i]) / ((alpha - 1) * cs[i] * (1 - cs[i]))
        temp_p = (alpha + 1) * (cp - cs[i]) / ((alpha - 1) * cs[i] * (1 - cs[i]))
        l.append(temp)
        l_p.append(temp_p)
    d_U.append(l_p[i] * (alpha + 1) * log(alpha) / (alpha - 1))
    U += d_U[i]

Z = U / (Lel * (alpha + 1) * log(alpha) / (alpha - 1))
print("Z =", Z)
L_sum = (2 * cp - 1) * log(Rp) + W * (2 * cw - 1) * log(Rw) / P - F * (2 * cf - 1) * log(Rf) / P
print("L_sum =", L_sum)
s_array = [i for i in range(S)]
fig = plt.subplots()
plt.plot(s_array, cs)
plt.title("C(s)")
plt.xlabel("S")
plt.ylabel("C(s)")
plt.show()

import math

'''
Force (tons)
q1 = 1.y (t/m)
P1 = 2.x
P2 = 3.y
P3 = 2.x
q2 = 1.y (t/m)

Distance (m)
a = 2.x
b = 2.x
c = 1.x
d = 1.x
e = 1.x
f = 1.x
g = 1.x
h = 1.x
i = 2.x
j = 2.x

d (distance)
d (A - B)
q1d = 2.x * 2
P1d = 2.x * 2 + 1.x
'''
VERSION = "0.1.0-ALPHA"

x = 5
y = 4

# Force 
q1 = float(f"1.{y}")
P1 = float(f"2.{x}")
P2 = float(f"3.{y}")
P3 = float(f"2.{x}")
q2 = float(f"1.{y}")

# Distance
a = float(f"2.{x}") # A to q1
b = float(f"2.{x}") # q1 to B
c = float(f"1.{x}") # B to E
d = float(f"1.{x}") # E to S1
e = float(f"1.{x}") # S1 to F
f = float(f"1.{x}") # F to S2
g = float(f"1.{x}") # S2 to G
h = float(f"1.{x}") # G to C
i = float(f"2.{x}") # C to q2
j = float(f"2.{x}") # q2 to D

# Span Sequence
# A, B, E, S1, F, S2, G, C, D

# (A) getting focus reactions

# (1) distance between S1 to S2 or (e + f)
# (1a) rs1v reaction
# ΣS2 = 0
rs1v = 0
rs1v = P2 * f / (e + f)

# (1b) rs2v reaction
# ΣS1 = 0
rs2v = 0
rs2v = P2 * e / (e + f)
# output
# print("RS1V Reaction = " + str(rs1v) + '\n' + "RS2V Reaction = " + str(rs2v), end='\n')

# (2) distance between A to B + B to S1 or (a + b + c + d)
# (2a) rav reaction
# ΣMB = 0
rav = 0
rav = ((0.5 * q1 * (a + b) ** 2) - (rs1v * (c + d)) - (P1 * d)) / (a + b)

# (2b) rav reaction
# ΣMA = 0
rbv = 0
rbv = ((0.5 * q1 * (a + b) ** 2) + (rs1v * (a + b + c + d)) + (P1 * (a + b + c))) / (a + b)
# output
# print("RAV Reaction = " + str(rav) + '\n' + "RBV Reaction = " + str(rbv), end='\n')

# (3) control
# ΣkV = 0

# A to S1 distance
# because A to S1 and S2 to D are the same
# we can check it just once ??
# rs1v become force
Q1 = q1 * (a + b)
S1Force_Total = Q1 + P1 + rs1v
control = None
if(round((rav + rbv), 3) == round(S1Force_Total, 3)):
    control = True
else:
    control = False
# output
# print("Control = " + str(control), end='\n')
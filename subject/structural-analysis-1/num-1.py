import math

'''
Force (tons)
q1 = 1.x (t/m)
P1 = 2.y (30°)
P2 = 1.y

Distance (m)
a = 2.x
b = 2.y
c = 2.y
d = 1.x

d (distance uniform load)
d (A - B)
q1d = 2.x
P1d = 2.x + 2.y
'''
VERSION = "0.1.0-ALPHA"

x = 2
y = 4

# Force
q1 = float(f"1.{x}")
P1 = float(f"2.{y}")
P2 = float(f"1.{y}")

# Distance
a = float(f"2.{x}") # A to C
b = float(f"2.{y}") # C to D
c = float(f"2.{y}") # D to B
d = float(f"1.{x}") # B to E

# Span Sequence
# A, C, D, B, E

# (A) getting focus reactions

# Inclined load
# degress 30°
P1H = P1*math.cos(math.radians(30))
P1V = P1*math.sin(math.radians(30))

# (1) distance between A to B or (a + b + c)
# (1a) rav reaction
# ΣMB = 0
rav = 0
rav = ((q1*a*((a/2)+b+c)) + (P1V*c) - (P2*d))/(a+b+c)

# (1b) rav reaction
# ΣMA = 0
rbv = 0
rbv = ((q1*a*(a/2)) + (P1V*(a+b)) + (P2*(a+b+c+d)))/(a+b+c) 
# output
# print("RAV Reaction = " + "{:.3f}".format(rav) + '\n' + "RBV Reaction = " + "{:.3f}".format(rbv), end='\n')

# (2) control
# ΣkV = 0

control = None
if "{:.3f}".format(rav+rbv) == "{:.3f}".format(q1*a+P1V+P2) :
    control = True
else :
    control = False
# output
# print("Control = " + str(control), end='\n')

# (B) Moment of force
# Ba Span (A-C)

# Distance (acx)
ac0 = 0
ac1 = 1
ac2 = 2
aca = a

# formula => macx = rav*acx - (q1/2*acx**2)
mac0 = rav*ac0 - (q1/2*ac0**2)
mac1 = rav*ac1 - (q1/2*ac1**2)
mac2 = rav*ac2 - (q1/2*ac2**2)
maca = rav*aca - (q1/2*aca**2)
# output
# print("{:.3f}".format(maca), end='\n')

# Bb Span (C-D)

# Distance (cdx)
cda = a
cd3 = 3
cd4 = 4
cdba = b+a

# formula => mcdx = rav*cdx - (q1*a*cdx)
mcda = rav*cda - (q1*a*(cda-(a/2)))
mcd3 = rav*cd3 - (q1*a*(cd3-(a/2)))
mcd4 = rav*cd4 - (q1*a*(cd4-(a/2)))
mcdba = rav*cdba - (q1*a*(cdba-(a/2)))
# output
# print("{:.3f}".format(mcda), end='\n')

# Bc Span (D-B)

# Distance (dbx)
dbba = b+a
db5 = 5
db6 = 6
dbbac = b+a+c

# formula => mdbx = rav*dbx - (q1*a*dbx)
mdbba = rav*dbba - (q1*a*(dbba-(a/2))) - P1V*(dbba-(a+b))
mdb5 = rav*db5 - (q1*a*(db5-(a/2))) - P1V*(db5-(a+b))
mdb6 = rav*db6 - (q1*a*(db6-(a/2))) - P1V*(db6-(a+b))
mdbbac = rav*dbbac - (q1*a*(dbbac-(a/2))) - P1V*(dbbac-(a+b))
# output
# print("{:.3f}".format(mdbbac), end='\n')

# Bd Span (B-E)

# Distance (acx)
bebac = b+a+c
be7 = 7
be8 = 8
bebacd = b+a+c+d

# formula => mbex = rav*bex - (q1*a*bex)
mbebac = rav*bebac - (q1*a*(bebac-(a/2))) - P1V*(bebac-(a+b)) + rbv*(bebac - (a+b+c))
mbe7 = rav*be7 - (q1*a*(be7-(a/2))) - P1V*(be7-(a+b)) + rbv*(be7 - (a+b+c))
mbe8 = rav*be8 - (q1*a*(be8-(a/2))) - P1V*(be8-(a+b)) + rbv*(be8 - (a+b+c))
mbebacd = rav*bebacd - (q1*a*(bebacd-(a/2))) - P1V*(bebacd-(a+b)) + rbv*(bebacd - (a+b+c)) + P2*(bebacd-(a+b+c+d))
# output
# print("{:.3f}".format(mbebacd), end='\n')
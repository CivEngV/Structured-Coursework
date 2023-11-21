import math

'''
1) calculate
  a) node equilibrium
     i) analytical
     ii) graphical
  b) cremona
     with:
       P = 21.5 kN
       I = 5.4 m
       T = 6.0 m
2) next..
'''
VERSION = "0.1.0-ALPHA1"

# i) analytical

P = 21.5
I = 5.4
T = 6.0

P_total = 6

span_length = 5 * I

def getSpanLength(length):
    return span_length - (I * length)

# (A) getting focus reactions

# because the load is symmetrical then rav = rbv
# simple method
# rav = (P * P_total) / 2
# rbv = rav

# (1) rav reaction
# ΣMB = 0
rav = None
rav = sum(P * getSpanLength(i) for i in range(6)) / span_length

# (2) rbv reaction
# ΣMA = 0
rbv = None
rbv = rav

# (3) control
# ΣkV = 0
# rav + rbv = P * P_total

control = None
if((rav + rbv) == (P * P_total)):
    control = True
else:
    control = False

# (4) rah reaction
# no rah reaction, because there is no horizontal force

# (B) get the angle measure

tanθ = None
tanθ = math.degrees(math.atan2(T, (I / 2)))
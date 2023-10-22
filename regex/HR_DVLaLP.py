"""
input
(75, 180)
(+90.0, -147.45)
(77.11112223331, 149.99999999)
(+90, +180)
(90, 180)
(-90.00000, -180.0000)
(75, 280)
(+190.0, -147.45)
(77.11112223331, 249.99999999)
(+90, +180.2)
(90., 180.)
(-090.00000, -180.0000)
"""

"""
output
Valid
Valid
Valid
Valid
Valid
Valid
Invalid
Invalid
Invalid
Invalid
Invalid
Invalid
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = input()
for i in range(int(N)):
    coordinate = input()
    X = re.findall(r'^\([+-]?[1-9]\d+\.?\d*,', coordinate)[0][1:-1]
    #^\([+-]?\d+\.?\d*,
    Y = re.findall(r', [+-]?\d+\.?\d*\)$', coordinate)[0][2:-1]
    if -90 <= float(X) and float(X) <= 90 and -180 <= float(Y) and float(Y) <= 180:
        print('Valid')
    else:
        print('Invalid')

# ToDo
# distinct between 090 and 90
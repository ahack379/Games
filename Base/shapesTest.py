LEN = 20
X = 100
Y = 100

#Adjust for later weirdness by adding in unecessary points...

T = [(X, Y), (X, Y + LEN), (X, Y +2*LEN), (X, Y + 3*LEN), (X + LEN, Y + 3*LEN), (X + LEN,Y + 2*LEN), (X + 2*LEN, Y + 2*LEN), (X + 2*LEN, Y + LEN), (X + LEN,Y + LEN), (X + LEN,Y)]

L = [(X, Y), (X, Y + LEN), (X, Y + 2*LEN), (X, Y + 3*LEN), (X + LEN, Y + 3*LEN), (X + LEN, Y + 2*LEN), (X + LEN,Y + LEN), (X + 2*LEN,Y+LEN), (X+2*LEN,Y), (X +LEN, Y) ]  

L_back = [(X + 2*LEN, Y), (X + 2*LEN, Y + LEN), (X + 2*LEN, Y + 2*LEN), (X + 2*LEN, Y + 3*LEN), (X +LEN, Y + 3*LEN), (X + LEN, Y + 2*LEN), (X + LEN,Y + LEN), (X,Y+LEN), (X,Y), (X + LEN, Y)]

I = [(X, Y), (X, Y + LEN), (X, Y + 2*LEN), (X, Y + 3*LEN), (X + LEN, Y + 3*LEN), (X + LEN, Y + 2*LEN), (X+LEN, Y + LEN ), (X + LEN,Y)]

Box = [(X, Y), (X, Y+LEN), (X, Y + 2*LEN), (X + LEN, Y + 2*LEN), (X + 2*LEN, Y + 2*LEN),(X + 2*LEN, Y + LEN), (X + 2*LEN,Y), (X + LEN, Y ) ] 

Z = [(X, Y), (X, Y + LEN), (X + LEN, Y + LEN), (X + LEN,Y + 2*LEN), (X + 2*LEN, Y + 2*LEN), (X + 3*LEN, Y + 2*LEN), (X + 3*LEN, Y + LEN), (X + 2*LEN,Y + LEN), (X + 2*LEN,Y), (X + LEN, Y) ]

Z_back = [(X + 3*LEN, Y), (X + 3*LEN, Y + LEN), (X + 2*LEN, Y + LEN), (X + 2*LEN,Y + 2*LEN), (X + LEN, Y + 2*LEN), (X,Y + 2*LEN), (X,Y + LEN), (X + LEN,Y + LEN), (X+LEN,Y), (X + 2*LEN, Y) ]


LEN = 20
X = 20
Y = 0

T = [(X, Y), (X, Y + 3*LEN), (X + LEN, Y + 3*LEN), (X + LEN,Y + 2*LEN), (X + 2*LEN, Y + 2*LEN), (X + 2*LEN, Y + LEN), (X + LEN,Y + LEN), (X + LEN,Y)]
T_box = [ (X + LEN/2, Y + LEN/2), (X + LEN/2, Y + 3*LEN/2), (X + LEN/2, Y + 5*LEN/2), (X + 3 * LEN/2, Y + 3*LEN/2) ]

L = [(X, Y), (X, Y + 3*LEN), (X + LEN, Y + 3*LEN), (X + LEN,Y + LEN), (X + 2*LEN,Y+LEN), (X+2*LEN,Y) ]  
L_box = [ (X + LEN/2, Y +LEN/2), (X + LEN/2, Y + LEN*3/2), (X + LEN/2, Y + LEN*5/2), (X + LEN*3/2, Y + LEN/2) ]

L_back = [(X + 2*LEN, Y), (X + 2*LEN, Y + 3*LEN), (X +LEN, Y + 3*LEN), (X +LEN,Y + LEN), (X,Y+LEN), (X,Y)]
L_back_box = [(X + LEN/2,Y + LEN/2), (X + 3*LEN/2, Y +LEN/2), (X + 3*LEN/2, Y + 3*LEN/2), (X + 3*LEN/2, Y + 5*LEN/2) ]

I = [(X, Y), (X, Y + 3*LEN), (X + LEN, Y + 3*LEN), (X + LEN,Y)]
I_box = [(X + LEN/2, Y + LEN/2), (X + LEN/2, Y + 3*LEN/2), (X + LEN/2, Y + 5*LEN/2)]

Box = [(X, Y), (X, Y + 2*LEN), (X + 2*LEN, Y + 2*LEN), (X + 2*LEN,Y)] 
Box_box = [(X + LEN/2, Y +LEN/2), (X + LEN/2, Y + 3*LEN/2), (X + 3*LEN/2, Y + 3*LEN/2), (X + 3*LEN/2, Y + LEN/2)]

Z = [(X, Y), (X, Y + LEN), (X + LEN, Y + LEN), (X + LEN,Y + 2*LEN), (X + 3*LEN, Y + 2*LEN), (X + 3*LEN, Y + LEN), (X + 2*LEN,Y + LEN), (X + 2*LEN,Y) ]
Z_box = [(X  + LEN/2, Y + LEN/2), (X + 3*LEN/2, Y + LEN/2), (X + 3*LEN/2, Y + 3*LEN/2), (X + 5*LEN/2, Y + 3*LEN/2)]

Z_back = [(X + 3*LEN, Y), (X + 3*LEN, Y + LEN), (X + 2*LEN, Y + LEN), (X + 2*LEN,Y + 2*LEN), (X,Y + 2*LEN), (X,Y + LEN), (X + LEN,Y + LEN), (X+LEN,Y) ]
Z_back_box = [( X + LEN/2, Y + 3*LEN/2), (X + 3*LEN/2, Y + 3*LEN/2), (X + 3*LEN/2,Y + LEN/2), (X + 5*LEN/2, Y+LEN/2)]


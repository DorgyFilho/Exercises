#126 - Triângulo

t = 'N'
Num = input().split()
A = int(Num[0])
B = int(Num[1])
C = int(Num[2])
D = int(Num[3])

if ((abs(B-C) < A < B+C or
    abs(B-D) < A < B+D or
    abs(C-D) < A < C+D or
    abs(A-C) < B < A+C or
    abs(A-D) < B < A+D or
    abs(C-D) < B < C+D or
    abs(A-B) < C < A+B or
    abs(A-D) < C < A+D or
    abs(B-D) < C < B+D or
    abs(A-B) < D < A+B or
    abs(A-C) < D < A+C or
    abs(B-C) < D < B+C)):
    
    t = 'S'

print(t)
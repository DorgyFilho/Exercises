#094 - Fibonacci Em Vetor

Fibo = []
T = int(input(''))
First = 0
Second = 1
Next = 0
Fibo.append(First)

for i in range(T):
    X = int(input(''))
    for i in range(X+1):
        First = Second + Next 
        Second = Next
        Next = First
        Fibo.append(Next)
    print('Fib(%d) = %d' %(X, Fibo[i]))


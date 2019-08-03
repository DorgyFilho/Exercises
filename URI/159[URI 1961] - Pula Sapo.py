#159 - Pula Sapo

def JumpingFrog():
    a,b = map(int, input().split())
    Height = a

    jump = [int(c) for c in input().split()]

    result = 'YOU WIN'

    for i in range(len(jump)-1):

        difference = abs(jump[i+1] - jump[i])
        if difference > Height:
            result = 'GAME OVER'
            break

    return result

print(JumpingFrog())


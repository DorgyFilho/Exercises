#025 - Celsius Para Fahreinheit

C = float(input('Temperatura em C°: '))
Coef = 9.0/5.0
F = (C*Coef) + 32
print(f'{C}° ------> {F}°F')
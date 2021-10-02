temperature=float(input('type in a number: '))
if temperature == 70 or temperature > 70:
    print('too hot!')
elif temperature < 70 and (temperature > 60 or temperature == 60):
    print('feels nice')
else:
    print('too cold')

for letter in 'python':
    print(f'{letter}',end=',')
print()

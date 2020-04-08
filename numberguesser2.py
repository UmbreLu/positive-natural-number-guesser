from math import log


#big number input treat function---------------------------------

def ninput():
    wrong_input = True
    while wrong_input:
        raw = input('<Enter positive number>')
        try:
            if int(raw) > 0:
                return int(raw)
            else:
                print('Invalid input. Please enter a positive integer.')
        except:
            print('Invalid input. Please enter a positive integer.')

#y/n input treat function-----------------------------------------

def cinput():
    wrong_input = True
    while wrong_input:
        raw = input('<y/n>' )
        if (raw == 'y') or (raw == 'n'):
            wrong_input = False
        else:
            print("Please insert only 'y' for 'yes' and 'n' for 'no'.")
            pass
    return raw

#-------------------------------------------------------

print('''
I'll guess any positive natural number you think of. Just keep in mind
that the bigger this number universe is, more steps it will take to
guess your number.

>ADVICE<: remember that in math no number is "bigger than" itself, so the
answer must be "no"(n) if it's the case.

>ADVICE2<: if you answer the "bigger or not" question wrongly, there is
no turning back, you'll have to restart the program. So, in order to
avoid errors, it's advised to write down your imagined number, spetially
if it's big or looks scrabbled.

Let's begin.
''')
#input_number = ninput()

max = 512
mul = 2
steps = 0
while True:
    print(f'Is your number bigger than {max}?')
    steps += 1
    if cinput() == 'y':
        min = max
        max = max * mul
        mul = mul * 2
        
    else:
        min += 1
        break

factor = max
f = 0
while not factor == 1:
    factor = factor / 2
    f += 1


print(f'''\nOk. I'll take more {f} steps to guess it.
''')

while f > 0:
    half = (max - min + 1) / 2 + (min - 1)
    steps += 1
    print(f'\n({f}) Is your number bigger than {int(half)}?', end='')
    if cinput() == 'y':
        min = half + 1
    else:
        max = half
    f -= 1

print(f"\n({f})  Your secret number is {int(max)}.\n It took {steps} steps in total.")


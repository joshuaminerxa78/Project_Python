import random

print('')
print('================================')
print('Rock Paper Scissors Lizard Spock')
print('================================')

print('1 Rock')
print('2 Paper')
print('3 Scissors')
print('4 Lizard')
print('5 Spock')

print('')


chose = int(input('Pick a number '))
cpu = random.randint(1,5)

if chose == 1:
    print('you chose: Rock')
elif chose == 2:
    print('you chose: Paper')
elif chose == 3:
    print('you chose: Scissors')
elif chose == 4:
    print('you chose: Lizard')
elif chose == 5:
    print('you chose: Spock')

if cpu == 1:
    print('cpu chose: Rock')
elif cpu == 2:
    print('cpu chose: Paper')
elif cpu == 3:
    print('cpu chose: Scissors')
elif cpu == 4:
    print('cpu chose: Lizard')
elif cpu == 5:
    print('cpu chose: Spock')

if chose > 5 or chose <= 0:
    print('')
    print('please only 1-5 type num')
    print('')

if chose == 2 and cpu == 1:
    print('The win is CPU')
elif chose == 1 and cpu == 2:
    print('The win is You')

if chose == 2 and cpu == 3:
    print('The win is CPU')
elif chose == 3 and cpu == 2:
    print('The win is You')

if chose == 1 and cpu == 4:
    print('The win is You')
elif chose == 4 and cpu == 1:
    print('The win is CPU')

if chose == 4 and cpu == 5:
    print('The win is You')
elif chose == 5 and cpu == 4:
    print('The win is CPU')

if chose == 5 and cpu == 3:
    print('The win is You')
elif chose == 3 and cpu == 5:
    print('The win is CPU')

if chose == 3 and cpu == 4:
    print('The win is You')
elif chose == 4 and cpu == 3:
    print('The win is CPU')

if chose == 4 and cpu == 2:
    print('The win is You')
elif chose == 2 and cpu == 4:
    print('The win is CPU')

if chose == 2 and cpu == 5:
    print('The win is You')
elif chose == 5 and cpu == 2:
    print('The win is CPU')

if chose == 5 and cpu == 1:
    print('The win is You')
elif chose == 1 and cpu == 5:
    print('The win is CPU')

if chose == 1 and cpu == 3:
    print('The win is You')
elif chose == 3 and cpu == 1:
    print('The win is CPU')


if chose == 1 and cpu == 1 or chose == 2 and cpu == 2 or chose == 3 and cpu == 3 or chose == 4 and cpu == 4 or chose == 5 and cpu == 5:
    print('It`s a tie')
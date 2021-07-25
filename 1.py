import random
# seed value = 3
random.seed(3)
for i in range(3):
    print(random.random(), end = ' ')

print('\n')

# seed value = 8
random.seed(8)
for i in range(3):
    print(random.random(), end = ' ')

print('\n')

# seed value again = 3
random.seed(3)
for i in range(3):
    print(random.random(), end = ' ')

print('\n')





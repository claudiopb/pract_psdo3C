import random

dice = random.randint(1,6)
print(dice)
count = 1

while dice != 6:
  dice = random.randint(1,6)
  print(dice)
  count += 1

print('You got 6!')
print('You rolled',count,'times')
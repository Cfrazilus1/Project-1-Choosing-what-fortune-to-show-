import random

lucky_number = random.randint(1,100) 

fortune_number = random.randint(1,3)

fortune_text = ''

if fortune_number == 1:
  fortune_text = 'You will win a million dollars'

if fortune_number == 2:
  fortune_text = 'You will buy a pet'

if fortune_number == 3:
  fortune_text = 'You will lose a shoe' 

print (f' {fortune_text} Your lucky number is: {lucky_number}')
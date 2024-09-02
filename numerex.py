import random

four_d = [0] * random.randint(2,3)
five_d = [0] * random.randint(7, 13)
six_d = [0] * random.randint(2, 4)
seven_d = [0] * random.randint(2, 4)
eight_d = [0] * random.randint(2, 3)
nine_d = [0] * random.randint(1, 2)
ten_d = [0]

## generate numbers
## the amount of numbers, the size of the numbers, the list of numbers
def gen_nums(qtt, size, nums):
  num = ""
  for x in range(qtt):
    for y in range(size):
      num += str(random.randint(0, 9))
    nums[x] = int(num)
    num = ""
    
  return nums

## the game is 15x15 and has a depth of 2
## in depth 0 we have the game the user plays with and see
## in depth 1 we have the completed game, which will be used to compare with the
## user's input
game = [[[" " for x in range(15)] for y in range(15)] for z in range(2)]

four_d = gen_nums(len(four_d), 4, four_d)
five_d = gen_nums(len(five_d), 5, five_d)
six_d = gen_nums(len(six_d), 6, six_d)
seven_d = gen_nums(len(seven_d), 7, seven_d)
eight_d = gen_nums(len(eight_d), 8, eight_d)
nine_d = gen_nums(len(nine_d), 9, nine_d)
ten_d = gen_nums(len(ten_d), 10, ten_d)

for x in range(15):
  for y in range(15):
      game[1][x][y] = "*"

#region Printing the game

print("4 Digits")
for x in range(len(four_d)):
  print(four_d[x])
print("\n")
print("5 Digits")
for x in range(len(five_d)):
  print(five_d[x])
print("\n")
print("6 Digits")
for x in range(len(six_d)):
  print(six_d[x])
print("\n")
print("7 Digits")
for x in range(len(seven_d)):
  print(seven_d[x])
print("\n")
print("8 Digits")
for x in range(len(eight_d)):
  print(eight_d[x])
print("\n")
print("9 Digits")
for x in range(len(nine_d)):
  print(nine_d[x])
print("\n")
print("10 Digits")
for x in range(len(ten_d)):
  print(ten_d[x])
print("\n")

print("         ", end="")
for x in range(15):
  ## avoiding spacing error
  if x < 10:
    print(f"{x}", end="   ")
  else:
    print(f"{x}", end="  ")
  
print("\n\n\n\n")

for x in range(15):
  ## avoiding spacing error
  if x < 10:
    print(f"{x}", end="        ")
  else:
    print(f"{x}", end="       ")
  for y in range(15):
    print(game[1][x][y], end="   ")
  print("\n")

#endregion

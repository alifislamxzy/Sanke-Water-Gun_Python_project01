import random

# 1 for snake
# -1 for water
# 0 for gun


computer = random.choice([-1, 0, 1])
yousrt = input("Enter you choice: ")
youDit = {"s":1, "w":-1, "g":0}
reverseDit = {1:"Snake", -1:"Water", 0:"Gun"}

you = youDit[yousrt]

print(f"You chose {reverseDit[you]}\nComputer chose {reverseDit[computer]}")

if(computer == you):
    print("It's a draw")
else:
    if(computer ==-1 and you ==1):
        print("You Win!")
    elif(computer ==-1 and you ==0):
        print("You Lose!")
    elif(computer ==1 and you ==-1):
        print("You Win!")
    elif(computer ==1 and you ==0):
        print("You Win!")
    elif(compile ==0  and you ==-1):
        print("You Win!")
    elif(computer ==0 and you ==1):
        print("You Win")
    else:
        print("somthing is worng!")
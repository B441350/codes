# while loop
#loop variable initialized , condition, loop varible update
#above 3 statements must be followed in iterative statements
n = int(input("enter n value"))
i = 0          # loop variable initialized
while i <= n:  # condition
    print (i)
    i = i+1   # loop variable updation


while = true:
    response = input()
    if int(response) %7 ==0:
        break



# While loop syntax
# while expression:
# You can use else block with while as well


guess_num_range = 20
num_to_be_guessed = int(guess_num_range * random.random()) + 1
guess = 0

while guess != num_to_be_guessed:
    guess = int(input("Guess the number: "))
    if guess > 0:
        if guess > num_to_be_guessed:
            print("Number is too large")
        elif guess < num_to_be_guessed:
            print("Number is too small")
    else:
        print("Sorry that you're giving up!")
        break
else:
    print("Congratulation. You made it!")


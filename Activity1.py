import time
import random
playing = True
number = random.randint(1,30)
print("Guess my number.(1 to 30)")
while playing:
    try:
        guess = int(input("Enter a number 1 to 30:"))
    except:
        print("Wrong input, try again")
    else:
        if number == guess:
            print("You got the correct number!")
            playing = False
        else:
            print("Wrong Number, try again.")
            if guess - number <= 10:
                if number - guess <=5:
                    print("HOT🔥")
                else:
                    print("Warm🌡️")
            else:
                print("Chilly🤧")
            if guess - number >= 15:
                print("Cold❄️")
            time.sleep(1)
            
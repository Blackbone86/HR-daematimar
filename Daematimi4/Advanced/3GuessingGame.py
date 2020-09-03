# These lines you can keep as is
print("Think of a number between 1 and 100 (inclusive)")
print("I am going to guess what it is")
input("Press enter when you are ready to play")

# Here you might want to initialize some variables
counter = 0
lower = 1
upper = 100
guess = 50
cmd = ""
# Then start a while loop
while cmd != "q":
    if counter == 7:
        print("Tsk, tsk, don't try to cheat me")
        break
    print("Is the number", guess, "?")
    print("Type one of the following letters and press enter:")
    print("h: if the guess is too (h)igh")
    print("l: if the guess is too (l)ow")
    print("c: if the guess is (c)orrect")
    print("q: to (q)uit the game")
    cmd = input()
    if cmd == "l":
        lower = guess
        guess = (lower + upper) // 2
    elif cmd == "h":
        upper = guess
        guess = (lower-1 + upper) // 2
    elif cmd == "c":
        print("I AM VICTORIOUS")
        break
    elif cmd == "q":
        print("Quitter")
        continue
    counter += 1

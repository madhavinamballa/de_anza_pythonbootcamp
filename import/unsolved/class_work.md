# write a program, give user 5 chances to guess the number ,If the number of attempts becomes greater than the number of chances the game stops and the user loses the game. If the user guesses the correct number in the given number of chances then he or she will win. After every guess made by the user, the program informs the user whether the guessed number was smaller, greater than the actual generated number



# Print any random number 5 times from a given list.
my_list=[12,23,4,5,6,7,8,8]
for x in range(5): 
    print(random.choice(my_list)) 
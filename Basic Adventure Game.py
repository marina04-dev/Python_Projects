print("Welcome to my First Game!")
name = input("What is your name? ")
age = int(input("What is your age? "))
    
health = 10 

if age >= 18:
    print("You are old enough to play!")
    wants_to_play = input("Do you want to play?(yes/no) ").lower()
    if wants_to_play == "yes":
        print("Let's Play!")
        print(f"You are starting with {health} health!")
        left_or_right = input("First Choice...Left Or Right?(left/right) ").lower()
        if left_or_right == "left":
            ans = input("Nice, you follow a path and reach\
            a lake...Do you swim accross or go around?(accross/around) ").lower()
            if ans == "around":
                print("You went around and reached the other side of the lake!")
                print(f"You're health is {health}!")
            elif ans == "accross":
                print("You managed to get accross, but were bit by a fish and lost 5 health!")
                health -= 5
                print(f"You're health is {health}!")
                
            ans = input("You notice a house and a river. Which do you go to?(river/house) ").lower()
            if ans == "house":
                print("You go to the house and are greated by the owner... He does not like you and you lost 5 health")
                health -= 5
                print(f"You're health is {health}!")
                
                if health <= 0:
                    print("You are out health! You lost!")
                else:
                    print("Hurray!!! You Survived! Congratulations!!!")
            else:
                print("You fell in the river and lost...")
                
            
                
        else:
            print("You fell down and lost...Try Again!")
        
        
    else:
        print("See you later!")
else:
    print("Ooops! You are not old enough to play! Sorry!")

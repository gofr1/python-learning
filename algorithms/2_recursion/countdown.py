# use recursion to implement a countdown counter

def countdown(x):
    if x == 0:
        print("Done!")
        return
    else:
        print(x, "...")
        countdown(x-1)
        print("foo") # if put something after function call this line will be executed after 
        # "return" as much times as function was called

countdown(5)
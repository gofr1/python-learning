#!/usr/bin/env python3
# 
# the CONTINUE clause is used to shortcut a loop
# and start it again as if it had reached the end
# of its body of code
# 
# the BREAK clause is used to break out of a loop
# prematurely, execution will continue after the 
# entire loop structure 
# 
# the ELSE executes only if the loop ends normally
# it will not execute if BREAK is used to end the loop

secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 5

while pw != secret:
    count += 1
    if count > max_attempt: break
    if count == 3: continue # the forth attempt will be skipped
    pw = input(f"{count}: What is the secret word? ")
else:
    auth = True

print("Authorized" if auth else "Calling the FBI ....")


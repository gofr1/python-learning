#!/usr/bin/env python3

import threading

slowcooker_lid = threading.Lock()
soup_servings = 11
soup_taken = threading.Condition(lock=slowcooker_lid) # if you not specify the lock python will create an RLock for this
number_of_people = 5

def hungry_person(person_id):
    global soup_servings, number_of_people
    while soup_servings > 0:
        with slowcooker_lid:
            # # This way threads will be repeatedly checking who's turn is it
            # if (person_id == (soup_servings%number_of_people)) and soup_servings > 0: # check if it is your turn
            #     soup_servings -= 1
            #     print(f'Person {person_id} took soup! Servings left: {soup_servings}')
            # else: # not your turn
            #     print(f'Person {person_id} checked... then put the lid back.')

            # with condition both will take there soup one by one
            while (person_id != (soup_servings%number_of_people)) and soup_servings > 0: # check if it is your turn
                print(f'Person {person_id} checked... then put the lid back.')
                soup_taken.wait()
            if soup_servings > 0:
                soup_servings -= 1
                print(f'Person {person_id} took soup! Servings left: {soup_servings}')
                soup_taken.notify() if number_of_people <= 2 else soup_taken.notify_all()
                
if __name__ == '__main__':
    for person in range(number_of_people):
        threading.Thread(target=hungry_person, args=(person,)).start()
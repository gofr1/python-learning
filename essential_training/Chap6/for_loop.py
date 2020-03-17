#!/usr/bin/env python3

animals = ("bear", "bunny", "dog", "cat", "velociraptor")

for pet in animals:
    print(pet)

for pet in animals:
    if pet == 'dog': continue # skipped 
    # if pet == 'velociraptor': break
    print(pet)
else:
    print("that is all of the animals")
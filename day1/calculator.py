#!/usr/bin/env python3
"""calculates the fuel required for a mass and the recursive fuel required for a mass """


def calc_mass(x):
    """calculates the fuel required for this mass"""
    return (x // 3) - 2


def calc_mass_with_adjustments(x):
    """calculates the fuel required for this mass taking into account the fuel needed for the extra fuel"""
    total_fuel = 0
    round = x
    while 1 == 1:
        fuel = calc_mass(round)
        if fuel <= 0:
            break
        total_fuel += fuel
        round = fuel
    return total_fuel


inputfile = input("what is the input file for the mass?")
total_fuel_for_all_modules = 0
with open(inputfile, 'r') as f:
    for line in f:
        # print(line)
        intval = int(line)
        total_fuel_for_all_modules += calc_mass_with_adjustments(intval)
print("the total recursive fuel required was ", total_fuel_for_all_modules)

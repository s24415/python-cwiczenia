# EXERCISE 1
import math


def panel_calc(floor_length, floor_width, panel_length, panel_width, panels_package_quantity):
    floor_area = (floor_length * floor_width) * 1.1
    panel_area = panel_length * panel_width

    panels_required = floor_area / panel_area
    packages_required = math.ceil(panels_required / panels_package_quantity)

    return packages_required


# EXERCISE 2

def prime(*numbers):
    for number in numbers:
        is_prime = True
        for i in range(2, int(math.sqrt(number))):
            if number % i == 0:
                is_prime = False
                break
        if number < 2:
            is_prime = False
        print(f"{str(number)} {'is prime' if is_prime else 'is not'} prime")

# EXERCISE 3

def caesar_cypher(message, shift):
    result = ""
    for char in message:
        ascii_value = ord(char.upper())
        if ascii_value < 65 or ascii_value > 90:
            result += char
            continue

        new_ascii_value = ascii_value + shift
        if new_ascii_value > 90:
            shift = new_ascii_value % 90
            new_ascii_value = 64 + shift

        result += chr(new_ascii_value)

    return result

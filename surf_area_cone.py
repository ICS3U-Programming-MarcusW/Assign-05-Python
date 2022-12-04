#!/usr/bin/env python3
# Created By: Marcus Wehbi
# Date: Dec 1 2022
# This program asks the user for a minimum and a maximum to create a range
# It then displays all of the perfect numbers that are within that range
# Then it asks the user for a second range
# It then displays all of the Armstrong numbers that are within that range

import math

# Function to calculate the power of two numbers passed through from the isArmstrong function
# The number is raised to the number of digits in that number
def surfaceCone(radius, height):
    slant_height_cone = math.sqrt(radius * radius + height * height)
    surface_area = math.pi * radius * (radius + slant_height_cone)
    return surface_area


def volumeCone(radius, height):
    volume = math.pi * (radius * radius) * (height / 3)
    return volume


def surfacePyramid(base_edge, height):
    surface_area = (base_edge * base_edge) + (2 * base_edge) * math.sqrt(
        ((base_edge * base_edge) / 4) + (height * height)
    )
    return surface_area


def volumePyramid(base_edge, height):
    volume = (base_edge * base_edge) * (height / 3)
    return volume


def main():
    while True:
        print(
            "This program displays the volume and surface area of cones and square pyramids."
        )

        print("We will start with cones.")
        print("")

        user_units_cone = input("Enter the units for this cone: ")
        print("")

        user_radius_cone = input("Enter the radius of your cone: ")
        print("")

        user_height_cone = input("Enter the height of your cone: ")
        print("")

        try:

            radius_cone = float(user_radius_cone)
            height_cone = float(user_height_cone)

        except Exception:
            print("Please enter a valid number.")
            print("")

        else:

            if radius_cone <= 0 or height_cone <= 0:
                print("Both the radius and height must be positive numbers.")
                print("")
            else:
                surf_area_cone = surfaceCone(radius_cone, height_cone)
                volume_cone = volumeCone(radius_cone, height_cone)
                print(
                    "The surface area of this cone is {:,.2f}{}^2.".format(
                        surf_area_cone, user_units_cone
                    )
                )
                print("")
                print(
                    "The volume of this cone is {:,.2f}{}^3.".format(
                        volume_cone, user_units_cone
                    )
                )
                print("")

        # ...............................................................................

        print("We will now calculate for square pyramids.")
        print("")

        user_units_pyramid = input("Enter the units for this square pyramid: ")
        print("")

        user_base_edge_pyramid = input("Enter the base edge of your square pyramid: ")
        print("")

        user_height_pyramid = input("Enter the height of your square pyramid: ")
        print("")

        try:

            base_edge = float(user_base_edge_pyramid)
            height_pyramid = float(user_height_pyramid)

        except Exception:
            print("Please enter a valid number.")
            print("")

        else:

            if base_edge <= 0 or height_pyramid <= 0:
                print("Both the base edge and the height must be positive numbers.")
                print("")
            else:
                surf_area_pyramid = surfacePyramid(base_edge, height_pyramid)
                volume_pyramid = volumePyramid(base_edge, height_pyramid)
                print(
                    "The surface area of this square pyramid is {:,.2f}{}^2.".format(
                        surf_area_pyramid, user_units_pyramid
                    )
                )
                print("")
                print(
                    "The volume of this square pyramid is {:,.2f}{}^3.".format(
                        volume_pyramid, user_units_pyramid
                    )
                )
                print("")

        play_again = input(
            "Do you want to use this program (enter 'y' if you would like to): "
        )
        if play_again != "y":
            break

    print("Thank you for playing!")


if __name__ == "__main__":
    main()

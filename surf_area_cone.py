#!/usr/bin/env python3
# Created By: Marcus Wehbi
# Date: Dec 1 2022
# This program calculates the surface area and the volume of a cone
# This program also calculates the surface area and volume of a square pyramid


import math

# Function to calculate the surface area of a cone
# Get radius and height parameters through main
def surfaceCone(radius, height):
    # Calculate for the slant height of the cone
    slant_height_cone = math.sqrt(radius * radius + height * height)
    # Use the slant height to calculate the total surface area
    surface_area = math.pi * radius * (radius + slant_height_cone)
    # Return the value to the function call
    return surface_area


# Function to calculate the volume of a cone
# Get radius and height parameters through main
def volumeCone(radius, height):
    # Calculate the volume of the cone using the formula
    volume = math.pi * (radius * radius) * (height / 3)
    # Return the volume of the cone to the function call
    return volume


# Function to calculate the surface area of a square pyramid
# Get base edge and height parameters through main
def surfacePyramid(base_edge, height):
    # Calculate the surface area of the pyramid using the formula
    surface_area = (base_edge * base_edge) + (2 * base_edge) * math.sqrt(
        ((base_edge * base_edge) / 4) + (height * height)
    )
    # Return the surface area value to the function call
    return surface_area


# Function to calculate the volume of a square pyramid
# Get base edge and height parameters through main
def volumePyramid(base_edge, height):
    # Calculate the volume using the formula
    volume = (base_edge * base_edge) * (height / 3)
    # Return the volume value to the function call
    return volume


# Function to receive input from user, call functions to complete calculations
# and output the surface areas and volumes of cones and square pyramids
def main():
    # Initialize an empty list
    play_again_counter = []
    # Append a cell to it with value zero
    play_again_counter.append(0)
    # Use a loop to ask the user if they want to keep playing
    while True:
        # Explain to the user what the program does
        print(
            "This program displays the volume and surface area of cones and square pyramids."
        )
        print("We will start with cones.")
        print("")
        # Get the units that the user would like to work with
        user_units_cone = input("Enter the units for this cone: ")
        print("")
        # Get the radius of the cone from the user
        user_radius_cone = input("Enter the radius of your cone: ")
        print("")
        # Get the height of the cone from the user
        user_height_cone = input("Enter the height of your cone: ")
        print("")

        try:
            # Use a try catch to convert the inputs (radius and height) to floats
            radius_cone = float(user_radius_cone)
            height_cone = float(user_height_cone)

        except Exception:
            # Message for invalid input
            print("Please enter valid numbers.")
            print("")

        else:

            # Make sure the radius and height are not less than or equal to 0
            if radius_cone <= 0 or height_cone <= 0:
                # Message for when they are less than or equal to 0
                print("Both the radius and height must be positive numbers.")
                print("")
            else:
                # Call the function to calculate for the surface area of a cone
                surf_area_cone = surfaceCone(radius_cone, height_cone)
                # Call the function to calculate for the volume of a cone
                volume_cone = volumeCone(radius_cone, height_cone)
                # Display the surface area rounded to two decimal places with
                # the users units of choice
                print(
                    "The surface area of this cone is {:,.2f}{}^2.".format(
                        surf_area_cone, user_units_cone
                    )
                )
                print("")
                # Display the surface area rounded to two decimal places with
                # the users units of choice
                print(
                    "The volume of this cone is {:,.2f}{}^3.".format(
                        volume_cone, user_units_cone
                    )
                )
                print("")

        # Message so the user knows we are now working on square pyramids
        print("We will now calculate for square pyramids.")
        print("")
        # Get the units that the user would like to work with
        user_units_pyramid = input("Enter the units for this square pyramid: ")
        print("")
        # Get the base edge of the pyramid from the user
        user_base_edge_pyramid = input("Enter the base edge of your square pyramid: ")
        print("")
        # Get the height of the pyramid from the user
        user_height_pyramid = input("Enter the height of your square pyramid: ")
        print("")

        try:
            # Use a try catch to convert the inputs (base edge and height) to floats
            base_edge = float(user_base_edge_pyramid)
            height_pyramid = float(user_height_pyramid)

        except Exception:
            # Message for invalid input
            print("Please enter valid numbers.")
            print("")

        else:
            # Make sure the base edge and height are not less than or equal to 0
            if base_edge <= 0 or height_pyramid <= 0:
                # Message for when they are less than or equal to 0
                print("Both the base edge and the height must be positive numbers.")
                print("")
            else:
                # Call the function to calculate for the surface area of a pyramid
                surf_area_pyramid = surfacePyramid(base_edge, height_pyramid)
                # Call the function to calculate for the volume of a pyramid
                volume_pyramid = volumePyramid(base_edge, height_pyramid)
                # Display the surface area rounded to two decimal places with
                # the users units of choice
                print(
                    "The surface area of this square pyramid is {:,.2f}{}^2.".format(
                        surf_area_pyramid, user_units_pyramid
                    )
                )
                # Display the volume rounded to two decimal places with
                # the users units of choice
                print("")
                print(
                    "The volume of this square pyramid is {:,.2f}{}^3.".format(
                        volume_pyramid, user_units_pyramid
                    )
                )
                print("")

        # Update the list to count how many times the user has used the
        # program
        play_again_counter[0] = play_again_counter[0] + 1
        # Ask the user if they would like play again
        play_again = input(
            "Do you want to use this program (enter 'y' if you would like to): "
        )
        # If they dont say yes, exit the loop
        if play_again != "y":
            # Display how many times they used the program
            print("You used this program " + str(play_again_counter) + " time(s).")
            # Break out of the loop
            break

    # Finally statement to thank the user for playing
    print("Thank you for playing!")


if __name__ == "__main__":
    main()

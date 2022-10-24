#----------------------------------------------------------------#
# source_ingredients.py
# Author: Shameek Hargrave, Nickolas Casalinuovo
# Purpose: queries the Food Data Central API to source nutrient
# data on a provided list of foods, placing the sourced data into
# Mealize propietary DB tables as defined by the categories of each
# food item in the list.
#----------------------------------------------------------------#
import argparse

#----------------------------------------------------------------#
def set_cmd_args():
    parser = argparse.ArgumentParser(description=
        'Retrieves nutrient data for provided food items.',
        allow_abbrev=False)
    parser.add_argument("food items", metavar="food_list",
        help="the list of of dictionary food items and their categories")
    return parser
#----------------------------------------------------------------#
def main():
    parser = set_cmd_args()
    args = parser.parse_args()
    food_list = args.food_list
    # structure 
    # [ { name: "bacon", category: "Meat" }, 
    # { name: "pork chop", category: "Meat" }] 
    # connect to API


    return None

#----------------------------------------------------------------#
if __name__ == "__main__":
    main()
#----------------------------------------------------------------#



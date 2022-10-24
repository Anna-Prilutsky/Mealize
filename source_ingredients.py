#----------------------------------------------------------------#
# source_ingredients.py
# Author: Shameek Hargrave, Nickolas Casalinuovo
# Purpose: queries the Food Data Central API to source nutrient
# data on a provided list of foods, placing the sourced data into
# Mealize propietary DB tables as defined by the categories of each
# food item in the list.
#----------------------------------------------------------------#
import argparse
import requests
import json
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
    # parser = set_cmd_args()
    # args = parser.parse_args()
    # food_list = args.food_list
    # structure 
    food_list = [ 
        { "name": "bacon", "category": "Meat" },
        { "name": "pork chop", "category": "Meat" }
    ] 
    # connect to API

    params = dict(
        # dataType = [],
        pageSize = 1,
    )
    url = 'https://api.nal.usda.gov/fdc/v1/foods/search?query='
    # url += '&api_key=z47Rw2u6Lx680CxpaSEes2tvNUk6fAw3AUtfEHwG'
    for food in food_list:
        full_query = url + food["name"] + '&'
        full_query += 'api_key=z47Rw2u6Lx680CxpaSEes2tvNUk6fAw3AUtfEHwG'
        resp = requests.get(url=full_query, params=params)
        data = resp.json()
        data = data["foods"][0]["foodNutrients"]
        # protein = data.get("nutrie")
        # protein id: 1003
        # carbs id: 1005
        # fats id: 1004,
        # calories id: 1008
        print(data.keys())

    return None

#----------------------------------------------------------------#
if __name__ == "__main__":
    main()
#----------------------------------------------------------------#



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
from datetime import datetime
# import random
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
def get_nutrient_from_list_of_dicts(nutrients, id):
    return next(( (float(nutrient["value"]), nutrient["unitName"]) for nutrient in nutrients if  nutrient["nutrientId"] == id), (0, ""))
#----------------------------------------------------------------#
def get_foods(food_list):
    """
    Queries the FDC food api for each item in the list. Accepts food names and FDC-ids. Returns a json object of each result as a dict of its information.
    """
    # connect to API
    params = dict(
        # dataType = [],
        pageSize = 1,
    )
    url = 'https://api.nal.usda.gov/fdc/v1/foods/search?query='
    # url += '&api_key=z47Rw2u6Lx680CxpaSEes2tvNUk6fAw3AUtfEHwG'
    # ingredients = {}
    result = []
    for food in food_list:
        full_query = url + str(food)+ '&'
        full_query += 'api_key=z47Rw2u6Lx680CxpaSEes2tvNUk6fAw3AUtfEHwG'
        resp = requests.get(url=full_query, params=params)
        data = resp.json()
        # preliminary protocol: grab the first result from the search for this food item
        if len(data["foods"]) > 0:
            item = data["foods"][0]
            # avoid survey data type it doesnt have serving sizes
            print(f"Looking for non-survey item for {food} ")
            for api_item in data["foods"]:
                if "Survey" not in api_item["dataType"]:
                    item = api_item
                    print(f"^^^Found non-survey item!!!")
                    break

            id = item.get("fdcId")
            name = item.get("description")
            category = item.get("foodCategory")
            serving_size = item.get("servingSize")
            units = item.get("servingSizeUnit")

            nutrients = item.get("foodNutrients")
            protein, protein_units = get_nutrient_from_list_of_dicts(nutrients, 1003)
            carbs, carb_units = get_nutrient_from_list_of_dicts(nutrients, 1004)
            fats, fat_units = get_nutrient_from_list_of_dicts(nutrients, 1005)
            cals, cals_units = get_nutrient_from_list_of_dicts(nutrients, 1008)
            type = max([protein, carbs, fats])
            if type == protein:
                type = "Protein"
            elif type == carbs:
                type = "Carb"
            elif type == fats:
                type = "Fat"

            key_pairs = {
                "fdc_id": id,
                "ingredient_name": name,
                "ingredient_type": type,
                "ingredient_category": category,
                "ingredient_calories": cals,
                "ingredient_calorie_units": cals_units,
                "ingredient_protein": protein,
                "ingredient_protein_units": protein_units,
                "ingredient_carbs": carbs,
                "ingredient_carb_units": carb_units,
                "ingredient_fats": fats,
                "ingredient_fat_units": fat_units,
                "ingredient_serving_size": serving_size,
                "ingredient_serving_size_units": units,
            }
            # ingredients[name] = key_pairs
            result.append(key_pairs)
            print("added " + food)
            # result.append([id, name, type, category, cals, cals_units, protein, protein_units, carbs, carb_units, fats, fat_units, serving_size, units])
        else:
            print("^^^didn't add " + food)
    return result
#----------------------------------------------------------------#

def main():
    # parser = set_cmd_args()
    # args = parser.parse_args()
    # food_list = args.food_list
    # structure
    # food_list = ["Chicken Sausage","Turkey Hot Dog","Salami","Smoked Salmon","Chicken Thigh","Steak"]
    food_list = ["Chicken Sausage","Turkey Hot Dog","Salami","Smoked Salmon","Chicken Thigh","Steak","Bacon Strips","Eggs","Ground Lamb (85%)","Ground Beef (85%)","Pork Loin Chop Boneless","Ground pork","Ground Turkey","flounder","chicken breast","Turkey Bacon","shrimp","turkey breast","cod","tilapia","scallop","yellow onions","asparagus","brussel sprouts","grean beans","cauliflower","Pecans","Walnuts","Parmesan","Feta Cheese","Goat Cheese","Grapeseed Oil","Coconut Oil","Salmon","Halibut","Lamb","Chicken Wings","Ground Beef (80%)","Duck","zucchini","shittake mushrooms","Brocoli","portabello mushrooms","tomatoe","red onion","carrot","pepper","cucumber","Spinach","Spring Mix","Romaine Lettucce","Iceberg","arugula","Cabbage","Cilantro","Chives","Basil","Mint","Blueberries","Strawberries","Raspberries","Blackberries","low-carb wrap","Barbeque Sauce","Pine Nuts","Almonds","Chia Seeds","Macadamia Nuts","Pumpkin Seeds","Blue-cheese","Brie","Swiss Cheese","Mozzarella Cheese","Cheddar Cheese","Avocado","Olives","Olive Oil","Pesto Sauce","Ranch Dressing","Asian Dressing","Alfredo Sauce","Tomatoe Sauce","Tzaziki Sauce","Hummus","Guacamole","creamcheese","Heavy Cream","Soy Milk","Oat Milk","Almond Coconut Milk","Whole Milk","2% Milk","Half and Half","Butter","sourcream","ricotta","farmer cheese","yogurt","Taco Seasoning","Curry Seasoning","Cacao Powder","Cinamomon Powder"]
    foods = get_foods(food_list)
    # list_rep = list(foods.items())
    # write json to file
    filename = "fdcId_data/" + str(foods[0].get("fdc_id")) + "-" + str(foods[len(foods)-1].get("fdc_id")) + ".json"

    with open(filename, "w") as file:
        json.dump(foods, file, indent=4)
        # writer = csv.writer(file)
        # header = ["FDC_ID",	"Ingredient Name", "Type", "Category", "Calories", "Calorie Units", "Protein", "Protein_units", "Carbs", "Carb_units", "Fats", "Fat_units", "Serving Size", "Units"]
        # writer.writerow(header)
        # writer.writerows(foods)

#----------------------------------------------------------------#
if __name__ == "__main__":
    main()
#----------------------------------------------------------------#



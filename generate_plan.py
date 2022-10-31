#----------------------------------------------------------------#
# generate_plan.py
# Author: Shameek Hargrave
# Purpose: object to store food name, serving size and
# macronutrient data.
#----------------------------------------------------------------#
import argparse
import json
import random
import psycopg2
from flask import Flask, request, jsonify
from datetime import datetime
from FoodItem import FoodItem as Ingredient
#----------------------------------------------------------------#

app = Flask(__name__, template_folder = ".")

#----------------------------------------------------------------#
def set_cmd_args():
    parser = argparse.ArgumentParser(description=
        'Generates a 7 day meal plan based on macronutrient constraints',
        allow_abbrev=False)
    parser.add_argument("p", metavar="protein", type=float,
        help="protein per meal in grams")
    parser.add_argument("c", metavar="carbs", type=float,
        help="carbs per meal in grams")
    parser.add_argument("f", metavar="fats", type=float,
        help="fats per meal in grams")
    return parser
#----------------------------------------------------------------#
def get_breakfast(MealType, constraints):
    return None
#----------------------------------------------------------------#
def get_lunch(MealType, constraints):
    return None
#----------------------------------------------------------------#
def get_dinner(MealType, constraints):
    return None
#----------------------------------------------------------------#
def is_mealValid(foods, constraints):
    protein = 0
    carbs = 0
    fats = 0
    for food in foods:
        protein += float(food.get_protein())
        carbs += float(food.get_carbs())
        fats += float(food.get_fats())

    return protein <= constraints["protein"] and carbs <= constraints["carbs"] and fats <= constraints["fats"]
#----------------------------------------------------------------#
def get_potenial_ingredients(constraints):
    conn = psycopg2.connect(dbname="postgres",
        user="postgres",
        password="mealize123",
        host="mealize.cuuze03lhsgn.us-east-1.rds.amazonaws.com",
        port="5432")

    cur = conn.cursor()
    cur.execute("SELECT * from \"Ingredients\"")
    row = cur.fetchone()
    potentials = []
    while row is not None:
        # name, serv_size, protein, carbs, fats, type, category, cals
        food = Ingredient(row[1], row[13], row[7], row[9], row[11], row[2], row[4], row[5])
        # print(food.to_string())
        if food.isValidFood(constraints.get("protein"), constraints.get("carbs"), constraints.get("fats")):
            potentials.append(food)
        row = cur.fetchone()
    return potentials
#----------------------------------------------------------------#
def get_western_meal(constraints):
    meat_cats = ["Sausages, Hotdogs & Brats","Frankfurters","Pepperoni, Salami & Cold Cuts","Fish & Seafood","Frozen Poultry, Chicken & Turkey", "Lamb, Veal, and Game Products","Beef Products","Meat/Poultry/Other Animals  Unprepared/Unprocessed","Other Meats","Poultry, Chicken & Turkey","Bacon, Sausages & Ribs","Frozen Fish & Seafood","Shellfish"]
    # meat = Ingredient()
    # starch = Ingredient()
    # vegetable = Ingredient()
    # with open("fdcId1893823-167806.csv", "r") as file:
    #     reader = csv.reader(file)
    #     next(reader, None)
    #     # find possible foods we could use
    #     potentials = []
    #     for row in reader:
    #         # name, serv_size, protein, carbs, fats, type, category
    #         food = Ingredient(row[1], row[12], row[6], row[8], row[10], row[2], row[3], row[4])
    #         # print(food.to_string())
    #         if food.isValidFood(constraints.get("protein"), constraints.get("carbs"), constraints.get("fats")):
    #             potentials.append(food)
    potentials = get_potenial_ingredients(constraints)
    # pick random items from potentials
    meat = potentials[random.randint(0,len(potentials)-1)]
    vegetable = potentials[random.randint(0,len(potentials)-1)]
    starch = potentials[random.randint(0,len(potentials)-1)]
    if is_mealValid([meat, vegetable, starch], constraints) is False:
        while (is_mealValid([meat, vegetable, starch], constraints) is False):
            randIndex = random.randint(0,len(potentials)-1)
            food = potentials[randIndex]
            if food.get_category() in meat_cats or "meat" in food.get_category():
                meat = food
                print("MEAT: \n" + meat.to_string())
            elif "vegetable" in food.get_category():
                vegetable = food
                print("VEG: \n" + vegetable.to_string())
            elif food.get_type() == "Carb":
                starch = food
                print("CARB: \n" + starch.to_string())
    meal = [meat.to_string(), vegetable.to_string(), starch.to_string()]
    return meal
#----------------------------------------------------------------#
@app.route("/", methods=['GET', 'POST'])
def get_7day_western():
    print(request.args)
    if not request.args.get("protein") or not request.args.get("carbs") or not request.args.get("fats"):
        return "not today homie"
    constraints = {
        "protein" : float(request.args.get("protein")),
        "carbs" : float(request.args.get("carbs")),
        "fats" :  float(request.args.get("fats")),
    }
    plan = []
    print("qoo\n\n")

    for i in range(0,7):
        print(plan)
        day = {
            "breakfast": get_western_meal(constraints),
            "lunch": get_western_meal(constraints),
            "dinner": get_western_meal(constraints),
        }
        plan.append(day)

    # save to file
    # filename = "meal_plans/" + "prot_" + str(int(constraints["protein"])) + "_" + "carbs_" + str(int(constraints["carbs"])) + "_" + "fats_" + str(int(constraints["fats"])) + "@" + datetime.now().strftime("%H:%M:%S") + ".json"
    # with open(filename, "w") as file:
    #     json.dump(plan, file, indent=4)
    response = jsonify(plan)
    response.headers.add('Access-Control-Allow-Origin', '*')
    print(response)
    return response
#----------------------------------------------------------------#
def main():
    parser = set_cmd_args()
    args = parser.parse_args()
    constraints = {
        "protein" : args.p,
        "carbs" : args.c,
        "fats" : args.f,
    }
    # plan = get_7day_western(constraints)
    # print(plan)
    # print(constraints)

#----------------------------------------------------------------#
if __name__ == "__main__":
    main()
#----------------------------------------------------------------#

#----------------------------------------------------------------#
# write_to_database.py
# Author: Nick Casa
# Purpose: object to store food name, serving size and
# macronutrient data.
#----------------------------------------------------------------#
import json
import sys
# from unicodedata import name
import psycopg2

#----------------------------------------------------------------#
def writeToDB(entry):
    conn = psycopg2.connect(dbname="postgres",
        user="postgres",
        password="mealize123",
        host="mealize.cuuze03lhsgn.us-east-1.rds.amazonaws.com",
        port="5432")

    cur = conn.cursor()


    cur.execute('''INSERT INTO "Ingredients" (fdc_id, ingredient_name, ingredient_type, nutrient_profile, ingredient_category, ingredient_calories, ingredient_calorie_units, ingredient_protein, ingredient_protein_units, ingredient_carbs, ingredient_carb_units, ingredient_fats, ingredient_fat_units, ingredient_serving_size, ingredient_serving_size_units) VALUES (%s,%s,%s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', (
        entry.get('fdc_id'),
        entry.get('ingredient_name'),
        entry.get('ingredient_type'),
        entry.get('nutrient_profile'),
        entry.get('ingredient_category'),
        entry.get("ingredient_calories"),
        entry.get("ingredient_calories_units"),
        entry.get("ingredient_protein"),
        entry.get("ingredient_protein_units"),
        entry.get("ingredient_carbs"),
        entry.get("ingredient_carb_units"),
        entry.get("ingredient_fats"),
        entry.get("ingredient_fat_units"),
        entry.get("ingredient_serving_size"),
        entry.get("ingredient_serving_size_units")
    ))

    # Commit changes
    conn.commit()
    # Close communication with DB
    cur.close()
    conn.close()

if __name__ == '__main__':
    file = sys.argv[1]
    with open(file, "r") as f:
        entries = json.load(f)
        for entry in entries:
            writeToDB(entry)
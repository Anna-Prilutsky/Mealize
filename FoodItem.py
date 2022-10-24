#----------------------------------------------------------------#
# FoodItem.py
# Author: Shameek Hargrave
# Purpose: object to store food name, serving size and
# macronutrient data.
#----------------------------------------------------------------#

#----------------------------------------------------------------#
class FoodItem:
    #----------------------------------------------------------------#
    def __init__(self, name, serv_size, avg_size, protein, carbs, fats, type, nutrient_prof, db_category_table, matching_label, cook_type, pairings):
        self.name = name
        self.serv_size = serv_size
        self.avg_size = avg_size
        self.protein = protein
        self.carbs = carbs
        self.fats = fats
        self.matching_config = {
            "Type": type,
            "Nutrient Profile": nutrient_prof,
            "Category": db_category_table,
            "Matching Label": matching_label,
            "Cooking Type": cook_type,
            "Pairing": pairings
        }
    #----------------------------------------------------------------#
    # MVP approximation of logical size: ratio of this serving vs the
    # avg serving
    def get_logical_serving_size(self):
        return int(self.serv_size/self.avg_size)
    #----------------------------------------------------------------#
    def get_macros(self):
        return [self.protein, self.carbs, self.fats]
    #----------------------------------------------------------------#
    def get_name(self):
        return self.name
    #----------------------------------------------------------------#
    def get_matching_config(self):
        return self.matching_config
    #----------------------------------------------------------------#


#----------------------------------------------------------------#
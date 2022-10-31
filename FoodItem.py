#----------------------------------------------------------------#
# FoodItem.py
# Author: Shameek Hargrave
# Purpose: object to store food name, serving size and
# macronutrient data.
#----------------------------------------------------------------#

#----------------------------------------------------------------#
class FoodItem:
    #----------------------------------------------------------------#
    def __init__(self, name, serv_size, protein, carbs, fats, types, category, cals):
        self.name = name
        self.serv_size = serv_size
        # self.avg_size = avg_size
        self.protein = protein
        self.carbs = carbs
        self.fats = fats
        self.type = types
        self.category = category
        self.cals = cals
        # self.matching_config = {
        #     "Type": type,
        #     "Nutrient Profile": nutrient_prof,
        #     "Category": db_category_table,
        #     "Matching Label": matching_label,
        #     "Cooking Type": cook_type,
        #     "Pairing": pairings
        # }
    #----------------------------------------------------------------#
    # MVP approximation of logical size: ratio of this serving vs the
    # avg serving
    # def get_logical_serving_size(self):
    #     return int(self.serv_size/self.avg_size)
    #----------------------------------------------------------------#
    def isValidFood(self, max_protein, max_carbs, max_fats):
        output = float(self.protein) <= max_protein and float(self.carbs) <= max_carbs and float(self.fats) <= max_fats
        return output
    #----------------------------------------------------------------#
    def get_protein(self):
        return self.protein
    #----------------------------------------------------------------#
    def get_carbs(self):
        return self.carbs
    #----------------------------------------------------------------#
    def get_fats(self):
        return self.fats
    #----------------------------------------------------------------#
    def get_name(self):
        return self.name
    #----------------------------------------------------------------#
    def get_type(self):
        return self.type
    #----------------------------------------------------------------#
    def get_category(self):
        return self.category
    # def get_matching_config(self):
    #     return self.matching_config
    #----------------------------------------------------------------#
    def to_string(self):
        serv_size = "~" if self.serv_size is None else str(self.serv_size)
        return self.name + " " + str(self.cals) + "cal " + serv_size + "g "
        # + self.protein + "g " + self.carbs + "g " + self.fats + "g " + self.category

#----------------------------------------------------------------#
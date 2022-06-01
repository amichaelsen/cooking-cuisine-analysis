import pandas as pd
import numpy as np 
import re 

def clean_ingredient1(ingredient):
    # remove processing instructions, e.g. "frozen chopped spinach, thawed and squeezed dry"
    ingredient = re.sub(r", .* and .*","", ingredient)
    # remove oz sizing, typically found on cans 
    ingredient = re.sub(r"\(.*oz\..*\)","", ingredient)
    # standardize garlic, removing "clove" or "cloves"
    ingredient = re.sub(r"garlic cloves?","garlic", ingredient)
    if "black pepper" in ingredient:
        return "pepper"
    # remove words appearing anywhere in the sequence, including beginning or end, but separated by spaces
    size_words = ["small", "medium", "large", "jumbo"]
    prep_words = ["chopped", "shredded", "sliced", "firmly packed", "diced", "finely","^ground", "^minced"]
    adjectives = ["fresh", "frozen", "firm", "extra firm", "^dried"]
    modifiers  = ["reduced fat", "reduced sodium", "fat free", "low-fat"]
    words = size_words + prep_words + adjectives + modifiers
    for word in words:
        reg = r"( "+word+" )|( "+word+")|("+word+" )"
        ingredient = re.sub(reg," ",ingredient)
    return ingredient.strip()

def ingredient_cleaning_v1():
    print("Loading data...",end="")
    train = pd.read_json("../data/train.json")
    test  = pd.read_json("../data/test.json")
    print("done!")
    print("Cleaning ingredients in training data...",end="",flush=True)
    train_processed_ingredients = train.explode("ingredients").set_index('id')[['ingredients']].applymap(clean_ingredient1).reset_index()
    train_processed_ingredients = train[['id','cuisine']].merge(train_processed_ingredients, on='id')
    train_processed_recipes = train_processed_ingredients.groupby("id").agg({'cuisine': 'first', "ingredients":lambda x: list(x)}).reset_index()
    print("done!")
    print("Cleaning ingredients in testing data...",end="",flush=True)
    test_processed_ingredients = test.explode("ingredients").set_index('id')[['ingredients']].applymap(clean_ingredient1).reset_index()
    test_processed_recipes = test_processed_ingredients.groupby("id").agg(list).reset_index()
    print("done!")
    print("Saving processed ingredients to csv...",end="",flush=True)
    train_processed_recipes.to_json("../data/train_cleaned_v1.json",orient="records")
    test_processed_recipes.to_json("../data/test_cleaned_v1.json",orient="records")
    print("done!")

if __name__ == "__main__":
    ingredient_cleaning_v1()
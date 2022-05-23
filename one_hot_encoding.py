import pandas as pd
import numpy as np 
from sklearn.preprocessing import OneHotEncoder
import time

def encode_recipes(recipe_df, enc=None):
    ingredients_df = recipe_df.explode("ingredients")
    if enc:
        col_name = enc.feature_names_in_[0]
        ingredient_arr = enc.transform(ingredients_df[[col_name]]).toarray()
        encoded_ingredients = pd.DataFrame(data=ingredient_arr, 
                                      columns=enc.categories_[0], 
                                      dtype=bool, 
                                      index=ingredients_df['id']).reset_index()
        encoded_recipes = encoded_ingredients.groupby('id').any().astype(int).reset_index()
    else: 
        enc = OneHotEncoder(handle_unknown='ignore')
        enc.fit(ingredients_df[['ingredients']])
        return encode_recipes(recipe_df, enc=enc)
    if 'cuisine' in recipe_df.columns:
        encoded_recipes = encoded_recipes.merge(recipe_df[['id','cuisine']], on='id')
    return encoded_recipes, enc
        

def ohe_encoding_v1():
    "Loads raw train/test data and one hot encodes ingredients for each recipe"
    start_time = time.time()
    print("Loading data...",end="")
    train = pd.read_json("data/train.json")
    test  = pd.read_json("data/test.json")
    print("done!")
    print("Encoding training data...",end="", flush=True)
    train_encoded, encoder = encode_recipes(train)
    print("done!")
    print("Encoding testing data...",end="", flush=True)
    test_encoded,   _      = encode_recipes(test, enc=encoder)
    print("done!")
    print("Saving dataframes to file...",end="", flush=True)
    train_encoded.to_csv("data/ohe_train_recipes_v1.csv", index=False)
    test_encoded.to_csv( "data/ohe_test_recipes_v1.csv",  index=False)    
    print("done!")
    print("--- %s seconds ---" % (time.time() - start_time))


def ohe_encoding_v2():
    "Loads V1 processed train/test data and one hot encodes ingredients for each recipe"
    start_time = time.time()
    print("Loading data...",end="")
    train = pd.read_json("data/train_cleaned_v1.json").sample(4000)
    test  = pd.read_json("data/test_cleaned_v1.json").sample(1000)
    print("done!")
    print("Encoding training data...",end="", flush=True)
    train_encoded, encoder = encode_recipes(train)
    print("done!")
    print("Encoding testing data...",end="", flush=True)
    test_encoded,   _      = encode_recipes(test, enc=encoder)
    print("done!")
    print("Saving dataframes to file...",end="", flush=True)
    train_encoded.to_csv("data/ohe_train_recipes_v2.csv", index=False)
    test_encoded.to_csv( "data/ohe_test_recipes_v2.csv",  index=False)    
    print("done!")
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    ohe_encoding_v2()


import pandas as pd 
import numpy as np
import time
from sklearn.feature_extraction.text import TfidfTransformer

def tfidf_transform(train, test):
    tfidf = TfidfTransformer()
    "Takes one hot encoded data. Dataframes have 'id' as index, and train has a 'cuisine' column"
    tfidf.fit(train.drop(columns=['cuisine']))
    train_tfidf = pd.DataFrame(data=tfidf.transform(train.drop(columns=['cuisine'])).toarray(),
                    index=train.index,
                    columns=train.drop(columns=['cuisine']).columns)
    test_tfidf = pd.DataFrame(data=tfidf.transform(test).toarray(),
                    index=test.index,
                    columns=test.columns)
    return train_tfidf, test_tfidf, tfidf

        

def tfidf_encoding_v2():
    "Loads V2 OHE train/test data and transforms using TFIDF"
    start_time = time.time()
    print("Loading data...",end="")
    train = pd.read_csv("data/ohe_train_recipes_v2.csv",index_col="id")
    test  = pd.read_csv("data/ohe_test_recipes_v2.csv",index_col="id")
    print("done!")
    print("TFIDF Encoding data...",end="", flush=True)
    train_tfidf, test_tfidf, tfidf_enc = tfidf_transform(train, test)
    print("done!")
    print("Saving dataframes to file...",end="", flush=True)
    train_tfidf.to_csv("data/tfidf_train_recipes_v2.csv")
    test_tfidf.to_csv( "data/tfidf_test_recipes_v2.csv")    
    print("done!")
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    tfidf_encoding_v2()
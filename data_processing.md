# Data Processing

## Data Cleaning

The python file `ingredient_preprocessing.py` contains methods for cleaning the raw data before any embeddings. 


To run the most recent data preprocessing script, run 
```
python ingredient_preprocessing.py 
```
The output files are saved to `data/` as json files, with names corresponding to the verion of cleaning performed. 

### Version 1
The method `ingredient_cleaning_v1` performs cleans each ingredient in the following ways (in the order listed):
* Remove preparation instructions matching the regex expression `",.* and .*"`, for example "frozen spinach, thawed and dried" becomes "frozen spinach"
* Remove oz labels for cans, captured with the regex expression `"\(.*oz\..*\)"`, for example "(10 oz.) diced tomatoes" becomes "diced tomatoes"
* Remove the following words that modify ingredients. In each case, these are captured using regex expressions find the appearance of these words separated by a space from the remaining ingredient description. Words with a leading `^` are only removed if they are the beginning of the ingredient description. 
    * size_words = `["small", "medium", "large", "jumbo"]`
    * prep_words = `["chopped", "shredded", "sliced", "firmly packed", "diced", "finely","^ground", "^minced"]`
    * adjectives = `["fresh", "frozen", "firm", "extra firm", "^dried"]`
    * modifiers  = `["reduced fat", "reduced sodium", "fat free", "low-fat"]`

This reduces the number of unique ingredients from about 6,700 to almost 3,000. 

## One Hot Encoding 

To generate the csv files for the most recent one hot encoding, within the main directory make sure you have `train.json` and `test.json` in the `data/` folder and run
```
python one_hot_encoding.py 
```
The output files are saved to `data/` as csv files, with names corresponding to the verion of cleaning performed. 

### OHE Version 1 

Perform one hot encoding on the raw ingredients lists. 

### OHE Version 2 

Perform one hot encoding on the cleaned ingredients lists, as output from [Version 1 of Data Preprocessing](#version-1).
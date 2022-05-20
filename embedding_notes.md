# Embedding Notes 

Input: recipes are labeled with a cuisine, and a list of ingredients as strings 

### Embedding Ideas 

#### Tokenization 

[Article](https://dataaspirant.com/word-embedding-techniques-nlp/#t-1597685144202) explaining bag of words, N-gram, TF-IDF, and Word2Vec. 

* **One-Hot-Encoding** - encode each ingredient as a feature, and a recipe with an ingredient will have a 1 for that feature and 0 for features it does not have 
* **Bag of Words** - break down ingredients further into words and count occurences of each word in a recipe list 
    * Useful if some words appear in multiple ingredients with similar meaning (ex: cheese or tufo) less useful for words that are generic/repeated with different meaning "sauce" from "soy sauce" or "pepper" from "black pepper" vs "bell pepper". 
    * This will be more sparse than one-hot-encoding
* **N-gram** - like bag of words but consider collection of N words
    * Even more sparse than bag of words, might be able to trim down features for combinations that appear exactly once or a very small number of times?

* **Word2Vec** - Use large corpus to learn semantic relationships between words and then encode words as vectors that capture meaning 

#### Dimensionality Reduction 
* **TF-IDF** (Term frequency-inverse document frequency) - For each token (ingredient, word, N-gram) compute a score for its relevance based on frequency within the document and frequency across all documents. 

* **Keras Embedding**  - embeds words into fixed lengths vector representations. 
    * [link](https://medium.com/analytics-vidhya/understanding-embedding-layer-in-keras-bbe3ff1327ce)

### Anya Thoughts

The simplest thing is start with a one-hot-encoding of the ingredients. Of all the methods, this one would most benefit from cleaning the data since similar/same ingredients may have slightly different representations 

The bag of words and N-gram encodings could handle some less cleaning, and could be good models to implement next. 

After each of these, we could try to add the TF-IDF and see if that preprocessing improves model performance. We certainly do have ingredients that are very common to all recipes and some rare ingredients that are cuisine specific that might get extra weight from this processing. 
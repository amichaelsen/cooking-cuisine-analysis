# Cuisine Exploration Project

This repo contains work for the [Erdos Institute's Bootcamp (May 2022)](https://www.erdosinstitute.org/code) for the Explorer Team (Alejandra Castillo, Anya Michaelsen, Benjamin Sheller, Karan Srivastava). We worked with the ["What's Cooking?" dataset](https://www.kaggle.com/datasets/kaggle/recipe-ingredients-dataset) from Kaggle.

The directory `data_proccessing/` contains python scripts for reproducing the data cleaning and encoding (read and saved from the `data/` directory). See the README within the directory for reproducibility instructions. The analysis is divided into classification models (`classifiers/`) and cuisine clustering analysis (`clustering/`), each containing several corresponding analysis notebooks. 

### Potential Stakeholders/Applications:
* Recipe Hosting Websites trying to automatically tag/predict cuisines of new recipes 
  * Could also use similar clustering techniques to generate recipe lists (wihtin or between cuisines) 
* For people looking to cook, could input a list of ingredients they have and get recommendations for what cuisine they might make and what other ingredients they could use with it
* Apps/Platforms with grocery lists could identify which cuisine you are most aligned with and recommend other ingredients relevant to that cuisine
  *  They could also target ads for restaurants of those cuisines 
* Restaurant apps (e.g. delivery platforms or Yelp) could identify which cuisines people like and then recommend adjacent cuisines using the cuisine clustering 


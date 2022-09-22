# Cuisine Exploration Project

This repo contains work for the [Erdos Institute's Bootcamp (May 2022)](https://www.erdosinstitute.org/code) for the Explorer Team (Alejandra Castillo, Anya Michaelsen, Benjamin Sheller, Karan Srivastava). We worked with the ["What's Cooking?" dataset](https://www.kaggle.com/datasets/kaggle/recipe-ingredients-dataset) from Kaggle.

The directory `data_proccessing/` contains python scripts for reproducing the data cleaning and encoding (read and saved from the `data/` directory). See the README within the directory for reproducibility instructions. The analysis is divided into classification models (`classifiers/`) and cuisine clustering analysis (`clustering/`), each containing several corresponding analysis notebooks. Classification model predictions are saved to `classifiers/model_predictions/` and clustering visualizations are saved to `figures/`. 

## Classification 

The best classification model was obtained using multi-class logistic regression (notebook [here](https://github.com/amichaelsen/cooking-cuisine-analysis/blob/main/classifiers/logistic_model.ipynb)), with a classification accuracy of 77.9%. A close second was the LinearSVC model (77.2%). k-Nearest Neighbors, LDA, and random forests all acheived slightly lower accuracies between 68% and 74%. 

## Clustering

Applying kMeans clustering to the cuisine data and reducing dimension via principal component analysis yields the following representation of cuisines: 

![K-Means Clustering](/figures/clustering_kmeans.jpg)

Applying agglomerative clustering and visualizing the result using a dendrogram gives the following hierarchical clustering of cuisines: 

![Agllomerative Clustering](/figures/clustering_dendrogram.jpg)


### Potential Stakeholders/Applications:
* Recipe Hosting Websites trying to automatically tag/predict cuisines of new recipes 
  * Could also use similar clustering techniques to generate recipe lists (wihtin or between cuisines) 
* For people looking to cook, could input a list of ingredients they have and get recommendations for what cuisine they might make and what other ingredients they could use with it
* Apps/Platforms with grocery lists could identify which cuisine you are most aligned with and recommend other ingredients relevant to that cuisine
  *  They could also target ads for restaurants of those cuisines 
* Restaurant apps (e.g. delivery platforms or Yelp) could identify which cuisines people like and then recommend adjacent cuisines using the cuisine clustering 

Project presentation and writeup can be found on the [Erdos Institute Project Database](https://www.erdosinstitute.org/project-database).


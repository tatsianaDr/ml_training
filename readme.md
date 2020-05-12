# Movie Reviews Analysis
This project is about movies review sentiment prediction. 

## Problem Undestanding
Here we will look at a Data Science challenge within the IMDB space. For our model fitting choose the f1-score metric.

## The Data
To build and train the models was used the <a href="https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews" target="_blank">IMDB dataset</a>.
The training set has 50K movie reviews for natural language processing. This is a dataset for binary sentiment classification. 

## The project structure
	.
	├── app_predict         # Application for build, train model and making predictions
	│   ├── notebooks       # Jupyter notebooks for solved ML part
	│   ├── service         # Web application for making prediction
	│   ├── src				# Python scripts, which are used to the application
	│   ├── dockerfile 			
	│   ├── readme.md	
	│   └── requirements.txt    
	├── data
	└── README.md

## Build and train models
The package **app_predict/notebooks** contains:
* `imdb_baseline_solution.ipynb`. The stage of selecting the baseline model. 						
* `imdb_preprocessing_and_vectorizer_selection.ipynb`. The stage of selecting the preprocessing and the vectorizer for the dataset.
* `imdb_model_selection.ipynb`. The stage of selection a ML algorithm for the application (including cross validation step).
* `imdb_best_model.ipynb`. Train and evaluate the best traditional model, selected in `imdb_model_selection.ipynb`
* `imdb_mlp_select_structure.ipynb`. The stage of exploring and selecting MLP model.
* `imdb_rnn_layer.ipynb`. The stage of exploring and selecting RNN model with the simple RNN layer.	
* `imdb_lstm_layer.ipynb`. The stage of exploring and selecting RNN model with the LSTM layer.
* `imdb_gru_layer.ipynb`. The stage of exploring and selecting RNN model with the GRU layer.
* `imdb-bidirectional_lstm.ipynb`. The stage of exploring and selecting Bidirectionsl model with the LSTM layer.
* `Compare_imdb-bidirectional_lstm_with_pretr_emb.ipynb`. Comparison of the models with the same structure but with different Embedding approaches (with pre-trained embeddings and without it). 
	
	
## Web service for make prediction
The web service was developed with Flask (Python).
It uses the sentiment prediction model.
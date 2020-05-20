### Movie Reviews Analysis web application 
This repository contains files necessary for building a Docker image of the application

#### Base Docker Image
`python:3.7.3-slim`

### For use the application you can:
1. Build your own docker image and run it
2. Pull and run the built docker image 

### 1. Build your own docker image and run it

###### Train and save models
Run the `./notebooks/imdb_best_model.ipynb` with `jupyter notebook`.
Run the `./notebooks/imdb_final_mlp_model.ipynb` with `jupyter notebook`.

###### Build Docker Image:
`docker build -t tatsianadr1/app_predict:2.0.0`


### 2. Pull the built docker image 

###### Pull the built docker image
`docker pull tatsianadr1/app_predict:2.0.0`



### Run the application  
`docker run -d  -p 5000:5000  tatsianadr1/app_predict:2.0.0`

### The application launches at port: 
`http://127.0.0.1:5000/predict`


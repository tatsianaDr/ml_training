##### For build docker image:

`docker build -t tatsianadr1/app_predict:1.0.0`

##### For run application with docker image:
`docker run -d  -p 5000:5000  tatsianadr1/app_predic`


##### The application launches at port: 
http://127.0.0.1:5000/predict

`env FLASK_APP=hello.py flask run`


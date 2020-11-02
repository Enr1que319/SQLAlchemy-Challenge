# SQLAlchemy-Challenge

[![](Resources/img/hawaii.jpg)]()        

## Introduction

This project is made to be able to give future references to people who plan to travel to Honolulu Hawaii or for people who want information about the weather in the place. It is composed of two parts that are:
- An analysis of the climate in the area
- A REST API from which you can make inquiries about the information

### Tools

The following tools were used to do the analysis and the REST API

#### Analysis:
- Python (Pandas, matplotlib, sqlalchemy)
- Jupyter Notebook
- SQL

#### REST API:
- Python (flask, datetime, pymongo, os)
- NoSQL
- MongoDB

The platform used to mount the REST API is Heroku

## Data

The information used is from the years 2016, 2017 and 2018 and is in a SQLite database and in .json format files, these can be found in the "Resources" folder, this was provided by Tecnológico de Monterrey.
With this the analysis was performed as well as the REST API
SQLite Database

#### Measurement Table

|  Column  | Data Type |
| -------- | ----------|
|    id    | `Integer` |
|  station |   `Text`  |
|   date   |   `Text`  |
|   prcp   |  `Float`  |
|   tobs   |  `Float`  |


- id -> Registry Identification Number
- station -> Station Code
- date -> Record Date
- prcp -> Precipitation Measurement
- tobs -> Temperature Measurement


#### Station Table

|    Column    | Data Type |
| ------------ | ----------|
|    id        | `Integer` |
|  station     |   `Text`  |
|   name       |   `Text`  |
|   latitude   |  `Float`  |
|   longitude  |  `Float`  |
|   elevation  |  `Float`  |


- id -> Station Identification Number
- station -> station code
- name -> station name
- latitude -> station latitude
- longitude -> station longitude
- elevation -> station elevation


-------------------------------
This project consist in making an API that contains data about climate Honolulu, Hawaii

Here you can see the API with more details:
- [Surfers Hawaii API](https://enr1qu319-api-hawaii-climate.herokuapp.com "API")


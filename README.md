# Weather_app
Weather application using Tkinter module

This GUI app will tell us the current weather of a particular city along with temperature details along with other details. 


**Modules required:**
  - Tkinter: It is a built-in python library for making GUI using tkinter toolkit
  - Requests: It is a library which helps in fetching the data with the help of URL

**Step 1:**
>Install requirements.txt
  - cd to the directory where requirements.txt is located
  - activate your virtualenv
  - run: pip3 install -r requirements.txt in your terminal

  
**Step 2:**
>Generate an API Key from the Open Weather Map website *https://openweathermap.org/*
  - we fetch data from the Open Weather Map website by generating an API key 
  - Sign up and Login in the Open Weather Map
  - Go to the API section. Then in the Current Weather Data section click on the Api doc
  - Now in the API Call section, we have the link of *api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}*
  - Click on the API key on the link it will direct to the page from where you can get the key
  - Once you get the API key paste the key into the pyhton scrip in variable api key 
                
                
                `api_key = "// ENTER YOUR API KEY HERE //"`
                
 
 **Step 3:**
 > Run Application
  - *python3 weather_app.py*
 
 

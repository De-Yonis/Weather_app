import tkinter as tk
from tkinter import font 
import requests
from PIL import Image, ImageTk

HEIGHT = 500
WIDTH = 500


def format_response(weather):
    try:
        name = (weather['name'])
        description = weather['weather'][0]['description']
        temp = int(weather["main"]["temp"] -273.15)
        humidity = weather["main"]["humidity"]

        final = 'City: %s \nConditions: %s \nTemperature (C): %s \nHumidity: %s' % (name, description, temp, humidity)
    except:
        final = 'There was a problem getting that information' 
    
    return final 

def get_weather(city): 
    #Follow instructions on README to get your api_key
    api_key = "// ENTER YOUR API KEY HERE //" 
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': api_key, 'q': city, "units": 'standard'}
    response = requests.get(url, params = params)
    weather = response.json()

    label['text'] = format_response(weather)
    
#root window to place everything into
root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width= WIDTH)
canvas.pack()

img = Image.open('zanzibar.jpg')
img = img.resize((250,250))
background_image = ImageTk.PhotoImage(img)
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)


#organize widgets on screen
frame = tk.Frame(root, bg = '#4B8BBE', bd=5)
frame.place(relx = 0.5, rely = 0.1, relheight= 0.1, relwidth= 0.75, anchor ='n')

 
entry = tk.Entry(frame, font = ('Comic Sans MS',25))
entry.place(relheight= 1, relwidth= 0.65)


button = tk.Button(frame, text = "Get Weather", font = ('Comic Sans MS',14), command = lambda: get_weather(entry.get()))
button.place(relx = 0.7, relheight= 1, relwidth= 0.25)
#easy to use when needing to stack a few things together in a grid formation
# button.grid(row=0, column=0)
# button.pack(side = 'left', fill = 'x', expand = 'True') 


lower_frame = tk.Frame(root, bg = '#4B8BBE', bd=10)
lower_frame.place(relx = 0.5, rely = 0.25, relheight= 0.6, relwidth= 0.75, anchor ='n')


label = tk.Label(lower_frame)
label.place(relheight= 1, relwidth= 1)


#Run the window
root.mainloop()
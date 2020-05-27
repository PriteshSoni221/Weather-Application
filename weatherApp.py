import tkinter as tk
import requests

# variables
var_width = 600
var_height = 600


def test_function(entry):
    print("Entered city is :",entry)


# API key : 2f1fa49a746c6674e86f07a6caddd95b
# API call : api.openweathermap.org/data/2.5/forecast?q={city name},{state code},{country code}&appid={your api key}
def get_weather(city):
    api_key = "2f1fa49a746c6674e86f07a6caddd95b"
    url = "https://api.openweathermap.org/data/2.5/weather"
    parameters = {"APPID": api_key, "q": city, "units": "metric"}
    response = requests.get(url, params=parameters)
    print(response.json())



# root is the lowest level of our window. canvas and frame stay on top of root.
root = tk.Tk()
root.title("Weather application")

# canvas will set the initial size of the window. Without this canvas, you will see a tiny screen.
canvas = tk.Canvas(root, height=var_height, width=var_width).pack()

background_image = tk.PhotoImage(file="weather-and-phenomena-backgrounds.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relheight=1, relwidth=1)

# """we are using place method with relative height and width method. So, if the size of window will change, size of our
#     frame will change, too. place method is a nice way to organise widgets on the frame because it is very responsive
#     frame will contain all the other widgets like buttons, labels, etc. We could have multiple frameworks. """
upper_frame = tk.Frame(root, bg="#82e1f5")
upper_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

# """pack method is to join the widget with other widget(frame, canvas, etc). We are saving one line of code by using
#     pack method right after we are initializing it. pack method has limited flexibility. On the other hand, grid
#     method has quite good flexibility and place is just the best which I have used for frame.
#     button = tk.Button(frame, text="text button", fg="#850411", bd=4).pack()
#     label = tk.Label(frame, text="this is a Label", bd=4).pack(side="right")
#     entry = tk.Entry(frame, cursor="xterm").pack(side="right") """

text_box = tk.Entry(upper_frame, cursor="xterm", bd=3)
text_box.place(relwidth=0.7, relheight=1)

weather_info_button = tk.Button(upper_frame, text="Weather Info", fg="#850411", font=40,
                                command=lambda: get_weather(text_box.get()))
weather_info_button.place(relx=0.75, relheight=1, relwidth=0.25)

lower_frame = tk.Frame(root, bg="#82e1f5")
lower_frame.place(relx=0.1, rely=0.3, relwidth = 0.8,relheight=0.6)
label = tk.Label(lower_frame, text="Weather details will appear here", bd=10, justify="center")
label.place(relx=0.02, rely=0.02, relheight = 0.96, relwidth=0.96)


root.mainloop()
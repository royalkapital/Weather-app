from tkinter import *
import requests
import time
from datetime import datetime
from tkinter import messagebox


class App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('1080x600+200+100')
        self.window.title('Weather App')

        self.window.resizable(width=False, height=False)
        self.window.configure(bg='#2b2e2c')

        self.window.iconphoto(False, PhotoImage(file='icon_photo.png'))

        self.font_1 = ('poppins', 15, 'bold')
        self.font_2 = ('poppins', 24, 'bold')
        self.font_3 = ('poppins', 35, 'bold')

        self.gui_components()

        self.window.mainloop()

    def gui_components(self):
        self.label = Label(self.window, font='poppins 35 bold', bg='#1b1c1b', fg='yellow', text='Weather app')
        self.label.place(relx=0, rely=0, relheight=0.12, relwidth=1)

        self.entry_city = Entry(self.window, justify=CENTER, font=self.font_1)
        self.entry_city.place(relx=0.25, rely=0.2, relheight=0.05, relwidth=0.5)
        self.entry_city.focus()
        self.entry_city.bind('<Return>', self.get_weather)

        self.label_1 = Label(self.window, font=self.font_2, bg='#2b2e2c', fg='white', borderwidth=1, relief="solid")
        self.label_1.place(relx=0.04, rely=0.6, relheight=0.24, relwidth=0.28)

        self.label_2 = Label(self.window, font=self.font_2, bg='#2b2e2c', fg='white', borderwidth=1, relief="solid")
        self.label_2.place(relx=0.36, rely=0.6, relheight=0.24, relwidth=0.28)

        self.label_3 = Label(self.window, font=self.font_2, bg='#2b2e2c', fg='white', borderwidth=1, relief="solid")
        self.label_3.place(relx=0.68, rely=0.6, relheight=0.24, relwidth=0.28)

        self.label_4 = Label(self.window, font=self.font_3, bg='#2b2e2c', fg='white')
        self.label_4.place(relx=0.45, rely=0.32)
        self.label_5 = Label(self.window, font=self.font_1, bg='#2b2e2c', fg='white')
        self.label_5.place(relx=0.46, rely=0.42)


    def get_weather(self, window):
        try:
            city = self.entry_city.get()
            api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=a4268b8e63c13c18c3dfad2472682603"
            json_data = requests.get(api).json()
            condition = json_data['weather'][0]['main']
            condition_description = json_data['weather'][0]['description']
            icon_address = json_data['weather'][0]['icon']
            temp = int(json_data['main']['temp'] - 273.15)
            min_temp = int(json_data['main']['temp_min'] - 273.15)
            max_temp = int(json_data['main']['temp_max'] - 273.15)
            pressure = json_data['main']['pressure']
            humidity = json_data['main']['humidity']
            wind = json_data['wind']['speed']
            sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
            sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
            today = datetime.date(datetime.now())

            label_hour_info = f'Today: {str(today)}\n' \
                              f'Sunrise: {str(sunrise)}\n' \
                              f'Sunset: {str(sunset)}'

            label_temp_info = f'Temperature: {str(temp)}°C\n' \
                              f'Max Temp: {str(max_temp)}°C\n' \
                              f'Min Temp: {str(min_temp)}°C'

            label_addition_info = f'Pressure: {str(pressure)}\n' \
                                  f'Wind speed: {str(wind)}\n' \
                                  f'Humidity: {str(humidity)}'



            self.label_1.config(text=label_hour_info)
            self.label_2.config(text=label_temp_info)
            self.label_3.config(text=label_addition_info)
            self.label_4.config(text=condition)
            self.label_5.config(text=condition_description)

        except KeyError as err:
            messagebox.showwarning('warning', 'The city name is not exist.')

if __name__ == '__main__':
    app = App()

from configparser import ConfigParser
from tkinter import *
from tkinter import messagebox
from io import BytesIO
from PIL import Image, ImageTk
import requests
import os
import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Tooltip:
  def __init__(self, widget, text):
    self.widget = widget
    self.text = text
    self.tooltip_window = None
    widget.bind('<Enter>', self.show_tooltip)
    widget.bind('<Leave>', self.hide_tooltip)

  def show_tooltip(self, event=None):
    if self.tooltip_window or not self.text:
      return
    try:
      x, y, cx, cy = self.widget.bbox('insert')
    except Exception:
      x = y = 0
    x += self.widget.winfo_rootx() + 20
    y += self.widget.winfo_rooty() + 20

    self.tooltip_window = Toplevel(self.widget)
    self.tooltip_window.wm_overrideredirect(True)
    self.tooltip_window.wm_geometry(f'+{x}+{y}')
    label = Label(self.tooltip_window, text=self.text, background='#ffffe0', relief='solid', borderwidth=1, font=('Helvetica', 9))
    label.pack(ipadx=1)

  def hide_tooltip(self, event=None):
    if self.tooltip_window:
      self.tooltip_window.destroy()
      self.tooltip_window = None


# Load API key from config.ini
config = ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
config.read(config_path)

try:
  api_key = config['weather']['api_key']
except KeyError:
  messagebox.showerror('Config Error', 'API key not  found in config.ini' )
  exit()

# Theme colors
light_theme = {
  'bg': '#F0F0F0',
  'fg': '#000000',
  'entry_bg': '#ffffff',
  'button_bg': '#dddddd'
}

dark_theme = {
  'bg': '#2e2e2e',
  'fg': '#ffffff',
  'entry_bg': '#3c3c3c',
  'button_bg': '#444444'
}

current_theme = light_theme

def apply_theme():
  def apply_recursive(widget):
    for child in widget.winfo_children():
      if isinstance(child, Label):
        child.configure(bg=current_theme['bg'], fg=current_theme['fg'])
      elif isinstance(child, Button):
        child.configure(bg=current_theme['button_bg'], fg=current_theme['fg'])
      elif isinstance(child, Entry):
        child.configure(
          bg=current_theme['entry_bg'],
          fg=current_theme['fg'],
          insertbackground=current_theme['fg'],
          highlightbackground=current_theme['fg'],
          highlightcolor=current_theme['fg'],
          highlightthickness=1
        )
      elif isinstance(child, Frame):
        child.configure(bg=current_theme['bg'])
      apply_recursive(child)

  app.configure(bg=current_theme['bg'])
  apply_recursive(app)

def toggle_theme():
  global current_theme
  current_theme = dark_theme if current_theme == light_theme else light_theme
  theme_btn.config(text='Light Theme' if current_theme == dark_theme else 'Dark Theme')
  apply_theme()

  # Redraw chart if a city has already been searched
  current_city = city_text.get().strip()
  if current_city:
    show_hourly_chart(current_city)

# Function to fetch weather data
def get_weather(city):
  url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'
  response = requests.get(url.format(city, api_key))
  if response.status_code == 200:
    data = response.json()
    city_name = data['name']
    country = data['sys']['country']
    temp_celsius = data['main']['temp']
    weather_desc = data['weather'][0]['description'].capitalize()
    icon_code = data['weather'][0]['icon']
    weather_main = data['weather'][0]['main']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    return city_name, country, temp_celsius, weather_desc, icon_code, weather_main, humidity, wind_speed
  else:
    return None

# Get 5-day forecast (at 12:00 PM)
def get_forecast(city):
  url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
  response = requests.get(url)
  forecast_list = []
  if response.status_code == 200:
    data = response.json()
    for entry in data['list']:
      if '12:00:00' in entry['dt_txt']:
        date = entry['dt_txt'].split()[0]
        temp = entry['main']['temp']
        desc = entry['weather'][0]['description'].capitalize()
        forecast_list.append(f'{date}: {temp}°C, {desc}')
  return forecast_list

# Show hourly chart (next 24h in 3h steps)
def show_hourly_chart(city):
  url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    times = []
    temps = []

    for entry in data['list'][:8]: # 8 x 3h = 24h
      dt = datetime.datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S')
      times.append(dt.strftime('%H:%M'))
      temps.append(entry['main']['temp'])

    # Plotting
    fig, ax = plt.subplots(figsize=(6, 4), dpi=100)

    # Add theme colors to Matplotlib figure
    fig.patch.set_facecolor(current_theme['bg'])
    ax.set_facecolor(current_theme['bg'])

    # Plot data
    ax.plot(times, temps, marker='o', color='red')
    ax.set_title('Next 24h Forecast', color=current_theme['fg'])
    ax.set_xlabel('Time', color=current_theme['fg'])
    ax.set_ylabel('Temp (°C)', color=current_theme['fg'])

    ax.grid(True, color='gray', linestyle='--', alpha=0.5)
    ax.tick_params(axis='x', colors=current_theme['fg'])
    ax.tick_params(axis='y', colors=current_theme['fg'])

    # Auto-adjust layout with padding
    fig.tight_layout(pad=3.0)

    # Clear old chart
    for widget in chart_frame.winfo_children():
      widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(padx=0, pady=0, expand=True, fill='both')

# Triggered when searching
def search():
  city = city_text.get().strip()
  if not city:
    messagebox.showwarning('Input Error', 'Please enter a city name')
    return
  weather = get_weather(city)
  if weather:
    city_name, country, temp, desc, icon_code, weather_main, humidity, wind_speed = weather
    location_lbl.config(text=f'{city_name}, {country}')
    temperature_lbl.config(text=f'{temp}°C')
    weather_lbl.config(text=f'{desc}')
    extra_lbl.config(text=f'Humidity: {humidity}%\n Wind: {wind_speed} m/s')

    # Show weather icon
    icon_url = f'https://openweathermap.org/img/wn/{icon_code}@2x.png'
    try:
      icon_response = requests.get(icon_url)
      icon_img = Image.open(BytesIO(icon_response.content))
      icon_img = ImageTk.PhotoImage(icon_img)
      icon_lbl.config(image=icon_img)
      icon_lbl.image = icon_img # Prevent garbage collection
    except Exception as e:
      print("Icon failed:", e)

    # 5-day chart
    forecast = get_forecast(city)
    if forecast:
      forecast_lbl.config(text='\n'.join(forecast))
    else:
      forecast_lbl.config(text='No forecast data available')

    # Forecast chart
    show_hourly_chart(city)
  else:
    messagebox.showerror('Error', f'Could not find weather for "{city}"')
    location_lbl.config(text='Location')
    temperature_lbl.config(text='')
    weather_lbl.config(text='')
    forecast_lbl.config(text='')
    icon_lbl.config(text='')

# GUI setup
app = Tk()
app.configure(bg='#F0F0F0')
app.title('Weather App')
app.geometry('500x700')
app.resizable(True, True)

# Bind the enter key
app.bind('<Return>', lambda event: search())

# Search row (Entry + Button side by side)
city_text = StringVar()

search_frame = Frame(app, bg=current_theme['bg'])
search_frame.pack(pady=10)

entry = Entry(search_frame, textvariable=city_text, font=('Helvetica', 12), width=30)
entry.grid(row=0, column=0, padx=(0, 10))
entry.focus()

search_btn = Button(
  search_frame,
  text='Search',
  command=search,
  font=('Helvetica', 10),
  bg=current_theme['button_bg'],
  fg=current_theme['fg'],
  relief='raised'
)

search_btn.grid(row=0, column=1)
Tooltip(search_btn, 'Click to search weather')

# Theme button
theme_btn = Button(app, text='Dark Theme', command=toggle_theme, font=('Helvetica', 10), width=20)
theme_btn.pack(pady=5)

# Labels
location_lbl = Label(app, text='Location', font=('Helvetica', 14, 'bold'))
location_lbl.pack()

# Weather frame with icon and info
weather_frame = Frame(app, bg=current_theme['bg'])
weather_frame.pack(pady=(10, 0))

icon_lbl = Label(weather_frame, bg=current_theme['bg'])
icon_lbl.grid(row=0, column=0, rowspan=1, padx=10)

# Sub-frame for temp + description
info_frame = Frame(weather_frame, bg=current_theme['bg'])
info_frame.grid(row=0, column=1, sticky='w')

temperature_lbl = Label(info_frame, text='', font=('Helvetica', 12), bg=current_theme['bg'], fg=current_theme['fg'])
temperature_lbl.pack(anchor='w')

weather_lbl = Label(info_frame, text='', font=('Helvetica', 12), bg=current_theme['bg'], fg=current_theme['fg'])
weather_lbl.pack(anchor='w')

extra_lbl = Label(app, text='', font=('Helvetica', 10))
extra_lbl.pack()

Label(app, text='5-Day Forecast: ', font=('Helvetica', 12, 'bold')).pack(pady=(20, 5))
forecast_lbl = Label(app, text='', justify=LEFT, font=('Helvetica', 10), wraplength=460)
forecast_lbl.pack(pady=(0, 0))

# Chart frame
chart_frame = Frame(app, width=460)
chart_frame.pack(pady=(10, 0), fill='both', expand=True)

# Tooltip
Tooltip(forecast_lbl, 'Midday forecast over next 5 days')
Tooltip(temperature_lbl, 'Current temperature in Celsius')
Tooltip(weather_lbl, 'Weather description\nHover over icon for details')
Tooltip(icon_lbl, 'Weather icon provided by OpenWeatherMap')
Tooltip(extra_lbl, 'Humidity in %, Wind speed in meter per second')

apply_theme()

if __name__ == '__main__':
  app.mainloop()
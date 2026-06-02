# ui.py
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from util import Tooltip, light_theme, dark_theme
from api import get_weather, get_forecast, get_hourly_chart_data
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from io import BytesIO
import requests

def create_ui(app, api_key):
  current_theme = {'value': light_theme}
  city_text = StringVar()

  def apply_theme():
    def apply_recursive(widget):
      for child in widget.winfo_children():
        if isinstance(child, Label):
          child.configure(bg=current_theme['value']['bg'], fg=current_theme['value']['fg'])
        elif isinstance(child, Button):
          child.configure(bg=current_theme['value']['button_bg'], fg=current_theme['value']['fg'])
        elif isinstance(child, Entry):
          child.configure(
            bg=current_theme['value']['entry_bg'],
            fg=current_theme['value']['fg'],
            insertbackground=current_theme['value']['fg'],
            highlightbackground=current_theme['value']['fg'],
            highlightcolor=current_theme['value']['fg'],
            highlightthickness=1
          )
        elif isinstance(child, Frame):
          child.configure(bg=current_theme['value']['bg'])
        apply_recursive(child)
    app.configure(bg=current_theme['value']['bg'])
    apply_recursive(app)

  def toggle_theme():
    current_theme['value'] = dark_theme if current_theme['value'] == light_theme else light_theme
    theme_btn.config(text='Light Theme' if current_theme['value'] == dark_theme else 'Dark Theme')
    apply_theme()
    if city_text.get().strip():
      show_hourly_chart(city_text.get().strip())

  def show_hourly_chart(city):
    times, temps = get_hourly_chart_data(city, api_key)
    fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
    fig.patch.set_facecolor(current_theme['value']['bg'])
    ax.set_facecolor(current_theme['value']['bg'])
    ax.plot(times, temps, marker='o', color='red')
    ax.set_title('Next 24h Forecast', color=current_theme['value']['fg'])
    ax.set_xlabel('Time', color=current_theme['value']['fg'])
    ax.set_ylabel('Temp (°C)', color=current_theme['value']['fg'])
    ax.grid(True, color='gray', linestyle='--', alpha=0.5)
    ax.tick_params(axis='x', colors=current_theme['value']['fg'])
    ax.tick_params(axis='y', colors=current_theme['value']['fg'])
    fig.tight_layout(pad=3.0)

    for widget in chart_frame.winfo_children():
      widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True, fill='both')

  def search():
    city = city_text.get().strip()
    if not city:
      messagebox.showwarning('Input Error', 'Please enter a city name')
      return
    weather = get_weather(city, api_key)
    if weather:
      city_name, country, temp, desc, icon_code, _, humidity, wind_speed = weather
      location_lbl.config(text=f'{city_name}, {country}')
      temperature_lbl.config(text=f'{temp}°C')
      weather_lbl.config(text=f'{desc}')
      extra_lbl.config(text=f'Humidity: {humidity}%\nWind: {wind_speed} m/s')

      icon_url = f'https://openweathermap.org/img/wn/{icon_code}@2x.png'
      try:
        icon_response = requests.get(icon_url)
        icon_img = Image.open(BytesIO(icon_response.content))
        icon_img = ImageTk.PhotoImage(icon_img)
        icon_lbl.config(image=icon_img)
        icon_lbl.image = icon_img
      except Exception as e:
        print("Icon load failed:", e)

      forecast = get_forecast(city, api_key)
      if forecast:
        forecast_lbl.config(text='\n'.join(forecast))
      else:
        forecast_lbl.config(text='No forecast data available')

      show_hourly_chart(city)
    else:
      messagebox.showerror('Error', f'Could not find weather for \"{city}\"')

  # --- GUI Layout ---
  app.bind('<Return>', lambda event: search())

  search_frame = Frame(app, bg=current_theme['value']['bg'])
  search_frame.pack(pady=10)

  entry = Entry(search_frame, textvariable=city_text, font=('Helvetica', 12), width=30)
  entry.grid(row=0, column=0, padx=(0, 10))
  entry.focus()

  search_btn = Button(search_frame, text='Search', command=search, font=('Helvetica', 10))
  search_btn.grid(row=0, column=1)
  Tooltip(search_btn, 'Click to search weather')

  theme_btn = Button(app, text='Dark Theme', command=toggle_theme, font=('Helvetica', 10), width=20)
  theme_btn.pack(pady=5)

  location_lbl = Label(app, text='Location', font=('Helvetica', 14, 'bold'))
  location_lbl.pack()

  weather_frame = Frame(app, bg=current_theme['value']['bg'])
  weather_frame.pack(pady=(10, 0))

  icon_lbl = Label(weather_frame, bg=current_theme['value']['bg'])
  icon_lbl.grid(row=0, column=0, padx=10)

  info_frame = Frame(weather_frame, bg=current_theme['value']['bg'])
  info_frame.grid(row=0, column=1, sticky='w')

  temperature_lbl = Label(info_frame, text='', font=('Helvetica', 12))
  temperature_lbl.pack(anchor='w')

  weather_lbl = Label(info_frame, text='', font=('Helvetica', 12))
  weather_lbl.pack(anchor='w')

  extra_lbl = Label(app, text='', font=('Helvetica', 10))
  extra_lbl.pack()

  Label(app, text='5-Day Forecast:', font=('Helvetica', 12, 'bold')).pack(pady=(20, 5))
  forecast_lbl = Label(app, text='', justify=LEFT, font=('Helvetica', 10), wraplength=460)
  forecast_lbl.pack()

  global chart_frame
  chart_frame = Frame(app, width=460)
  chart_frame.pack(pady=(10, 0), fill='both', expand=True)

  Tooltip(forecast_lbl, 'Midday forecast over next 5 days')
  Tooltip(temperature_lbl, 'Current temperature in Celsius')
  Tooltip(weather_lbl, 'Weather description')
  Tooltip(icon_lbl, 'Weather icon provided by OpenWeatherMap')
  Tooltip(extra_lbl, 'Humidity and wind info')

  apply_theme()
# main.py
import os
from tkinter import Tk
from configparser import ConfigParser
from tkinter import messagebox
from ui import create_ui

def load_api_key():
  config = ConfigParser()
  config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
  config.read(config_path)

  try:
    return config['weather']['api_key']
  except KeyError:
    messagebox.showerror('Config Error', 'API key not found in config.ini')
    exit()

if __name__ == '__main__':
  api_key = load_api_key()

  app = Tk()
  app.title('Weather App')
  app.geometry('500x700')
  app.resizable(True, True)

  create_ui(app, api_key)
  app.mainloop()

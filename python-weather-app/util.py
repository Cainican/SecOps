# util.py
from tkinter import Label, Toplevel

# Tooltip class
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
      x, y, _, _ = self.widget.bbox('insert')
    except Exception:
      x = y = 0
    x += self.widget.winfo_rootx() + 20
    y += self.widget.winfo_rooty() + 20

    self.tooltip_window = Toplevel(self.widget)
    self.tooltip_window.wm_overrideredirect(True)
    self.tooltip_window.wm_geometry(f'+{x}+{y}')
    label = Label(
      self.tooltip_window,
      text=self.text,
      background='#ffffe0',
      relief='solid',
      borderwidth=1,
      font=('Helvetica', 9)
    )
    label.pack(ipadx=1)

  def hide_tooltip(self, event=None):
    if self.tooltip_window:
      self.tooltip_window.destroy()
      self.tooltip_window = None

# Theme definitions
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

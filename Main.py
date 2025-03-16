import tkinter as tkint
from tkhtmlview import HTMLLabel
import configparser as c
import os
config = c.ConfigParser()
class GUI():
    def Show():
        config.read(os.getcwd() + "\\ConfigHTML.ini")
        root = tkint.Tk()
        html_label = HTMLLabel(root, html=config['HTML_CONFIG']['Output'])
        html_label.pack(fill="both", expand=True)
        html_label.fit_height()
        root.mainloop()

if __name__ == "__main__":
    GUI.Show()
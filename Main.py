import tkinter as tkint
from tkhtmlview import HTMLText, RenderHTML
import os
class GUI():
    def Show():
        root = tkint.Tk()
        root.geometry("660x660")
        html_label = HTMLText(root, html=RenderHTML(file="{}".format("HelloWorld.html")))
        html_label.pack(fill="both", expand=True)
        html_label.fit_height()
        root.mainloop()

if __name__ == "__main__":
    GUI.Show()

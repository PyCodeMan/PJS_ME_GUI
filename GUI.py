import tkinter as tk
from parser import scrape
from texts_templates import *
import webbrowser as browser
import threading as thread


def refresh_manually():
    refresh()


def refresh():
    
    text_of_order = None
    link_to_order = None

    if text_of_order:
        text_of_order.destroy()
    if link_to_order:
        link_to_order.destroy()
        
    def open_link():
        browser.open(link)

    text, link = scrape(url, tag, class_name, base_url)
    text_of_order = tk.Label(
        **text_config,
        **colors_config,
        text=text,
        wraplength=1200
    )
    text_of_order.place(x=5, y=120)

    link_to_order = tk.Button(
        **text_config,
        text=link_button_text,
        command=lambda: thread.Thread(target=open_link).start()
    )
    link_to_order.place(x=5, y=260)


def main():
    
    main_window = tk.Tk()

    main_window.configure(
        background='#C0C0C0',
        padx=10,
        pady=10,
        cursor='arrow',
        relief='groove',
        width=1280,
        height=720)

    main_window.resizable(False, False)

    hello_label = tk.Label(
        **text_config,
        **colors_config,
        text=hello_text,
    ).place(x=5, y=5)
    
    refresh_manually_button = tk.Button(
        **text_config,
        text=refresh_manually_text,
        command=refresh_manually
    ).place(x=5, y=40)

    main_window.title('Поисковая система')

    main_window.mainloop()


if __name__ == '__main__':
    main()

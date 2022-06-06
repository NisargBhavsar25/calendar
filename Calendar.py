import calendar
import tkinter as tk
import os


def getCalendar():
    gui = tk.Tk()
    gui.config(background='grey')
    year = int(year_field.get())
    gui.title(f"Calendar for {year}")
    gui.geometry("600x560")
    gui.minsize(600, 560)
    gui_text = calendar.calendar(year)

    calYear = tk.Text(gui, width=600, height=600, font="Consolas 10 bold")
    calYear.insert(tk.INSERT, gui_text)
    calYear.config(state="disabled")
    calYear.grid(row=1, column=1, padx=20, pady=5)

    print(gui_text)

    gui.grid_rowconfigure(1,  weight=1)

    gui.grid_columnconfigure(1,  weight=1)

    gui.mainloop()


if __name__ == '__main__':

    root = tk.Tk()
    root.config(background='grey')
    root.title("Calendar")
    root.geometry("242x200")
    icon = tk.PhotoImage(file = os.path.join(os.path.dirname(__file__), 'calendar-512.png'))
  
    root.iconphoto(True, icon)

    cal = tk.Label(root, text="   Calendar   ",
                   bg='grey', font=("times", 32, "bold"))
    year = tk.Label(root, text="Enter year below", bg='dark grey')
    year_field = tk.Entry(root)
    button = tk.Button(root, text='Show Calendar',
                       fg='Black', bg='Green', command=getCalendar)
    Exit = tk.Button(root, text='Exit', fg='Black',
                     bg='Red', command=root.destroy)

    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)
    Exit.grid(row=6, column=1)

    for i in range(6):
        root.grid_rowconfigure(i,  weight=1)

    root.grid_columnconfigure(1,  weight=1)

    root.mainloop()

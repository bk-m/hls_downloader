import tkinter as tk


def main():
    window = tk.Tk()
    greeting = tk.Label(text="Hello World")
    greeting.pack()
    window.mainloop()

if __name__ == "__main__":
    main()

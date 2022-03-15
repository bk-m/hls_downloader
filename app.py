import tkinter as tk

def generate_new_entry(window):
    frame = tk.Frame(master=window, borderwidth=1)
    lbl_url = tk.Label(text="URL", master=frame)
    ent_url = tk.Entry(master=frame)
    lbl_url.grid(row=0, column=0)
    ent_url.grid(row=1, column=0)
    lbl_title = tk.Label(text="Title", master=frame)
    ent_title = tk.Entry(master=frame)
    lbl_title.grid(row=0, column=1)
    ent_title.grid(row=1, column=1)
    btn_remove = tk.Button(master=frame, text="x", command=lambda: remove_frame(frame))
    btn_remove.grid(row=0, rowspan=2, column=2)
    frame.pack()

def remove_frame(frame: tk.Frame):
    frame.pack_forget()
    frame.destroy()

def main():
    window = tk.Tk()
    header_frame = tk.Frame(master=window, borderwidth=1)
    lbl_ffmpeg_path = tk.Label(master=header_frame, text="Path to FFMPEG")
    lbl_ffmpeg_path.grid(row=0, column=0)
    ent_ffmpeg_path = tk.Entry(master=header_frame)
    ent_ffmpeg_path.grid(row=1, column=0)
    btn_add_entry = tk.Button(master=header_frame, text="+", command=lambda: generate_new_entry(window))
    btn_add_entry.grid(row=0, rowspan=2, column=2)
    btn_dl = tk.Button(master=header_frame, text="v")
    btn_dl.grid(row=0, rowspan=2, column=3)
    header_frame.pack()

    generate_new_entry(window)

    window.mainloop()

if __name__ == "__main__":
    main()

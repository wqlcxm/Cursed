import tkinter as tk
import base64

def encode_base64():
    input_text = input_entry.get()
    encoded_text = base64.b64encode(input_text.encode('utf-8')).decode('utf-8')
    output_entry.delete(0, tk.END)
    output_entry.insert(tk.END, encoded_text)

def change_background_color():
    r, g, b = window.winfo_rgb(window.cget('bg'))
    r += 2
    g += 2
    b += 2
    if r > 85:
        r = 0
    if g > 85:
        g = 0
    if b > 85:
        b = 0
    hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    window.configure(bg=hex_color)
    window.after(10, change_background_color)

window = tk.Tk()
window.title("Cursed | Give Start Token With ID Discord Coded by @FileZ_Plus")
window.geometry("500x200")

input_frame = tk.Frame(window)
input_frame.pack(pady=10)

input_label = tk.Label(input_frame, text="Введите ID Discord:")
input_label.pack(side=tk.LEFT)

input_entry = tk.Entry(input_frame)
input_entry.pack(side=tk.LEFT)

encode_button = tk.Button(window, text="Скан. Айди", command=encode_base64)
encode_button.pack(pady=10)

output_frame = tk.Frame(window)
output_frame.pack(pady=10)

output_label = tk.Label(output_frame, text="Начало Токена:")
output_label.pack(side=tk.LEFT)

output_entry = tk.Entry(output_frame)
output_entry.pack(side=tk.LEFT)

change_background_color()

window.mainloop()
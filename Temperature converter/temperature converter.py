import tkinter as tk
from tkinter import font

# Function to perform conversion
def convert():
    try:
        temp = float(entry.get())
        if scale.get() == "Celsius":
            fahrenheit = (temp * 9/5) + 32
            kelvin = temp + 273.15
            output_label.config(text=f"{temp}°C = {fahrenheit:.2f}°F = {kelvin:.2f}K")
        elif scale.get() == "Fahrenheit":
            celsius = (temp - 32) * 5/9
            kelvin = celsius + 273.15
            output_label.config(text=f"{temp}°F = {celsius:.2f}°C = {kelvin:.2f}K")
        elif scale.get() == "Kelvin":
            celsius = temp - 273.15
            fahrenheit = (celsius * 9/5) + 32
            output_label.config(text=f"{temp}K = {celsius:.2f}°C = {fahrenheit:.2f}°F")
    except ValueError:
        output_label.config(text="Invalid input!", fg="red")
        root.after(2000, reset_label)

def reset_label():
    output_label.config(text="Result: ", fg="black", bg='#E0E0E0')

# Main window
root = tk.Tk()
root.title("Converter")
root.geometry("450x300")
root.config(bg="#D5F5E3")  # Light pastel green background

# Custom font for output
output_font = font.Font(family="Times New Roman", size=16, weight="bold")

# Scale selection
scale = tk.StringVar(value="Celsius")
scale_menu = tk.OptionMenu(root, scale, "Celsius", "Fahrenheit", "Kelvin")
scale_menu.grid(row=0, column=1, padx=10, pady=10)

# Input label
entry_label = tk.Label(root, text="Enter Value:", bg="#D5F5E3", fg="#333333", font=('Times New Roman', 14))
entry_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Input entry
entry = tk.Entry(root, font=('Times New Roman', 14), bg="#FFFFFF", borderwidth=2, relief="solid", width=10)
entry.grid(row=0, column=2, padx=10, pady=10, sticky="w")

# Output label
output_label = tk.Label(root, text="Result: ", font=output_font, bg='#ADD8E6', fg='#333333', width=40, height=2, relief="solid", bd=1)
output_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert, font=('Times New Roman', 14), bg="#1ABC9C", fg="#ECF0F1", activebackground="#16A085", relief="flat", padx=10, pady=5)
convert_button.grid(row=2, column=0, columnspan=3, pady=20)

# Add grid configuration for columns
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()

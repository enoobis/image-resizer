import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Define the function to resize the image
def resize_image():
    # Get the file path and new size from the UI
    input_path = input_entry.get()
    output_path = output_entry.get()
    new_size = (int(width_entry.get()), int(height_entry.get()))

    # Open the image and resize it
    with Image.open(input_path) as image:
        resized_image = image.resize(new_size)
        resized_image.save(output_path)

    # Show the resized image in the UI
    resized_image = ImageTk.PhotoImage(resized_image)
    image_label.configure(image=resized_image)
    image_label.image = resized_image

# Define the function to select the input file
def select_input_file():
    input_path = filedialog.askopenfilename()
    input_entry.delete(0, tk.END)
    input_entry.insert(0, input_path)

# Define the function to select the output file
def select_output_file():
    output_path = filedialog.asksaveasfilename()
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_path)

# Create the main window
root = tk.Tk()
root.title("Image Resizer")
root.config(bg="#24292e")
root.geometry("820x400")

# Create the input file path label and entry
input_label = tk.Label(root, text="Input file path:", fg="#c9d1d9", bg="#24292e")
input_label.grid(row=0, column=0, padx=10, pady=10)
input_entry = tk.Entry(root, bg="#1f2428", fg="#c9d1d9", width=50)
input_entry.grid(row=0, column=1, padx=10, pady=10)
input_button = tk.Button(root, text="Browse", bg="#1f6feb", fg="#c9d1d9", command=select_input_file)
input_button.grid(row=0, column=2, padx=10, pady=10)

# Create the output file path label and entry
output_label = tk.Label(root, text="Output file path:", fg="#c9d1d9", bg="#24292e")
output_label.grid(row=1, column=0, padx=10, pady=10)
output_entry = tk.Entry(root, bg="#1f2428", fg="#c9d1d9", width=50)
output_entry.grid(row=1, column=1, padx=10, pady=10)
output_button = tk.Button(root, text="Browse", bg="#1f6feb", fg="#c9d1d9", command=select_output_file)
output_button.grid(row=1, column=2, padx=10, pady=10)

# Create the width and height labels and entries
width_label = tk.Label(root, text="Width:", fg="#c9d1d9", bg="#24292e")
width_label.grid(row=2, column=0, padx=10, pady=10)
width_entry = tk.Entry(root, bg="#1f2428", fg="#c9d1d9", width=10)
width_entry.grid(row=2, column=1, padx=10, pady=10)
height_label = tk.Label(root, text="Height:", fg="#c9d1d9", bg="#24292e")
height_label.grid(row=2, column=2, padx=10, pady=10)
height_entry = tk.Entry(root, bg="#1f2428", fg="#c9d1d9", width=10)
height_entry.grid(row=2, column=3, padx=10, pady=10)

# Create the resize button
resize_button = tk.Button(root, text="Resize Image", bg="#1f6feb", fg="#c9d1d9", command=resize_image)
resize_button.grid(row=3, column=1, padx=10, pady=10)

# Create the image label
image_label = tk.Label(root, bg="#1f2428", padx=10, pady=10)
image_label.grid(row=4, column=0, columnspan=4)

# Run the main loop
root.mainloop()
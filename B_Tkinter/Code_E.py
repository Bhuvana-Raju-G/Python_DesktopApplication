import tkinter as tk

# Creating the main window
root = tk.Tk()

#Cretaing Title for the window
root.title("Text to Speech Web Application")

#Customised Size
root.geometry("900x450")

#Restricting to resize the window
root.resizable(False,False)

# Set the path to your image file (preferably in .png or .jpg format)
image_path = 'B_Tkinter\icon4.png'

# Load the image file and set it as the window icon
icon_image = tk.PhotoImage(file=image_path)
root.iconphoto(True, icon_image)

def print_text():
    # Get text from the text area
    text = text_area.get("1.0", "end-1c")
    print("Text to print:", text)


# Create a text area (Text widget)
text_area = tk.Text(root, height=15, width=80)
text_area.pack(padx=10, pady=10)

# Create a button to print the text
print_button = tk.Button(root, text="Print", command=print_text)
print_button.pack()

# Running the main loop to display the window
root.mainloop()

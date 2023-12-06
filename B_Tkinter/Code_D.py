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


# Running the main loop to display the window
root.mainloop()

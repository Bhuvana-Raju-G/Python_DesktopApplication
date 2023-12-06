import tkinter as tk
from text_to_speech import *


# Creating the main window
root = tk.Tk()

#Cretaing Title for the window
root.title("Text to Speech Web Application")

#Customised Size
root.geometry("680x400")

#Restricting to resize the window
root.resizable(False,False)

# Set the path to your image file (preferably in .png or .jpg format)
image_path = 'B_Tkinter\icon4.png'

# Load the image file and set it as the window icon
icon_image = tk.PhotoImage(file=image_path)
root.iconphoto(True, icon_image)



def speak_from_textarea():
    # Get text from the text area
    text = text_area.get("1.0", "end-1c")
    speak_text(text, rate=170)
    
    
def saving_to_audio():
    # Get text from the text area
    text = text_area.get("1.0", "end-1c")
    save_to_file(text, "Output2.mp3", rate=170)
    

label_text = tk.Label(root, text="  Welcome to ' Text to Speech Web Application ' ", font=("Arial", 12, "bold"))
label_text.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# Create a text area (Text widget)
text_area = tk.Text(root, height=15, width=80)
text_area.grid(row=1, column=0, columnspan=2, padx=15, pady=5)

# Create a button to speak the text
speak_button = tk.Button(root, text="Speak the Above text", command=speak_from_textarea, bg="green" ,fg="white" )
speak_button.grid(row=2, column=0, padx=4, pady=4)

# Create a button to save the text to speech in .mp3 
save_button = tk.Button(root, text="Save the text as Mp3", command=saving_to_audio , bg="Orange" ,fg="Black")
save_button.grid(row=2, column=1, padx=4, pady=4)



# Running the main loop to display the window
root.mainloop()

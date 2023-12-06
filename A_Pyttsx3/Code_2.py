# Importing the pyttsx3 module, which is a text-to-speech conversion library in Python.
import pyttsx3

# object creation
engine = pyttsx3.init() 

#Assiging a String to the variable "text"
text="Hello , I'm a Code that helps to make speech from text ."

"""Saving Voice to a file"""
engine.save_to_file(text, 'test.mp3')

# Running the engine to speak the text and wait for it to complete before proceeding.
engine.runAndWait()
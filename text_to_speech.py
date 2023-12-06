# Importing the pyttsx3 module, which is a text-to-speech conversion library in Python.
import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()


def speak_text(text, rate=200): 
    """
    Function to speak the provided text.
    
    Args:
    - text: Text to be spoken out loud.
    - rate: Speaking rate (default is 200).
    """
    
    # Set the speaking rate for the engine
    engine.setProperty('rate', rate)
    

    # Add the provided text to the engine to be spoken
    engine.say(text)
    
    # Run the engine to speak the text and wait for it to complete before stopping
    engine.runAndWait()
    
    # Stop the engine to release resources
    engine.stop()



def save_to_file(text, file_name, rate=200):
    """
    Function to save the speech of the provided text to a file.
    
    Args:
    - text: Text to be converted into speech and saved.
    - file_name: Name of the file to save the speech to.
    - rate: Speaking rate (default is 200).
    """
    # Set the speaking rate for the engine
    engine.setProperty('rate', rate)
    
    # Save the speech of the provided text to the specified file
    engine.save_to_file(text, file_name)
    
    # Run the engine to generate the speech and wait for it to complete before stopping
    engine.runAndWait()
    
    # Stop the engine to release resources
    engine.stop()



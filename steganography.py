'''
Importing Modules
Tkinter module – Tkinter is the standard interface in python for creating a GUI that is Graphical User Interface.
tkinter import * – import everything from the module.
tkinter.filedialog – This module is used to work with files.
from tkinter import messagebox – Import message box separately for showing messages on the screen.
PIL module – This is the images module from the pillow. The PIL module helps to open, manipulate and save many different forms of images.
Import ImageTk – ImageTk module used to create and modify Tkinter photoimage from PIL images.
Import os – This module is used for creating and removing any directory.
from stegano import lsb – This module is used to hide and reveal the secret message in the image.
import random – This module is used to generate random numbers.
from gtts import gTTS –
gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate's text-to-speech API.
This module is used to convert text to speech.
import speech_recognition as sr –
Library for performing speech recognition with the Google Speech Recognition API.
This module is used to convert speech to text.
'''

from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb   # pip install stegano
import random
from tkinter import messagebox

from gtts import gTTS
import speech_recognition as sr

#Create main frame or start page

global root

root = Tk()  # Create the default window, initializing the root window of steganography project.
root.title("Steganography - Hide a Secret Text Message in an Image") # Set the title of the window
root.geometry("930x595+200+28")    #Set size and position on the screen when opened
root.resizable(False, False)  # Disable resizing the GUI ( width , height ) / create a fixed size window
root.configure(bg="#2f4155") # Background color

def showimage():

    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), # Return the current working directory
                                          title='Select Image File',
                                          filetypes=( ("PNG file","*.png"), ("JPG File","*.jpg"), ("All file","*.txt"), ) )
    # Open the file dialog box and allow the user to select an image file

    img = Image.open(filename) # Open the image
    img = ImageTk.PhotoImage(img) # Convert the image to Tkinter compatible image format
    lbl.configure(image=img, width=250, height=250) # Set the image in the label
    lbl.image = img # Keep a reference


def Hide():

    global secret
    message = text1.get(1.0, END) # Get the text from the text box  # 1.0 means the first line and the first character
    secret = lsb.hide(str(filename), message) # Hide the text in the image

def showHiddenMessage():

 try:
    clear_message = lsb.reveal(filename) # Reveal the hidden text in the image
    text1.delete(1.0, END) # Clear the text box
    text1.insert(END, clear_message) # Insert the hidden text in the text box
 except:
        messagebox.showerror("Error", "No hidden message found in the image!") # If there is no hidden text show error message

def save():

    mylist = list() # Create an empty list
    i = 1       # Set the counter to 1
    while i < 1000:     # Loop until the counter is less than 1000
        mylist.append(i)   # Append the counter to the list
        i += 1     # Increment the counter

    randomName = "stego_image" + str(random.choice(mylist)) + ".png"     # Generate a random name for the image

    secret.save(randomName)   # Save the image with the hidden text

    messagebox.showinfo("Success!",
                        "Data hiding successful\n"
                        "File is saved as \"{}\" in the same directory".format(randomName)) # Show a message box

def textToSpeech(text1):
    language = 'en'    # tr (ISO Code Language)
    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells the module that the converted audio should have a high speed
    speech = gTTS(text=text1, lang=language, slow=False)    # slow=False (fast)
    speech.save("text.mp3")  # Save the text as an mp3 file
    os.system("start text.mp3")  # Play the mp3 file

def speechToText():      # recording voice
    while True: # Loop forever
        r = sr.Recognizer()  # Create a recognizer object
        with sr.Microphone() as source: # Use the microphone as the audio source
            audio=r.listen(source)  # Listen for the audio via source
            try:
                text = r.recognize_google(audio,language="en-US")  # Convert audio to text  #tr-TR (ISO Code Language)
            except:  # If speech is unintelligible
                pass # Do nothing
            return text


def reset():
    os.startfile("steganography.py")  # Restart program tkinter

    text1.delete('1.0', END)  # Clear/delete the contents of a Tkinter Text widget

    lbl.config(image=None)  # Python Tkinter remove/delete Image from Label
    lbl.image = None  # Python Tkinter remove/delete Image from Label


def close():
    root.destroy()     # Close the window, destroying GUI components.


#icon
image_icon = PhotoImage(file="icon.png") # Create a PhotoImage object of the image in the path
root.iconphoto(False, image_icon) # Set icon of master window

#background picture

logo = PhotoImage(file="backgroundPicture.png")   # Create a PhotoImage object of the image in the path
Label(root, image= logo, bg= "#17202a").place(x= 0, y= 0)  # Setting the background

Label(root, text="Steganography", bg="#04254a", fg="white", font="arial 25 bold").place(x=340, y=5) # Create a label to show the title


#First Frame

f = Frame(root, bd=3, bg="black", width=340, height=280, relief= GROOVE)  # Create a frame
f.place(x=10, y=80) # Set the position of the frame

lbl = Label(f, bg="black")  # Create a label to show the image
lbl.place(x=40, y=10)  # Set the position of the label

#Second Frame

frame2 = Frame(root, bd=3, width=340, height=280, bg="white", relief= GROOVE) # Create a frame
frame2.place(x=580, y=80) # Set the position of the frame

text1 = Text(frame2, font="Robote 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)  # Create a text box
text1.place(x=0, y=0, width=320, height=295) # Set the position of the text box

scrollbar1 = Scrollbar(frame2)  # Create a scrollbar
scrollbar1.place(x=320, y=0, height=300) # Set the position of the scrollbar

scrollbar1.configure(command=text1.yview)  # Configure the scrollbar
text1.configure(yscrollcommand=scrollbar1.set) # Configure the text box

#Third Frame

frame3 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE) # Create a frame
frame3.place(x=15, y=370) # Set the position of the frame

Button(frame3, text="Open Image", width=10, height=2, font="arial 14 bold", bg="#CD8500", fg='white', command=showimage).place(x=20, y=30) # Create a button to open the image
Button(frame3, text="Save Image", width=10, height=2, font="arial 14 bold", bg="#CD8500", fg='white', command=save).place(x=180, y=30)  # Create a button to save the image

Label(frame3, text="Picture, Image, Photo File", bg="#2f4155", fg="#FFEC8B").place(x=20, y=5) # Create a label to show the title

#Fourth Frame

frame4 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE) # Create a frame
frame4.place(x=585, y=370) # Set the position of the frame

Button(frame4, text="Hide Data", width=10, height=2, font="arial 14 bold", bg="#CD8500", fg='white', command=Hide).place(x=20, y=30) # Create a button to hide the text
Button(frame4, text="Show Data", width=10, height=2, font="arial 14 bold", bg="#CD8500", fg='white', command=showHiddenMessage).place(x=180, y=30) # Create a button to show the hidden text

Label(frame4, text="Picture, Image, Photo File", bg="#2f4155", fg="#EEDC82").place(x=20, y=5) # Create a label to show the title

#Five Frame

frame5 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE) # Create a frame
frame5.place(x=300, y=488) # Set the position of the frame

Button(frame5, text="Reset", width=10, height=2, font="arial 14 bold", bg="#CD8500", fg='white', command=reset ).place(x=20, y=30) # Create a button to reset the program
Button(frame5, text="Close", width=10, height=2, font="arial 14 bold", bg="#CD8500", fg='white', command=close ).place(x=180, y=30) # Create a button to close the program

Label(frame5, text="Reset, Close Program", bg="#2f4155", fg="#FFEC8B").place(x=26, y=8) # Create a label to show the title


# Create the list of options
options_list = ["Text To Speech", "Speech To Text"]

# Variable to keep track of the option
# selected in OptionMenu
value_inside = tk.StringVar(root) # Create a variable to store the selected option

# Set the default value of the variable
value_inside.set("Conversion")

# Create the optionmenu widget and passing
# the options_list and value_inside to it.
question_menu = tk.OptionMenu(root, value_inside, *options_list).place(x=795, y=49)

# Function to print the submitted option-- testing purpose

def selected_action():  # Create a function to get the selected option

    if(value_inside.get() == options_list[0]): # If the selected option is the first option

        textToSpeech(str(text1.get(1.0, END))) # Call the textToSpeech function

    if(value_inside.get() == options_list[1]):  # If the selected option is the second option

        text1.insert(END, speechToText())  # Call the speechToText function

    return None

# Submit button
# Whenever we click the submit button, our submitted
# option is printed ---Testing purpose
submit_button = tk.Button(root, text='Submit',bg="#800000", fg='white', command=selected_action).place(x=746, y=52) # Create a button to submit the option


root.mainloop()  # Start the GUI
#!/Users/pfb2024/mamba/envs/projects/bin/python3

#This is the home page 
import ttkbootstrap as ttkb
import tkinter as tk
from PIL import Image, ImageTk

current_question = 1
questions = {1:"How old are you?", 2:"What is your favorite animal?", 3:"Where do you live?"}
answers = []

#function to create a new window 
def open_new_window():
    if current_question < len(questions)+1:
        display_question()
    else:
        end_quiz()
# def open_new_window(question_number):
#    for widget in overlay_frame.winfo_children():
#         widget.destroy()
#    second_page()

def display_question():
    question_text = questions[current_question]
    
    # Clear the previous widgets
    for widget in overlay_frame.winfo_children():
        widget.destroy()

    # Display the current question
    label1 = tk.Label(overlay_frame, text=question_text, font=("Arial", 40, "bold"), bg='LightBlue1')
    label1.pack(pady=20)

    entry1 = tk.Entry(overlay_frame, font=font)
    entry1.pack(pady=20)

    button1 = tk.Button(overlay_frame, text="Next question!", font=font, bg='LightBlue1',
                        command=lambda: next_question(entry1.get()))  # Capture user input
    button1.pack(pady=20)

# def second_page():
#      entry1 = tk.Entry(overlay_frame, font = font)
#      button1 = tk.Button(overlay_frame, text = "Next question!", font = font, bg='LightBlue1')
#      label1 = tk.Label(overlay_frame, text = "question", font = ("Arial", 40, "bold"), bg='LightBlue1')
#      label1.pack(pady = 20)
#      entry1.pack(pady = 20) 
#      button1.pack(pady = 20)

def next_question(user_answer):
    global current_question
    answers.append(user_answer)  # Store the user's answer
    current_question += 1  # Move to the next question
    open_new_window()

def end_quiz():
    for widget in overlay_frame.winfo_children():
        widget.destroy()
    label_end = tk.Label(overlay_frame, text="Thank you for participating! You have been matched with _____", font=("Arial", 40, "bold"), bg='LightBlue1')
    label_end.pack(pady=20)


# def open_new_window2(question_number):
#    for widget in overlay_frame.winfo_children():
#         widget.destroy()
#    question_text = questions.get(question_number, "Question not found")
#    entry1 = tk.Entry(overlay_frame, font = font)
#    button1 = tk.Button(overlay_frame, text = "Next question!", font = font, bg='LightBlue1')
#    label1 = tk.Label(overlay_frame, text = question_text, font = ("Arial", 40, "bold"), bg='LightBlue1')
#    label5 = tk.Label(overlay_frame, text = "Only enter an integer", font = 30, bg='LightBlue1')
#    label1.pack(pady = 20)
#    label5.pack(pady = 20)  
#    entry1.pack(pady = 20) 
#    button1.pack(pady = 20)


#Make a window and add the image as the background 
parent = tk.Tk()
parent.title("Image in Tkinter")
parent.attributes("-fullscreen", True) 
image = Image.open("Bestie_artwork1.png")
image = image.resize((parent.winfo_screenwidth(), parent.winfo_screenheight()))
image = ImageTk.PhotoImage(image)
image_label = tk.Label(parent, image = image)

#Make it so that the widgets can be layered on 
overlay_frame = tk.Frame(parent, bg='LightBlue1', bd=0)
overlay_frame.place(relx=0.5, rely=0.2, anchor='center')

#Change the font 
font_size = 40
font = ("Arial", font_size)

#To get the user input of names this is the function
def on_button1_click():
    name = entry.get()
    label3 = tk.Label(overlay_frame, text = f'Welcome {name}!', font = font, bg='LightBlue1')
    label3.pack()
    overlay_frame.after(1000, open_new_window)

# def on_button2_click():
#     name = entry.get()
#     overlay_frame.after(1000, lambda: open_new_window(2))

#Add the other widgets 
entry = tk.Entry(overlay_frame, font = font)
button = tk.Button(overlay_frame, text = "Click here to begin!", command = on_button1_click, font = font)
#button2 = tk.Button(overlay_frame, text = "Click me to begin!", command = open_new_window, font = font)
label = tk.Label(overlay_frame, text = "Welcome! You are on the right path to finding your bestie! ", font = ("Arial", 40, "bold"), bg='LightBlue1')
label2 = tk.Label(overlay_frame, text = "Please enter your name in the box", font = font, bg='LightBlue1')

#Push the widgets into the frame 
label.pack()
label2.pack()   
entry.pack(pady = 20)
button.pack(pady = 20)
#button2.pack(pady = 20)
image_label.pack()
parent.mainloop()

print(answers)





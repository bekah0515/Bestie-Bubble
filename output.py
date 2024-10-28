#!/Users/pfb2024/mamba/envs/projects/bin/python3

#This is the home page 
import ttkbootstrap as ttkb
import tkinter as tk
from PIL import Image, ImageTk
import csv
import os

current_question = 0
answers = ""

def function1():
    all_lines = []
    with open("personality_data_info.txt", 'r') as input_file:
        lines = input_file.readlines()
        for line in lines:
            line = line.strip().split("\t")
            processed_line = '\t'.join(line[1:])
            all_lines.append(processed_line)
    return(all_lines)

questions = function1()

#function to create a new window 
def open_new_window():
    if current_question < len(questions)+1:
        display_question()
    else:
        end_quiz()
       
        # match_page()
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
    label1 = tk.Label(overlay_frame, text=question_text, font=("Arial", 40, "bold"), bg='light sea green')
    label1.pack(pady=20)
    label2 = tk.Label(overlay_frame, text = "Please answer the question with an integer value. 1 corresponds to least agree, 3 is neutral, and 5 is most agree.", font=("Arial", 30), bg='light sea green')
    label2.pack(pady=20)

    entry1 = tk.Entry(overlay_frame, font=font, justify = "center")
    entry1.pack(pady=20)

    button1 = tk.Button(overlay_frame, text="Next question!", font=font, bg='light sea green',
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
    global current_question, answers
    answers += user_answer + ","  # Store the user's answer
    current_question += 1  # Move to the next question
    open_new_window()

def end_quiz():
    for widget in overlay_frame.winfo_children():
        widget.destroy()
    label_end = tk.Label(overlay_frame, text="Thank you for participating! You have been matched with _____", font=("Arial", 40, "bold"), bg='light sea green')
    label_end.pack(pady=20)

    export_to_csv

def export_to_csv():
    # Specify the file path (you can change this to your desired location)
    file_path = os.path.expanduser('~/answers.csv')
    
    # Write answers to CSV
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Answers'])  # Write header
        writer.writerow(answers)  # Write the collected answers

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

# def export_to_csv():
#     with open('answers.csv', mode='w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([answers])

#Make a window and add the image as the background 
parent = tk.Tk()
parent.title("Image in Tkinter")
parent.attributes("-fullscreen", True) 
image = Image.open("Bestie_artwork1.png")
image = image.resize((parent.winfo_screenwidth(), parent.winfo_screenheight()))
image = ImageTk.PhotoImage(image)
image_label = tk.Label(parent, image = image)

#Make it so that the widgets can be layered on 
overlay_frame = tk.Frame(parent, bg='light sea green', bd=0)
overlay_frame.place(relx=0.5, rely=0.2, anchor='center')

#Change the font 
font_size = 40
font = ("Arial", font_size)

#To get the user input of names this is the function
def on_button1_click():
    global user_name, answers
    user_name = entry.get()
    answers += user_name + ","
    label3 = tk.Label(overlay_frame, text = f'Welcome {user_name}!', font = font, bg='light sea green')
    label3.pack()
    overlay_frame.after(1000, open_new_window)

# def on_button2_click():
#     name = entry.get()
#     overlay_frame.after(1000, lambda: open_new_window(2))

#Add the other widgets 
entry = tk.Entry(overlay_frame, font = font, justify = "center")
button = tk.Button(overlay_frame, text = "Click here to begin!", command = on_button1_click, font = font)
#button2 = tk.Button(overlay_frame, text = "Click me to begin!", command = open_new_window, font = font)
label = tk.Label(overlay_frame, text = "Welcome! You are on the right path to finding your bestie! ", font = ("Arial", 40, "bold"), bg='light sea green')
label2 = tk.Label(overlay_frame, text = "Please enter your name in the box", font = font, bg='light sea green')

#Push the widgets into the frame 
label.pack()
label2.pack()   
entry.pack(pady = 20)
button.pack(pady = 20)
#button2.pack(pady = 20)
image_label.pack()
parent.mainloop()

print(answers)

# def match_page():
#     # Clear the previous widgets
#     for widget in overlay_frame.winfo_children():
#         widget.destroy()

#     # Display the current question
#     label7 = tk.Label(overlay_frame, text="Your Match Is", font=("Arial", 40, "bold"), bg='light sea green')
#     label7.pack(pady=20)
#     button7 = tk.Button(overlay_frame, text="Exit!", font=font, bg='light sea green' command = parent.destroy())  # Capture user input
#     button7.pack(pady=20)
#     image = Image.open("X")
#     image = image.resize((parent.winfo_screenwidth(), parent.winfo_screenheight()))
#     image = ImageTk.PhotoImage(image)
#     image_label = tk.Label(parent, image = image)
#!/Users/pfb2024/mamba/envs/projects/bin/python3

#This is the home page 
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
        export_to_csv(user_name)
       
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

def next_question(user_answer):
    global current_question, answers
    answers += user_answer + ","  # Store the user's answer
    current_question += 1  # Move to the next question
    open_new_window()

def end_quiz():
    global current_question, answers
    for widget in overlay_frame.winfo_children():
        widget.destroy()
    label_end = tk.Label(overlay_frame, text="Thank you for participating!", font=("Arial", 40, "bold"), bg='light sea green')
    label_end.pack(pady=20)
    button10 = tk.Button(overlay_frame, text = "Click here to get your match!", command = on_button2_click, font = font)
    button10.pack()
    export_to_csv(user_name)

def export_to_csv(user_name):
    # Specify the file path (you can change this to your desired location)
    file_path = os.path.expanduser(f'~/{user_name}_answers.csv')
    print(file_path)
    # Write answers to CSV
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Answers'])  # Write header
        writer.writerow(answers.split(','))  # Write the collected answers


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

def on_button2_click():
    open_match()

def open_match():
    for widget in overlay_frame.winfo_children():
        widget.destroy()
    parent1 = tk.Toplevel()
    parent1.title("Your Match")
    parent1.attributes("-fullscreen", True) 
    image2 = Image.open("Bestie_artwork2.png")
    image2 = image.resize((parent.winfo_screenwidth(), parent.winfo_screenheight()))
    image2 = ImageTk.PhotoImage(image2)
    image_label2 = tk.Label(parent1, image = image2)
    image_label2.pack()
    label_match = tk.Label(match_window, text="Your match is: _____", font=("Arial", 40, "bold"), bg='light sea green')
    label_match.pack(pady=20)

#Make it so that the widgets can be layered on 
overlay_frame2 = tk.Frame(parent, bg='light sea green', bd=0)
overlay_frame2.place(relx=0.5, rely=0.2, anchor='center')

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

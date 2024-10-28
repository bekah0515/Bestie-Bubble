fi#!/Users/pfb2024/mamba/envs/projects/bin/python3

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
    if current_question < len(questions):
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
    file_path = os.path.expanduser(f'./{user_name}_answers.csv')
    print(file_path)
    # Write answers to CSV
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file) 
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
    # Clear previous widgets
    for widget in overlay_frame.winfo_children():
        widget.destroy()
    info_frame = tk.Frame(overlay_frame, bg='light sea green')
    info_frame.pack(side="top", pady=(700, 20))  # Add padding to move it down

    label_match = tk.Label(info_frame, text="Your top two matches are: April Tran and Grace Watson", font=("Arial", 40, "bold"), bg='light sea green')
    label_match.pack(pady=10)

    button11 = tk.Button(info_frame, text="Click here to get more information!", font=font, command = open_match2)
    button11.pack(pady = 10)

    image_frame2 = tk.Frame(overlay_frame, bg='light sea green')
    image_frame2.pack(side="top", fill="x", pady = 20)  # Fill the width at the bottom

    image6 = Image.open("Simon_bestie_matches.png")
    image6 = image6.resize((1100, 800))
    image6_tk = ImageTk.PhotoImage(image6)
    image_label6 = tk.Label(image_frame2, image=image6_tk, bg='light sea green')
    image_label6.image = image6_tk  # Keep a reference
    image_label6.pack()



      # Fill the width at the bottom
    

def open_match2():
    for widget in overlay_frame.winfo_children():
        widget.destroy()

    # Adjust the padding for image_frame3
    image_frame3 = tk.Frame(overlay_frame, bg='light sea green')
    image_frame3.pack(side="top", pady=(700, 20))  # Add more top padding

    # Load images 3, 4, and 5
    image3 = Image.open("DavidDukeandAprilTran.png")
    image4 = Image.open("DavidDukeandGraceWatson.png")
    # image5 = Image.open("SMOLLYandAmanda Herrera MD.png")
    image3 = image3.resize((500, 500))
    image4 = image4.resize((500, 500))
    # image5 = image5.resize((500, 500))

    # Create PhotoImage references
    image3_tk = ImageTk.PhotoImage(image3)
    image4_tk = ImageTk.PhotoImage(image4)
    # image5_tk = ImageTk.PhotoImage(image5)

    # Create labels for images and grid them
    image_label3 = tk.Label(image_frame3, image=image3_tk, bg='light sea green')
    image_label3.image = image3_tk  # Keep a reference
    image_label3.pack(side="left", padx=10, pady=10)

    image_label4 = tk.Label(image_frame3, image=image4_tk, bg='light sea green')
    image_label4.image = image4_tk  # Keep a reference
    image_label4.pack(side="left", padx=10, pady=10)

    # image_label5 = tk.Label(image_frame3, image=image5_tk, bg='light sea green')
    # image_label5.image = image5_tk  # Keep a reference
    # image_label5.pack(side="left", padx=10, pady=10)

    # Create a frame for image 7
    info_frame3 = tk.Frame(overlay_frame, bg='light sea green')
    info_frame3.pack(side="top", pady=(20, 20))

    image7 = Image.open("nearest_neighbor_plot.png")
    image7 = image7.resize((900, 500))
    image7_tk = ImageTk.PhotoImage(image7)

    image_label7 = tk.Label(info_frame3, image=image7_tk, bg='light sea green')
    image_label7.image = image7_tk  # Keep a reference
    image_label7.pack(pady=10)


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

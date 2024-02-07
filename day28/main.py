'''
Pomodoro GUI app
After each 25min session one check mark is added and there will be 5min break
After 4th session there's going to be 20min break and session will reset automatically
'''

import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetitions = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global repetitions
    repetitions = 0
    window.after_cancel(timer) # type: ignore
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global repetitions
    repetitions += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if repetitions % 8 == 0 and repetitions > 1:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
        repetitions = 0
    elif repetitions == 0 or repetitions % 2 != 0:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    else:
        count_down(short_break_sec)       
        title_label.config(text="Break", fg=PINK)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = math.floor(repetitions / 2)
        check_marks.config(text="✓"*marks, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25))
        

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = tk.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=False)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start", bd=5, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", bd=5, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = tk.Label()
check_marks.grid(column=1, row=3)

window.mainloop()
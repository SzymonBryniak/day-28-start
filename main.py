import tkinter
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Calibri"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
ADD_CHECK_MARK = "✓"
timer = None
minus = 1
reset = 0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def break_count(count):
    count_min = math.floor(count / 1)
    count_sec = count * 1
    canvas.itemconfig(timer_text, text=f"0: 0{count_sec}")
    if count > 0:
        window.after(1000, break_count, count - 1)
    elif count == 0:
        count_down(WORK_MIN)


def stop_countdown():
    global timer, ADD_CHECK_MARK, minus, reset
    label_mark.config(text="✓")

    canvas.itemconfig(timer_text, text=f"00:00")
    minus = 100


def start_timer():
    global minus
    minus = 1
    count_count_down = count_down(25 * 1)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


def count_down(count):

    global ADD_CHECK_MARK, reps, reset
    if reset != 0:
        count = 0
    if reps > 5:
        return print('Game Over')
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}: {count_sec}")

    if count > 0:
        window.after(1000, count_down, count - minus)
    elif count == 0:
        reps += 1
        ADD_CHECK_MARK = ADD_CHECK_MARK + "✓" * reps
        print('mark added')
        label_mark.config(text=ADD_CHECK_MARK)
        if reps < 5:
            break_count(SHORT_BREAK_MIN)
        elif reps == 5:
            break_count(LONG_BREAK_MIN)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image=tomato_img)
timer_text = canvas.create_text(101, 112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

check_mark = "✓"
label_mark = tkinter.Label(text=check_mark, fg=GREEN, bg=YELLOW)
label_mark.grid(column=1, row=4)

label1 = tkinter.Label(text="Timer", font=(FONT_NAME, 45, "bold"), bg=YELLOW)
label1.grid(column=1, row=0)

button_start = tkinter.Button(text="Start", command=start_timer)
button_start.grid(column=0, row=3)

button_reset = tkinter.Button(text="Reset", command=stop_countdown)
button_reset.grid(column=3, row=3)


window.mainloop()







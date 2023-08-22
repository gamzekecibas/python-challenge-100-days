from tkinter import *
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

reps = 0
my_timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text="00:00")
    main_title.config(text="Timer")
    check_mark.config(text="")

    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        main_title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        # If it's 2nd/4th/6th rep:
        count_down(short_break_sec)
        main_title.config(text="Short Break", fg=PINK)
    else:
        # If it's the 1st/3rd/5th/7th rep:
        count_down(work_sec)
        main_title.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sess = math.floor(reps / 2)
        for _ in range(work_sess):
            mark += "✔"
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

main_title = Label(text="Timer", fg=GREEN, bg=YELLOW,
                   font=(FONT_NAME, 50))
main_title.grid(row=0, column=1)

canvas = Canvas(width=200, height=224,
                bg=YELLOW, highlightthickness=0)
bg_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=bg_image)
timer_text = canvas.create_text(100, 130, text="00:00",
                                fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start",
                      bg=YELLOW, highlightthickness=0,
                      command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset",
                      bg=YELLOW, highlightthickness=0,
                      command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark = Label(text="", fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)

window.mainloop()

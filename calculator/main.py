from tkinter import *
# global after_number, before_number, operator
window = Tk()
window.title("Calculator")
window.geometry('280x425')
window.config(bg="black")

def view_num(digit):
    first = label['text']
    value = str(first) + digit
    label.config(text=value)


def clear():
    label.config(text="")


def result():
    # global after_number, before_number, operator
    import re

    k = label["text"]
    special_chars = re.findall(r'[^a-zA-Z0-9]', k)
    operator = special_chars[0]

    pattern = r'(\d+)\s*' + re.escape(operator) + r'\s*(\d+)'
    matches = re.findall(pattern, k)
    for match in matches:
        before_number = int(match[0])
        after_number = int(match[1])

    print(before_number)
    print(after_number, operator)

    if operator == "-":
        res = int(before_number) - int(after_number)
        print(before_number)
        print(after_number, operator)
        label.config(text=res)

    elif operator == "+":
        print(before_number)
        print(after_number, operator)
        res = int(before_number) + int(after_number)
        label.config(text=res)

    elif operator == "*":
        res = int(before_number) * int(after_number)
        label.config(text=res)

    else:
        if after_number == 0 or before_number == 0:
            va = "error"
            label.config(text=va)
        else:
            res = int(before_number) / int(after_number)
            label.config(text=res)


button1 = Button(window, text="1", command=lambda: view_num("1"), font=("Helvetica", 30), fg="white", bg="black")
button1.grid(row=2, column=1, padx=0, pady=5)
button2 = Button(window, text="2", command=lambda: view_num("2"), font=("Helvetica", 30), fg="white", bg="black")
button2.grid(row=2, column=2, padx=0, pady=5)
button3 = Button(window, text="3", command=lambda: view_num('3'), font=("Helvetica", 30), fg="white", bg="black")
button3.grid(row=2, column=3, padx=0, pady=5)
button4 = Button(window, text="4", command=lambda: view_num('4'), font=("Helvetica", 30), fg="white", bg="black")
button4.grid(row=3, column=1, padx=0, pady=5)
button5 = Button(window, text="5", command=lambda: view_num('5'), font=("Helvetica", 30), fg="white", bg="black")
button5.grid(row=3, column=2, padx=0, pady=5)
button6 = Button(window, text="6", command=lambda: view_num('6'), font=("Helvetica", 30), fg="white", bg="black")
button6.grid(row=3, column=3, padx=5, pady=5)

button7 = Button(window, text="7", command=lambda: view_num('7'), font=("Helvetica", 30), fg="white", bg="black")
button7.grid(row=4, column=1, padx=5, pady=5)

button8 = Button(window, text="8", command=lambda: view_num('8'), font=("Helvetica", 30), fg="white", bg="black")
button8.grid(row=4, column=2, padx=5, pady=5)

button9 = Button(window, text="9", command=lambda: view_num('9'), font=("Helvetica", 30), fg="white", bg="black")
button9.grid(row=4, column=3, padx=5, pady=5)

clear = Button(window, text="C", command=clear, font=("Helvetica", 30), fg="white", bg="black")
clear.grid(row=5, column=1, padx=5, pady=5)
zero = Button(window, text="0", command=lambda: view_num('0'), font=("Helvetica", 30), fg="white", bg="black")
zero.grid(row=5, column=2, padx=5, pady=5)

equal_to = Button(window, text="=", command=result, font=("Helvetica", 30), fg="white", bg="black")
equal_to.grid(row=5, column=3, padx=5, pady=5)

add = Button(window, text="+", font=("Helvetica", 30), command=lambda: view_num("+"), fg="white", bg="black")
add.grid(row=2, column=7, padx=5, pady=5)
sub = Button(window, text="-", font=("Helvetica", 30), command=lambda: view_num("-"), fg="white", bg="black")
sub.grid(row=3, column=7, padx=5, pady=5)
mul = Button(window, text="*", font=("Helvetica", 30), command=lambda: view_num("*"), fg="white", bg="black")
mul.grid(row=4, column=7, padx=5, pady=5)
div = Button(window, text="/", font=("Helvetica", 30), command=lambda: view_num("/"), fg="white", bg="black")
div.grid(row=5, column=7, padx=5, pady=5)

label = Label(window, text="", font=("Helvetica", 30), fg="white", bg="black")
label.grid(row=1, columnspan=15, column=1, padx=5, pady=5, sticky="w")

window.mainloop()

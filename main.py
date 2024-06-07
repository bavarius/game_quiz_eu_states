from tkinter import *
import pandas as pd

df = pd.read_csv("resources/EU-Länder.csv", delimiter=';')
countries = {row.country: {'state_x': row.state_x, 'state_y': row.state_y} for index, row in df.iterrows()}
all_countries = [key for key in countries.keys()]
num_guessed_countries = 0


# Determine the origin by clicking
# def get_origin(event_origin):
#     x0 = event_origin.x
#     y0 = event_origin.y
#     print(f"{x0}; {y0}")


def enter_country():
    guessed_country = entry_country.get().title()
    if guessed_country in all_countries:
        global num_guessed_countries
        num_guessed_countries += 1
        canvas.create_text(
            countries[guessed_country]['state_x'],
            countries[guessed_country]['state_y'],
            text=guessed_country,
            width=74,
            fill='yellow',
            font=('Arial', 8, 'bold'))
        entry_country.delete(0, END)
        all_countries.remove(guessed_country)
        if num_guessed_countries >= len(countries):
            lbl_status.config(text=f"Gratuliere! Alle {len(countries)} Länder erraten!")
        else:
            lbl_status.config(text=f"{num_guessed_countries} von {len(countries)} erraten, weiter:")
    else:
        lbl_status.config(text=f"{guessed_country} ist kein EU-Mitgliedsstaat!")


def key_press(event):
    if event is not None:
        enter_country()


def quit_game():
    with open('zu_lernen.txt', 'w', encoding='utf-8') as f:
        f.write("Diese {} Länder musst Du Dir noch einprägen:\n{}\n".format(len(all_countries), '\n'.join(all_countries)))
    window.destroy()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Europa - Quiz")
window.config(padx=50, pady=20, bg="black")
# window.bind("<Button 1>", get_origin)
window.bind("<Return>", key_press)

btn_quit = Button(window, text="Aufgeben", command=quit_game)
btn_quit.grid(column=0, row=0)

lbl_status = Label(
    window,
    text="Bitte Land eingeben + 'Enter' - oder Klick auf 'OK'!",
    width=40,
    justify="center",
    fg="yellow",
    bg="blue")
lbl_status.grid(column=1, row=0)

entry_country = Entry(window, width=40, justify="center")
entry_country.grid(column=2, row=0)
entry_country.focus_set()

btn_enter = Button(window, text="OK", command=enter_country)
btn_enter.grid(column=3, row=0)

canvas = Canvas(window, width=824, height=824, highlightthickness=0)
europa_img = PhotoImage(file='resources/eu_mitgliedsstaaten.png')
canvas.create_image(412, 412, image=europa_img)
# Display all country names immediately - for calibration of coordinates
# for key, details in countries.items():
#     lbl_state = canvas.create_text(details['state_x'], details['state_y'], text=key, width=74,
#                                    fill='yellow', font=('Arial', 8, 'bold'))
canvas.grid(column=0, row=1, columnspan=4)

window.mainloop()

import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",

layout=[[sg.Text("SELAMAT DATANG DI KELAS",

font=("Arial",25))],

[sg.Text("NPM : 2210010143 ")],
[sg.Text("Nama : Hambali Abdan ")],
[sg.Text("Kelas : 5E Regular Banjarmasin ")]
],

size=(500,200),
font=("Times", 18))

window()
window.close()
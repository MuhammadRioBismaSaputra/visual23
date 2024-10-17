import PySimpleGUI as sg
susunan=[[sg.text("UNISKA MAAB",font=("helvetica",24))],
          [sg.text("BANJARMASIN", font=("Courier",18))]],
window = sg.window(title="elemen ttext",
                   layout=susunan,
                   elemen_justifiction = "center",
                   size=(430,200))

window.read()      
window.close()  
from PySimpleGUI import PySimpleGUI as sg
import tkinter as tk

sg.theme('Reddit')

layout = [
    [sg.Text('User'), sg.Input(key='user')],
    [sg.Text('Password'), sg.Input(key='password',password_char='*')],
    [sg.Checkbox('Save login?')],
    [sg.Button('Enter')]
]

# Janela 
janela = sg.Window('Login Screen', layout)

# Ler os eventos 
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Enter':
        if valores['user'] == 'sabino' and valores['password'] == '123456':
            print('Welcome!')

import PySimpleGUI as sg



def load_gui():
    sg.theme('Dark Blue 3')

    layout = [
        [sg.Text('KaiOS Scraper')],
        [sg.Text('Are you parsing a directory or a file? (e.g. .zip, .bin, .upg)')],
        [sg.Button('Directory'), sg.Button('File')]
    ]

    window = sg.Window('KaiOS Scraper', layout)
    while True:
        event, values = window.read()
        if event == 'Directory':
            window.close()
            return '2'
        elif event == 'File':
            window.close()
            return '1'
        break
    window.close()

def main_gui(option):

    sg.theme('Dark Blue 3')

    if option == '1':
        layout = [
            [sg.Text('KaiOS Scraper')],
            [sg.Text('Enter Filename to parse (e.g extraction.bin, extraction.zip): '), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]
        ]
    elif option == '2':
        layout = [
            [sg.Text('KaiOS Scraper')],
            [sg.Text('Enter Directory to Parse: '), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]
        ]

    window = sg.Window('KaiOS Scraper', layout)
    while True:
        event, values = window.read()
        if event == 'Ok':
            window.close()
            return values
        elif event == 'Cancel':
            window.close()
        break
    window.close()
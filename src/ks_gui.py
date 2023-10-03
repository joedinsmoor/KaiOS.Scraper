import PySimpleGUI as sg



def load_gui():
    sg.theme('Dark Blue 3')

    layout = [
        [sg.Text('KaiOS Scraper')],
        [sg.Text('Are you parsing a directory or a file? (e.g. .zip, .bin, .upg)')],
        [sg.Button('Directory', tooltip='e.g. Users/Username/Downloads/extraction/'), sg.Button('File',tooltip='e.g. Users/Username/Downloads/extraction.zip' ), sg.Button('Cancel')]
    ]

    window = sg.Window('KaiOS Scraper', layout, alpha_channel=0.7)
    while True:
        event, values = window.read()
        if event == 'Directory':
            window.close()
            path()
            return '2'
        elif event == 'File':
            window.close()
            file()
            return '1'
        elif event == 'Cancel':
            exit()
        break
    window.close()


def file():
    layout = [
            [sg.Text('KaiOS Scraper')],
            [sg.Text('Enter Filename to parse (e.g extraction.bin, extraction.zip): '), sg.InputText(focus=True, tooltip='Enter path to file being parsed, e.g. (/Users/Username/Downloads/extraction.zip)')],
            [sg.Button('Ok'), sg.Button('Cancel')]
        ]
    window = sg.Window('KaiOS Scraper', layout, alpha_channel=0.7)
    while True:
        event, values = window.read(timeout=1)
        if event == 'Ok':
            window.close()
            return values
        elif event =='Cancel':
            exit()
        break
    window.close

def path():
    layout = [
            [sg.Text('KaiOS Scraper')],
            [sg.Text('Enter Directory to Parse: '), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]
        ]
    window = sg.Window('KaiOS Scraper', layout, alpha_channel=0.7)
    while True:
        event, values = window.read(timeout=1)
        if event == 'Ok':
            window.close()
            return values
        elif event =='Cancel':
            exit()
        break
    window.close
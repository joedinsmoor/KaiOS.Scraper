import PySimpleGUI as sg



def load_gui():
    '''
    - Enables selection between directory parsing and file parsing, returns menu options for sqlite_scraper menu method. 
    - Arguments: 
      - Selection -> button event
      - Returns -> method of parsing, dir/file
    '''
    sg.theme('Dark Blue 2')

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
            return "2"
        elif event == 'File':
            window.close()
            file()
            return "1"
        elif event == 'Cancel':
            exit()
        break
    window.close()


def file():
    '''
    - Enables input of filename and path for file parsing
    - Arguments: 
      - User Input -> values
      - Returns -> values
    '''
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
    '''
    - Enables input of directory path for directory parsing
    - Arguments: 
      - User input -> pathval
      - Returns -> values
    '''
    layout = [
            [sg.Text('KaiOS Scraper')],
            [sg.Text('Enter Directory to Parse: '), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]
        ]
    window = sg.Window('KaiOS Scraper', layout, alpha_channel=0.7)
    while True:
        try:
            event, values = window.read(timeout=10000)
        except:
            pass
        finally:
            pass
        if callable(event):
            event()
        elif event == 'Ok':
            window.close()
            return values
        elif event =='Cancel':
            exit()
        break
    window.close
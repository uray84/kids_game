# 算数ゲーム
import random
import time
import PySimpleGUI as sg

# ↓↓code to save as exe file↓↓
# pip install PyInstaller
# pyinstaller -wF クイ～ズクイズ.py
# use kivy for smartphone apps


# 質問と答えの記入
addition2 = [["2+9=", "11"], ["3+8=", "11"], ["3+9=", "12"], ["4+7=", "11"],
             ["4+8=", "12"], ["4+9=", "13"], ["5+6=", "11"], ["5+7=", "12"],
             ["5+8=", "13"], ["5+9=", "14"], ["6+5=", "11"], ["6+6=", "12"],
             ["6+7=", "13"], ["6+8=", "14"], ["6+9=", "15"], ["7+4=", "11"],
             ["7+5=", "12"], ["7+6=", "13"], ["7+7=", "14"], ["7+8=", "15"],
             ["7+9=", "16"], ["8+3=", "11"], ["8+4=", "12"], ["8+5=", "13"],
             ["8+6=", "14"], ["8+7=", "15"], ["8+8=", "16"], ["8+9=", "17"],
             ["9+2=", "11"], ["9+3=", "12"], ["9+4=", "13"], ["9+5=", "14"],
             ["9+6=", "15"], ["9+7=", "16"], ["9+8=", "17"], ["9+9=", "18"]]

subtraction2 = [["11-2=", "9"], ["11-3=", "8"], ["11-4=", "7"], ["11-5=", "6"],
            ["11-6=", "5"], ["11-7=", "4"], ["11-8=", "3"], ["11-9=", "2"],
            ["12-3=", "9"], ["12-4=", "8"], ["12-5=", "7"], ["12-6=", "6"],
            ["12-7=", "5"], ["12-8=", "4"], ["12-9=", "3"], ["13-4=", "9"],
            ["13-5=", "8"], ["13-6=", "7"], ["13-7=", "6"], ["13-8=", "5"],
            ["13-9=", "4"], ["14-5=", "9"], ["14-6=", "8"], ["14-7=", "7"],
            ["14-8=", "6"], ["14-9=", "5"], ["15-6=", "9"], ["15-7=", "8"],
            ["15-8=", "7"], ["15-9=", "6"], ["16-7=", "9"], ["16-8=", "8"],
            ["16-9=", "7"], ["17-8=", "9"], ["17-9=", "8"], ["18-9=", "9"]]

# sample code for the simpleGUI (sg) library
"""
-------------------------------------
# stopwatch code

sg.theme('DarkBrown1')

layout = [  [sg.Text('Stopwatch', size=(20, 2), justification='center')],
            [sg.Text(size=(10, 2), font=('Helvetica', 20), justification='center', key='-OUTPUT-')],
            [sg.T(' ' * 5), sg.Button('Start/Stop', focus=True), sg.Quit()]]

window = sg.Window('Stopwatch Timer', layout)

timer_running, counter = True, 0

while True:                                 # Event Loop
    event, values = window.read(timeout=10) # Please try and use as high of a timeout value as you can
    if event in (sg.WIN_CLOSED, 'Quit'):             # if user closed the window using X or clicked Quit button
        break
    elif event == 'Start/Stop':
        timer_running = not timer_running
    if timer_running:
        window['-OUTPUT-'].update('{:02d}:{:02d}.{:02d}'.format((counter // 100) // 60, (counter // 100) % 60, counter % 100))
        counter += 1
window.close()

---------------------------------------------

# multiple elements in a single ui


#!/usr/bin/env Python3      
import PySimpleGUI as sg      

sg.ChangeLookAndFeel('GreenTan')      

# ------ Menu Definition ------ #      
menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],      
            ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],      
            ['Help', 'About...'], ]      

# ------ Column Definition ------ #      
column1 = [[sg.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))],      
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],      
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],      
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]      

layout = [      
    [sg.Menu(menu_def, tearoff=True)],      
    [sg.Text('All graphic widgets in one window!', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],    
    [sg.Text('Here is some text.... and a place to enter text')],      
    [sg.InputText('This is my text')],      
    [sg.Frame(layout=[      
    [sg.Checkbox('Checkbox', size=(10,1)),  sg.Checkbox('My second checkbox!', default=True)],      
    [sg.Radio('My first Radio!     ', "RADIO1", default=True, size=(10,1)), sg.Radio('My second Radio!', "RADIO1")]], title='Options',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],      
    [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),      
        sg.Multiline(default_text='A second multi-line', size=(35, 3))],      
    [sg.InputCombo(('Combobox 1', 'Combobox 2'), size=(20, 1)),      
        sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],      
    [sg.InputOptionMenu(('Menu Option 1', 'Menu Option 2', 'Menu Option 3'))],      
    [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),      
        sg.Frame('Labelled Group',[[      
        sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25),      
        sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),      
        sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),      
        sg.Column(column1, background_color='#F7F3EC')]])],      
    [sg.Text('_'  * 80)],      
    [sg.Text('Choose A Folder', size=(35, 1))],      
    [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),      
        sg.InputText('Default Folder'), sg.FolderBrowse()],      
    [sg.Submit(tooltip='Click to submit this window'), sg.Cancel()]    
]      


window = sg.Window('Everything bagel', layout, default_element_size=(40, 1), grab_anywhere=False)      

event, values = window.read()      

window.close()    

sg.popup('Title',      
            'The results of the window.',      
            'The button clicked was "{}"'.format(event),      
            'The values are', values)      
            
"""
# TODO: add parent GUI to select question list (buttons) and display stopwatch

# 質問選択
print("クイ～ズ クイズ、なんのクイズ？")
print("たしざん２： 1 \nひきざん２： 2 ")
quiz_choice = input("クイズをえらんでください： ")
while quiz_choice != "1" and quiz_choice != "2":
    quiz_choice = input("もう１かい、クイズをえらんでください： ")

if quiz_choice == "1":
    question_list = addition2
    print("たしざんのクイズやりましょう～")
else:
    question_list = subtraction2
    print("ひきざんのクイズやりましょう～")

# 順番をランダム可
random.shuffle(question_list)

start_time = time.time()
mistake_count = 0
temp_mistake = 0
count = 0

# code for number pad window

sg.theme('TanBlue')

layout = [[sg.Text('クイ～ズ クイズ！', font=25)],
          [sg.Text(size=(7, 1), key='question'),
           sg.Text(size=(20, 1), key='number', justification='right')],
          [sg.Input(size=(20, 1), font=('Helvetica', 20), key='input'),
           sg.Text(size=(5, 1), key='out')],
          [sg.Button('7'), sg.Button('8'), sg.Button('9')],
          [sg.Button('4'), sg.Button('5'), sg.Button('6')],
          [sg.Button('1'), sg.Button('2'), sg.Button('3')],
          [sg.Button('Submit'), sg.Button('0'), sg.Button('Clear')]]

window = sg.Window('Keypad', layout, default_button_element_size=(10, 2), auto_size_buttons=False, font=20)

# Loop forever reading the window's values, updating the Input field
keys_entered = ''
submit = ''

# TODO: fix display to update with next question after answer

for i in question_list:

    count += 1
    count_text = (str(count) + "/" + str(len(question_list)))
    print(count_text)
    question = (i[0])
    answer = (i[1])

    while True:
        event, values = window.read()  # read the window
        window['question'].update(question)
        window['number'].update(count_text)

        if event == sg.WIN_CLOSED:  # if the X button clicked, just exit
            break
        if event == 'Clear':  # clear keys if clear button
            keys_entered = ''
        elif event in '1234567890':
            keys_entered = values['input']  # get what's been entered so far
            keys_entered += event  # add the new digit
        elif event == 'Submit':
            submit = values['input']
            window['out'].update(submit)  # output the final string
            keys_entered = ''

        window['input'].update(keys_entered)  # change the window to reflect current key string

        if answer == submit:
            window['out'].update(answer+' ◯')
            submit = ''
            break
#            if temp_mistake >= 1:
#                mistake_count += 1
#                temp_mistake = 0
        else:
            window['out'].update('')
#            temp_mistake += 1


# 時間計算
seconds = int(time.time() - start_time)

# 結果発表
print("終わりました、おめでとうございます！")
print("かかった時間：", int(seconds / 60), "分", seconds % 60, "秒")
print("まちがえたしつもん：", mistake_count, "件")
print("明日もがんばりましょう～")

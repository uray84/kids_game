# 算数ゲーム
import random
import time
import PySimpleGUI as sg

# 質問と答えの記入
addition = [["2+9=", "11"], ["3+8=", "11"], ["3+9=", "12"], ["4+7=", "11"],
            ["4+8=", "12"], ["4+9=", "13"], ["5+6=", "11"], ["5+7=", "12"],
            ["5+8=", "13"], ["5+9=", "14"], ["6+5=", "11"], ["6+6=", "12"],
            ["6+7=", "13"], ["6+8=", "14"], ["6+9=", "15"], ["7+4=", "11"],
            ["7+5=", "12"], ["7+6=", "13"], ["7+7=", "14"], ["7+8=", "15"],
            ["7+9=", "16"], ["8+3=", "11"], ["8+4=", "12"], ["8+5=", "13"],
            ["8+6=", "14"], ["8+7=", "15"], ["8+8=", "16"], ["8+9=", "17"],
            ["9+2=", "11"], ["9+3=", "12"], ["9+4=", "13"], ["9+5=", "14"],
            ["9+6=", "15"], ["9+7=", "16"], ["9+8=", "17"], ["9+9=", "18"]]

subtraction = [["11-2=", "9"], ["11-3=", "8"], ["11-4=", "7"], ["11-5=", "6"],
               ["11-6=", "5"], ["11-7=", "4"], ["11-8=", "3"], ["11-9=", "2"],
               ["12-3=", "9"], ["12-4=", "8"], ["12-5=", "7"], ["12-6=", "6"],
               ["12-7=", "5"], ["12-8=", "4"], ["12-9=", "3"], ["13-4=", "9"],
               ["13-5=", "8"], ["13-6=", "7"], ["13-7=", "6"], ["13-8=", "5"],
               ["13-9=", "4"], ["14-5=", "9"], ["14-6=", "8"], ["14-7=", "7"],
               ["14-8=", "6"], ["14-9=", "5"], ["15-6=", "9"], ["15-7=", "8"],
               ["15-8=", "7"], ["15-9=", "6"], ["16-7=", "9"], ["16-8=", "8"],
               ["16-9=", "7"], ["17-8=", "9"], ["17-9=", "8"], ["18-9=", "9"]]

sg.theme('SandyBeach')

layout = [[sg.Text('クイ～ズ クイズ！', font=25, justification='center')],
          [sg.Text('何のクイズ？', font=25, justification='center')],
          [sg.Button('たし算', size=(16, 2), pad=((10, 5), 10)), sg.Button('ひき算', size=(16, 2), pad=((5, 10), 10))],
          [sg.Frame(layout=[
              [sg.Text(size=(7, 1), key='question'),
               sg.Text(size=(7, 1), key='number', justification='right', pad=((150, 5), 5))],
              [sg.Input(size=(22, 2), font=20, key='input', pad=(5, (5, 10))),
               sg.Text(size=(10, 1), key='out', justification='center', pad=(5, (5, 10)), relief=sg.RELIEF_RIDGE)],
              [sg.Button('7'), sg.Button('8'), sg.Button('9')],
              [sg.Button('4'), sg.Button('5'), sg.Button('6')],
              [sg.Button('1'), sg.Button('2'), sg.Button('3')],
              [sg.Button('Submit'), sg.Button('0'), sg.Button('Clear')]
          ], title='クイズ！', pad=(5, 5))]
          ]

main_window = sg.Window('Keypad', layout, default_button_element_size=(10, 2), size=(350, 450),
                        auto_size_buttons=False, font=20, element_justification='c')

keys_entered = ''
submit = ''

question_list = []
count = 0
mistake_count = 0
temp_mistake = 0
start_time = 0
seconds = 0

while True:
    event, values = main_window.read()  # read the window

    if event == sg.WIN_CLOSED:  # if the X button clicked, just exit
        break

    if event == 'たし算':  # choose question list & start timer
        question_list = addition
        start_time = time.time()
    elif event == 'ひき算':
        question_list = subtraction
        start_time = time.time()

    random.shuffle(question_list)

    for i in question_list:

        if event == sg.WIN_CLOSED:  # if the X button clicked, just exit
            break

        count += 1
        if count > len(question_list):
            break
        count_text = (str(count) + "/" + str(len(question_list)))
        print(count_text)
        question = (i[0])
        answer = (i[1])

        main_window['question'].update(question)
        main_window['number'].update(count_text)

        while True:
            event, values = main_window.read()  # read the window

            if event == sg.WIN_CLOSED:  # if the X button clicked, just exit
                break
            if event == 'Clear':  # clear keys if clear button
                keys_entered = ''
            elif event in '1234567890':
                keys_entered = values['input']  # get what's been entered so far
                keys_entered += event  # add the new digit
            elif event == 'Submit':
                if count > len(question_list):
                    break
                submit = values['input']
                main_window['out'].update(submit)  # output the final string
                keys_entered = ''

            main_window['input'].update(keys_entered)  # change the window to reflect current key string

            if event == 'Submit' and submit != answer:
                main_window['out'].update(submit + ' Ｘ')
                temp_mistake += 1

            if answer == submit:
                main_window['out'].update(submit + ' ◯')
                submit = ''
                if temp_mistake >= 1:
                    mistake_count += 1
                    temp_mistake = 0
                break

    if question_list:

        if event == sg.WIN_CLOSED:  # if the X button clicked, just exit
            break

        main_window['question'].update('終わり')
        seconds = int(time.time() - start_time)

        # 結果発表
        sg.popup("終わりました、おめでとうございます！",
                 "かかった時間：" + str(int(seconds / 60)) + "分" + str(seconds % 60) + "秒",
                 "まちがえたしつもん：" + str(mistake_count) + "件",
                 "明日もがんばりましょう～",
                 title='終わり！',
                 font=20)

        # reset quiz
        main_window['out'].update('')
        main_window['number'].update('')
        question_list = []
        count = 0
        mistake_count = 0
        temp_mistake = 0
        start_time = 0
        seconds = 0
        keys_entered = ''
        submit = ''

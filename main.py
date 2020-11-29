# 算数ゲーム
import random
import time
import PySimpleGUI as sg

# 質問と答えの記入
# 足し算
addition = [
    ["2+9=", "11"],    ["3+8=", "11"],    ["3+9=", "12"],    ["4+7=", "11"],
    ["4+8=", "12"],    ["4+9=", "13"],    ["5+6=", "11"],    ["5+7=", "12"],
    ["5+8=", "13"],    ["5+9=", "14"],    ["6+5=", "11"],    ["6+6=", "12"],
    ["6+7=", "13"],    ["6+8=", "14"],    ["6+9=", "15"],    ["7+4=", "11"],
    ["7+5=", "12"],    ["7+6=", "13"],    ["7+7=", "14"],    ["7+8=", "15"],
    ["7+9=", "16"],    ["8+3=", "11"],    ["8+4=", "12"],    ["8+5=", "13"],
    ["8+6=", "14"],    ["8+7=", "15"],    ["8+8=", "16"],    ["8+9=", "17"],
    ["9+2=", "11"],    ["9+3=", "12"],    ["9+4=", "13"],    ["9+5=", "14"],
    ["9+6=", "15"],    ["9+7=", "16"],    ["9+8=", "17"],    ["9+9=", "18"],
]

# 引き算
subtraction = [
    ["11-2=", "9"],    ["11-3=", "8"],    ["11-4=", "7"],    ["11-5=", "6"],
    ["11-6=", "5"],    ["11-7=", "4"],    ["11-8=", "3"],    ["11-9=", "2"],
    ["12-3=", "9"],    ["12-4=", "8"],    ["12-5=", "7"],    ["12-6=", "6"],
    ["12-7=", "5"],    ["12-8=", "4"],    ["12-9=", "3"],    ["13-4=", "9"],
    ["13-5=", "8"],    ["13-6=", "7"],    ["13-7=", "6"],    ["13-8=", "5"],
    ["13-9=", "4"],    ["14-5=", "9"],    ["14-6=", "8"],    ["14-7=", "7"],
    ["14-8=", "6"],    ["14-9=", "5"],    ["15-6=", "9"],    ["15-7=", "8"],
    ["15-8=", "7"],    ["15-9=", "6"],    ["16-7=", "9"],    ["16-8=", "8"],
    ["16-9=", "7"],    ["17-8=", "9"],    ["17-9=", "8"],    ["18-9=", "9"],
]

# 掛け算2～5の段
times2_5 = [
    ["2x1=", "2"],    ["2x2=", "4"],    ["2x3=", "6"],    ["2x4=", "8"],
    ["2x5=", "10"],    ["2x6=", "12"],    ["2x7=", "14"],    ["2x8=", "16"],
    ["2x9=", "18"],    ["3x1=", "3"],    ["3x2=", "6"],    ["3x3=", "9"],
    ["3x4=", "12"],    ["3x5=", "15"],    ["3x6=", "18"],    ["3x7=", "21"],
    ["3x8=", "24"],    ["3x9=", "27"],    ["4x1=", "4"],    ["4x2=", "8"],
    ["4x3=", "12"],    ["4x4=", "16"],    ["4x5=", "20"],    ["4x6=", "24"],
    ["4x7=", "28"],    ["4x8=", "32"],    ["4x9=", "36"],    ["5x1=", "5"],
    ["5x2=", "10"],    ["5x3=", "15"],    ["5x4=", "20"],    ["5x5=", "25"],
    ["5x6=", "30"],    ["5x7=", "35"],    ["5x8=", "40"],    ["5x9=", "45"],
]

# 掛け算6～9の段
times6_9 = [
    ["6x1=", "6"],    ["6x2=", "12"],    ["6x3=", "18"],    ["6x4=", "24"],
    ["6x5=", "30"],    ["6x6=", "36"],    ["6x7=", "42"],    ["6x8=", "48"],
    ["6x9=", "54"],    ["7x1=", "7"],    ["7x2=", "14"],    ["7x3=", "21"],
    ["7x4=", "28"],    ["7x5=", "35"],    ["7x6=", "42"],    ["7x7=", "49"],
    ["7x8=", "56"],    ["7x9=", "63"],    ["8x1=", "8"],    ["8x2=", "16"],
    ["8x3=", "24"],    ["8x4=", "32"],    ["8x5=", "40"],    ["8x6=", "48"],
    ["8x7=", "56"],    ["8x8=", "64"],    ["8x9=", "72"],    ["9x1=", "9"],
    ["9x2=", "18"],    ["9x3=", "27"],    ["9x4=", "36"],    ["9x5=", "45"],
    ["9x6=", "54"],    ["9x7=", "63"],    ["9x8=", "72"],    ["9x9=", "81"],
]

sg.theme("SandyBeach")

layout = [
    [sg.Text("クイ～ズ クイズ！", font=25, justification="center")],
    [sg.Text("何のクイズ？", font=25, justification="center")],
    [
        sg.Button("たし算", size=(16, 2), pad=((10, 5), 10)),
        sg.Button("ひき算", size=(16, 2), pad=((5, 10), 10)),
    ],
    [
        sg.Button("九九2～5", size=(16, 2), pad=((10, 5), 10)),
        sg.Button("九九6～9", size=(16, 2), pad=((5, 10), 10)),
    ],
    [
        sg.Frame(
            layout=[
                [
                    sg.Text(size=(7, 1), key="question"),
                    sg.Text(
                        size=(7, 1),
                        key="number",
                        justification="right",
                        pad=((150, 5), 5),
                    ),
                ],
                [
                    sg.Input(size=(22, 2), font=20, key="input", pad=(5, (5, 10))),
                    sg.Text(
                        size=(10, 1),
                        key="out",
                        justification="center",
                        pad=(5, (5, 10)),
                        relief=sg.RELIEF_RIDGE,
                    ),
                ],
                [sg.Button("7"), sg.Button("8"), sg.Button("9")],
                [sg.Button("4"), sg.Button("5"), sg.Button("6")],
                [sg.Button("1"), sg.Button("2"), sg.Button("3")],
                [sg.Button("Submit"), sg.Button("0"), sg.Button("Clear")],
            ],
            title="クイズ！",
            pad=(5, 5),
        )
    ],
]

# 画面のサイズ
# ボタン追加するとこの「size(350, xxx)」も増やす必要ある
main_window = sg.Window(
    "Keypad",
    layout,
    default_button_element_size=(10, 2),
    size=(350, 500),
    auto_size_buttons=False,
    font=20,
    element_justification="c",
)

keys_entered = ""
submit = ""

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

    if event == "たし算":  # choose question list & start timer
        question_list = addition
        start_time = time.time()
    elif event == "ひき算":
        question_list = subtraction
        start_time = time.time()
    elif event == "九九2～5":
        question_list = times2_5
        start_time = time.time()
    elif event == "九九6～9":
        question_list = times6_9
        start_time = time.time()

    random.shuffle(question_list)

    for i in question_list:

        if event == sg.WIN_CLOSED:  # if the X button clicked, just exit
            break

        count += 1
        if count > len(question_list):
            break
        count_text = str(count) + "/" + str(len(question_list))
        question = i[0]
        answer = i[1]

        main_window["question"].update(question)
        main_window["number"].update(count_text)

        while True:
            event, values = main_window.read()  # read the window

            if event == sg.WIN_CLOSED:  # if the X button clicked, just exit
                break
            if event == "Clear":  # clear keys if clear button
                keys_entered = ""
            elif event in "1234567890":
                keys_entered = values["input"]  # get what's been entered so far
                keys_entered += event  # add the new digit
            elif event == "Submit":
                if count > len(question_list):
                    break
                submit = values["input"]
                main_window["out"].update(submit)  # output the final string
                keys_entered = ""

            main_window["input"].update(
                keys_entered
            )  # change the window to reflect current key string

            if event == "Submit" and submit != answer:
                main_window["out"].update(submit + " Ｘ")
                temp_mistake += 1

            if answer == submit:
                main_window["out"].update(submit + " ◯")
                submit = ""
                if temp_mistake >= 1:
                    mistake_count += 1
                    temp_mistake = 0
                break

    if question_list:

        if event == sg.WIN_CLOSED:  # if the X button clicked, just exit
            break

        main_window["question"].update("終わり")
        seconds = int(time.time() - start_time)

        # 結果発表
        sg.popup(
            "終わりました、おめでとうございます！",
            f"かかった時間：{int(seconds / 60)}分{seconds % 60}秒",
            f"まちがえたしつもん：{mistake_count}件",
            "明日もがんばりましょう～",
            title="終わり！",
            font=20,
        )

        # reset quiz
        main_window["out"].update("")
        main_window["number"].update("")
        question_list = []
        count = 0
        mistake_count = 0
        temp_mistake = 0
        start_time = 0
        seconds = 0
        keys_entered = ""
        submit = ""

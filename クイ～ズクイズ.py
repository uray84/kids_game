# 算数ゲーム
import random
import time
import PySimpleGUI as sg

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
sg.theme('SandyBeach')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
"""


# 質問選択
print("クイ～ズクイズ、なんのクイズ？")
print("たしざん２： 1\nひきざん２： 2")
quiz_choice = input("クイズをえらんでください。 ")
while quiz_choice != "1" and quiz_choice != "2":
    quiz_choice = input("もう１かい、クイズをえらんでください。 ")

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

# 質問・答え確認
for i in question_list:
    count += 1
    print(str(count) + "/" + str(len(question_list)) + ")")
    question = (i[0])
    answer = (i[1])
    guess = input(question)
    while guess != answer:
        print("☓")
        guess = input(question)
        temp_mistake = temp_mistake + 1
    else:
        print("◯\n")
        if temp_mistake >= 1:
            mistake_count = mistake_count + 1
            temp_mistake = 0

# 時間計算
seconds = int(time.time() - start_time)

# 結果発表
print("おわりました、おめでとうございます！")
print("かかったじかん：", int(seconds / 60), "ふん", seconds % 60, "びょう")
print("まちがえたしつもん：", mistake_count, "けん")
print("明日もがんばりましょう～")

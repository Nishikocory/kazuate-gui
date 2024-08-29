import PySimpleGUI as sg
import numpy as np


def start_window(): 
    layout = [
        [sg.Text("任意の整数を入力してね")],
        [sg.InputText()], [sg.Button("OK")]
    ]
    window = sg. Window("スタート画面", layout, resizable=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event =="OK": 
            window.close()
            rule_window()

    window.close()

def rule_window():
    layout = [
        [sg.Text("2.数を推測して入力してね.")],
        [sg.Text("3.間違っていれば、正解の数より大きいか小さいか教えるよ.")],
        [sg.Text("4.少ない試行回数で数を当てよう")],
        [sg.Button("ゲームスタート")]
        ]
    
    window = sg.Window("Rule Explanation", layout, resizable=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "ゲームスタート":
            answer = np.random.randint(1, 101)
            window.close()
            game_window(answer)
        
    window.close()

def game_window(answer):
    warning = ""
    hint = ""
    attempts = 0
    layout = [
        [sg.Text(f"数の推定(1~100):"), sg.Spin(values=list(range(1, 101)), initial_value=1, size=(3, 1))],
        [sg.Text(warning, key="-WARNING-")],
        [sg.Button("Submit")],
        [sg.Text(hint, key="-HINT-")]
    ]
    window = sg.Window("Game in Progress", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event == "Submit":
            try:
                guess = int(values[0])
                if 1 <= guess <= 100:
                    if guess < answer:
                        hint = f"{guess} is lower than the answer.\n" + hint
                        warning = ""
                        attempts += 1
                    elif guess > answer:
                        hint = f"{guess} is higher than the answer.\n" + hint
                        warning = ""
                        attempts += 1
                    else:
                        attempts += 1
                        window.close()
                        break
                        #end_window(answer, attempts)
                else:
                    warning = "Please enter a guess between 1 and 100"

            except ValueError:
                warning = "Your submission is not a valid integer"

        window["-HINT-"].update(hint)
        window["-WARNING-"].update(warning)

    window.close()


start_window()       
rule_window()
game_window()

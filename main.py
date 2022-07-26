import os
from tkinter import *
from tkinter import ttk, messagebox
from functools import partial
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import pyautogui


list_tasks = ["Follow twitter", "Registration button"]
list_profile = []
choise_list_task = []
choise_profile_list = []
message_twiter = []
var_list = []
var_list_1 = []
window = Tk()
select_all_var = IntVar(value=0)
premint = []


with open("config.txt", "r") as file:
    config = file.read()
    config = config.split("=")


PROFILE_DIR = config[0]
CHROME_DRRIVER_PATH = config[1]




def get_acount():
    dirs = next(os.walk(PROFILE_DIR), ([], [], []))[1]
    for elem in dirs:
        if "Profile " in elem:
            list_profile.append(elem)



def run_win_1(list_profile):
    draw_wid(list_profile)
    mainloop()


def draw_wid(list_profile):
    win_1 = LabelFrame(window)
    win_2 = LabelFrame(window)
    mycanvas = Canvas(win_1)
    mycanvas.pack(side=LEFT)
    ysc = ttk.Scrollbar(win_1, orient="vertical", command=mycanvas.yview)
    ysc.pack(side=RIGHT, fill="y")
    mycanvas.configure(yscrollcommand=ysc.set)
    mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))
    myframe = Frame(mycanvas)
    mycanvas.create_window((0, 0), window=myframe, anchor="nw")
    win_1.pack(fill="both", expand="yes", padx=20, pady=20)
    win_2.pack(fill="both", expand="yes", padx=20, pady=20)
    Checkbutton(myframe, variable=select_all_var, text="select all", command=select_all).pack()
    for index, task in enumerate(list_profile):
        var_list.append(IntVar(value=0))
        Checkbutton(myframe, variable=var_list[index],
                    text=task, command=partial(get_profile, index, task)).pack()
    Button(win_2, text="Next", command=next_win).pack()


def select_all():
    if select_all_var.get() == 1:
        for elem in list_profile:
            if elem in choise_profile_list:
                continue
            else:
                choise_profile_list.append(elem)
        print("All profile append")
        print(choise_profile_list)
    else:
        choise_profile_list.clear()
        print(choise_profile_list)


def get_profile(index, task):
    print(f'Selected profile: {task}' if var_list[index].get() == 1 else f'Unselected profile: {task}')
    if var_list[index].get() == 1:
        choise_profile_list.append(task)
    else:
        for elem in choise_profile_list:
            if elem == task:
                choise_profile_list.remove(elem)
    print(choise_profile_list)


def get_tasks(index1, task1):
    print(f'Selected task: {task1}' if var_list_1[index1].get() == 1 else f'Unselected task: {task1}')
    if var_list_1[index1].get() == 1:
        choise_list_task.append(task1)
    else:
        for elem in choise_list_task:
            if elem == task1:
                choise_list_task.remove(elem)
    print(choise_list_task)


def next_win():
    if len(choise_profile_list) == 0:
        messagebox.showinfo(message='Select Profile(s) to continue')
    else:

        window.withdraw()
        second_window = Toplevel()
        win_1 = LabelFrame(second_window)
        win_2 = LabelFrame(second_window)
        mycanvas = Canvas(win_1)
        mycanvas.pack(side=LEFT)
        ysc = ttk.Scrollbar(win_1, orient="vertical", command=mycanvas.yview)
        ysc.pack(side=RIGHT, fill="y")
        mycanvas.configure(yscrollcommand=ysc.set)
        mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))
        myframe = Frame(mycanvas)
        mycanvas.create_window((0, 0), window=myframe, anchor="nw")
        win_1.pack(fill="both", expand="yes", padx=20, pady=20)
        win_2.pack(fill="both", expand="yes", padx=20, pady=20)
        for index1, task1 in enumerate(list_tasks):
            var_list_1.append(IntVar(value=0))
            Checkbutton(myframe, variable=var_list_1[index1],
                        text=task1, command=partial(get_tasks, index1, task1)).pack()
        Button(win_2, text="Next", command=partial(last_win, second_window)).pack()


def last_win(second_window):
    if "Open discord link" in choise_list_task and "Registration button" in choise_list_task:
        messagebox.showinfo(message='You can use either\n"Open discord link" or "Registration button"')
    elif len(choise_list_task) == 0:
        messagebox.showinfo(message='Select task(s) to continue')
    else:
        second_window.withdraw()
        last_window = Toplevel()
        last_window.title("Write premint link")
        win_1 = LabelFrame(last_window)
        win_2 = LabelFrame(last_window)
        mycanvas = Canvas(win_1)
        mycanvas.pack(side=LEFT)
        ysc = ttk.Scrollbar(win_1, orient="vertical", command=mycanvas.yview)
        ysc.pack(side=RIGHT, fill="y")
        mycanvas.configure(yscrollcommand=ysc.set)
        mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))
        myframe = Frame(mycanvas)
        mycanvas.create_window((0, 0), window=myframe, anchor="nw")
        win_1.pack(fill="both", expand="yes", padx=20, pady=20)
        win_2.pack(fill="both", expand="yes", padx=20, pady=20)
        message_twiter_1 = StringVar()
        message_twiter_2 = StringVar()
        message_twiter_3 = StringVar()
        message_twiter_4 = StringVar()
        message_twiter_5 = StringVar()
        message2 = StringVar()
        message3 = StringVar()
        if "Follow twitter" in choise_list_task:
            Label(myframe, text="Write premint link by twitter 1").pack()
            Entry(myframe, textvariable=message_twiter_1).pack()
            Label(myframe, text="Write premint link by twitter 2").pack()
            Entry(myframe, textvariable=message_twiter_2).pack()
            Label(myframe, text="Write premint link by twitter 3").pack()
            Entry(myframe, textvariable=message_twiter_3).pack()
            Label(myframe, text="Write premint link by twitter 4").pack()
            Entry(myframe, textvariable=message_twiter_4).pack()
            Label(myframe, text="Write premint link by twitter 5").pack()
            Entry(myframe, textvariable=message_twiter_5).pack()
        if "Open discord link" in choise_list_task:
            Label(myframe, text="Write premint link by discord").pack()
            Entry(myframe, textvariable=message2).pack()
        if "Registration button" in choise_list_task:
            Label(myframe, text="Write premint link by Registration button").pack()
            Entry(myframe, textvariable=message3).pack()
        Button(win_2, text="Start",
               command=partial(show_message, message_twiter_1, message_twiter_2, message_twiter_3, message_twiter_4,
                               message_twiter_5, message2, message3)).pack()


def show_message(message_twiter_1, message_twiter_2, message_twiter_3, message_twiter_4, message_twiter_5, message2,
                 message3):
    premint.clear()
    if len(message_twiter_1.get()) > 0:
        premint.append(f"twitter:LiNK:{message_twiter_1.get()}")
    if len(message_twiter_2.get()) > 0:
        premint.append(f"twitter:LiNK:{message_twiter_2.get()}")
    if len(message_twiter_3.get()) > 0:
        premint.append(f"twitter:LiNK:{message_twiter_3.get()}")
    if len(message_twiter_4.get()) > 0:
        premint.append(f"twitter:LiNK:{message_twiter_4.get()}")
    if len(message_twiter_5.get()) > 0:
        premint.append(f"twitter:LiNK:{message_twiter_5.get()}")
    if len(message2.get()) > 0:
        premint.append(f"discord:LiNK:{message2.get()}")
    if len(message3.get()) > 0:
        premint.append(f"registration:LiNK:{message3.get()}")
    print(premint)
    start_webdriwer()


def start_webdriwer():
    with open("eroor_register.txt", "a") as file:
        file.write(f"1")
    for task in premint:
        task = str(task).split(":LiNK:")[0]
        if task == "registration":
            print(f"connect to  {task}")
        elif task == "discord":
            print(f"connect to  {task}")
        else:
            print(f"connect to  {task}")

    for profile in choise_profile_list:
            for task in premint:
                link = str(task).split(":LiNK:")[1]
                task = str(task).split(":LiNK:")[0]
                if task == "twitter":
                    options = webdriver.ChromeOptions()
                    options.add_argument("--allow-profiles-outside-user-dir")
                    options.add_argument(f"--profile-directory={profile}")
                    options.add_experimental_option("excludeSwitches", ["enable-automation"])
                    options.add_experimental_option('useAutomationExtension', False)
                    options.add_argument("--disable-blink-features=AutomationControlled")
                    options.add_argument("window-size=1280,800")
                    options.add_argument(
                        "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36")
                    options.add_argument(f"user-data-dir={PROFILE_DIR}")
                    browser = webdriver.Chrome(executable_path=CHROME_DRRIVER_PATH, options=options)
                    print(f"Webdriver use {profile}")
                    print(f"connect to  {task}, {link}")
                    browser.get("chrome://settings/")
                    time.sleep(1)
                    pyautogui.hotkey('ctrl', 'shift', '0')
                    time.sleep(1)
                    browser.get(link)
                    time.sleep(1)
                    try:
                        browser.find_element(by=By.XPATH,
                                             value="/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]/div/div[1]/div").click()
                    except:
                        with open("eroor_twitter.txt", "a") as file:
                            file.write(f"{profile}, {link}\n")
                        pyautogui.hotkey('ctrl', 'shift', '1')
                        browser.quit()
                        continue
                    pyautogui.hotkey('ctrl', 'shift', '1')
                    time.sleep(1)
                    browser.quit()

    for profile in choise_profile_list:
            for task in premint:
                link = str(task).split(":LiNK:")[1]
                task = str(task).split(":LiNK:")[0]
                if task == "discord":
                    options = webdriver.ChromeOptions()
                    options.add_argument("--allow-profiles-outside-user-dir")
                    options.add_argument(f"--profile-directory={profile}")
                    options.add_argument(f"user-data-dir={PROFILE_DIR}")
                    browser = webdriver.Chrome(executable_path=CHROME_DRRIVER_PATH, options=options)
                    print(f"Webdriver use {profile}")
                    print(f"connect to  {task}, {link}")

                    time.sleep(1)
                    browser.get(link)
                    time.sleep(2)

                    browser.find_element(by=By.XPATH,
                                         value="/html/body/div/div/div/div/div/section[2]/div/div/div[1]/div[2]/div[5]/span/a").click()
                    time.sleep(2)
                    print("continue")

    for profile in choise_profile_list:
            with open("eroor_register.txt", "a") as file:
                file.write(f"1")
            for task in premint:
                link = str(task).split(":LiNK:")[1]
                task = str(task).split(":LiNK:")[0]
                if task == "registration":
                        options = webdriver.ChromeOptions()
                        options.add_argument("--allow-profiles-outside-user-dir")
                        options.add_argument(f"--profile-directory={profile}")
                        options.add_argument(f"user-data-dir={PROFILE_DIR}")
                        browser = webdriver.Chrome(executable_path=CHROME_DRRIVER_PATH, options=options)
                        print(f"Webdriver use {profile}")
                        print(f"connect to  {task}, {link}")
                        time.sleep(1)
                        browser.get(link)
                        time.sleep(1)
                        try:
                            browser.find_element(by=By.XPATH, value=
                                    "/html/body/div/div/div/div/div/section[2]/div/div/div[2]/form/div/div[2]/div[6]/div/button").click()
                            time.sleep(2)
                            try:
                                d = browser.find_element(by=By.XPATH, value="/html/body/div/div/div/div/div/section[2]/div/div/div[2]/form/div/div[2]/div[2]/div/text()")
                                if "in your wallet to join this list" in str(d):
                                    with open("eroor_register.txt", "a") as file:
                                        file.write(f"{profile}, {link}, You need at least  ETH in your wallet to join this list\n" )
                            except:
                                browser.quit()
                                continue
                        except:
                            with open("eroor_register.txt", "a") as file:
                                file.write(f"{profile}, {link}" "you need register twiter or discord\n")

                        time.sleep(1)
                        browser.quit()
                        print("continue")


    print("all tasks continue")
get_acount()
run_win_1(list_profile)







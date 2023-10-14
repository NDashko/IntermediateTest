import csv
from datetime import datetime
import os


def delite_note(list_of_list):
    serch = str(input("Введите значение для поиска "))
    for elem in list_of_list:
        if elem.count(serch) > 0:
            print(elem)
            print("Хотите удалить заметку ? ")
            user_choise = str(input("y или n: ")).lower()
            if user_choise == "y":
                list_of_list.remove(elem)
            else:
                break
    return list_of_list


def read_file_note():
    somelist = []
    with open("notebook.csv", "r", newline="") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            somelist.append(row)
    return somelist


def write_in_file(data):
    with open("notebook.csv", "w", encoding="utf - 8", newline="") as f:
        writer = csv.writer(f)
        for elem in data:
            writer.writerow(elem)


def add_note():
    somelist = []
    title = str(input("Введите название заметки: "))
    body = str(input("Введите тело заметки: "))
    datenow = datetime.now()
    dt_string = datenow.strftime("%d/%m/%Y %H:%M:%S")
    somelist.append(dt_string)
    somelist.append(title)
    somelist.append(body)
    return somelist


def start():
    noteList = read_file_note()
    noteList.sort()
    flag = True
    menu()
    while flag:
        menu_choise = str(input("Введите команду: ")).lower()
        if menu_choise == "add":
            temp = add_note()
            noteList.append(temp)
        elif menu_choise == "read":
            print("Number:  Date:   Title:   Body:")
            for i, elem in enumerate(noteList):
                print(i + 1, ":", *elem)
        elif menu_choise == "del":
            delite_note(noteList)
        elif menu_choise == "exit":
            write_in_file(noteList)
            break
    os.system("cls")


def menu():
    print(
        "Добавить заметку введите команду: add\nПосмотреть заметки введите команду: read\nУдалить заметку введите команду: del\nЗакончить работу программы введите команду: exit\n"
    )


start()
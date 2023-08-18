import os
from datetime import datetime
from Note import Note


index = -1
def printArray(arr):
    print()
    for i in range(0, len(arr)):
        outString(arr[i])
        # print("i = ", i)

def outString(n_):
    print(
        "id: ",
        str(n_.id),
        "  ",
        str(n_.date_mark),
        "  ",
        str(n_.time_mark),
        " Заголовок: ",
        str(n_.title),
        "  Заметка: ",
        str(n_.body),
    )


def editNote(arr, item):
    newTitle = input("Введите новое название заголовка: ")
    newBody = input("Введите новый текст заметки: ")
    item.title = newTitle
    item.body = newBody
    arr = rebuildArr(arr)
    return arr


def addNote(arr):
    newTitle = input("Введите заголовок новой заметки: ")
    newBody = input("Введите текст новой заметки: ")
    newDate_mark = (
        str("{:02d}".format(datetime.now().day))
        + "."
        + str("{:02d}".format(datetime.now().month))
        + "."
        + str("{:4d}".format(datetime.now().year))
    )
    newTime_mark = (
        str("{:02d}".format(datetime.now().hour))
        + ":"
        + str(datetime.now().minute)
        + ":"
        + str(datetime.now().second)
    )
    newNote = Note(Note.units_num, newTitle, newBody, newDate_mark, newTime_mark)
    arr.append(newNote)
    arr = rebuildArr(arr)
    return arr


def rebuildArr(arr):
    workId = 0
    for i in range(0, len(arr)):
        arr[i].id = i + 1
    return arr


def findNote(arr):
    index = -1
    print()
    findStr = str(
        input(
            "Введите любую часть содержимого заметки (из любого поля, включая дату или время ), несколько символов: "
        )
    )
    tempStr = ""
    tempArr = []
    for i in range(0, len(arr)):
        tempStr += str(arr[i].id) + " "
        tempStr += arr[i].title + " "
        tempStr += arr[i].body + " "
        tempStr += arr[i].date_mark + " "
        tempStr += arr[i].time_mark + " "

        if findStr.lower() in tempStr.lower():
            tempArr.append(arr[i])
        tempStr = ""

    print()
    if len(tempArr) > 0:
        print("Найдено " + str(len(tempArr)) + " похожих записей:")

        for i in range(0, len(tempArr)):
            print(
                "id: ",
                tempArr[i].id,
                " ",
                tempArr[i].title,
                " ",
                tempArr[i].body,
                " ",
                tempArr[i].date_mark,
                " ",
                tempArr[i].time_mark,
                # " ",
            )
        print()
        findId = input("Введите id нужной заметки (цифра в начале строки): ")
        out = False
        for i in range(0, len(arr)):
            if findId == str(arr[i].id):
                index = i
                break
        if index == -1:
            print("Заметка с таким id не найдена")
            pauseIt()

    else:
        print("Похожих записей не найдено")
        pauseIt()
    return index


def pauseIt():
    str = input("...... press 'Enter', please ...............")

def promptMenu():
    print()
    print("Выберите пункт меню, нажав соответствующую цифру и Enter.")
    print("1. Найти заметку/Изменить заметку/Удалить заметку")
    print("2. Вывести полный список заметок")
    print("3. Добавить новую заметку")
    print("Q/q - Выйти из программы")



def scrollIt():
    for i in range(0, 50):
        print()


def main_Menu(fileContent):
    tempList = list()
    getOut = False  
    while getOut != True:
        scrollIt()
        os.system("CLS")
        printArray(fileContent)

        promptMenu()
        choice = input("Ваш выбор: ")
        choice = choice.lower()
        if choice == "Q" or choice == "q" or choice == "й" or choice == "Й":
            getOut = True
            print()
            print("Дело хозяйское... До новых встреч!")
            print()
        if choice == "1":
            index = findNote(fileContent)
            if index != -1:
                print()
                print(
                    "Выбрана запись: ",
                    "id: ",
                    str(fileContent[index].id),
                    "  ",
                    str(fileContent[index].date_mark),
                    "  ",
                    str(fileContent[index].time_mark),
                    " Заголовок: ",
                    str(fileContent[index].title),
                    "  Заметка: ",
                    str(fileContent[index].body),
                )
                print()
                print("Ведите цифру, соответствующую необходимому действию,")
                print("'1' - Редактировать")
                print("'2' - Удалить")
                print("Клавиша 'Enter' - Выйти из редактирования")
                action = input("Ваш выбор: ")
                print()
                if action == "1":
                    arr = editNote(fileContent, fileContent[index])
                    printArray(fileContent)
                elif action == "2":
                    fileContent.pop(index)
                    rebuildArr(fileContent)
                    printArray(fileContent)
                    print("len(fileContent) = ", len(fileContent))
                elif action == "":
                    getOut = True
                else:
                    print("Что-то пошло не так")
                    pauseIt()
                    break

        if choice == "2":
            printArray(fileContent)

        if choice == "3":
            fileContent = addNote(fileContent)

    return fileContent

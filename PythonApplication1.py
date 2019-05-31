import vk_api
import time
import json
import random
import test
import xlrd, xlwt
import datetime
import os

today = datetime.date.today()
print(datetime.date(today.year, today.month, today.day).isocalendar()[1])


token = os.environ.get("BOT_TOKEN")
vk._auth_token()



rb = xlrd.open_workbook('\Расписание1.xlsx')
sheet = rb.sheet_by_index(0)
val = str(sheet.row_values(0)[1])


print("Старт")

class Subject:
    def __init__(self, weekday, time, tip, name, vid, room, building, prepod):
        self.weekday = weekday
        self.time = time #vid - во сколько пара
        self.tip = tip # чет/нечет
        self.name = name
        self.vid = vid #пр лек л.р.
        self.room = room #ауд
        self.building = building #здание
        self.prepod = prepod #преподаватель


for rownum in range(sheet.nrows):
    Subject(str(int(sheet.row_values(rownum)[0])),str(sheet.row_values(rownum)[1]),str(sheet.row_values(rownum)[2]),str(sheet.row_values(rownum)[3]), 
           str(sheet.row_values(rownum)[4]),str(sheet.row_values(rownum)[5]),str(sheet.row_values(rownum)[6]),str(sheet.row_values(rownum)[7]))
rownum=0
lis=[]

for rownum in range(sheet.nrows):
    new = Subject(str(int(sheet.row_values(rownum)[0])),str(sheet.row_values(rownum)[1]),str(sheet.row_values(rownum)[2]),str(sheet.row_values(rownum)[3]), 
           str(sheet.row_values(rownum)[4]),str(sheet.row_values(rownum)[5]),str(sheet.row_values(rownum)[6]),str(sheet.row_values(rownum)[7]))
    lis.append(new)


#lis = []
#print("Ввод расписания:" )
#name = ""
#while name != "no":
#    name = input("Введите пару")
#    if name == "no":
 #        break
  #  room = input("Введите аудиторию")
   # weekday = input("Введите день недели")
    #teacher = input("Введите препода")
#    vid = input("Введите чет/нечет")
 #   typ = input("Введите вид занятия")
  #  new = Subject(name, room, weekday, teacher, vid, typ)
   # lis.append(new)


str_raspisanie=""
for element in lis:
    str_raspisanie +=  str(element.weekday) + " " +str(element.tip) + " " + str(element.time) + " " + str(element.name) + " " + str(element.room) + "\n"
    
i=0









def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }


keyboard = {
    "one_time": True,
    "buttons": [

        
        [get_button(label="Расписание на завтра", color="positive")],
        [get_button(label="Расписание на сегодня", color="primary")],
        [get_button(label="Вывести расписание", color="primary")],
        [get_button(label="Кнопка 4", color="default")]

    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))


lesson1 ='8:00-9:30'
lesson2 ='9:40-11:10'
lesson3 ='11:20-12:50'
lesson4 ='13:30-15:00'
print(datetime.date(today.year, today.month, today.day).isoweekday()+1)
today = datetime.date.today()
str_raspisanie_tomorrow = ""
lislis=[]

print(str_raspisanie_tomorrow)
while True:
    try:
        #  главный цикл
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]

            str_raspisanie_tomorrow = ""
            if body == "Привет":
                vk.method("messages.send",
                          {"peer_id": id, "message": "Привет, друг!", "random_id": random.randint(1, 2147483647)})
            elif body == "Меню" \
                         "":
                vk.method("messages.send", {"peer_id": id, "message": "Выбери кнопку!", "keyboard": keyboard,
                                            "random_id": random.randint(1, 2147483647)})
            elif body == "Вывести расписание":
                    print("Вывод расписания")
                    vk.method("messages.send",
                              {"peer_id": id, "message": str_raspisanie, "random_id": random.randint(1, 2147483647)})
               # vk.method("messages.send", {"peer_id": id, "message": body, "random_id": random.randint(1, 2147483647)})
                #vk.method("messages.send",
                         # {"peer_id": id, "message": "Ты нажал на кнопку 1", "random_id": random.randint(1, 2147483647)})

                         # str_raspisanie_tomorrow += str(obj.tip) + " " + str(obj.time) + " " + str(obj.name) + " " + str(obj.room) +" " + str(obj.time)+"\n"
            elif body == "Расписание на завтра":
                for obj in lis:
                    if int(obj.weekday) == int(datetime.date(today.year, today.month, today.day).isoweekday()+1):
                        if (str(obj.tip) == "чет/неч" and datetime.date(today.year, today.month, today.day).isocalendar()[1] % 2 ==0):
                            str_raspisanie_tomorrow += "I гр " + str(obj.time) + " " + str(obj.name) + " " + str(int(obj.room)) +"\n"
                        elif (str(obj.tip) == "чет/неч" and not (datetime.date(today.year, today.month, today.day).isocalendar()[1] % 2 ==0)):
                            str_raspisanie_tomorrow += "II гр " + str(obj.time) + " " + str(obj.name) + " " + str(obj.room) +" " +"\n"
                        elif (str(obj.tip) == "неч/чет" and datetime.date(today.year, today.month, today.day).isocalendar()[1] % 2 ==0):
                            str_raspisanie_tomorrow += "II гр " + str(obj.time) + " " + str(obj.name) + " " + str(obj.room) +" " +"\n"
                        elif (str(obj.tip) == "неч/чет" and not (datetime.date(today.year, today.month, today.day).isocalendar()[1] % 2 ==0)):
                            str_raspisanie_tomorrow += "I гр " + str(obj.time) + " " + str(obj.name) + " " + str(obj.room) +" " +"\n"
                        elif (str(obj.tip) == "чет" and datetime.date(today.year, today.month, today.day).isocalendar()[1] % 2 ==0):
                            str_raspisanie_tomorrow += str(obj.vid) + " " + str(obj.time) + " " + str(obj.name) + " " + str(obj.room) +" " + "\n"
                        elif (str(obj.tip) == "неч" and not(datetime.date(today.year, today.month, today.day).isocalendar()[1] % 2 ==0)):
                            str_raspisanie_tomorrow += str(obj.vid) + " " + str(obj.time) + " " + str(obj.name) + " " + str(obj.room) +"\n"
                        else:
                                str_raspisanie_tomorrow += str(obj.tip) + " " + str(obj.time) + " " + str(obj.name) + " " + str(obj.room) +"\n"
                        
                  
                vk.method("messages.send", {"peer_id": id, "message": str_raspisanie_tomorrow, "random_id": random.randint(1, 2147483647)})
                vk.method("messages.send", {"peer_id": id, "message": body, "random_id": random.randint(1, 2147483647)})
                str_raspisanie_tomorrow = ""
                print(str_raspisanie_tomorrow)
            elif body == "Расписание на сегодня":
                str_raspisanie_today = ""
                for obj in lis:
                    if int(obj.weekday) == int(datetime.date(today.year, today.month, today.day).isoweekday()):
                        if (str(obj.tip) == "чет/неч" and datetime.date(today.year, today.month, today.day).isocalendar()[1] % 2 ==0):
                            str_raspisanie_today += "I гр " + str(obj.time) + " " + str(obj.name) + " " + str(int(obj.room)) +"\n"
                        elif (str(obj.tip) == "чет/неч" and not (datetime.date(today.year, today.month, today.day).isocalendar()[1] % 2 ==0)):
                            str_raspisanie_today += "II гр " + str(obj.time) + " " + str(obj.name) + " " + str(obj.room) +" " +"\n"
                        elif (str(obj.tip) == "неч/чет" and datetime.date(today.year, today.month, today.day).isocalendar()[1] % 2 ==0):
                            str_raspisanie_today += "II гр " + str(obj.time) + " " + str(obj.name) + " " + str(obj.room) +" " +"\n"
                        elif (str(obj.tip) == "неч/чет" and not (datetime.date(today.year, today.month, today.day).isocalendar()[1] % 2 ==0)):
                            str_raspisanie_today += "I гр " + str(obj.time) + " " + str(obj.name) + " " + str(obj.room) +" " +"\n"
                        elif (str(obj.tip) == "чет" and datetime.date(today.year, today.month, today.day).isocalendar()[1] % 2 ==0):
                            str_raspisanie_today += str(obj.vid) + " " + str(obj.time) + " " + str(obj.name) + " " + str(obj.room) +" " + "\n"
                        elif (str(obj.tip) == "неч" and not(datetime.date(today.year, today.month, today.day).isocalendar()[1] % 2 ==0)):
                            str_raspisanie_today += str(obj.vid) + " " + str(obj.time) + " " + str(obj.name) + " " + str(obj.room) +"\n"
                        else:
                                str_raspisanie_today += str(obj.tip) + " " + str(obj.time) + " " + str(obj.name) + " " + str(obj.room) +"\n"
                vk.method("messages.send", {"peer_id": id, "message": body, "random_id": random.randint(1, 2147483647)})
                vk.method("messages.send", {"peer_id": id, "message": str_raspisanie_today, "random_id": random.randint(1, 2147483647)})
            elif body == "Четверг":
                vk.method("messages.send", {"peer_id": id, "message": body, "random_id": random.randint(1, 2147483647)})
                for obj in lis:
                    print(obj.name, " ", obj.room)
                    vk.method("messages.send",
                              {"peer_id": id, "message": obj.name + " " + obj.room, "random_id": random.randint(1, 2147483647)})
            elif body == "Начать":
                vk.method("messages.send",
                          {"peer_id": id, "message": "Начинаем, друг!", "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send",
                          {"peer_id": id, "message": "Я не понял тебя!", "random_id": random.randint(1, 2147483647)})
        time.sleep(0.5)
    except Exception as E:
        time.sleep(1)

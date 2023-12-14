from hub import Hub
from item import Item


item1 = Item("песок","для строительных работ",2000, "2021-11-12")
item2 = Item("ананас","мрок хранения 3 дня",1500, "2020-07-11")
item3 = Item("мороженое","хранить при низкой температуре",1200, "2023-07-12")
item4 = Item("альбом","не мять",2000, "2023-12-12")
item5 = Item("клевер","сушеный",1500, "2019-11-01")
item6 = Item("процессор","хрупкий",1200, "2022-09-12")

item5.add_tags(["липкий","хрупкий"])
item3.add_tags(["хрупкий","липкий","тяжелый"])
item4.add_tags(["тяжелый","липкий"])


hub = Hub()
hub.date = "2020-12-19"
hub.add_item(item1)
hub.add_item(item5)
hub.add_item(item2)
hub.add_item(item4)
hub.add_item(item3)
hub.add_item(item6)

# print(Hub.get_items)
# print(hub.find_by_id(4))
# print(hub.find_by_tags(["хрупкий","липкий"]))
# print(hub.get_items)
# print(hub.find_most_valuable(5))


print(hub.find_by_date("2021-12-12"))
A = list()
for i in hub.get_items()[:]:
    if i.get_name()[0] == "а":
        hub.rm_item(i)
        A.append(i)
print(A)
Outdated = list()
for i in hub.get_items():
    if hub.date > i.get_date():
        hub.rm_item(i)
        Outdated.append(i)
print(Outdated)
MostValuable = hub.find_most_valuable(10)
for i in MostValuable:
    hub.rm_item(i)
print(MostValuable)
print(hub.get_items())
Others = []
for i in hub.get_items():
    Others.append(i)
print(Others)

















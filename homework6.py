my_dict = {"Ilya": 333, "Dmitriy": 989, "Alex": 123}
print(my_dict)
print(my_dict.get("Alex"))
print(my_dict.get("Lola", "Такого ключа нет"))
my_dict.update({"Lola": 545, "Denis": 876})
del my_dict["Ilya"]
print(my_dict)
my_set = {8, "Илья", "Голова", 8, 9, 4, "Рука", "Илья", True, 8, True}
print(my_set)
my_set.update({"Нога", "Конечности"})
print(my_set)
my_set.remove(1)
print(my_set)

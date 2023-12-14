from hub import Hub
from item import Item
import unittest


class TestHubSingleton(unittest.TestCase):
    def setUp(self):
        self.hub1 = Hub()
        self.hub2 = Hub()
        self.item3 = Item("мороженое", "хранить при низкой температуре", 1200, "2023-07-12")
        self.item4 = Item("альбом", "не мять", 2000, "2023-12-12")
        self.item5 = Item("клевер", "сушеный", 1500, "2019-11-01")
        self.hub1.add_item(self.item5)
        self.hub1.add_item(self.item3)
        self.hub1.add_item(self.item4)
        
    def tearDown(self):
        self.hub1.clear()
        self.hub2.clear()
    
    def test_hub_singleton(self):
        'Проверка того что hub - синглтон'
        self.assertTrue(self.hub1 is self.hub2)


    def test_len(self):
        'Проверка того что при добавлении предметов меняется значение len(item)'
        self.hub1.add_item(Item("Товар", "Описание",2500, "2022-09-12"))
        self.assertEqual(len(self.hub1), 4)
        
    def test_rm_item(self):
        'Проверка того метод удаляет item с id=i если i это число, или удаляет item=i если i это Item'
        self.hub1.rm_item('item5')
        self.hub1.rm_item('2')
        i = self.hub1.get_items()
        h = [self.item4]
        self.assertEqual(i,h)
        
    def test_find_by_date(self):
        'Проверка того что метод возвращает лист всех Item, подходящих по дате'
        self.hub1.find_by_date("2018-08-15","2020-08-15")
        i = self.hub1.get_items()
        h = [ self.item5]
        self.assertEqual(i, h)
        
    def test_find_by_date(self):
        'Проверка того что метод возвращает лист всех Item, подходящих по промежутку дат'
        self.hub1.find_by_date("2023-07-12")
        i = self.hub1.get_items()
        h = [self.item3, self.item5]
        
    def test_find_by_tags(self):
        'Проверка того что в отбираются item содержащие все введенные теги'
        self.item5.add_tags(["липкий", "хрупкий"])
        self.item3.add_tags(["хрупкий", "липкий", "тяжелый"])
        self.item4.add_tags(["тяжелый", "липкий"])
        h = self.hub1.find_by_tags(["липкий", "хрупкий"])
        i = [self.item5, self.item3]
        self.assertEqual(h,i)
        
    def test_find_most_valuable(self):
        'Проверка того что возвращаются самые дорогие предметы на складе'
        i = self.hub1.find_most_valuable(2)
        h = [self.item4,self.item5]
        self.assertEqual(i, h)
    

class TestItem(unittest.TestCase):
    def setUp(self):
        self.item1 = Item("песок", "для строительных работ", 2000, "2021-11-12")
        self.item2 = Item("ананас", "cрок хранения 3 дня", 1500, "2020-07-11")
       
    def test_item_id(self):
        'Проверка того что у разных Items разные id'
        self.assertTrue(self.item1.get_id != self.item2.get_id)

    def test_len(self):
        'Проверка того что при добавлении тэгов меняется значение len(item)'
        self.item1.add_tag("сыпучий")
        self.assertNotEqual(self.item1.__len__(), self.item2.__len__())


    def test_equal_tags(self):
        'Проверка того что если к предмету добавить два идентичных тега - их колчество будет один'
        self.item1.add_tag("сыпучий")
        self.item1.add_tag("сыпучий")
        self.assertTrue(self.item1.__len__() == 1)




if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
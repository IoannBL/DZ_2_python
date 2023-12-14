from datetime import date, datetime
from item import Item

class Hub:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
            cls._items = []
            cls._date = None
        return cls._instance
    
    def add_item(self, item):
        if isinstance(item, Item):
            self._items.append(item)
        else:
            raise ValueError("item не является экземпляром класса Item или его подкласса.")
    def __repr__(self):
        return f"{self._items[:3:]}"
    
    
    def __len__(self):
        return len(self._items)
    
    def __getitem__(self, item):
        return self._items[item]
    
    def find_by_id(self, item_id):
        for pos, item in enumerate(self._items):
            if item_id == item._id:
                return pos, item
        return -1, None
    
  
    def find_by_tags (self, tags):
        result = []
        for item in self._items:
            if item.is_tagged(tags):
                result.append(item)
        return result
    
    def rm_item(self, i):
        for id, item in enumerate(self._items):
            if isinstance(i, int) and i == id:
                self._items.remove(item)
                break
            if isinstance(i, str) or i == item:
                self._items.remove(item)
                break
    
    def drop_items(self, *items):
        new_items = []
        for i in self._items:
            if i not in items:
                new_items.append(i)
        self._items = new_items
    
    def clear(self):
        return self._items.clear()
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, hub_date):
        self._date = datetime.strptime(hub_date, "%Y-%m-%d").date()
    
    def find_by_date(self, *args):
        if len(args) == 1:
            search_date_str = args[0]
            search_date = datetime.strptime(search_date_str, "%Y-%m-%d").date()
            matching_items = []
            for item in self._items:
                if item.get_date() <= search_date:
                    matching_items.append(item)
            return matching_items
        elif len(args) == 2:
                start_date_str, end_date_str = args
                start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
                end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
                matching_items = []
                for item in self._items:
                    if start_date <= item.get_date()  <= end_date:
                        matching_items.append(item)
                return matching_items
        else:
            raise ValueError("Передано неверное количество аргументов")
    def find_most_valuable(self, amount=1):
        sorted_items = sorted(self._items, key=lambda item: item.cost, reverse=True)
        
        return sorted_items[:amount]
    
    def get_items(self):
        return self._items
    
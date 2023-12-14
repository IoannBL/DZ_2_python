from datetime import date,datetime
class Item:
    id_count = 0
    def __init__(self, name, desc,cost, item_date):
        self._id = Item.id_count
        Item.id_count += 1
        self._name = name
        self._desc = desc
        self._tags = set()
        self._cost = cost
        self._date = datetime.strptime(item_date, "%Y-%m-%d").date()

    def add_tag(self,tag):
        self._tags.add(tag)

    def remove_tag(self,*args,**kwargs):
        self._tags.remove()

    def __repr__(self):
         return f"{self._id},{self._name},{list(self._tags)[:3]},{self._cost},{self._date}"
    
    def __str__(self):
        return f"{self._name}"
    

    def __len__(self):
        return len(self._tags)

    def is_tagged(self,tag):
        if isinstance(tag, str):
            return tag in self._tags
        elif isinstance(tag, list):
            return set(tag).issubset(self._tags)
        else:
            return False
    # def is_tagged(self, tag):
    #     return tag in self._tag


    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost):
        self._cost = cost

    def __abs__(self):
        return abs(self._cost)

    def __lt__(self, other):
        return abs(self) < abs(other)
    
    def add_tags(self,tags):
        self._tags.update(tags)

    def rm_tags(self,tags):
        self._tags.difference_update(tags)

    def copy(self):
        return (Item(self._name, self._tags, self._cost, self._desc, self._date))
    
    def get_date(self):
        return self._date
    
    def get_name(self):
        return self._name
    
    def get_id(self):
        return self._id
    
    def get_tags(self):
        return self._tags
    
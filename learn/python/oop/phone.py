from item import Item
# below is how you use inheritance, by inherting Item
class Phone(Item):
    # ins_list = [] child can access the parent instances so it is not needed
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # calling super function to access parents attributes
        super().__init__(name, price, quantity)
        assert broken_phones>=0 , f"Broken Phones {broken_phones} needs to be greater than or equal to 0"

        # assign class attribute assignment dynamically using below statements
        self.broken_phones = broken_phones
        
        # append instance to all
        # Phone.ins_list.append(self)
        

# p1 = Phone('Ph10',500,5,1)
# print(Item.ins_list)
# print(Phone.ins_list)
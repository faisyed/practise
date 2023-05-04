# Notes:
# 1. Attributes accessible only within the single instance are called instance attributes
# 2. Attributes that are accessible across instances are called global/class attributes 
# 3. When to use static method?
# Ans: Static method should do something that has a relationship with the class, but not something that must be unique per instance
# 4. When to use class method?
# Ans: Whenever you are trying to create an instances of a class then u can use class method/ manipulate different structures of data to instantiate objects
# 5. static and class methods can be also called from instances as well, but very rarely seen
# 6. attribuites can be made protected by prefix one _ before attribute name and private by using two _ before attribute name
# 7. Encapsulation is used to restrict direct access to attributes of class
# 8. Abstraction is used to hide methods can be made private by prefixing two _ before name 


# creating the item class
class Item:
    # defining class attributes as below
    pay_rate = 0.8

    # to get list of all instances created till now
    ins_list = []

    # default constructor: called when an instance of class is created
    # to mandate the type of the parameter we can use : and the type
    # if default value is already assign then the type is mandated internaly, which means quantity need to be a number and cannot be a string
    def __init__(self, name: str, price: float, quantity=0):
        # assert can be used to provide validations on the input, for e.g, price and quantity cannot be negative
        # if above validation fails then we get AssertionError
        # assert error message can be customized by giving error message after ,
        assert price>=0 , f"Price {price} needs to be greater than or equal to 0" 
        assert quantity>=0 , f"Quantity {quantity} needs to be greater than or equal to 0"

        # assign class attribute assignment dynamically using below statements
        self.__name = name
        self.price = price
        self.quantity = quantity
        
        # append instance to all
        Item.ins_list.append(self)
    
    # creating getter
    # Property-Decorator = Read-only attribute
    @property
    def name(self):
        return self.__name
    
    # creating setter, where name is the getter name
    @name.setter
    def name(self, value):
        self.__name = value 

    def calculate_total_price(self):
        # this is how methods can access the attributes of an instance.
        return self.price*self.quantity
    
    def apply_discount(self):
        # self.price = self.price * pay_rate we cannot access class attribute like this instead use
        self.price = self.price * self.pay_rate
    
    # to define class method use decorators, class methods are called to creates instance, cls will be class
    @classmethod
    def instantiate_from_csv(cls):
        # read csv and store them in a list such as items
        items = []
        # to create instances
        for item in items:
            Item(
                name=item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )
    
    # to define static method use decorators
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
    
    # to represent the object of instance when retreived u can customize using repr
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})" # can be anything you want better to give something to uniquely identify them

# problem with below set of statements is we have to always hardcode the parameters after creating a class instance. To overcome this we use constructors
# it1 = Item()
# it1.name = "Phone"
# it1.price = 100
# it1.quantity = 5
# print(it1.calculate_total_price(it1.price, it1.quantity))
# it2 = Item()
# it2.name = "Laptop"
# it2.price = 1000
# it2.quantity = 3
# print(it1.calculate_total_price(it2.price, it2.quantity))

# it1 = Item("Phone", 100, 1)
# it2 = Item("Laptop", 1000, 3)
# print(it1.name)
# print(it2.name)
# print(it1.price)
# print(it2.price)
# print(it1.quantity)
# print(it2.quantity)

# We can still update attributes of an instance of class using
# it1.quantity = 10
# print(it1.quantity)

# accessing class attributes
# print(Item.pay_rate) # through class name
# print(it1.pay_rate) # through instances
# print(it2.pay_rate) # through instances

# to get all the attributes of an instance use __dict__
# print(Item.__dict__) # class level attributes
# print(it1.__dict__) # instance level attribute

# to change instance attribute using class attribute
# it1.apply_discount()
# print(it1.price)

# we can change the class attribute value for a single instance
# it2.pay_rate = 0.7
# it2.apply_discount()
# print(it2.price) # you must have seen 0.8 still that happens because in apply_discount we use Item.pay_rate instead use self.pay_rate to get correct results

# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)
# print(Item.ins_list)
# to access attributes of all instance
# for instance in Item.ins_list:
#     print(instance.name)

# class method can be accessed as
# Item.instantiate_from_csv()
# print(Item.ins_list)

# static method can be accessed as
# print(Item.is_integer(10.0))




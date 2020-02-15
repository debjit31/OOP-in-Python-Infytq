from abc import ABCMeta, abstractmethod
class Product(metaclass=ABCMeta):
    @abstractmethod
    def return_policy(self):
        pass

class Shoe(Product):
    def return_policy(self):
        print('Shoes must be returned within 7 days of purchase!!!')

class Mobile(Product):
    def return_policy(self):
        print('Mobiles must be returned within 1 month of purchase!!!!')

class Furniture(Product):
    def return_policy(self):
        print('Furnitures must be returned within 15 days of purchase!!!')

if __name__ == '__main__':
    s = Shoe()
    s.return_policy()
    m = Mobile()
    m.return_policy()
    f = Furniture()
    f.return_policy()
    
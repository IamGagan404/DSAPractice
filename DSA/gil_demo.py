# import time,random
# import datetime
# from threading import Thread
# from multiprocessing import Process



# def count(n):
#     while n > 0:
#         n -= 1
#     # time.sleep(2)

# n = 50_000_000_0

# def get_threding():
#     t1 = Thread(target=count,args=(n,))
#     t2 = Thread(target=count,args=(n,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()

# def get_processing():
#     p1 = Process(target=count,args=(n,))
#     p2 = Process(target=count,args=(n,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()

# if __name__ == '__main__':
#     t1 = datetime.datetime.now()
#     count(n)
#     count(n)
#     t2 = datetime.datetime.now()
#     print(t2-t1)
#     t1 = datetime.datetime.now()
#     get_threding()
#     t2 = datetime.datetime.now()
#     print(t2-t1)
#     t1 = datetime.datetime.now()
#     get_processing()
#     t2 = datetime.datetime.now()
#     print(t2-t1)




from abc import ABC, abstractmethod

# ABSTRACTION: hides implementation, defines a contract
class Payment(ABC):
    @abstractmethod
    def pay(self, amount): ...

# ENCAPSULATION: data is hidden behind methods
class Wallet:
    def __init__(self, balance):
        self.__balance = balance          # name-mangled, "private"

    @property
    def balance(self):                    # controlled read access
        return self.__balance

    def deduct(self, amount):             # controlled write access
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

class CardPayment(Payment):
    def pay(self, amount): print(f"Paid {amount} by card")

class UpiPayment(Payment):
    def pay(self, amount): print(f"Paid {amount} via UPI")

# POLYMORPHISM: same interface, different behavior
def checkout(method: Payment, amount):
    method.pay(amount)

checkout(CardPayment(), 500)   # Paid 500 by card
checkout(UpiPayment(), 500)    # Paid 500 via UPI

w = Wallet(1000)
w.deduct(300)
print(w.balance)               # 700
# Payment()  -> TypeError: can't instantiate abstract class




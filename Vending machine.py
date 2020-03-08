class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def updateStock(self, stock):
        self.stock = stock

    def buyFromStock(self):
        if self.stock == 0:
            # raise not item exception
            pass
        self.stock -= 1

class VendingMachine:
    def __init__(self):
        self.amount = 0
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def showItems(self):
        print('\nitems available \n***************')

        for item in self.items:      
            if item.stock == 0:
                self.items.remove(item)
        for item in self.items:
            print(item.name, item.price)

        print('***************\n')

    def addCash(self, money):
        self.amount = self.amount + money

    def buyItem(self, item):
        if self.amount < item.price:
            print('You can\'t but this item. Insert more coins.')
        else:
            self.amount -= item.price
            item.buyFromStock()
            print('You got ' +item.name)
            print('Your Change is: ' + str(self.amount))

    def containsItem(self, wanted):
        ret = False
        for item in self.items:
            if item.name == wanted:
                ret = True
                break
        return ret

    def getItem(self, wanted):
        ret = None
        for item in self.items:
            if item.name == wanted:
                ret = item
                break
        return ret

    def insertAmountForItem(self, item):
        price = item.price
        while self.amount < price:
                self.amount = self.amount + float(input('insert ' + str(price - self.amount) + ': '))

    def checkRefund(self):
        if self.amount > 0:
            print(self.amount + " refunded.")
            self.amount = 0

        print('Thank you, have a nice day!\n')


def vend():

    machine = VendingMachine()
    item1 = Item('choc',  1.5,  2)
    item2 = Item('pop', 2.5,  1)
    item3 = Item('chips',  2.0,  3)
    item4 = Item('gum',  0.50, 1)
    item5 = Item('mints',1.0,  3)
    machine.addItem(item1)
    machine.addItem(item2)
    machine.addItem(item3)
    machine.addItem(item4)
    machine.addItem(item5)

    print('Welcome to the vending machine!\n***************')

    continueToBuy = True
    while continueToBuy == True:
        machine.showItems()
        selected = input('select item: ')
        if machine.containsItem(selected):
            item = machine.getItem(selected)

            machine.insertAmountForItem(item)
            machine.buyItem(item)

            a = input('buy something else? (y/n): ')
            if a == 'n':
                continueToBuy = False
                machine.checkRefund()
            else:
                continue

        else:
            print('Item not available. Select another item.')
            continue

vend()

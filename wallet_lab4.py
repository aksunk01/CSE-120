# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 08:59:23 2023

@author: aksun
"""

class Currency():
    def __init__(self,u,v):
        self.unit = u
        self.value = v
        
class Bill(Currency):
    def __init__(self, v):
        super().__init__('dollar', v)
    def printCurrency(self):
        print(self.value, self.unit,'bill')
        
class Coins(Currency):
    def __init__(self,v):
        super().__init__('cent',v)
    def printCurrency(self):
        print(self.value,self.unit,'coin')
class Wallet():
    def __init__(self,a):
        self.amount = a
        self.currency = []
        self.setCurrency()
    
    def setCurrency(self):
        values = [100,50,20,10,5,2,1,0.5,0.25,0.10,0.05,0.01]
        
        a = self.amount
        
        for v in values:
            while a >= v:
                a = round(a-v,2)
                
                if v>=1:
                    self.currency.append(Bill(v))
                else:
                    self.currency.append(Coins(int(100*v)))
    def printWallet(self):
        for c in self.currency:
            c.printCurrency()

if __name__ == '__main__':
    a = round(float(input("How much money is in your wallet? ")),2)
    wallet = Wallet(a)
    wallet.printWallet()
    
    
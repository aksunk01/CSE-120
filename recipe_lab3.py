# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 13:54:56 2023

@author: aksun
"""

if __name__ == '__main__':
    salad = {'lettuce', 'tomato', 'carrots', 'dressing', 'croutons'}
    sandwhich = {'lettuce', 'onion', 'pickles','tomato', 'bread'}
    
    ingredients = set()
    new = ''
    
    
    while True:
        new = input('\nEnter an ingredient (if done, type done): ')
        if(new == 'done'):
            break
        else:
            ingredients.add(new)
    
    if(ingredients.intersection(salad) == salad and ingredients.intersection(sandwhich) == sandwhich):
        print("You can make both a Salad and a Sandwich")
    elif(ingredients.intersection(salad) == salad):
        print("You can make a Salad")
    elif(ingredients.intersection(sandwhich) == sandwhich):
        print("You can make a Sandwich")
    else:
        print("You can make neither")
        
    
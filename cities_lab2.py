# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 09:01:18 2023

@author: aksun
"""

if __name__ == "__main__":
    cities = ['Tokyo','Dehli', 'Shanghai', 'Sao Paulo', 'Mexico City', 'Cairo', 'Mumbai', ' Beijing', 'Dhaka', 'Osaka', 'New York', 'Karachi', 'Buenos Aires', 'Istanbul']
    
    
    city = input("\nEnter the city name: ")
    print("The cities smaller than",city,"are:")
    citys = cities.index(city)
    
    for i in range(citys+1,len(cities)):
        print(cities[i])
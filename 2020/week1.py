import sys
import os
import random

def GenerateRandomID(range):
    return random.randrange(range)

def GenerateIDs(n):
    
    list = []
    i = 0
    while i < n:
        list.append(GenerateRandomID(32000))
        i += 1
        
    return list
    
def DuplicateIDs(array):
    
    list = array[:] #create local copy that is immutable
    
    for id in list:
        array.insert(GenerateRandomID(len(array)-1), id)
        
    return array
    
def GenerateDeliveryOrders():
    
    array = GenerateIDs(99)
    array = DuplicateIDs(array)
    array.insert(GenerateRandomID(len(array)-1), GenerateRandomID(32000))
    
    return array

def GetStaticArray():
    return [8636, 3316, 18248, 20712, 29649, 12014, 28050, 26729, 24623, 26483, 557, 11895, 21257, 18281, 15106, 4171, 7560, 30544, 8056, 15102, 15106, 122, 9551, 14557, 10822, 28050, 29306, 5315, 3032, 8254, 16599, 3032, 19065, 5276, 8664, 7764, 557, 24621, 4415, 22744, 16506, 6814, 9551, 3156, 9512, 4369, 25467, 24621, 26360, 3156, 20743, 50, 10973, 10840, 29159, 29159, 5423, 21629, 21629, 3251, 12014, 8636, 20743, 22493, 8303, 11312, 22318, 27217, 24098, 4532, 23247, 30052, 20712, 10973, 22493, 28715, 18669, 10822, 6814, 3101, 11921, 4394, 24261, 19937, 13691, 3059, 8254, 16867, 12731, 5315, 20148, 23204, 3059, 27261, 29306, 9358, 18011, 24623, 10182, 10182, 5815, 7330, 15102, 26729, 12919, 30572, 7629, 18929, 30544, 11312, 18011, 1677, 19937, 28173, 23531, 8836, 7560, 16867, 10143, 16506, 3316, 29649, 8303, 24814, 4171, 8664, 26360, 4415, 50, 455, 29973, 14557, 4369, 25444, 29983, 8056, 25467, 30572, 8836, 21335, 13691, 16599, 4394, 27261, 18669, 25444, 10143, 28715, 5423, 18248, 19615, 31706, 10708, 5276, 22318, 11637, 24814, 21257, 26483, 7764, 5123, 23531, 9358, 20148, 18929, 30603, 24261, 5123, 4532, 3101, 22744, 29973, 27217, 7330, 3251, 23204, 29983, 24098, 11921, 1677, 11637, 455, 23247, 31706, 122, 9512, 10840, 12731, 19615, 7629, 10708, 30603, 21335, 28173, 30052, 11895, 5815, 18281, 12919]
    
def FindUnique(array):

    #define dictionary to track unique ids
    returned_orders = {}
    
    for order in array:
        if order in returned_orders:
            returned_orders[order] = True
        else:
            returned_orders[order] = False
    
    for id in returned_orders:
        if returned_orders[id] == False:
            return id

def main():

    #array = GenerateDeliveryOrders()
    array = GetStaticArray()
    missing_drone = FindUnique(array)
    print ("Missing drone delivery ID: {}".format(missing_drone))
    
if __name__=="__main__":main()
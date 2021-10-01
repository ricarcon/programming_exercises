
def max_duffel_bag_value(tuples, num):
    
    temp = []
    
    #first we'll take a look at which single cake has the highest value if we took just one type of cake
    for entry in tuples:
        
        weight, value = entry
        count = int(num/weight)
        temp.append((weight, count * value))
    
    #sort by the total value in desc order
    ordered = sorted(temp, key=lambda x: x[1], reverse=True)
    
    
    #here's where we track how many of each to take
    map = {}
    
    #we maximize by subtracting the most cakes from the total weighted value and get more of the cakes we can get from the other types
    remainder = num
    
    for ordered_entry in ordered:
        
        weight, value = ordered_entry
        
        done = False
        count = 0
        
        while not done:
            if remainder >= weight:
                remainder -= weight
                count += 1
            else:
                done = True
                
        map[weight] = count
    
    total_value = 0
    for entry in tuples:
        total_value += map[entry[0]] * entry[1]
    
    return (map, total_value)

def main():
    cake_tuples = [(7, 160), (3, 90), (2, 15)]
    capacity    = 20
    result = max_duffel_bag_value(cake_tuples, capacity)
    
    print("Max value: {}".format(result[1]))
    print("By getting cakes:")
    cake_map = result[0]
    for cake in cake_map:
        
        if cake_map[cake] != 0:
            print("\tCake of weight {}: {}".format(cake, cake_map[cake]))
    
if __name__=="__main__":main()
#lane1_flag = 0
#lane2_flag = 0 
#lane3_flag = 0
#lane4_flag = 0

# numBikes1[] = number of bikes in lane 1
# numBikes2[] = number of bikes in lane 2
# numBikes3[] = number of bikes in lane 3
# numBikes4[] = number of bikes in lane 4

def bike_count(numBikes1, numBikes2, numBikes3, numBikes4):
    bikes = [len(numBikes1), len(numBikes2), len(numBikes3), len(numBikes4)]
    max_bikes = max(bikes)
    
    # If multiple lanes have the same number of bikes
    if bikes.count(max_bikes) > 1:
       max_index = max(i for i, length in enumerate(lengths) if length == max_length)
        if max_index == 0:
            lane1_flag = 1
        elif max_index == 1:
            lane2_flag = 1
        elif max_index == 2:
            lane3_flag = 1        
        elif max_index == 3:
            lane4_flag = 1    
                 
    if len(numBikes1) == max_bikes:
        lane1_flag = 1
    elif len(numBikes2) == max_bikes:
        lane2_flag = 1
    elif len(numBikes3) == max_bikes:
        lane3_flag = 1
    elif len(numBikes4) == max_bikes:
        lane4_flag = 1

# reduce():

from functools import reduce

rain_water = [1,2,3,4,5]

def collector(bucket,water):
    print(bucket,water)
    return bucket + water
    
print(reduce(collector,rain_water,0))    


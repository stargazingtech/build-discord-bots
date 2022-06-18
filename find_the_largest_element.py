import random, time


start_time1 = time.time()

random_list1 = []
for x in range(0, 20):
    random_list1.append( random.randint(0, 100) )
finish_time1 = time.time()

print(random_list1, "time to finsh", finish_time1 - start_time1)

start_time2 = time.time()
random_list2 = random.sample( range(0,100), 10 )
finish_time2 = time.time()
print(random_list2, "time to finish = %e"%(finish_time2-start_time2) )

string = "I am string"
list = ["I am string", "I am string 2", 3]

print( "string[0] = ", string[0], "list[0] = ", list[0] )

#
# The Question: to find the largest value and its position in a list
#
#  Step 1: initialize a valuable, largest_value, to be the first item of the list
#  Step 2: compare largest_value with the next item in the list
#

largest_value    = random_list1[0]
index_of_largest = 0

for x in range(1, len(random_list1)):
    print("iteration %d:  let's compare the current value, %d, with largest_value = %d"%(x, random_list1[x], largest_value) )
    if( random_list1[x] > largest_value ):
        largest_value = random_list1[x]
        index_of_largest = x
        print("\tfound another larger value: %d, which is the %dth item"%(random_list1[x], x) )

print( "largest_value = %d, index_of_largest = %d"%(largest_value, index_of_largest) )


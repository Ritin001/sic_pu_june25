import random as rand
#any number between 0 and 1
print(rand.random())

#few data from randoly from list
data=[1,2,3,4,5,6,7,8,9]
print(rand.sample(data,6))

#random choice
print(rand.choice(data))

#between any range
print(rand.uniform(1,5))

#any int value between range
print(rand.randint(1,100))

# random value of range step value
print(rand.randrange(0,100,2))

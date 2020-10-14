class IceCream(object):
    def __init__(self, flavor, numScoops, costPerSCoop, remaining_icecream):
        self.flavor = flavor
        self.numScoops = numScoops
        self.costPerScoop = costPerSCoop
        self.remaining_icecream = remaining_icecream

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
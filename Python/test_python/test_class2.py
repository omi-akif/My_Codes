class Car(object):
    def __init__(self, model, color, company, speed_limit):
        self.color = color
        self.company = company
        self.model = model
        self.speed_limit = speed_limit

    def start(self):
        print("started")
    
    def stop(self):
        print("stopped")

    def accelerate(self):
        print("accelerating")
    
    def change_gear(self, gear_type):
        self.gear_type = gear_type
        print(self.gear_type)
        print("gear changed")

maruti_suzuki = Car("ertiga", "black", "suzuki", 60)
audi = Car("A6", "red", "audi", 80)

maruti_suzuki.start()

maruti_suzuki.change_gear("gear3")


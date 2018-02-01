class person:
    mood = ('happy','tired','lazy')
    def __init__(self,name,money,health_rate):
        self.name=name
        self.money=money
        if health_rate > 0 and health_rate <100:
            self.health_rate=health_rate
        else:
            print("health rate must be between 0 and 100")
    def sleep(self,hours):
        msg=''
        if hours == 7:
            msg = mood[0]
        elif hours < 7:
            msg = mood[1]
        elif hours > 7:
            msg = mood[2] 
        return msg
    def eat(self,meals):
        msg=''
        if meals == 3:
            msg = '100%'
        elif meals == 2:
            msg = '75%'
        elif meals == 1 :
            msg = '50%'
        return msg

    def buy(self,items):
        if items == 1:
            self.money - 10
class employee(person):
    def __init__(self,id,car,email,salary,distance_to_work):
        self.id=id
        self.car=car
        self.email=email
        if salary >= 1000:
            self.salary=salary
        else:
            print("salary must be 1000 or more")
        self.distance_to_work=distance_to_work
    
    def work(self,hours):
        msg=''
        if hours == 8:
            msg = mood[0]
        elif hours < 8:
            msg = mood[1]
        elif hours > 8:
            msg = mood[2] 
        return msg
    def drive(self,distance):
        car.run(self.velocity,self.distance_to_work)

    def refuel(self,gas_amount=100):
        self.fuelrate = self.fuelrate + gas_amount
        
    def send_mail(self):
        pass
class office:
    def __init__(self,name,employees):
        self.name=name
        self.employee=employee
    def get_all_employees(self):
        pass
    def get_employee(self):
        pass
    def hire(self):
        pass
    def fire(self):
        pass
    def calculate_lateness(self):
        pass
    def deduct(self):
        pass
    def reward(self):
        pass
class car:
    def __init__(self,name,fuelrate,velocity):
        self.name=name
        if fuelrate >0 and fuelrate <100:
            self.fuelrate=fuelrate
        if velocity >0 and velocity<200:
            self.velocity=velocity
    def run(self,velocity,distance):
        if self.fuelrate >0:
            self.fuelrate = self.fuelrate -1
            distance = distance - 1
        velocity = self.velocity
        if(distance == 0):
            stop(-1)
        else:
            stop(distance)
    def stop(self,remain_distance):
        self.velocity = 0
        if remain_distance == -1:
            print("you arrive the destination")
        else:
            print("remain distance : ",remain_distance)


    
    




























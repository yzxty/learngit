import random


class Car:
    count = 0

    def __init__(self):
        # todo: 构造一个车,车牌号
        Car.count = Car.count + 1
        self.id = Car.count


class Ticket:

    def __init__(self,parkId,carId):
        self.parkId = parkId
        self.carId = carId

    def show(self):
        print('ParkingLot：',self.parkId,'Car:',self.carId)

    def __str__(self):
        return str(self.parkId).rjust(3, '0') + str(self.carId).rjust(7, '0')

# 停车场，ID，当前停车数列，
class ParkingLot:
    count = 0

    def __init__(self , capacity):
        ParkingLot.count = ParkingLot.count + 1
        self.id = ParkingLot.count
        self.capacity = capacity  # 最大车位数
        self.cars = []   #  车辆car数列；其长度是当前停车数

    def park_car(self , car: Car):# 停车，给票
        if (self.print_spare() != 0):  # 可停车
            # 算车票，依据停车场id，车id计算停车票
            # ticket = str(self.id).rjust(3, '0') + str(car.id).rjust(7, '0')
            ticket=Ticket(self.id , car.id)
            print('请取票：',ticket)
            self.cars.append(car)
            return ticket
        else:
            print('该停车场已满')
            return None

    def take_car(self, ticket):  # 判断票，取车

        if ticket.parkId == self.id:
            # 停车场正确
            for cindex in range(len(self.cars)):
                car = self.cars[cindex]
                if car.id == ticket.carId:
                    print('停车票正确，请取车!')
                    self.cars.remove(car)
                    return car
            print('该停车场未停该车')
            return None
        else:
            print('该车未停在该停车场')
            return None

    def print_spare(self):  # 剩余车位
        return self.capacity - len(self.cars)


# 停车小弟，parkID:car
class Parkingboy ():
    def __init__(self):
        # 管理的车：停车场id ，
        self.manage_car_num = 0 # 当前管理车辆的数量
        # self.ParkingLot_Cars= []

    def parking_car(self, park_list , car: Car):  # 给车，根据停车场列表，停车并返回ticket
        # 循环park_list，判断是否是空的，如果有位置，进行停车
        for i in range(len(park_list)):
            if park_list[i].print_spare()>0:# 有位置
                ticket=park_list[i].park_car(car)#停车
                self.manage_car_num = self.manage_car_num + 1  # 更新
                """
                ParkingLot_Car=[i,car.id,ticket]
                self.ParkingLot_Cars.append(ParkingLot_Car)#更新                
                """
                return ticket
        print("所有停车场已满")
        return None

    def take_car(self, park_list , ticket: Ticket):#依据车 找到车票和对应停车场，取车
        # 从ParkingLot_Cars中寻找车，找到车票，进行取车
        for i in range(len(park_list)):
            if park_list[i].id == ticket.parkId:
                park_list[i].take_car(ticket)
                self.manage_car_num = self.manage_car_num - 1


class Smart_Parkingboy(Parkingboy):
    def parking_car(self, park_list, car: Car):
        maxPark=park_list[0];
        maxNum=0;
        for i in range(len(park_list)):
            if park_list[i].print_spare()>maxNum:
                maxPark=park_list[i]
                maxNum=maxPark.print_spare()
        if maxNum == 0:
            print("所有停车场已满")
            return None
        else:
            ticket = maxPark.park_car(car)
            self.manage_car_num = self.manage_car_num + 1
            return ticket


class Super_Parkingboy(Parkingboy):# 空置率
    def parking_car(self, park_list, car: Car):
        maxPark=park_list[0];
        maxVacancy=0;
        for i in range(len(park_list)):
            temp = park_list[i].print_spare()/park_list[i].capacity
            if temp>maxVacancy:
                maxPark=park_list[i]
                maxVacancy=temp
        if maxVacancy == 0:
            print("所有停车场已满")
            return None
        else:
            ticket = maxPark.park_car(car)
            self.manage_car_num = self.manage_car_num + 1
            return ticket


class Parkingmanager(Parkingboy):

    def boy_parking(self,boy_list,park_list,car):
        i = random.randint(0,len(boy_list)-1)  # 随机让一个人停车
        return boy_list[i].parking_car(park_list, car);


# 以下是测试代码
import unittest
from unittest import TestCase


class TestParkingLot(TestCase):
    def test_park_two_cars_should_get_different_tickets(self):
        print("test_park_two_cars_should_get_different_tickets")
        parking_lot = ParkingLot(2)
        car1 = Car()
        car2 = Car()
        t1 = parking_lot.park_car(car1)
        t2 = parking_lot.park_car(car2)
        self.assertNotEquals(t1, t2)

    def test_when_park_car_and_parking_lot_is_full_should_get_exception(self):
        print("test_when_park_car_and_parking_lot_is_full_should_get_exception")
        parking_lot = ParkingLot(1)
        car1 = Car()
        car2 = Car()
        parking_lot.park_car(car1)
        parking_lot.park_car(car2)

    def test_get_car(self):
        print("test_get_car")
        parking_lot = ParkingLot(1)
        car1 = Car()
        t1 = parking_lot.park_car(car1)
        taken_car1 = parking_lot.take_car(t1)
        self.assertEquals(car1, taken_car1)

    def test_get_cars_when_a_car_is_taken_should_get_exception(self):
        print("test_get_cars_when_a_car_is_taken_should_get_exception")
        parking_lot = ParkingLot(1)
        car = Car()
        t = parking_lot.park_car(car)
        parking_lot.take_car(t)
        parking_lot.take_car(t)

    def test_Parkingboy(self):
        print("test_Parkingboy")
        parkingLot_List = []
        parkingLot_List.append(ParkingLot(2))
        parkingLot_List.append(ParkingLot(1))
        parkingLot_List.append(ParkingLot(5))
        cars = []
        for i in range(6):
            car = Car()
            cars.append(car)
        parkingboy = Parkingboy()
        ts = []
        for i in range(6):
            t = parkingboy.parking_car(parkingLot_List, cars[i])
            ts.append(t)

    def test_Smart_Parkingboy(self):
        print("test_Smart_Parkingboy")
        parkingLot_List = []
        parkingLot_List.append(ParkingLot(2))
        parkingLot_List.append(ParkingLot(1))
        parkingLot_List.append(ParkingLot(5))
        cars = []
        for i in range(6):
            car = Car()
            cars.append(car)
        smart_parkingboy = Smart_Parkingboy()
        ts = []
        for i in range(6):
            t = smart_parkingboy.parking_car(parkingLot_List,cars[i])
            ts.append(t)

    def test_Super_Parkingboy(self):
        print("test_Super_Parkingboy")
        parkingLot_List = []
        parkingLot_List.append(ParkingLot(2))
        parkingLot_List.append(ParkingLot(1))
        parkingLot_List.append(ParkingLot(5))
        cars = []
        for i in range(6):
            car = Car()
            cars.append(car)
        super_parkingboy = Super_Parkingboy()
        ts = []
        for i in range(6):
            t = super_parkingboy.parking_car(parkingLot_List,cars[i])
            ts.append(t)
    def test_Parkingmanager(self):
        print("test_Parkingmanager")
        parkingLot_List = []
        parkingLot_List.append(ParkingLot(2))
        parkingLot_List.append(ParkingLot(1))
        parkingLot_List.append(ParkingLot(5))
        parkingmanager = Parkingmanager()
        cars = []
        for i in range(6):
            car = Car()
            cars.append(car)
        persons = []
        for i in range(2):
            parkingboy = Parkingboy()
            smart_parkingboy = Smart_Parkingboy()
            super_parkingboy = Super_Parkingboy()
            persons.append(parkingboy)
            persons.append(smart_parkingboy)
            persons.append(super_parkingboy)
        ts = []
        for i in range(6):
            t = parkingmanager.boy_parking(persons,parkingLot_List, cars[i])
            ts.append(t)


if __name__ == '__main__':
    unittest.main()

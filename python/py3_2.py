import numpy as np

class parking():#停车场
    def _init_(self):
        self.car_max = 100  # 最大车位数
        self.car_num = 0  # 停车场停车数
        self.car_mark = np.random.rand(1, self.car_max)  # 每个车位对应的停车票

    def parking(self):#停车
        if (self.car_num < car_max):  # 可停车
            print('停车票是', self.car_mark(1, self.car_num))
            self.car_num = self.car_num + 1
            return self.car_mark(1, self.car_num - 1)
        else:
            print('停车场已满')
            return -1

    def pick_up(self, user_mark):
        for i in range(self.car_max):
            if (self.car_mark(1, i) == user_mark):  # 判断停车票是否正确
                print('停车票正确，请取车!')
                self.car_num = self.car_num - 1
                return 0
        print('停车票错误!')
        return -1

    def print_spare(self):
        return self.car_max - self.car_num, self.car_max


class parkingboy():

    def _init_(self, park_lot):
        self.car_num = 0
        self.mark_num = {}
        self.park_lot = park_lot#停车场队列

    def parking_car(self, park_num):
        park_mark = self.park_lot[park_num].parking()#停到park_num的停车场
        self.mark_num[park_mark] = park_num#车票对应停车场

    def pick_up_car(self, park_mark):
        park_num = self.mark_num[park_mark]#得到停车场
        self.park_lot[park_num].pick_up(park_mark)


class smart_parkingboy(parkingboy):
    def parking_car(self, park_num):
        max_parknum = 0
        max_parkspare = 0
        for i in self.park_lot:
            parkspare, temp = self.park_lot.print_spare()
            if (max_parkspare < parkspare):
                max_parknum = i
                max_parkspare = parkspare
        park_mark = self.park_lot[max_parknum].parking()
        self.mark_num[park_mark] = park_num

class super_parkingboy(parkingboy):
    def parking_car(self, park_num):
        max_parknum = 0
        max_parkspare = 0
        for i in self.park_lot:
            parkspare, max_num = self.park_lot.print_spare()
            temp = parkspare / max_num
            if (max_parkspare < temp):
                max_parknum = i
                max_parkspare = temp
        park_mark = self.park_lot[max_parknum].parking()
        self.mark_num[park_mark] = park_num


class parkingmanager(parkingboy):

    def boy_parking(self, park_num, boy):
        boy.parking_car(park_num)

    def boy_pickup(self, park_mark, boy):
        boy.pick_up_car(park_mark)


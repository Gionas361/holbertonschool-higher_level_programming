#!/usr/bin/python3

class Hehe():
    objects = []

    def __init__(self, num):
        self.num = num
        self.example = num

    @property
    def num(self):
        return(self.objects)

    @num.setter
    def num(self, value):
        self.objects.append(value)
        return(self.objects)

    def sum_each(self):
        mult = 0
        for i in self.objects:
            mult = mult + (i * 2)
        print("[*2] = " + str(mult))

        sub = 0
        for i in self.objects:
            sub = sub + (i - 2)
        print("[-2] = " + str(sub))

        sum = 0
        for i in self.objects:
            sum = sum + (i + 2)
        print("[+2] = " + str(sum))

        power = 0
        for i in self.objects:
            power = power + (i * i)
        print("[*num] = " + str(power))


my_Hehe1 = Hehe(2)
my_Hehe2 = Hehe(10)
my_Hehe3 = Hehe(15)

my_Hehe3.sum_each()

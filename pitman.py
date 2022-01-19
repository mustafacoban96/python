import random

import time


class Pitman:
    def __init__(self, name, machine_power=100, rope_durability=10, lvl=1, exp=0, money=0):
        self.name = name
        self.machine_power = machine_power
        self.rope_durability = rope_durability
        self.lvl = lvl
        self.exp = exp
        self.money = money

    def loots(self):
        stones = [{"diamond": 80}, {"gold": 70}, {"silver": 60}, {"bronze": 40}, {"copper": 25},
                  {"coal": 15},
                  {"stone": 5},
                  {"waste": 0}]
        a = random.choice(stones)
        booty = list(a.keys())
        price = list(a.values())
        for booty in booty:
            pass
        for lidya in price:
            pass
        print("you pull", booty)
        print(f"{booty} is ", lidya)
        self.money += lidya
        return

    def pass_lvl(self):
        if answer == 1:
            self.exp += 10
            up = self.lvl*101
            if self.exp >= up:
                self.lvl += 1

    def use_machine(self):
        if answer == 1:
            self.machine_power -= 10
            if self.machine_power <= 0:
                self.machine_power = 0
                print("You have", self.money, "lidyas")
                cost = int(input("enter the amount of machine's cost: "))
                if cost < self.money:
                    self.money -= cost
                    self.machine_power += cost
                elif self.money <= 0:
                    self.money = 0
                    print("you don't have enough money!")
                else:
                    print("you only have", self.money)

    def resistance(self):
        lvl = random.randint(1, 5)
        if self.lvl == lvl:
            self.rope_durability -= random.randint(1, 5)
            if self.rope_durability <= 0:
                print("The rope broke !!!")
                self.rope_durability = 0
                print("One rope durability equals 10 Lidyas ")
                cost_rope = int(input("amount of rope's durability: "))
                if self.money >= cost_rope*10:
                    self.rope_durability += cost_rope
                    self.money -= cost_rope*10
                    print("you have: ", self.money, "anymore")
                else:
                    print("You don't have enough money")

    def status(self):

        print("*-"*8)
        print("report of status:")
        time.sleep(1)
        print("your money =>", self.money, "\n<>")
        time.sleep(0.3)
        print("machine's power =>", self.machine_power, "\n<>")
        time.sleep(0.3)
        print("your exp =>", self.exp, "\n<>")
        time.sleep(0.3)
        print("your level =>", self.lvl, "\n<>")
        time.sleep(0.3)
        print("rope's durability =>", self.rope_durability)
        print("*-" * 8)
        print("><"*25)
        time.sleep(0.3)


def gaming_system():
    if answer == 1:
        player.loots()
        player.pass_lvl()
        player.use_machine()
        time.sleep(1)
        player.status()
        player.resistance()


player = Pitman(input("enter your name pitman: "))
print(f"Hello", player.name)
time.sleep(0.5)
print("If you are patient, you will beat whole difficulty...")
time.sleep(0.5)
print("If you are ready,you start to pull loots!!!!")
time.sleep(0.5)
print("Press 's' for starting,also 'q' for quit")
time.sleep(0.3)
print("Please press [s]/[q]")
choose = input("press: ")

while True:
    if choose == "s" or choose == "S":
        answer = int(input("let's pull loots for this,press [1]: "))
        print("If you want exit, you press [2]")
        print("><"*25)
        if answer == 1:
            gaming_system()
        elif answer == 2:
            print("You are exiting....")
            break
        else:
            print("Please enter correct value")

    elif choose == "q" or choose == "Q":
        break

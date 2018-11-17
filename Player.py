# Character Class

class player:
    # combat-related properties and methods (monster, player, NPC).
    def __init__(self, speed, strength, knowledge, sanity, death_function=None):
        self.base_speed = speed
        self.base_strength = strength
        self.base_knowledge = knowledge
        self.base_sanity = sanity
        self.death_function = death_function
        self.equipment = []
        self.equipped =[]

    @property
    def strength(self):  # return actual strength, by summing up the bonuses from all equipped items
        bonus = 0
        for item in self.equipped:
            if item.type == strength:
                bonus += item.bonus
        return self.base_strength + bonus

    @property
    def speed(self):  # return actual speed, by summing up the bonuses from all equipped items
        bonus = 0
        for item in self.equipped:
            if item.type == speed:
                bonus += item.bonus
        return self.base_speed + bonus

    @property
    def knowledge(self):  # return actual knowledge, by summing up the bonuses from all equipped items
        bonus = 0
        for item in self.equipped:
            if item.type == knowledge:
                bonus += item.bonus
        return self.base_knowledge + bonus

    @property
    def sanity(self):  # return actual sanity, by summing up the bonuses from all equipped items
        bonus = 0
        for item in self.equipped:
            if item.type == sanity:
                bonus += item.bonus
        return self.base_sanity + bonus

    def attack(self, target):
        # a simple formula for attack damage
        damage = self.strength - target.fighter.defense

        if damage > 0:
            # make the target take some damage
            message(self.owner.name.capitalize() + ' attacks ' + target.name + ' for ' + str(damage) + ' hit points.')
            target.fighter.take_damage(damage)
        else:
            message(self.owner.name.capitalize() + ' attacks ' + target.name + ' but it has no effect!')

    def pickup(self, item): # Takes items and adds it to the equipment list
        self.equipment.append(item)
        if item.status() = passive:
            self.equipped.append(item)

    def equip(self): # Should return a list of active items, that currently affect stats
        return self.equipped

    def use_item(self):
        count = 0
        option = []
        for item in self.equipment:
            if item.status == active:
                print(count, ". ", item.name, '/n')
                option.append(item)
                self.equipped.remove(item)
                count += 1
        x = input("Please enter the number of item to activate: ")
        self.equipped.append(option[x])
        option.remove(option[x])
        for item in option:
            self.equipment.append(item)

    def destroy(self):
        for item in self.equipped:
            if item.status == active
                self.equipped.remove(item)

import json


class Herios:
    def __init__(self, d):
        self.race = d['race']
        self.lord = d['lord']
        self.health = int(d['health'])
        self.attack = int(d['attack'])
        self.defence = int(d['defence'])
        self.exp = int(d['experience'])
        if self.race == 'Sorceress' or self.race == 'Warlock':
            self.mana = int(d['mana'])
        else:
            self.mana = 0
str = input()
j = json.loads(str)
a = j['armies']
b = j['battle_steps']
army = {}
for i in a.keys():
    h = Herios(a[i])
    army[i] = h
for battle in b:
    h1 = army[battle['id_from']]
    h2 = army[battle['id_to']]
    power = int(battle['power'])
    act = battle['action']
    if h1.health > 0 and h2.health > 0:
        if act == 'attack':
            if h2.defence >= power:
                h2.defence = h2.defence - power
                h1.attack = h1.attack - power
                h1.exp += 1
                h2.exp += 1
            elif h2.defence + h2.health > power:
                h2.health = h2.health - power + h2.defence
                h2.defence = 0
                h1.attack = h1.attack - power
                h1.exp += 1
                h2.exp += 1
            else:
                h1.attack -= power
                h2.health = 0
                h1.exp += 5
        if act == 'cast_damage_spell':
            if h2.defence >= power:
                h2.defence = h2.defence - power
                h1.mana -= power
                h1.exp += 1
                h2.exp += 1
            elif h2.defence + h2.health > power:
                h2.health = h2.health - power + h2.defence
                h2.defence = 0
                h1.mana -= power
                h1.exp += 1
                h2.exp += 1
            else:
                h1.mana -= power
                h2.health = 0
                h1.exp += 5
        if act == 'cast_health_spell':
                h1.mana -= power
                h1.exp += 1
                if h2.race == 'Knight':
                    if power + h2.health > 100:
                        h2.health = 100
                    else:
                        h2.health += power
                elif h2.race == 'Warlock':
                    if power + h2.health > 70:
                        h2.health = 70
                    else:
                        h2.health += power
                elif h2.race == 'Barbarian':
                    if power + h2.health > 120:
                        h2.health = 120
                    else:
                        h2.health += power
                else:
                    if power + h2.health > 50:
                        h2.health = 50
                    else:
                        h2.health += power
archibald = 0
ronald = 0
counta = 0
countr = 0
for pers in army.keys():
    h = army[pers]
    if h.health > 0:
        if h.lord == 'Archibald':
            archibald += h.exp + h.defence * 2 + h.attack * 3 + h.mana * 10
            counta += 1
        else:
            ronald += h.exp + h.defence * 2 + h.attack * 3 + h.mana * 10
            countr += 1
if archibald > ronald or (countr == 0 and counta > 0):
    print('Archibald')
elif archibald < ronald or (counta == 0 and countr > 0):
    print('Ronald')
else:
    print('unknown')

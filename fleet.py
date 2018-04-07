class Ship(object):
	def __init__(self, name, cost, hit_on, capacity=0, rolls=1, sustain=0, race='', tech=1):
		self.name = name
		self.capacity = capacity
		self.cost = cost
		self.hit_on = hit_on
		self.rolls = rolls
		self.sustain = sustain
		self.race = race
		self.tech = tech
		self.cannons = {'rolls': 0, 'hit_on': 10}
		self.ship_buff = {'rolls': 0, 'hit_on': 0}
		if race == 'sardakk':
			self.hit_on = self.hit_on - 1

	def hits(self):
		return (10.0 - self.hit_on) / 10.0 * self.rolls


class Flagship(Ship):
	def __init__(self, race='', tech=1):
		if race == '':
			super().__init__(self.__class__.__name__, cost=8, sustain=1, hit_on=7, rolls=2, capacity=2)
		elif race == 'arborec':
			super().__init__(self.__class__.__name__, cost=8, sustain=1, hit_on=7, rolls=2, capacity=5)
		elif race == 'creuss':
			super().__init__(self.__class__.__name__, cost=8, sustain=1, hit_on=5, rolls=1, capacity=3)
		elif race == 'hacan':
			super().__init__(self.__class__.__name__, cost=8, sustain=1, hit_on=7, rolls=2, capacity=3)
		elif race == 'jol-nar':
			super().__init__(self.__class__.__name__, cost=8, sustain=1, hit_on=6, rolls=2, capacity=5)
		elif race == 'l1z1x':
			super().__init__(self.__class__.__name__, cost=8, sustain=1, hit_on=5, rolls=2, capacity=5)
		elif race == 'letnev':
			super().__init__(self.__class__.__name__, cost=8, sustain=1, hit_on=5, rolls=2, capacity=3)
		elif race == 'mentak':
			super().__init__(self.__class__.__name__, cost=8, sustain=1, hit_on=7, rolls=2, capacity=3)
		elif race == 'muaat':
			super().__init__(self.__class__.__name__, cost=8, sustain=1, hit_on=5, rolls=2, capacity=3)
		elif race == 'naalu':
			super().__init__(self.__class__.__name__, cost=8, sustain=1, hit_on=9, rolls=2, capacity=6)
		elif race == 'nekro':
			super().__init__(self.__class__.__name__, cost=8, sustain=1, hit_on=9, rolls=2, capacity=3)
		elif race == 'saar':
			super().__init__(self.__class__.__name__, cost=8, sustain=1, hit_on=5, rolls=2, capacity=3)
		elif race == 'sardakk':
			super().__init__(self.__class__.__name__, cost=8, sustain=1, hit_on=6, rolls=2, capacity=3)
			self.ship_buff = {'rolls': 0, 'hit_on': 1}
		elif race == 'sol':
			super().__init__(self.__class__.__name__, cost=8, sustain=1, hit_on=5, rolls=2, capacity=12)
		elif race == 'winnu':
			super().__init__(self.__class__.__name__, cost=8, sustain=1, hit_on=7, rolls=1, capacity=3)
		elif race == 'xxcha':
			super().__init__(self.__class__.__name__, cost=8, sustain=1, hit_on=7, rolls=2, capacity=3)
			self.cannons = {'rolls': 3, 'hit_on': 5}
		elif race == 'yin':
			super().__init__(self.__class__.__name__, cost=8, sustain=1, hit_on=9, rolls=2, capacity=3)
		elif race == 'yssaril':
			super().__init__(self.__class__.__name__, cost=8, sustain=1, hit_on=5, rolls=2, capacity=6)
		else:
			raise Exception('Invalid race')

	def hits(self):
		hits = super().hits()
		if self.race == 'jol-nar':
			hits = hits + 0.2*2
		return hits


class Warsun(Ship):
	def __init__(self, race='', tech=1):
		if race == 'muaat':
			if tech == 2:
				super().__init__(self.__class__.__name__, cost=10, hit_on=3, capacity=6, rolls=3, sustain=1)
			else:
				super().__init__(self.__class__.__name__, cost=12, hit_on=3, capacity=6, rolls=3, sustain=1)
		else:
			super().__init__(self.__class__.__name__, cost=12, hit_on=3, capacity=6, rolls=3, sustain=1)


class Dreadnought(Ship):
	def __init__(self, race='', tech=1):
		if tech == 2:
			if race == 'l1z1x':
				super().__init__(self.__class__.__name__, cost=4, hit_on=4, capacity=2, rolls=1, sustain=1)
			else:
				super().__init__(self.__class__.__name__, cost=4, hit_on=5, capacity=1, rolls=1, sustain=1)
		else:
			super().__init__(self.__class__.__name__, cost=4, hit_on=5, capacity=1, rolls=1, sustain=1)


class Cruiser(Ship):
	def __init__(self, race='', tech=1):
		if tech == 2:
			super().__init__(self.__class__.__name__, cost=4, hit_on=6, capacity=1, rolls=1, sustain=0)
		else:
			super().__init__(self.__class__.__name__, cost=2, hit_on=7, capacity=0, rolls=1, sustain=0)


class Fighter(Ship):
	def __init__(self, race='', tech=1):
		if tech == 2:
			super().__init__(self.__class__.__name__, cost=0.5, hit_on=8, capacity=0, rolls=1, sustain=0)
		else:
			super().__init__(self.__class__.__name__, cost=0.5, hit_on=9, capacity=0, rolls=1, sustain=0)


class Destroyer(Ship):
	def __init__(self, race='', tech=1):
		if tech == 2:
			super().__init__(self.__class__.__name__, cost=1, hit_on=8, capacity=0, rolls=1, sustain=0)
		else:
			super().__init__(self.__class__.__name__, cost=1, hit_on=9, capacity=0, rolls=1, sustain=0)


class Carrier(Ship):
	def __init__(self, race='', tech=1):
		if tech == 2:
			if race=='sol':
				super().__init__(self.__class__.__name__, cost=3, hit_on=9, capacity=8, rolls=1, sustain=1)
			else:
				super().__init__(self.__class__.__name__, cost=3, hit_on=9, capacity=6, rolls=1, sustain=0)
		else:
			if race=='sol':
				super().__init__(self.__class__.__name__, cost=3, hit_on=9, capacity=4, rolls=1, sustain=0)
			else:
				super().__init__(self.__class__.__name__, cost=3, hit_on=9, capacity=6, rolls=1, sustain=0)


class Fleet(object):
	def __init__(self, ships):
		self.ships = ships
		self.cost = 0
		self.capacity = 0
		self.resilience = 0
		self.hits = 0
		for ship in ships:
			self.cost = self.cost + ship.cost
			self.capacity = self.capacity + ship.capacity
			self.resilience = self.resilience + ship.sustain + 1
			self.hits = self.hits + (10.0 - ship.hit_on) / 10.0 * ship.rolls

	def breakdown(self, fighter_capacity, fighter):
		fighters = int(self.capacity * fighter_capacity / 100)
		resilience = self.resilience
		cost = self.cost
		hits = self.hits
		types = [ship.name[:2] for ship in self.ships]
		for _ in range(fighters):
			resilience = resilience + fighter.sustain + 1
			cost = cost + fighter.cost
			hits = hits + (10.0 - fighter.hit_on) / 10.0 * fighter.rolls

		return ','.join([('.'.join(types)), str(fighters), str(cost), str(hits), str(hits / cost), str(resilience)])

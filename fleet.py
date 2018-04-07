class Ship(object):
	def __init__(self, name, cost, hit_on, capacity=0, rolls=1, sustain=0):
		self.name = name
		self.capacity = capacity
		self.cost = cost
		self.hit_on = hit_on
		self.rolls = rolls
		self.sustain = sustain

class Flagship(Ship):
	def __init__(self, race='', tech=1):
		if race == 'hacan':
			super().__init__(self.__class__.__name__, cost=8, sustain=1, hit_on=7, rolls=2, capacity=3)
		elif race == 'naalu':
			super().__init__(self.__class__.__name__, cost=8, sustain=1, hit_on=9, rolls=2, capacity=6)
		elif race == 'yssaril':
			super().__init__(self.__class__.__name__, cost=8, sustain=1, hit_on=5, rolls=2, capacity=6)
		elif race == 'saar':
			super().__init__(self.__class__.__name__, cost=8, sustain=1, hit_on=5, rolls=2, capacity=3)
		else:
			super().__init__(self.__class__.__name__, cost=8, sustain=1, hit_on=7, rolls=2, capacity=2)

class Warsun(Ship):
	def __init__(self, race='', tech=1):
		super().__init__(self.__class__.__name__, cost=12, hit_on=3, capacity=6, rolls=3, sustain=1)

class Dreadnought(Ship):
	def __init__(self, race='', tech=1):
		if tech == 2:
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
			super().__init__(self.__class__.__name__, cost=3, hit_on=9, capacity=6, rolls=1, sustain=0)
		else:
			super().__init__(self.__class__.__name__, cost=3, hit_on=9, capacity=4, rolls=1, sustain=0)

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
			types.append(fighter.name[:2])

		return ','.join([('.'.join(types)), str(cost), str(hits), str(hits / cost), str(resilience)])

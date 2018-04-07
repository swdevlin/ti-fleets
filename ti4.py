import argparse

from fleet import Flagship, Warsun, Dreadnought, Cruiser, Destroyer, Carrier, Fighter, Fleet

FLAGSHIPS=1
WARSUNS=2
DREADNOUGHTS=5
CRUISERS=8
DESTROYERS=8
CARRIERS=4

RACES = [
	'', 'arborec', 'creuss', 'hacan', 'jol-nar', 'l1z1x', 'letnev', 'mentak', 'muaat', 'naalu', 'nekro', 'saar',
	'sardakk', 'sol', 'winnu', 'xxcha', 'yin', 'yssaril'
]


class tech2(argparse.Action):
	def __call__(self, parser, namespace, values, option_string=None):
		setattr(namespace, self.dest, 2)


parser = argparse.ArgumentParser()
parser.add_argument("--race", help="Race for the fleet", choices=RACES, default='')
parser.add_argument("--size", type=int, help="fleet size", default=1)
parser.add_argument("--percent", type=int, help="precentage of capacity that is fighters", default=0, choices=range(0,101))
parser.add_argument("-de", "--destroyer", help="destroyers are tech 2", action=tech2, default=1)
parser.add_argument("-fi", "--fighter", help="fighter are tech 2", action=tech2, default=1)
parser.add_argument("-ca", "--carrier", help="carrier are tech 2", action=tech2, default=1)
parser.add_argument("-cr", "--cruiser", help="cruisers are tech 2", action=tech2, default=1)
parser.add_argument("-w", "--warsun", help="destroyers are tech 2, only relevant for muaat", action=tech2, default=1)
parser.add_argument("-dr", "--dreadnought", help="dreadnoughts are tech 2", action=tech2, default=1)
parser.add_argument("--debug", help="debug mode", action="store_true")
args = parser.parse_args()

flagship = Flagship(race=args.race, tech=1)
warsun = Warsun(race=args.race, tech=args.warsun)
dreadnought = Dreadnought(race=args.race, tech=args.dreadnought)
cruiser = Cruiser(race=args.race, tech=args.cruiser)
destroyer = Destroyer(race=args.race, tech=args.destroyer)
carrier = Carrier(race=args.race, tech=args.carrier)
fighter = Fighter(race=args.race, tech=args.fighter)

available_units = []

for _ in range(FLAGSHIPS):
	available_units.append(flagship)
for _ in range(WARSUNS):
	available_units.append(warsun)
for _ in range(DREADNOUGHTS):
	available_units.append(dreadnought)
for _ in range(CRUISERS):
	available_units.append(cruiser)
for _ in range(DESTROYERS):
	available_units.append(destroyer)
for _ in range(CARRIERS):
	available_units.append(carrier)
fighter = Fighter(race=args.race, tech=args.fighter)

fleets = set()

def add_ship(fleet, pool):
	if len(pool) == 0:
		return
	fleet = list(fleet)
	fleet.append(pool[0])
	if len(fleet) == args.size:
		fleets.add(tuple(fleet))
	else:
		for _ in range(1, len(pool) + 1):
			add_ship(fleet, pool[_:])


def fleet_dump(fleet, fighter_capacity=0):
	cost = 0
	hits = 0
	ships = []
	capacity = 0
	resilience = 0

	for ship in fleet:
		if ship.ship_buff['rolls'] > 0:
			for other in fleet:
				if other != ship:
					other.rolls = other.rolls + ship.ship_buff['rolls']
		if ship.ship_buff['to_hit'] != 0:
			for other in fleet:
				if other != ship:
					other.rolls = other.rolls - ship.ship_buff['to_hit']

	for ship in fleet:
		ships.append(ship.name)
		cost = cost + ship.cost
		capacity = capacity + ship.capacity
		resilience = resilience + ship.sustain + 1
		hits = hits + ship.hits()
	fighters = int(capacity * fighter_capacity / 100)
	for _ in range(fighters):
		resilience = resilience + fighter.sustain + 1
		cost = cost + fighter.cost
		hits = hits + fighter.hits()
		ships.append(fighter.name[:2])

	return ','.join(['.'.join(ships), cost, hits, hits / cost, resilience])


for _ in range(len(available_units) + 1):
	if args.debug:
		print('computing', _)
	pool = available_units[_:]
	if len(pool) >= args.size:
		add_ship([], pool)

final = []
for fleet in fleets:
	final.append(list(fleet))

breakdown = []
for f in final:
	fleet = Fleet(f)
	breakdown.append(fleet.breakdown(fighter_capacity=args.percent, fighter=fighter))

print('Fleet,Fighters,Cost,Hits in Round,Hits/Cost,Resilience')
print('\n'.join(sorted(breakdown)))
print(len(final), " total fleets")



import argparse

from fleet import Flagship, Warsun, Dreadnought, Cruiser, Destroyer, Carrier, Fighter, Fleet


class tech2(argparse.Action):
	def __call__(self, parser, namespace, values, option_string=None):
		setattr(namespace, self.dest, 2)


parser = argparse.ArgumentParser()
parser.add_argument("--race", help="Race for the fleet", default='')
parser.add_argument("--size", type=int, help="fleet size", default=1)
parser.add_argument("--percent", type=int, help="precentage of capacity that is fighters", default=0, choices=range(0,101))
parser.add_argument("-de", "--destroyer", help="destroyers are tech 2", action=tech2, default=1)
parser.add_argument("-fi", "--fighter", help="fighter are tech 2", action=tech2, default=1)
parser.add_argument("-ca", "--carrier", help="carrier are tech 2", action=tech2, default=1)
parser.add_argument("-cr", "--cruiser", help="cruisers are tech 2", action=tech2, default=1)
parser.add_argument("-w", "--warsun", help="destroyers are tech 2, only relevant for muaat", action=tech2, default=1)
parser.add_argument("-dr", "--dreadnought", help="dreadnoughts are tech 2", action=tech2, default=1)
args = parser.parse_args()

race = ''
flagship = Flagship(race=args.race, tech=1)
warsun = Warsun(race=race, tech=args.warsun)
dreadnought = Dreadnought(race=race, tech=args.dreadnought)
cruiser = Cruiser(race=race, tech=args.cruiser)
destroyer = Destroyer(race=race, tech=args.destroyer)
carrier = Carrier(race=race, tech=args.carrier)
fighter = Fighter(race=race, tech=args.fighter)

source = [
	flagship,
	warsun, warsun,
	dreadnought, dreadnought, dreadnought, dreadnought, dreadnought,
	cruiser, cruiser, cruiser, cruiser, cruiser, cruiser, cruiser, cruiser,
	destroyer, destroyer, destroyer, destroyer, destroyer, destroyer, destroyer, destroyer,
	carrier, carrier, carrier, carrier
]

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
		ships.append(ship.name)
		cost = cost + ship.cost
		capacity = capacity + ship.capacity
		resilience = resilience + ship.sustain + 1
		hits = hits + (10.0 - ship.hit_on) / 10.0 * ship.rolls
	fighters = int(capacity * fighter_capacity / 100)
	for _ in range(fighters):
		resilience = resilience + fighter.sustain + 1
		cost = cost + fighter.cost
		hits = hits + (10.0 - fighter.hit_on) / 10.0 * fighter.rolls
		ships.append(fighter.name[:2])

	return ','.join(['.'.join(ships), cost, hits, hits / cost, resilience])


for _ in range(len(source) + 1):
	print('computing', _)
	pool = source[_:]
	if len(pool) >= args.size:
		add_ship([], pool)

final = []
for fleet in fleets:
	final.append(list(fleet))

for f in final:
	fleet = Fleet(f)
	print(fleet.breakdown(fighter_capacity=args.percent, fighter=fighter))

print(len(final), " total fleets")

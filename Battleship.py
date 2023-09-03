import random


# class Vessel:
#     def __init__(self, name, capacity, length, type):
#         self.name = name  # Nom du navire
#         self.capacity = capacity  # nombre maximum de passager
#         self.length = length  # Taille du vaisseau en mètres
#         self.type = type  # types de vaiseau ( refueling, mechanical assistance and cargo)

#     def __str__(self):
#         return f"{self.name} ({self.type}) - Capacity: {self.capacity}, Length: {self.length}m"


# class Fleet:
#     def __init__(self):
#         self.vessels = []

#     def add_vessel(self, vessel):
#         self.vessels.append(vessel)

#     def list_vessels(self):
#         for vessel in self.vessels:
#             print(vessel)


# Example usage:
# if __name__ == "__main__":
#     fleet = Fleet()

#     # ajouter les vaisseaux à la flotte
#     vessel1 = Vessel("mechanical 1", 200, 50, "mechanical")
#     vessel2 = Vessel("refueling", 5000, 150, "refueling")
#     vessel3 = Vessel("cargo", 300, 250, "cargo")
#     fleet.add_vessel(vessel1)
#     fleet.add_vessel(vessel2)
#     fleet.add_vessel(vessel3)

#     # Lister les vaisseaux de la flotte
#     print("Fleet:")
#     fleet.list_vessels()

class Vessel:
    def __init__(self, name, vessel_type, medical_unit=True):
        self.name = name
        self.vessel_type = vessel_type
        self.medical_unit = medical_unit
        self.x = None
        self.y = None
        self.shield_up = False

    def move(self, x, y):
        self.x = x
        self.y = y

    def raise_shield(self):
        self.shield_up = True

    def lower_shield(self):
        self.shield_up = False

class SupportCraft(Vessel):
    def __init__(self, name, support_type, medical_unit=True):
        super().__init__(name, "Support", medical_unit)
        self.support_type = support_type

class OffensiveCraft(Vessel):
    def __init__(self, name, offensive_type, cannon_count):
        super().__init__(name, "Offensive")
        self.offensive_type = offensive_type
        self.cannon_count = cannon_count

class CommandShip(OffensiveCraft):
    def __init__(self, name):
        super().__init__(name, "Battleship", 24)

class Fleet:
    def __init__(self):
        self.vessels = []

    def add_vessel(self, vessel):
        self.vessels.append(vessel)

    def list_vessels(self):
        for vessel in self.vessels:
            print(vessel.name, " - Type:", vessel.vessel_type)

# Exemple d'utilisation :

if __name__ == "__main__":
    fleet = Fleet()

    # ajout des support craft
    fleet.add_vessel(SupportCraft("Refueling Ship 1", "Refueling"))
    fleet.add_vessel(SupportCraft("Mechanical Assistance Ship 1", "Mechanical Assistance"))
    fleet.add_vessel(SupportCraft("Cargo Ship 1", "Cargo"))

    # ajout des offensive craft
    fleet.add_vessel(OffensiveCraft("Battleship 1", "Battleship", 24))
    fleet.add_vessel(OffensiveCraft("Cruiser 1", "Cruiser", 6))
    fleet.add_vessel(OffensiveCraft("Destroyer 1", "Destroyer", 12))

    # ajout des command ship
    fleet.add_vessel(CommandShip("Command Ship 1"))

    # Lister les vaisserau de la flottes
    print("Fleet:")
    fleet.list_vessels()




class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]

    def place_ship(self, ship, x, y):
        if 0 <= x < self.size and 0 <= y < self.size:
            if self.grid[x][y] is None:
                self.grid[x][y] = ship
                ship.set_position(x, y)
                return True
        return False

class Ship:
    def __init__(self, name, ship_type):
        self.name = name
        self.ship_type = ship_type
        self.x = None
        self.y = None

    def set_position(self, x, y):
        self.x = x
        self.y = y

# déplacer un navire vers une nouvelle position sur une grille. Elle vérifie d'abord si le déplacement est possible, puis met à jour la grille pour refléter le nouveau placement du navire.
    def move(self, grid, new_x, new_y):
        if grid.place_ship(self, new_x, new_y):
            grid.grid[self.x][self.y] = None
            self.set_position(new_x, new_y)

def generate_pairs(ships):
    pairs = []
    while len(pairs) < 25:
        offensive_ship = random.choice(ships)
        support_ship = random.choice(ships)
        if offensive_ship != support_ship and (offensive_ship, support_ship) not in pairs and (support_ship, offensive_ship) not in pairs:
            pairs.append((offensive_ship, support_ship))
    return pairs

# fonction créant une flotte de 50 navires (25 offensive et 25 support)
fleet = []
for i in range(25):
    fleet.append(Ship(f"Navire offensif {i+1}", "Offensif"))
    fleet.append(Ship(f"Navire de Support  {i+1}", "Support"))

# creation d'une grille de 100x100
grid = Grid(100)

# placement aléatoire des navires
for ship in fleet:
    while True:
        x = random.randint(0, 99)
        y = random.randint(0, 99)
        if grid.place_ship(ship, x, y):
            break

# Génération des paires de navires et déplacez-les les uns à côté des autres
pairs = generate_pairs(fleet)
for offensive_ship, support_ship in pairs:
    x_offset = random.choice([-1, 0, 1])
    y_offset = random.choice([-1, 0, 1])
    new_x = offensive_ship.x + x_offset
    new_y = offensive_ship.y + y_offset
    offensive_ship.move(grid, new_x, new_y)
    support_ship.move(grid, new_x, new_y)

#  afficher la grille pour visualiser les positions des navires
for row in grid.grid:
    for cell in row:
        if cell:
            print(f"{cell.name} ({cell.ship_type}) ", end="")
        else:
            print(" [] ", end="")
    print()
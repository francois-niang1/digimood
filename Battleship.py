import random


class Vessel:
    def __init__(self, name, capacity, length, type):
        self.name = name  # Nom du navire
        self.capacity = capacity  # nombre maximum de passager
        self.length = length  # Taille du vaisseau en mètres
        self.type = type  # types de vaiseau ( 'Ferry', 'Cargo', 'Pétrolier', etc.)

    def __str__(self):
        return f"{self.name} ({self.type}) - Capacity: {self.capacity}, Length: {self.length}m"


class Fleet:
    def __init__(self):
        self.vessels = []

    def add_vessel(self, vessel):
        self.vessels.append(vessel)

    def list_vessels(self):
        for vessel in self.vessels:
            print(vessel)


# Example usage:
# if __name__ == "__main__":
#     fleet = Fleet()

#     # ajouter les vaisseaux à la flotte
#     vessel1 = Vessel("Ferry 1", 200, 50, "Ferry")
#     vessel2 = Vessel("Cargo", 5000, 150, "Cargo")
#     fleet.add_vessel(vessel1)
#     fleet.add_vessel(vessel2)

#     # Lister les vaisseaux de la flotte
#     print("Fleet:")
#     fleet.list_vessels()



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
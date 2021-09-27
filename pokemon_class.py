class Pokemon:
    def __init__(self, name, type, health):
        self.name = name
        self.type = type
        self.health = health
    
    def displayname(self):
        print("Name:", self.name)

Pikachu = Pokemon("Pikachu", "electric", "100")
Pikachu.displayname()

print(Pikachu.type)
print(Pikachu.health)
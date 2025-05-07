#Elizabeth Pettit
#04/27/2025
#P5HW
#Use of loops, functions and module import to complete a program and game simulation.

import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        damage = random.randint(1, self.attack_power)
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} now has {self.health} health remaining.")

def create_character():
    name = input("Enter your character's name: ")
    health = int(input("Enter health points: "))
    attack_power = int(input("Enter attack points: "))
    
    return Character(name, health, attack_power)

def display_characters(characters):
    if not characters:
        print("No characters created yet!")
        return
    
    print("\nCharacter List:")
    for index, char in enumerate(characters):
        print(f"{index + 1}. {char.name} - Health: {char.health}, Attack Points: {char.attack_power}")

def attack(characters):
    """Performs an attack between the first two characters."""
    if len(characters) < 2:
        print("You need at least two characters to battle!")
        return
    
    attacker = characters[0]
    defender = characters[1]
    
    attacker.attack(defender)

def main():
    characters = []

    while True:
        print("\nMenu:")
        print("1. Create Character")
        print("2. Display Characters")
        print("3. Attack")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            characters.append(create_character())
        elif choice == "2":
            display_characters(characters)
        elif choice == "3":
            attack(characters)
        elif choice == "4":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

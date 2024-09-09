class Pet:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def __str__(self) -> str:
        self.is_adopted = False
        return f"{self.name} is a {self.species}"

class AdoptionCenter:
    def __init__(self):
        self.pet_store = []

    def add_pet(self, name ,species):
        try: 
            pet = Pet(name,species)
            self.pet_store.append(pet)
            print("Successful Added",name)
        except Exception:
            print("Something went worry :( in the add function")
    def view_available(self):
        try:
            if not self.adopt_pet:
                print("No Pets Availables")
            else:
                print("Available Pets: ")
                for pet in self.pet_store:
                    print(pet)
        except Exception:
            print("Something went worry :( in the view function")
        
    def adopt_pet(self,name):
       try: 
            for pet in self.pet_store:
                if pet.name == name:
                    if not pet.is_adopted:
                        pet.is_adopted = True
                        print("You can have adopted",name)
                    else:
                        print(name,"is already adopted")
       except Exception:
                print("Something went worry :( in the adopt function")
           
    def return_adopt_pet(self,name):
        try:
         for pet in self.pet_store:
            if pet.name == name:
                if pet.is_adopted:
                    pet.is_adopted = False
                    print("You can have Return",name)
                else:
                    print(name,"is not adopted")
        except Exception:
            print("Something went worry :( in the return function")

AC = AdoptionCenter()
while True:
    try:
        print("\nOptions")
        print("1. Add New Pet")
        print("2. View Pets")
        print("3. Adopt AN Pet")
        print("4. Return An Pet")
        print("5. Exit")

        op = int(input("Enter your option 1-5: "))
   

        if op  == 1:
            try:
                pet_name = input("Enter pet name: ")
                pet_species =input("Enter pet species: ")
                AC.add_pet(pet_name,pet_species)
                continue
            except ValueError:
                print("pet name  and pet species must be string")
        
        elif op == 2:
            AC.view_available()
        elif op == 3:
            try:
                pet_name = input("Enter pet name: ")
                AC.adopt_pet(pet_name)
                continue
            except ValueError:
                print("pet name must be string")
        elif op == 4:
            try:
                pet_name = input("Enter pet name: ")
                AC.return_adopt_pet(pet_name)
                continue
            except ValueError:
                print("pet name must be string")
        elif op == 5:
            print("Thanks for visiting")
            break
    except ValueError:
        print("Option must be integer")
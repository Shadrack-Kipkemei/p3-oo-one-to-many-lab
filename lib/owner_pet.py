class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return the list of pets owned by the owner."""
        return [pet for pet in Pet.all if isinstance(pet.owner, Owner) and pet.owner == self]

    def add_pet(self, pet):
        """Adds a pet to the owner. Raises an exception if the pet is not of type Pet."""
        if not isinstance(pet, Pet):
            raise Exception("The pet must be of type Pet.")
        pet.owner = self

    def get_sorted_pets(self):
        """Returns a sorted list of pets by their names."""
        return sorted(self.pets(), key=lambda pet: pet.name)

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type. Allowed types are: {', '.join(Pet.PET_TYPES)}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        if owner and not isinstance(owner, Owner):
            raise Exception("Owner must be of type Owner.")
        
        # Add pet to the class-level `all` list
        Pet.all.append(self)
        
        if owner:
            owner.add_pet(self)


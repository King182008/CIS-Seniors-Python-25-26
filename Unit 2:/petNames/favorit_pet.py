# a script favorite_pet.py that imports and uses the pet_names module

import pet_names #imports the pet_names

print("my favorite is", pet_names.pet_name1, "-")
print("I remember when he weighted only", pet_names.pet_weight, "pounds")
print("I love", pet_names.pet_name2, "too, of course")

if __name__ == "__main__":
    print("This is the __main__ code from favorite_pet.py")
def discoverAnimal(animal):
    if animal[1] == "ave" and animal[-1] == "carnivoro":
        return "aguia"
    elif animal[1] == "ave" and animal[-1] == "onivoro":
        return "pomba"
    elif animal[1] == "mamifero" and animal[-1] == "onivoro":
        return "homem"
    elif animal[1] == "mamifero" and animal[-1] == "herbivoro":
        return "vaca"
    elif animal[1] == "inseto" and animal[-1] == "hematofago":
        return "pulga"
    elif animal[1] == "inseto" and animal[-1] == "herbivoro":
        return "lagarta"
    elif animal[1] == "anelideo" and animal[-1] == "hematofago":
        return "sanguessuga"
    elif animal[1] == "anelideo" and animal[-1] == "onivoro":
        return "minhoca"


animal = [input().strip(), input().strip(), input().strip()]

print(discoverAnimal(animal))

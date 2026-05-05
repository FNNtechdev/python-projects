class Planet:
    def __init__(self, name, planet_type, star):
        if not all(isinstance(attr, str) for attr in [name, planet_type, star]):
            raise TypeError("name, planet type, and star must be strings")
        
       
        if not all(len(attr.strip()) > 0 for attr in [name, planet_type, star]):
            raise ValueError("name, planet_type, and star must be non-empty strings")

       
        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."

    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"


planet_1 = Planet("Earth", "Terrestrial", "the Sun")
planet_2 = Planet("Jupiter", "Gas Giant", "the Sun")
planet_3 = Planet("Proxima Centauri b", "Super-Earth", "Proxima Centauri")


print(planet_1)
print(planet_2)
print(planet_3)


print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())

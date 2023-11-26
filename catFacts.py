import requests
class Cat:
    def __init__(self, age, breed):
        self.age = age
        self.breed = breed

    def get_age(self):
        return self.age
    
    def get_breed(self):
        return self.breed
    
    def get_new_breed(self, n):
        breeds = []
        for i in range(n):
            result = requests.get('https://catfact.ninja/breeds').json()
            breeds.extend([cat['breed'] for cat in result['data']])
        self.breed = breeds[-1]
        return self.breed

my_cat = Cat(10, "Black")
print(my_cat.get_age())
print(my_cat.get_breed())
print(my_cat.get_new_breed(7))
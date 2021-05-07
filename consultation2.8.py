class Plane:
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f'Plane brand {self.brand}, {self.model}', end=' ')

class Destroyer(Plane):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.can_fire = True
        print(f'Airplane {self.brand} {self.model}, can fire = {self.can_fire}')

    def fire(self):
        return(f'This airplane can fire {self.can_fire}')

class Stelth(Plane):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.is_visible = False

    def hide(self):
        return(f'This airplane {self.brand} {self.model}, can hide anywhere = {self.is_visible}')

class Kukuruznik(Plane):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.can_fertilize = True
        print(f'This airplane can fertilize {self.can_fertilize}')

    def fertilize(self):
        return(f'This airplane is good for farms because he can {self.can_fertilize}')

d = Destroyer('FirePlane', 'F-2')
print(d.fire())
s = Stelth('IlonPLane', 'Stelth-1')
print(s.hide())
k = Kukuruznik('PopcornPLane', 'Eagle')
print(k.fertilize())
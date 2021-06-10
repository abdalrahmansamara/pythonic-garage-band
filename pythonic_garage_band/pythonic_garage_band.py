from abc import abstractmethod


class Musician():

     def __init__(self,arr):
        self.members = arr

     @abstractmethod
     def __str__(self):
         pass
     @abstractmethod
     def __repr__(self):
         pass
     @abstractmethod
     def get_instrument(self):
         pass
     @abstractmethod
     def play_solo(self):
         pass


class Band(Musician):
    instances = []
    def __init__(self,name,arr):
        self.name=name
        super().__init__(arr)
        Band.instances.append(self)
    @classmethod
    def to_list(cls):
        return cls.instances
    def play_solos(self):
        solos=[]
        for i in self.members:
            solos.append(i.play_solo())
        return solos
    def __str__(self):
        return f'our name is {self.name}, and we rock'
    def __repr__(self):
        return f"Band instance. Name = {self.name}"




class Guitarist(Musician):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    @staticmethod
    def get_instrument():
        return "guitar"
    @staticmethod
    def play_solo():
        return "face melting guitar solo"
        

# return super().get_instrument()

class Drummer(Musician):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"My name is {self.name} and I play drums"
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    @staticmethod
    def get_instrument():
        return "drums"
    @staticmethod
    def play_solo():
        return "rattle boom crash"
    

class Bassist(Musician):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"My name is {self.name} and I play bass"
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    @staticmethod
    def get_instrument():
        return "bass"
    @staticmethod
    def play_solo():
        return "bom bom buh bom"
    

# members = [
#     Guitarist("Kurt Cobain"),
#     Bassist("Krist Novoselic"),
#     Drummer("Dave Grohl"),
# ]

# some_band = Band("Nirvana", members)
# some_band.play_solos()
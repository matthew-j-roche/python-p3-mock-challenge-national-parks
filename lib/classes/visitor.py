class Visitor:

    def __init__(self, name):
        if isinstance(name, str) and 1 <= len(name) <=15:
            self._name = name
        else:
            raise Exception("Name must be a string")
        
    @property
    def name(self):
        return self._name
        
    def trips(self):
        from classes.trip import Trip
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        from classes.national_park import NationalPark
        return list(set([trip.national_park for trip in self.trips()]))
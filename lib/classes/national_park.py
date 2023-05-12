



class NationalPark:

    def __init__(self, name):
        if isinstance(name, str) and name:
            self._name = name
        else:
            raise Exception("Name must be a string")
    
    @property
    def name(self):
        return self._name
    
        
    def trips(self):
        from classes.trip import Trip
        return [trip for trip in Trip.all if trip.national_park == self]
    

    def visitors(self):
        return list(set([trip.visitor for trip in self.trips()]))
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visitors = [t.visitor for t in self.trips()]
        return max(visitors, key=visitors.count)
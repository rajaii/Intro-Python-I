# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

l = LatLon(44.052137, -121.41556)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.name = name
    
    def __str__(self):
        return '{self.name}, {self.lat}, {self.lon}'.format(self=self)

# YOUR CODE HERE

w = Waypoint(l, l, "Newberry Views")

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, lat, lon, name, size, difficulty):
        super().__init__(lat, lon, name)
        self.size = size
        self.difficulty = difficulty

    def __str__(self):
        return '{self.lat}, {self.lon}, {self.name}, {self.size}, {self.difficulty}'.format(self=self)
    
    

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

n = Waypoint(41.70505, -121.51521, "Catacombs")


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(Waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
g = Geocache(n, n, n, 'diff 2', 'size 1.5')

# YOUR CODE HERE

# Print it--also make this print more nicely
print(Geocache)
print(g)


class Colors:
    blue = '\033[0;94m'
    red = '\033[0;91m'
    green = '\033[0;92m'
    nc = '\033[0m'


class Chain:
    def __init__(self, north=None, south=None, east=None, west=None):
        self.north = north
        self.south = south
        self.left = east
        self.right = west
        if north is not None:
            north.south = self
        if south is not None:
            south.north = self
        if east is not None:
            east.west = None
        if west is not None:
            west.east = None


class Location:
    def __init__(self, name, visited, view, ooi, chain):
        self.name = name
        self.visited = visited
        self.view = view
        self.ooi = ooi
        self.chain = chain


class ObjectOfInterest:
    def __init__(self, name, desc, used_with):
        self.name = name
        self.desc = desc
        self.used_with = used_with




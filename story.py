import models

'''
Every Location has:
    name - str
    visited (has the user come here before?) - bool
    view (text that shows up when a user enters the view command) - str
    ooi (objects of interest on the location) - list of ObjectOfInterest objects
    chain (locations to the north/west/east/south) - Chain object

Every object has:
    name - str
    descrip (the text that shows up when user enters the examine command) - str
    used_with (like key can have lock as its used_with) - a list of ObjectOfInterest objects
'''

forest = models.Location
cave = models.Location

beach = models.Location(name="Beach", visited=False, view="A beach with bright sunlight and waves crashing on the"
                                                         "shore. Straight ahead is a forest, while to the right"
                                                         "is a cave. The cave gives off an eerie vibe.",
                        ooi=['rock', 'broken boat'], chain=models.Chain(north=forest, west=cave))

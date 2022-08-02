class car(object):
    def __init__(self, color, doors, tires):
        self.color = color
        self.doors = doors
        self.tires = tires
    def brake(self):
       """
        Stop the car
        """
       return "Braking"
    def drive(self):
        """
        Drive the car
        """
        return "I’m driving!"

    def paint(self):
        """
        Paint the car
        """
        return "Grtting some paint"

        pass

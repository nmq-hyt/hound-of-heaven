# since all integers are either even or odd
# we can use the monotonically increasing series of numbers
# to split turns
# with the hounds going first
class TurnCounter():

    def __init__(self):
        self.count = 0

    def whoseTurn(self):
        return (self.count % 2)

    def incrementcount(self):
        self.count = self.count + 1
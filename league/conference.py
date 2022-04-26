from league import division

class Conference:

    North = division.Division()
    South = division.Division()
    East = division.Division()
    West = division.Division()

    def __init__(self, North, South, East, West):
        self.North = North
        self.South = South
        self.East = East
        self.West = West

    # Design Conference Standings
    # - This along with Division standings is likely only important for the playoff
    #   schedule 
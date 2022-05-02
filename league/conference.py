from league.division import Division

class Conference:

    """North = Division()
    South = Division()
    East = Division()
    West = Division()"""

    def __init__(self, East, North, South, West):
        self.North = North
        self.South = South
        self.East = East
        self.West = West

    # Design Conference Standings
    # - This along with Division standings is likely only important for the playoff
    #   schedule 
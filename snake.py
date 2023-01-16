from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
class Snake:
    
    def __init__(self) -> None:
        self.segments = []
        self.length = len(self.segments)
        self.create_snake()


    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape = "square")
            new_segment.up()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)
    

    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_position = self.segments[seg-1].position()
            self.segments[seg].goto(new_position)
        self.segments[0].forward(MOVE_DISTANCE)

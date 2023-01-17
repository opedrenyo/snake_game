from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    
    def __init__(self) -> None:
        self.segments = []
        self.length = len(self.segments)
        self.create()
        self.head = self.segments[0]
        


    def create(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape = "square")
            new_segment.up()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)
    
    ## MOVE AND ONKEY METHODS
    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_position = self.segments[seg-1].position()
            self.segments[seg].goto(new_position)
        self.head.forward(MOVE_DISTANCE)


    def right(self):
        if self.head.heading() == UP or self.head.heading() == DOWN:
            self.head.setheading(RIGHT)


    def left(self):
        if self.head.heading() == UP or self.head.heading()== DOWN:
            self.head.setheading(LEFT)


    def up(self):
        if self.head.heading() == RIGHT or self.head.heading()== LEFT:
            self.head.setheading(UP)

        
    def down(self):
        if self.head.heading() == RIGHT or self.head.heading() == LEFT:
            self.head.setheading(DOWN)

    def eats(self):
        
        new_segment = new_segment = Turtle(shape = "square")
        new_xcor = self.segments[-1].xcor()
        new_ycor = self.segments[-1].ycor()
        new_segment.up()
        new_segment.color("white")
        if self.head.heading() == UP:
            new_segment.goto(new_xcor,new_ycor -20)
        elif self.head.heading() == DOWN:
            new_segment.goto(new_xcor,new_ycor +20)
        elif self.head.heading() == LEFT:
            new_segment.goto(new_xcor +20,new_ycor)
        elif self.head.heading() == RIGHT:
            new_segment.goto(new_xcor -20,new_ycor)
        self.segments.append(new_segment)

    def collision(self):


    



import random as r
from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_MARGIN = 40
MAX_DICE = 256
DICE_LOWER_CAP = 228
PLAYER_X_PADDING = 10
PLAYER_Y_PADDING = 20
CAR_X_PADDING = 20
CAR_Y_PADDING = 10


class CarManager:

    def __init__(self, max_coordinate):
        self.max_coordinate = max_coordinate
        self.car_speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def maybe_create_car(self):
        """
        Create a car with random chance
        """
        dice_roll = r.randint(0, MAX_DICE+1)
        if dice_roll > DICE_LOWER_CAP:
            color = r.choice(COLORS)
            start_x = self.max_coordinate - CAR_MARGIN
            start_y = r.randint(-self.max_coordinate+CAR_MARGIN, self.max_coordinate-CAR_MARGIN)
            self.cars.append(Car(self.car_speed, color, start_x, start_y))

    def blacklist_cars(self):
        """
        Blacklist cars that have surpassed the left edge of the screen to remove them
        """
        blacklist = []
        for car in self.cars:
            if car.xcor() < -self.max_coordinate:
                blacklist.append(car)
        for car in blacklist:
            car.reset()
            car.clear()
            car.hideturtle()
            self.cars.remove(car)

    def next_level(self):
        """
        Increase speed of cars for next level
        """
        for car in self.cars:
            car.reset()
            car.clear()
            car.hideturtle()
        self.cars = []
        self.car_speed += MOVE_INCREMENT

    def move_cars(self):
        """
        Move all cars forward
        """
        for car in self.cars:
            car.move()

    def player_collided_with_car(self, player):
        """
        Check if a car has collided with the player by comparing their hitboxes
        """
        player_has_collided = False
        for car in self.cars:
            car_left_x = car.xcor() + CAR_X_PADDING
            car_right_x = car.xcor() - CAR_X_PADDING
            car_top_y = car.ycor() + CAR_Y_PADDING
            car_bottom_y = car.ycor() - CAR_Y_PADDING

            player_left_x = player.xcor() + PLAYER_X_PADDING
            player_right_x = player.xcor() - PLAYER_X_PADDING
            player_top_y = player.ycor() + PLAYER_Y_PADDING
            player_bottom_y = player.ycor() - PLAYER_Y_PADDING

            player_and_car_overlap_x = car_left_x > player_right_x and car_right_x < player_left_x
            player_and_car_overlap_y = car_top_y > player_bottom_y and car_bottom_y < player_top_y

            if player_and_car_overlap_x and player_and_car_overlap_y:
                player_has_collided = True
        return player_has_collided

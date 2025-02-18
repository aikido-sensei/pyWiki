import time


class Car(object):
    """
    Abstracts a car. It is meant to have all the functionalities of an actual car.
    """

    def __init__(self) -> None:
        self.__engine_on: bool = False
        self.__speed_in_kmph: float = 0
        self.max_speed_in_kmph = 0


    @staticmethod
    def get_type() -> str:
        return "Car"

    def set_engine_on(self, engine_on: bool) -> None:
        """
        Set the state of the engine.
        :param engine_on: Engine state as a boolean value. If True, it means the engine is ON, else it is OFF.
        """
        self.__engine_on = engine_on

    def get_engine_on(self) -> bool:
        """
        Get the state of the engine.
        :return: True if engine is ON, else False.
        """
        return self.__engine_on

    def set_speed_in_kmph(self, speed_in_kmph: float) -> None:
        """
        Set speed of the car in kmph.
        :param speed_in_kmph: Speed of car in kmph.
        """
        # TODO: Input validation. Check if the speed_in_kmph variable contains valid values.
        if speed_in_kmph < 0:
            raise AttributeError("Can't set the speed to a negative value.")

        if not self.__engine_on:
            raise AttributeError("Cannot set speed when engine isn't ON!")

        elif not self.is_speed_possible(speed_in_kmph):
            raise AttributeError(f"Cannot set speed ({speed_in_kmph} kmph) as it's not attainable!")


    def get_speed_in_kmph(self) -> float:
        """
        Get the speed of the car in kmph.
        :return: The speed of the car in kmph.
        """
        return self.__speed_in_kmph

    """
    TODO: Add functionality to brake. Braking reduces the speed by 5kmph per second. Two brake methods. 
    One to got to desired speed. Another to brake for specified duration.
    """

    def brake_to_speed(self, desired_speed: float) -> None:
        """
        This function makes the car brake at a rate of 5kmph/s until the car is at the desired speed.
        :param desired_speed: speed at which you want the car to be. 
        """
        if desired_speed > self.__speed_in_kmph:
            raise AttributeError("Cannot brake to a higher speed")

        if desired_speed < 0:
            raise AttributeError("Cannot brake to a speed lower than 0 kmp/h")

        time.sleep((self.__speed_in_kmph - desired_speed) / 5)
        self.__speed_in_kmph = desired_speed

    def brake_for(self, time_in_seconds: int) -> None:
        """
        Brake at a rate of 5kmph/s for a certain duration.
        Time: Is the duration for which you want to brake. 
        """

        time.sleep(time_in_seconds)
        self.__speed_in_kmph = int(max(self.__speed_in_kmph - time * 5, 0))

    def get_manufacturer(self) -> str:
        """
        Returns the manufacturer name.
        :return: Manufacturer name.
        """
        raise NotImplementedError

    def get_max_speed_in_kmph(self) -> float:
        """
        Returns the maximum speed of the car.
        :return: The maximum speed of the car.
        """
        return self.max_speed_in_kmph

    def is_speed_possible(self, speed: float) -> bool:
        """
        Returns if the specified speed is attainable by the car.
        :param speed: Speed to attain.
        :return: True if speed is attainable, else False.
        """
        # TODO: Implement negative and over max speed checks.
        raise NotImplementedError


if __name__ == '__main__':
    car1: Car = Car()
    print(Car.get_type())
    print(car1.get_engine_on())
    print(car1.get_speed_in_kmph())

    # car.set_speed_in_kmph(100) # Raises an error as car speed cannot be set when engine isn't ON.

    car1.set_engine_on(True)
    car1.set_speed_in_kmph(100)
    print(car1.get_engine_on())
    print(car1.get_speed_in_kmph())

    car2: Car = Car()
    print(car2.get_engine_on())
    print(car2.get_speed_in_kmph())

    time.sleep(1)

    car1.brake_to_speed(80)
    print(car1.get_speed_in_kmph)

    car1.brake_for(5)
    print(car1.get_speed_in_kmph)



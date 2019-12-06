class Director(object):
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_car(self):
        car = Car()

        # For the body
        body = self.__builder.get_body()
        car.set_body(body)

        # For the engine
        engine = self.__builder.get_engine()
        car.set_engine(engine)

        # For the four wheels
        for i in range(4):
            wheel = self.__builder.get_wheel()
            car.attach_wheel(wheel)

        return car


class Car(object):
    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def set_body(self, body):
        self.__body = body

    def attach_wheel(self, wheel):
        self.__wheels.append(wheel)

    def set_engine(self, engine):
        self.__engine = engine

    def specification(self):
        print("body: %s" % self.__body.shape)
        print("enginer horsepower: %s" % self.__engine.horsepower)
        print("tire size: %s" % self.__wheels[0].size)


class Builder:
    def get_wheel():
        pass

    def get_engine():
        pass

    def get_body():
        pass


class JeepBuilder(Builder):

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def get_engine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def get_body(self):
        body = Body()
        body.shape = "SUV"
        return body


# Car Parts
class Wheel():
    size = None


class Engine():
    horsepower = None


class Body():
    shape = None


def main():
    jeep_builder = JeepBuilder()

    director = Director()

    print("Jeep!")
    director.set_builder(jeep_builder)
    jeep = director.get_car()
    jeep.specification()


if __name__ == "__main__":
    main()

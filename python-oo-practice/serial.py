"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        self.start = self.next = start

    def __repr__(self):
        return f"Serial Generator: Start = {self.start} Next = {self.start + 1}"

    def generate(self):
        self.next += 1
        return self.next

    def reset(self):
        return self.start

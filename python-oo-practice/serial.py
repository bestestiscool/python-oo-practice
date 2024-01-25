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
    def __init__(self,start):
        self.start = start
        self.current = start

    def generate(self):
        current_number = self.current  # Store the current number
        self.current += 1  # Increment for the next call
        return current_number 
    
    def reset(self):
        self.current = self.start


serial = SerialGenerator(start=100)
print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.generate())
print(serial.generate())
serial.reset()
print(serial.generate())
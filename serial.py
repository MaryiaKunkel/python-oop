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
    def __init__(self, start=0):
        '''Initialising the class SerialGenerator with a starting value'''
        self.start=self.next=start

    def __repr__(self):
        return f'SerialGenerator start={self.start}, next={self.next}'

    def generate(self):
        '''Increasing a starting value by 1'''
        self.next+=1
        return self.next-1

    def reset(self):
        '''Resetting the starting value back to 100'''
        self.next=self.start

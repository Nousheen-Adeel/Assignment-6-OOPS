class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Usage
m = Multiplier(3)

print(callable(m))     # Check if object is callable → True
print(m(5))            # Call object like a function → 15

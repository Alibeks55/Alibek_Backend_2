class Distance:
    conversion_factors = {"cm": 0.01, "m": 1, "km": 1000}

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    def __add__(self, other):
        total_meters = self.value * self.conversion_factors[self.unit] + \
                       other.value * self.conversion_factors[other.unit]
        new_value = total_meters / self.conversion_factors[self.unit]
        return Distance(new_value, self.unit)

    def __sub__(self, other):
            total_meters = self.value * self.conversion_factors[self.unit] - \
                           other.value * self.conversion_factors[other.unit]
            if total_meters < 0:
                total_meters = 0
            new_value = total_meters / self.conversion_factors[self.unit]
            return Distance(new_value, self.unit)

    def __eq__(self, other):
        return self.value * self.conversion_factors[self.unit] == \
         other.value * self.conversion_factors[other.unit]

    def __lt__(self, other):
        return self.value * self.conversion_factors[self.unit] < \
        other.value * self.conversion_factors[other.unit]

    def __le__(self, other):
        return self.value * self.conversion_factors[self.unit] <= \
        other.value * self.conversion_factors[other.unit]

    def __gt__(self, other):
        return self.value * self.conversion_factors[self.unit] > \
        other.value * self.conversion_factors[other.unit]

    def __ge__(self, other):
        return self.value * self.conversion_factors[self.unit] >= \
         other.value * self.conversion_factors[other.unit]



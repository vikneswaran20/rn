import random
import click


class Numbers:

    def __init__(self, range, iteration, delimiter, unique, sort, precision):
        self.min = range[0]
        self.max = range[1]
        self.iteration = iteration
        self.delimiter = delimiter
        self.unique = unique
        self.sort = sort
        self.precision = precision
        self.precision_str = '{:.%sf}' % self.precision

    def generate_random(self):
        nums = self.get_numbers()
        self.apply_sort(nums)
        nums = map(str, nums)
        return self.delimiter.join(nums)

    def get_numbers(self):
        if self.unique:
            self.get_unique_numbers()

        return [self.precision_str.format(round(random.uniform(self.min, self.max), self.precision))
                if self.precision is not None else random.randint(int(self.min), int(self.max))
                for i in range(self.iteration)]

    def get_unique_numbers(self):
        try:
            if self.precision is not None:
                factor = (10 * self.precision)
                local_min = int(self.min * factor)
                local_max = int((self.max + 1) * factor)
                return [self.precision_str.format(round(num/factor, self.precision))
                        for num in random.sample(range(local_min, local_max), self.iteration)]

            return random.sample(
                range(int(self.min), int(self.max) + 1), self.iteration)
        except ValueError:
            raise click.BadParameter(
                "No of iterations are greater than the given range"
                + " with uniq enabled")

    def apply_sort(self, nums):
        if self.sort is not None:
            nums.sort(reverse=(self.sort == 'desc'))

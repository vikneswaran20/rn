import random
import click


class Numbers:

    def __init__(self, range, iteration, delimiter, uniq, sort):
        self.min = range[0]
        self.max = range[1]
        self.iteration = iteration
        self.delimiter = delimiter
        self.uniq = uniq
        self.sort = sort

    def genrate_random(self):
        nums = self.getNumbers()
        self.apply_sort(nums)
        nums = map(str, nums)
        return self.delimiter.join(nums)

    def getNumbers(self):
        if self.uniq:
            try:
                return random.sample(
                    range(self.min, self.max+1), self.iteration)
            except ValueError:
                raise click.BadParameter(
                    "No of iterations are greater than the given range"
                    + " with uniq enabled")

        return [random.randint(self.min, self.max)
                for i in range(self.iteration)]

    def apply_sort(self, nums):
        if self.sort is not None:
            nums.sort(reverse=(self.sort == 'desc'))

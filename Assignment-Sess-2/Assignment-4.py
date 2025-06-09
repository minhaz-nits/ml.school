#Create a flow that takes a list of numbers as a parameter. Use a foreach loop to square 
#each number in a separate step. In the join step, collect the squared results and print 
#both the full list and the total sum.

from metaflow import FlowSpec, step

class Foreach(FlowSpec):
    """A flow that showcases how the foreach works."""

    @step
    def start(self):
        """Initialize the list of numbers as artifact."""
        self.num = [3,4,5]
        self.next(self.square, foreach="num")

    @step
    def square(self):
        """Square the input number."""
        num_sqr = self.input * self.input  or 0
        print("Start value:", num_sqr)
        self.sqr = num_sqr
        print(f'Turned "{self.input}" into "{self.sqr}"')

        self.next(self.join)

    @step
    def join(self, inputs):
        """Join the results of the foreach."""
        self.num = [i.sqr for i in inputs]
        self.final_value = sum(i.sqr for i in inputs)
        self.next(self.end)

    @step
    def end(self):
        """Print the final list of people."""
        print("People:", self.num, self.final_value)


if __name__ == "__main__":
    Foreach()

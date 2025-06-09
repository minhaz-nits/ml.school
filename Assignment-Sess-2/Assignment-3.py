# Create a flow that starts initializing an artifact with a numerical value. Then split 
# into two predetermined parallel branches, where the first branch adds a constant to 
# the artifact and the second branch multiplies the artifact by a constant. In a subsequent
# join step, merge the results by printing both branch outcomes and computing the sum of 
# the two outcomes.

from metaflow import FlowSpec, step

class Artifacts(FlowSpec):
    """A flow that showcases how artifacts work."""

    @step
    def start(self):
        """Initialize the variable."""
        self.start_value = 5
        #print("Initial value:", self.variable)
        self.next(self.addition,self.multiplication)

    @step
    def addition(self):
        """Add the value of the variable."""
        print("Add the value of the variable")
        self.common = self.start_value + 5
        self.next(self.join)

    @step
    def multiplication(self):
        """Multiply the value of the variable."""
        print("Multiply the value of the variable")
        self.common = self.start_value * 5
        self.next(self.join)

    @step
    def join(self, inputs):
        """Join the two branches."""
        self.merge_artifacts(inputs, exclude=["common"])

        print("Step 1's artifact value:", inputs.addition.common)
        print("Step 2's artifact value:", inputs.multiplication.common)

        self.final_value = sum(i.common for i in inputs)
        self.next(self.end)


    @step
    def end(self):
        """Print the final value of the variable."""
        print("Start value:", self.start_value)
        print("Final value:", self.final_value)


if __name__ == "__main__":
    Artifacts()

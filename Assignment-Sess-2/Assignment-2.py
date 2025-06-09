#Create a simple flow that tracks a sequence of numerical operations. In the first step, 
# initialize an artifact with a number. In each subsequent step, update the artifact by 
# applying a different arithmetic operation (e.g., addition, subtraction, multiplication) 
# and append each new value to a list. In the final step, print the entire history of 
# values and calculate both the sum and average.

from metaflow import FlowSpec, step

class Artifacts(FlowSpec):
    """A flow that showcases how artifacts work."""

    @step
    def start(self):
        """Initialize the variable."""
        self.variable = 1
        self.var_2 = 2
        print("First value:", self.variable)
        print("2nd value:", self.var_2)
        self.next(self.addition)

    @step
    def addition(self):
        """Add the value of the variable."""
        print("Add the value of the variable")
        self.var_add = self.variable + self.var_2
        self.next(self.substraction)
    
    @step
    def substraction(self):
        """Substract the value of the variable."""
        print("Substract the value of the variable")
        self.var_subs = self.var_2 - self.variable
        self.next(self.multiplication)

    @step
    def multiplication(self):
        """Multiply the value of the variable."""
        print("Multiply the value of the variable")
        self.var_mul = self.var_2 * 5
        self.next(self.divison)

    @step
    def divison(self):
        """Divide the value of the variable."""
        print("Divide the value of the variable")
        self.var_div = 10 / self.var_2
        self.next(self.end)


    @step
    def end(self):
        """Print the final value of the variable."""
        print("Addition value:", self.var_add)
        print("Substraction value:", self.var_subs)
        print("Multiplication value:", self.var_mul)
        print("Divison value:", self.var_div)


if __name__ == "__main__":
    Artifacts()

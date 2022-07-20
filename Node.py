import random


class Node_t:

    def __init__(self, weights, output):
        self.weights = weights
        self.hidden_weights = [random.uniform(-0.1, 0.1) for x in range(len(weights))]
        self.output = output
        self.ile_weights = len(weights)

    def learn_node(self, inputs, learn_rate):
        output = 0
        for i in range(self.ile_weights):
            output += self.weights[i] * inputs[i]

        self.output = output

        for i in range(self.ile_weights):  # exp output
            self.weights[i] = self.weights[i] + learn_rate * inputs[i] * (inputs[self.ile_weights] - self.output)

        return self.output

    def activate_node(self):

        for i in range(self.ile_weights):
            if self.weights[i] < 0:
                self.weights[i] = 0

    def display(self):
        for i in range(self.ile_weights):
            print(f"weight{i}:{self.weights[i]}", end=' ')

        print(f"output:{self.output}")

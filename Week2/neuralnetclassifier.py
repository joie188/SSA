# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 10:59:42 2019

@author: Brian
"""

"""
DO NOT USE YET
 - SOMETHING IS BROKEN AND I NEED TO FIX IT
"""

import random
import numpy as np
import matplotlib.pyplot as plt

import sat_classifier as sc

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def LRAdjust(x):
    return abs(np.exp(-x)*(np.cos(5*x) + np.sin(5*x)))

class SimpleNN:
    def __init__(self, depth, layer_size, class_range, image_size):
        # Miscellaneous variables
        self.class_range = class_range
        self.image_size = image_size
        self.memo = {} # For backpropagation DP
        self.expected = 2

        # Initialize all neurons
        self.neurons = [np.array([random.random() for i in range(self.image_size)])]
        for i in range(depth):
            self.neurons.append([0 for i in range(layer_size)])
        self.neurons.append([0 for i in range(self.class_range)])
        self.size = len(self.neurons)

        # Initialize weights and biases
        self.biases = np.array([[random.uniform(-3,3) for j in range(len(self.neurons[i+1]))] for i in range(self.size-1)])
        self.weights = np.array([[[random.uniform(-3,3) for k in range(len(self.neurons[i]))]
                                          for j in range(len(self.neurons[i+1]))]
                                          for i in range(self.size - 1)])

    # The feed-forward stage
    def loadInput(self, data):
        data_copy = [i for i in data]
        self.neurons[0] = data_copy

    def feedForward(self):
        for i in range(self.size - 1):
            a = np.matmul(self.weights[i], self.neurons[i]) + self.biases[i]
            self.neurons[i+1] = sigmoid(a)

    def calculateError(self):
        error = 0
        for i in range(self.class_range):
            diff = 1 if i == self.expected else 0
            error += (diff-self.neurons[-1][i])**2
        return error

    # Helper functions to calculate partial derivatives for backprop
    def dcda(self, a_index):
        target_neuron = self.neurons[-1][a_index]
        diff = 1 if a_index == self.expected else 0
        return 2*(target_neuron - diff)

    def dada(self, layer, index1, index2):
        weight = self.weights[layer-1][index1][index2]
        activation = self.neurons[layer][index1]
        return weight*activation*(1-activation)

    def dadw(self, layer, source_index, target_index):
        src_neuron = self.neurons[layer-1][source_index]
        trgt_neuron = self.neurons[layer][target_index]
        return src_neuron*trgt_neuron*(1-trgt_neuron)

    def dadb(self, layer, neuron_index):
        neuron = self.neurons[layer][neuron_index]
        return neuron*(1-neuron)

     
    def DPPartial(self, *args):
        """
        Checks if a particular derivative is memoized. If not, compute the derivative.
        Parameters:
            deriv_index: a tuple containing info about a particular partial derivative
        Returns the value of that partial derivative
        """
        if args in self.memo:
            result = self.memo[args]
        else:
            if args[0] == 'C':
                result = self.dcda(args[1])
            elif args[0] == 'w':
                result = self.dadw(args[1], args[2], args[3])
            else:
                result = self.dada(args[1], args[2], args[3])
            self.memo[args] = result
        return result

    def backProp(self, variable, n = 0, a_index = 0):
        """
        Possibly the most important helper of all...

        Computes and returns the partial derivative of C, the cost function with respect to
        a given variable.
        
        Parameters:
            variable: a tuple containing a string (w or b) and another tuple with length of either 2 or 3
            depending on the variable type whose elements denote the indices of our variable.
        """
        var_type, var_coordinate = variable
        layer_level = self.size-n
        layer_size = len(self.neurons[layer_level-1])
        neuron_index = var_coordinate[1] 
        result = 0

        # Special trivial case where weight or bias layer is the last one
        if self.size - var_coordinate[0] == 2:
            partial = self.DPPartial('C',neuron_index)
            if var_type == 'w':
                return partial * self.dadw(-1, var_coordinate[2], neuron_index)
            else:
                return partial * self.dadb(-1, neuron_index)

        # Base case
        if layer_level - var_coordinate[0] == 2:
            partial = self.DPPartial('a',layer_level,a_index,neuron_index) 
            if var_type == 'w':
                return partial*self.DPPartial('w', layer_level-1, var_coordinate[2], neuron_index)
            else:
                return partial*self.dadb(layer_level-1, neuron_index)

        # Recursive case
        else:
#            if n == 0:
#                # For starting recursive case
#                return sum(self.DPPartial('C', i)*self.backProp(variable, n+1, i) for i in range(layer_size))
#            else:
#                return sum(self.DPPartial('a', layer_level, a_index, i)*self.backProp(variable, n+1, i) for i in range(layer_size))
            for i in range(layer_size):
                # Distinguishes between starting and general recursive case
                derivative_index = ('C',i) if n == 0 else ('a',layer_level,a_index,i) 
                partial = self.DPPartial(*derivative_index)
                result += partial * self.backProp(variable, n+1, i)
            return result
        
    def doGradientDescent(self, batch_size = 1):
        for i in range(self.size - 1):
            matrix = self.weights[i]
            bias_array = self.biases[i]
            # Update biases according to gradient
            for j in range(len(bias_array)):
                yield ('b', i, j, self.backProp(('b', (i,j)))/batch_size)
            for j in range(len(matrix)):
                row = matrix[j]
                saved_grad_term = self.backProp(('w', (i,j,0)))/batch_size
                first_neuron = self.neurons[i][0]
                # Update weights according to gradient
                for k in range(len(row)):
                    if k == 0:
                        result = saved_grad_term
                    else:
                        if first_neuron != 0:
                            result = (self.neurons[i][k]/first_neuron) * saved_grad_term
                        else:
                            result = self.backProp(('w', (i,j,k)))/batch_size
                            first_neuron = result
                    yield ('w', i, j, k, result)
                    
                    
                    
def do_training(rounds, batch_size, layers, layer_size, class_range, input_size, update_interval, training_data):
    costs = []
    steps = [i for i in range(rounds)]
    
    network = SimpleNN(layers, layer_size, class_range, input_size)
    for i in range(rounds):
        print(i)
        biases = np.array([[0 for j in range(len(network.neurons[i+1]))] for i in range(network.size-1)])
        weights = np.array([[[0 for k in range(len(network.neurons[i]))]
                                          for j in range(len(network.neurons[i+1]))]
                                          for i in range(network.size - 1)])
        run_training_one_round(batch_size, network, training_data, weights, biases)
        if i % update_interval == 0:
            print('round ' + str(i) + ' out of ' +str(len(training_data)) + ' completed.')
            
    plt.plot(steps, costs)
    plt.title('Cost over training steps')
    plt.xlabel("Training steps")
    plt.ylabel("Cost")
        

def run_training_one_round(batch_size, network, training_data, weights, biases):
    '''
    Does 1 round of training with specified batch size and network
    '''
    for i in range(batch_size):
        network.loadInput(training_data[i])
        network.feedForward()
        gradients = network.doGradientDescent(batch_size)
        for j in gradients:
            if j[0] == 'w':
                weights[j[1]][j[2]][j[3]] += j[-1]
            else:
                biases[j[1]][j[2]] += j[-1]
        network.memo = {}
    network.biases -= biases
    network.weights -= weights
    
    
                   
'''ABOVE IS DEFINITION OF USEFUL CLASSES AND METHODS'''                    
                    
                    


nn = SimpleNN(3, 4, 4, 5)
training_rounds = 10
data = [[param for param in sat.orbit_param.values()] for sat in sc.sat_list]
training_data = [data[i] for i in range(len(data)) if i%5 != 0]
testing_data = [data[i] for i in range(len(data)) if i%5 == 0]

#do_training(5, 1649, 2, 15, 4, 5, 1, training_data)
    
    


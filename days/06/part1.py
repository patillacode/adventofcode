#!/usr/bin/env python


class Matrix(object):
    """docstring for Matrix"""
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.counter = 0
        self.matrix = []
        for i in range(self.dimensions):
            self.matrix.append([])
            for j in range(self.dimensions):
                self.matrix[i].append('0')

    def turn(self, action, first_point, last_point):
        for y in range(first_point[1], last_point[1] + 1):
            for x in range(first_point[0], last_point[0] + 1):
                if action == 'on':
                    self.matrix[y][x] = '1'
                else:
                    self.matrix[y][x] = '0'
        return matrix

    def toggle(self, first_point, last_point):
        for y in range(first_point[1], last_point[1] + 1):
            for x in range(first_point[0], last_point[0] + 1):
                if self.matrix[y][x] == '0':
                    self.matrix[y][x] = '1'
                else:
                    self.matrix[y][x] = '0'

    def output(self):
        for row in self.matrix:
            print ''.join(row)

    def count(self):
        for row in self.matrix:
            for light in row:
                if light == '1':
                    self.counter += 1
        return self.counter

dimensions = 1000
matrix = Matrix(dimensions)

input_text = open('input.txt')
for line in input_text:
    # split instructions line to grab each parameter
    line = line.split()
    method = line[0]
    # is it turn or is it toogle
    if method == 'turn':
        # parse points
        first_point = (int(line[2].split(',')[0]), int(line[2].split(',')[1]))
        last_point = (int(line[4].split(',')[0]), int(line[4].split(',')[1]))
        # Call method with parsed parameters
        matrix.turn(line[1], first_point, last_point)
    else:
        # parse points
        first_point = (int(line[1].split(',')[0]), int(line[1].split(',')[1]))
        last_point = (int(line[3].split(',')[0]), int(line[3].split(',')[1]))
        # Call method with parsed parameters
        matrix.toggle(first_point, last_point)

print "Number of lit lights: {0}".format(matrix.count())

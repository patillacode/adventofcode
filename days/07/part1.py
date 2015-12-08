#!/usr/bin/env python

# 'AND': &,
# 'OR': |
# 'LSHIFT': <<
# 'RSHIFT': >>
# 'NOT': ~

wires = {}


# Here I use recursion, I try to find the value of a wire
# if the value in our dict is not numeric then I parse the command
# and try to solve the wires in the command
# Like that recursively until I find a value, then that value is returned
# to the call, until we get the value we are looking for.
def solve(wire):
    # if the wire is a number then return it
    if wire.isdigit():
        return int(wire)
    # parse command stored in dictionary
    command = wires[wire]
    # if value in dcitionary is numeric the return it as an integer
    if str(command).isdigit():
        wires[wire] = int(command)
        return wires[wire]
    # this case if for commands like 'a -> b'
    # pure input from a wire to another wire
    elif len(command.split()) == 1:
        wires[wire] = solve(command)
    # NOT commands
    elif command.split()[0] == 'NOT':
        lol = solve(command.split()[1])
        wires[wire] = ~(lol)
        return wires[wire]
    # RSHIFT commands
    elif command.split()[1] == 'RSHIFT':
        wires[wire] = solve(command.split()[0]) >> int(command.split()[2])
        return wires[wire]
    # LSHIFT commands
    elif command.split()[1] == 'LSHIFT':
        wires[wire] = solve(command.split()[0]) << int(command.split()[2])
        return wires[wire]
    # AND commands
    elif command.split()[1] == 'AND':
        wires[wire] = solve(command.split()[0]) & solve(command.split()[2])
        return wires[wire]
    # OR commands
    elif command.split()[1] == 'OR':
        wires[wire] = solve(command.split()[0]) | solve(command.split()[2])
        return wires[wire]

# Here I fill the dictionary with all values/commands
input_text = open('input.txt')
for line in input_text:
    command = (line.split(' -> ')[0])
    wire = (line.split(' -> ')[1]).replace('\n', '')
    wires[wire] = command

solve('a')
print "a:{0}".format(wires['a'])

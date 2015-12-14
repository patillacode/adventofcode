#!/usr/bin/env python
import operator


# parse input data into a dictionary
def create_raindeers_data(input_file):
    input_txt = open(input_file)
    raindeers_data = {}
    for line in input_txt:
        name = line.split(' can fly ')[0]
        speed = line.split(' can fly ')[1].split()[0]
        run_time = line.split(' seconds')[0].split()[-1]
        rest_time = line.split(' seconds')[1].split()[-1]
        raindeers_data[name] = {'speed': int(speed),
                                'run_time': int(run_time),
                                'rest_time': int(rest_time)}
    return raindeers_data


def calculate_distance(time, raindeer, raindeers_data):
    # break time into cycles
    # one cycle is run_time + rest_time
    speed = raindeers_data[raindeer]['speed']
    run_time = raindeers_data[raindeer]['run_time']
    rest_time = raindeers_data[raindeer]['rest_time']
    cycle = run_time + rest_time
    # number of rounds/cycles that can be done in the given time
    rounds = time / cycle
    extra_seconds = time % cycle

    # calculate distance in those cycles
    distance = rounds * speed * run_time

    # calculate distance for the extra seconds off the cycle
    if extra_seconds < run_time:
        extra_distance = speed * extra_seconds
    else:
        extra_distance = speed * run_time

    total_distance = distance + extra_distance

    return total_distance


def total_distance(time, raindeers_data):
    distance = {}
    for name in raindeers_data.keys():
        distance[name] = calculate_distance(time, name, raindeers_data)
    return distance


def calculate_points(time, raindeers_data):
    # First calculate distance for every moment in time
    # and store it in a dictionary like:
    # distance[moment_in_time] = {raindeer_name: distance up to that moment}
    distance = {}
    for t in range(1, time + 1):
        distance[t] = {}
        for name, data in raindeers_data.iteritems():
            d = calculate_distance(t, name, raindeers_data)
            distance[t].update({name: d})

    # calculate each point based on distance for every moment in time
    points = {}
    for data in distance.values():
        # get name of the raindeer with the most distance in that moment
        name = max(data.iteritems(), key=operator.itemgetter(1))[0]
        # Add that raindeer a point
        if name in points.keys():
            points[name] += 1
        else:
            points[name] = 1

    return points

if __name__ == '__main__':
    # create data dict
    raindeers_data = create_raindeers_data('input.txt')
    # set time
    seconds = 2503
    # get total distance for each raindeer in given time
    distance = total_distance(seconds, raindeers_data)
    # get the name from where the maximum value is found
    name = max(distance.iteritems(), key=operator.itemgetter(1))[0]
    # get the maximum value
    distance = max(distance.iteritems(), key=operator.itemgetter(1))[1]
    print "(part 1) Max distance: {0} ({1})".format(distance, name)

    # get points earned for each raindeer after the given time span
    points = calculate_points(seconds, raindeers_data)
    # get the name from where the maximum value is found
    name = max(points.iteritems(), key=operator.itemgetter(1))[0]
    # get the maximum value
    points = max(points.iteritems(), key=operator.itemgetter(1))[1]
    print "(part 2) Max points: {0} ({1})".format(points, name)

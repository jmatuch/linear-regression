#!/usr/bin/env python
# coding: utf-8

# # Project: Linear Regression

# The line I will end up with will have a formula that looks like:
# ```
# y = m*x + b
# ```
# `m` is the slope of the line and `b` is the intercept, where the line crosses the y-axis.

def get_y(m, b, x):
    y = m*x + b
    return y

print(get_y(1, 0, 7) == 7)
print(get_y(5, 10, 3) == 25)

# To find the distance:
# 1. Get the x-value from the point and store it in a variable called `x_point`
# 2. Get the y-value from the point and store it in a variable called `y_point`
# 3. Use `get_y()` to get the y-value that `x_point` would be on the line
# 4. Find the difference between the y from `get_y` and `y_point`
# 5. Return the absolute value of the distance (you can use the built-in function `abs()` to do this)
# 
# The distance represents the error between the line `y = m*x + b` and the `point` given.

def calculate_error(m, b, point):
 x_point, y_point = point
 est_y = get_y(m, b, x_point)
 distance = abs(est_y - y_point)
 return distance

# Testing my function!

#this is a line that looks like y = x, so (3, 3) should lie on it. thus, error should be 0:
print(calculate_error(1, 0, (3, 3)))
#the point (3, 4) should be 1 unit away from the line y = x:
print(calculate_error(1, 0, (3, 4)))
#the point (3, 3) should be 1 unit away from the line y = x - 1:
print(calculate_error(1, -1, (3, 3)))
#the point (3, 3) should be 5 units away from the line y = -x + 1:
print(calculate_error(-1, 1, (3, 3)))

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]

# The first datapoint, `(1, 2)`, means that his 1cm bouncy ball bounced 2 meters. The 4cm bouncy ball bounced 4 meters.
# 
# As I try to fit a line to this data, we will need a function called `calculate_all_error`, which takes `m` and `b` that describe a line, and `points`, a set of data like the example above.
# 
# `calculate_all_error` should iterate through each `point` in `points` and calculate the error from that point to the line (using `calculate_error`). It should keep a running total of the error, and then return that total after the loop.

#WHY DOES CHANGING THE WORD DATAPOINTS OR POINTS IN THE FOR LOOP CHANGE HOW THIS WORKS?
def calculate_all_error(m, b, points):
    total_error = 0
    for item in points:
        temp = calculate_error(m, b, item)
        total_error += temp
    return total_error

# Testing my function!

#every point in this dataset lies upon y=x, so the total error should be zero:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 0, datapoints))

#every point in this dataset is 1 unit away from y = x + 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 1, datapoints))

#every point in this dataset is 1 unit away from y = x - 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, -1, datapoints))

#the points in this dataset are 1, 5, 9, and 3 units away from y = -x + 1, respectively, so total error should be
# 1 + 5 + 9 + 3 = 18
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(-1, 1, datapoints))

# My next step is to find the `m` and `b` that minimizes this error, and thus fits the data best!

# I'll find a line of best fit is by trial and error. I'll try a bunch of different slopes (`m` values) and a bunch of different intercepts (`b` values) and see which one produces the smallest error value for the dataset.
# 
# Using a list comprehension, I'll create a list of possible `m` values to try. Make the list `possible_ms` that goes from -10 to 10 inclusive, in increments of 0.1.

import math
def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier
possible_ms = [round_down(0.1*i, 1) for i in range(-100, 101)]

possible_bs = [round_down(0.1*i, 1) for i in range(-200, 201)]

# I'll find the smallest error. First, I will make every possible `y = m*x + b` line by pairing all of the possible `m`s with all of the possible `b`s. Then, I will see which `y = m*x + b` line produces the smallest total error with the set of data stored in `datapoint`.
# 
# First, I create the variables that we will be optimizing:
# * `smallest_error` &mdash; this should start at infinity (`float("inf")`) so that any error we get at first will be smaller than our value of `smallest_error`
# * `best_m` &mdash; we can start this at `0`
# * `best_b` &mdash; we can start this at `0`
# 
# I want to:
# * Iterate through each element `m` in `possible_ms`
# * For every `m` value, take every `b` value in `possible_bs`
# * If the value returned from `calculate_all_error` on this `m` value, this `b` value, and `datapoints` is less than our current `smallest_error`,
# * Set `best_m` and `best_b` to be these values, and set `smallest_error` to this error.
# 
# By the end of these nested loops, the `smallest_error` should hold the smallest error we have found, and `best_m` and `best_b` should be the values that produced that smallest error value.

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
def lobf(possible_ms, possible_bs, points):
    smallest_error = float('inf')
    best_m = 0
    best_b = 0
    for m in possible_ms:
        for b in possible_bs:
            e = calculate_all_error(m, b, points)
            if e < smallest_error:
                smallest_error = e
                best_m = m
                best_b = b
    return smallest_error, best_m, best_b
print(lobf(possible_ms, possible_bs, datapoints))

# Now, we can see that the line that fits the data best has an `m` of 0.3 and a `b` of 1.7:
# 
# ```
# y = 0.3x + 1.7
# ```
# 
# This line produced a total error of 5.
# 
# Using this `m` and this `b`, what will my line predict the bounce height of a ball with a width of 6 to be?

get_y(0.4, 1.6, 6)

# Our model predicts that the 6cm ball will bounce 3.5m.
# 
# Now, Reggie can use this model to predict the bounce of all kinds of sizes of balls he may choose to include in the ball pit!

# In[ ]:





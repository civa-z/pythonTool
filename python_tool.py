import csv
import numpy

def get_maxtimes_value(a):
    bin_count = numpy.bincount(a)
    max_index = numpy.argmax(bin_count)
    return max_index 


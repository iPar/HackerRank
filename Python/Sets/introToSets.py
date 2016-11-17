'''

This is the initial challenge for the 'Sets' problem set challenges within the Python Domain.

Note that the 'sys' library is imported and implemented to read from a file for local testing,
by checking for the passing in of a filename argument at the command line.  However, this file
can be uploaded to HackerRank.com directly for submittal without issue as it will handle the
raw_input method supplied by HackerRank through its web interface submittal.

'''

import sys

if len(sys.argv) > 1:                           # Checks to confirm filename argument passed in.
    f = open(sys.argv[1], "r")                  # Opens the file using argv in 'read' mode.
    N = int(f.readline().rstrip('\n'))          # Reads first and second lines of the file,
    string_input = f.readline().rstrip('\n')    #   stripping the trailing newline and casting
    f.close()                                   #   'N' to (integer) before closing file.
else:                                           # Runs 'else' statements if filename not passed in.
    N = int(raw_input())                        # Reads in raw_input from web interface (or user
    string_input = raw_input()                  #   provided CLI), cating N to (integer) type.

input_list = string_input.split()               # Splits string input (from second line) on spaces.
input_list = map(int, input_list)               # Maps list from strings into integers.

# Prints floating point division result after using the set, sum and length functions to eliminate
#   duplicates from the list, summing the resultant set and dividing the sum by the number of
#   integers in the set.
print float(sum(set(input_list))) / float(len(set(input_list)))

'''
print 'Set:'
print set(input_list)

print 'Input Received:'
print N
print input_list
'''

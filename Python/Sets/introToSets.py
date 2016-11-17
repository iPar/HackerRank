import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1], "r")
    N = int(f.readline().rstrip('\n'))
    string_input = f.readline().rstrip('\n')
    f.close()
else:
    N = int(raw_input())
    string_input = raw_input()

input_list = string_input.split()
input_list = map(int, input_list)

print float(sum(set(input_list))) / float(len(set(input_list)))

'''
print 'Set:'
print set(input_list)

print 'Input Received:'
print N
print input_list
'''

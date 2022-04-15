# // Import the library
import re

# // Read the file

def open_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    return lines
lines = open_file(file='floorplan01.txt')
# print(lines)


# // for every line that has () in the line, we will get the string between ()

def parse_rooms(lines):
    rooms = []
    for line in lines:
        room = re.findall(r'\((.*?)\)', line)
        rooms.append(room)
    return rooms
rooms = parse_rooms(lines)
# print(rooms)


# // But this list was nested Empty empty list, so we need to flatten it
def flatten_rooms_list(lines):
    newlist = []
    for i in lines:
        for sub in i:
            if sub != []:
                newlist.append(sub)
    return newlist

flatten_rooms_list = flatten_rooms_list(rooms)
print(f'Flatten rooms list: {flatten_rooms_list}')


# TODO: We need to parses the chair types on the floor plan

def parse_chairs(lines):
    chair_types = [
        'S',
        'W',
        'P',
        'C'
    ]
    chairs = []
    for line in lines:
        for chair_type in chair_types:
            if chair_type in line:
                chairs.append(line)
    return chairs
parse_chairs = parse_chairs(lines)
# print(parse_chairs)

# // Number of different chair types for the apartment

def total_chair_count(lines):
    c_count, w_count,p_count, s_count = [], [], [], []
    for i in range(len(lines)):
        c_count.append(lines[i].count('C')) 
        w_count.append(lines[i].count('W'))
        p_count.append(lines[i].count('P'))
        s_count.append(lines[i].count('S'))
        c_count1 = sum(c_count)
        s_count1 = sum(s_count)
        p_count1 = sum(p_count)
        w_count1 = sum(w_count)
    return {'C': c_count1,'P': p_count1,'S': s_count1,'W': w_count1}

chairs = total_chair_count(lines)
total_chairs = chairs['C'] + chairs['P'] + chairs['S'] + chairs['W']
print(f'Total number of chairs: {total_chairs}')
print(f'Total chair counts every kind in the apartment.: {chairs}')


# #### Trying to fine the pattern from the floor plan design by using regex horizontal boundary and vertical boundary: 
# '|', '/', or '\'
# '+' until next with number of '-' inbetween+'

def parse_horizontal_boundary(line):
    """
    spitting the lines with pattern for + until next + (not sure this will work)
    """
    horizontal_line_boundary = '\+(-*)\+'
    print(re.findall(horizontal_line_boundary, line))

for line in lines:
    parse_horizontal_boundary(line)

# vertical boundary

def parse_vertical_boundary(line):
    """
    splitting the lines with '|', '/', or '\' or if + does not follow -
    """
    vertical_line_boundary = '\|(.*)\|'
    print(re.findall(vertical_line_boundary, line))

for line in lines:
    parse_vertical_boundary(line)


# TODO: Logic
"""
Start saving if  |, \, or / or + (without -)
Stop saving line if + or - with any number of - in between

If lin
 only contains spaces, don't save
s
If line
"""

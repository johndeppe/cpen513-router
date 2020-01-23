import layout
import itertools
import collections
import copy

unmodified_layout = layout.parseInputfile('example.infile')
unmodified_layout.print_values()

# TODO move to layout.py and make part of class

sources = {} # {net_index : xy_tuple}
sinks = collections.defaultdict(list) # {net_index : [xy_tuple, ...]}
# i'm going to constrain myself to routing sink-to-source instead of doing
# sink-to-sink or source-to-sink
# positives:
#   don't have to keep track of whole net connectivity (confusing with 4+ pins)
#   fewer pin routing order permutations possible is less runtime
# negatives:
#   fewer pin routing order permutations possible might miss some routings?
for net_index, net in enumerate(unmodified_layout.nets):
    for pin_index, pin in enumerate(net):
        net_and_pin = (net_index, pin)
        if pin_index == 0:
            sources[net_index] = pin
        else:
            sinks[net_index].append(pin)
print(sources)
print(sinks)

# store the lee-moore / a* map in dict

L = copy.copy(unmodified_layout)
print(sinks[0])

def add_adjacent(coord):
    found_source = False
    (coord_x, coord_y) = coord
    adjacent = [(coord_x+1, coord_y  ),
                (coord_x-1, coord_y  ),
                (coord_x  , coord_y+1),
                (coord_x  , coord_y-1)]
    (x_size, y_size) = L.size
    for (x, y) in adjacent:
        if x >= x_size or x < 0 or y >=y_size or y < 0:
            continue
        #elif L.free():
            # insert into our thing
        #if coord = : # check to see if we hit target
        #    found_source = True
    return found_source
    

distances = collections.defaultdict(list) # {dist : [xy_tuple, ...]}

while True:
    add_adjacent(sinks[0])


        
            
    
#pick sink pin
#expand until hit source
#backtrace
#add to pile of routes

# if failed, try again with remaining permutation that does 1 first
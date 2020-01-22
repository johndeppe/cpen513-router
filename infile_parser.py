class Layout:
    def __init__(self, name=None, size=(1,1), obstacles=[], wires=[]):
        self.name = name # from filename
        self.size = size # (x,y) tuple
        self.obstacles = obstacles # list of (x,y) tuples
        self.wires = wires # list of lists of (x,y) tuples

    def console_print(self):
        print(self.name)
        print(self.size)
        print(self.obstacles)
        print(self.wires)
        #for y in range(size[1]):
            #for x in range(size[0]):
                #print('b', end='')

def parseInputfile(filename):
    with open('benchmarks/'+filename, 'rt') as f:
        name = filename # TODO strip extension
        # TODO add some parsing exception checking
        # TODO check for non-negative integers
        size = tuple( map( int, f.readline().split() ) )
        # TODO make sure len(size) == 2
        num_obstacles = int( f.readline() )
        obstacles = []
        for _ in range(num_obstacles):
            obstacle = tuple( map( int, f.readline().split() ) )
            obstacles.append(obstacle)
        num_wires = int( f.readline() )
        wires = []
        for wire_index in range(num_wires):
            wires.append([])
            # iterate over the line, extracting pins
            it = iter( map( int, f.readline().split() ) )
            # https://stackoverflow.com/questions/16789776/iterating-over-two-values-of-a-list-at-a-time-in-python
            # TODO check for odd number of pin coordinates
            num_pins = next(it)
            for val in it:
                x = val
                y = next(it)
                wires[wire_index].append( (x,y) )
        return Layout(name, size, obstacles, wires)

my_layout = parseInputfile('example.infile')
my_layout.console_print()
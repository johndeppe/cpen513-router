class Layout:
    def __init__(self, name=None, size=(1,1), obstacles=[], wires=[]):
        self.name = name # from filename
        self.size = size # (x,y) tuple
        self.obstacles = obstacles # list of (x,y) tuples
        self.wires = wires # list of lists of (x,y) tuples
        # points dict keeps track of our routing
        # Keys:   (x, y) tuples
        # Values: non-negative are wires (of that number's index)
        # Values: not present is empty, -1 is obstacle
        self.grid = {}
        for o in obstacles:
            self.grid[o] = -1
        for wire_ndx in range( len(wires) ):
            for pin in wires[wire_ndx]:
                self.grid[pin] = wire_ndx

    def print_values(self):
        print('name', self.name)
        print('size', self.size)
        print('obstacles', self.obstacles)
        print('wires', self.wires)

    def print_grid(self):
        def print_x_guide():
            # print x-coordinate guide
            print('\n  ', end='')
            for x in range(self.size[0]):
                print( str(x%10), end='')
            print('\n')

        print_x_guide()
        for y in range(self.size[1]):
            print(str(y%10)+' ', end='') # left y-coord guide
            # print grid
            for x in range(self.size[0]):
                if self.grid.get( (x,y) ) == None :
                    print('.', end='')
                elif self.grid.get( (x,y) ) == -1 :
                    print('X', end='')
                else:
                    # TODO fix for more than 10 nets
                    print( self.grid.get( (x,y) )%10, end='' )
            print( ' '+str(y%10) ) # right y-coord guide
        print_x_guide()

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
my_layout.print_values()
my_layout.print_grid()
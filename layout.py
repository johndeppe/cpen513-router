class Layout:
    def __init__(self, name=None, size=(1,1), obstacles=[], nets=[]):
        self.name = name # from filename
        self.size = size # (x,y) tuple
        self.obstacles = obstacles # list of (x,y) tuples
        self.nets = nets # list of lists of (x,y) tuples
        # grid dict keeps track of our routing
        # Keys:   (x, y) tuples
        # Values: not present is empty
        # Values: 'o' is obstacle
        # Values: '('p', number)' is a pin of that net index
        self.grid = {}
        for o in obstacles:
            self.grid[o] = 'o'
        for net_ndx in range( len(nets) ):
            for pin in nets[net_ndx]:
                self.grid[pin] = ('p', net_ndx)

    def coord(self, coordinate_tuple):
        return self.grid.get( coordinate_tuple )

    def free(self, coordinate_tuple):
        square = self.grid.get( coordinate_tuple )
        if square == None:
            return True
        else:
            return False

    def print_values(self):
        print('name', self.name)
        print('size', self.size)
        print('obstacles', self.obstacles)
        print('nets', self.nets)

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
                entry = self.grid.get( (x,y) )
                if entry == None:
                    print('.', end='')
                elif entry == 'o':
                    print('X', end='')
                elif entry[0] == 'p':
                    # TODO fix for more than 10 nets
                    print( entry[1]%10, end='' )
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
        num_nets = int( f.readline() )
        nets = []
        for net_index in range(num_nets):
            nets.append([])
            # iterate over the line, extracting pins
            it = iter( map( int, f.readline().split() ) )
            # https://stackoverflow.com/questions/16789776/iterating-over-two-values-of-a-list-at-a-time-in-python
            # TODO check for odd number of pin coordinates
            num_pins = next(it)
            for val in it:
                x = val
                y = next(it)
                nets[net_index].append( (x,y) )
        return Layout(name, size, obstacles, nets)

if __name__ == '__main__':
    my_layout = parseInputfile('example.infile')
    my_layout.print_values()
    my_layout.print_grid()

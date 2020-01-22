class Layout:
    def __init__(self, name, size, obstacles, wires):
        self.name = name # from filename
        self.size = size # (x,y) tuple
        self.obstacles = obstacles # list of (x,y) tuples
        self.wires = wires # list of lists of (x,y) tuples

class InfileParser:
    def __init__(self, filename):
        with open('benchmarks/'+filename, 'rt') as f:
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
                num_pins = next(it)
                for val in it:
                    x = val
                    y = next(it)
                    wires[wire_index].append( (x,y) )
            print("size", size)
            print("obstacles", obstacles)
            print("wires", wires)

_ = InfileParser('example.infile')
#
# eight_puzzle.py (Final Project)
#
# driver/test code for state-space search on Eight Puzzles
#
# name: 
# email:
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

from searcher import *
from timer import *

def create_searcher(algorithm, depth_limit = -1, heuristic = None):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * depth_limit - an optional parameter that can be used to
            specify a depth limit 
          * heuristic - an optional parameter that can be used to pass
            in a heuristic function
            
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(depth_limit)
## You will uncommment the following lines as you implement
## other algorithms.
    elif algorithm == 'BFS':
        searcher = BFSearcher(depth_limit)
    elif algorithm == 'DFS':
        searcher = DFSearcher(depth_limit)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(depth_limit, heuristic)
    elif algorithm == 'A*':
        searcher = AStarSearcher(depth_limit, heuristic)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, depth_limit = -1, heuristic = None):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * depth_limit - an optional parameter that can be used to
            specify a depth limit 
          * heuristic - an optional parameter that can be used to pass
            in a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')

    searcher = create_searcher(algorithm, depth_limit, heuristic)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()

def process_file(filename, algorithm, depth_limit = -1, heuristic = None):
    """ inputs: a string filename specifying the name of a text file in 
    which each line is a digit string for an eight puzzle, a string algorithm
    that specifies which state-spaced search algorithm should be used to solve
    the puzzles, an integer depth_limit that can be used to specify     
    an optional parameter for the depth limit and an optional parameter 
    heuristic which will be used to pass in a reference to the heuristic 
    function to use 
    """
    file = open(filename, 'r')
    num_puzzles = 0
    num_moves = 0
    num_tested_states = 0
    for line in file:
        line = line[:-1]
        init_board = Board(line)
        init_state = State(init_board, None, 'init')
        searcher = create_searcher(algorithm, depth_limit, heuristic)
        if searcher == None:
            return 
        
        soln = None
        try:
            soln = searcher.find_solution(init_state)
        except KeyboardInterrupt:
            print('search terminated, ', end = '')
        if soln == None:
            print(line + ':','no solution')
        else:
            print(line + ':', soln.num_moves, 'moves,', searcher.num_tested, 'states tested')
            num_puzzles += 1
            num_moves += soln.num_moves
            num_tested_states += searcher.num_tested
    print()
    print('solved', num_puzzles, 'puzzles')
    if num_puzzles != 0:
        print('average:', num_moves/num_puzzles, 'moves,', num_tested_states/num_puzzles, 'states tested')
    file.close()

   
        

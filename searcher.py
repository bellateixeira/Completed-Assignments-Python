#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Isabella Teixeira
# email: imt@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    def __init__(self, depth_limit):
        """ a constructor that connstructs a new Searcher
        object by initializing the following attributes
        """
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit
        if depth_limit == -1:
           return None

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s
    
    def should_add(self, state):
        """ takes a State object called state and returns 
        True if the called Searcher should add state to its 
        list of untested states, and False otherwise
        """
        if self.depth_limit != -1 and state.num_moves > self.depth_limit:
            return False
        elif state.creates_cycle() == True:
            return False
        else:
            return True       
    
    def add_state(self, new_state):
        """ takes a single State object called new_state 
        and adds it to the Searcher‘s list of untested states
        """
        self.states.append(new_state)
    
    def add_states(self, new_states):
        """ takes a list State objects called new_states, 
        and that processes the elements of new_states one at a time
        """
        for s in new_states:
            if self.should_add(s) == True:
                self.add_state(s)
                
    def next_state(self):
        """ chooses the next state to be tested from the list of 
        untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s

    def find_solution(self, init_state):
        """ performs a full random state-space search, 
        stopping when the goal state is found or when 
        the Searcher runs out of untested states
        """
        self.add_state(init_state)
        while len(self.states) > 0:
            self.num_tested += 1
            s = self.next_state()
            if s.is_goal() == True:
                return s
            else:
                self.add_states(s.generate_successors())
        return None
    
### Add your BFSeacher and DFSearcher class definitions below. ###

class BFSearcher(Searcher):
    """ A class for searcher objects that perform breadth-first 
    search instead of random search and inherits from the 
    Searcher object
    """
    
    def next_state(self):
        """ overrides the next_state method that is 
        inherited from Searcher
        """
        s = self.states[0]
        self.states.remove(s)
        return s

class DFSearcher(Searcher):
    """ A class for sarcher objects that perform depth-first
    search instead of random search and inherits from the Searcher
    object
    """
    
    def next_state(self):
        """ overrides the next_state method that is 
        inherited from Searcher
        """
        s = self.states[-1]
        self.states.remove(s)
        return s

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###

def h1(state):
    """ a heuristic function that takes a State object
    called state, and that computes and returns an
    estimate of how many additional moves are needed to
    get from state to the goal state
    """
    return state.board.num_misplaced()

def h2(state): 
    """ a heuristic function that takes a State object
    called state, and computes and returns a better
    estimate of the distance (how much the tiles need to move)
    to get from the current state to the goal state
    """
    return state.board.distance_from_goal()

class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    def __init__(self, depth_limit, heuristic):
        """ constructor for a GreedySearcher object
        inputs:
        * depth_limit - the depth limit of the searcher
        * heuristic - a reference to the function that should be used 
        when computing the priority of a state
        """
    # add code that calls the superclass constructor
        super().__init__(depth_limit)
        self.heuristic = heuristic

    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s
    
    def priority(self, state):
        """ takes a State object calleed state, and that 
        computes and returns the priority of that state
        """
        p = -1 * self.heuristic(state)
        return p
    
    def add_state(self, state):
        """ overrides the add_state method that is 
        inherited from Searcher
        """
        p = self.priority(state)
        self.states += [[p, state]]
        
    def next_state(self):
        """ overrides the next_state method that is inherited from 
        Searcher
        """
        s = max(self.states)
        self.states.remove(s)
        return s[-1]

### Add your AStarSeacher class definition below. ###

class AStarSearcher(GreedySearcher):
    """ A class for objects that perform an informed A* state-space 
    search on an Eight puzzle and which inherits from GreedySearcher class 
    and Searcher class
    """
    
    def priority(self, state):
        """ Overrides the priority method from the
        GreedySearcher class
        """
        p = -1 * (self.heuristic(state) + state.num_moves)
        return p
    

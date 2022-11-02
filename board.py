#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Isabella Teixeira
# email: imt@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[0] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        for r in range(0,3):
            for c in range(0,3):
                self.tiles[r][c] = int(digitstr[3 * r + c])
                if (self.tiles[r][c] == 0):
                    self.blank_r = r
                    self.blank_c = c

    ### Add your other method definitions below. ###
       
    def __repr__(self):
        """ returns a string representation of a Board object
        """
        s = ''
        for r in range(0, 3):
            for c in range(0, 3):
                if self.tiles[r][c] == 0:
                    s += '_' + ' '
                else:
                    s += str(self.tiles[r][c]) + ' '
            s += '\n'
        return s
    
    def move_blank(self, direction): #HELP - returning incorrectly
        """ takes as input a string direction that specifies 
        the direction in which the blank should move, and that 
        attempts to modify the contents of 
        the called Board object accordingly
        """
        assert(direction in ['up', 'down', 'left', 'right'])
        if direction not in ['up', 'down', 'left', 'right']:
            print('Invalid direction!')
            return False
    
        row_new = 0
        col_new = 0
        
        if direction == 'up':
            row_new = self.blank_r - 1
            col_new = self.blank_c 
            if row_new < 0 or row_new > 2:
                return False
        if direction == 'down':
            row_new = self.blank_r + 1
            col_new= self.blank_c 
            if row_new < 0 or row_new > 2:
                return False
        if direction == 'left':
            row_new = self.blank_r 
            col_new = self.blank_c - 1
            if col_new < 0 or col_new > 2:
                return False
        if direction == 'right':
            row_new = self.blank_r
            col_new = self.blank_c + 1
            if col_new < 0 or col_new > 2:
                return False 
            
        self.tiles[self.blank_r][self.blank_c] = self.tiles[row_new][col_new]
        self.tiles[row_new][col_new] = 0
        self.blank_r = row_new
        self.blank_c = col_new
        return True
    
    def digit_string(self):
        """ creates and returns a string of digits that corresponds 
        to the current contents of the called Board object's
        tiles attribute
        """
        s = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[r])):
                s += str(self.tiles[r][c])
        return s 
    
    def copy(self):
        """ returns a newly-constructed Board object that is a 
        deep copy of the called object
        """
        new_board = Board(self.digit_string())
        return new_board
    
    def num_misplaced(self):
        """ counts and returns the number of tiles in the called 
        Board object that are not where they should be in the 
        goal state
        """
        count = 0
        goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[r])):
                if self.tiles[r][c] == 0:
                    count += 0
                elif self.tiles[r][c] == goal[r][c]:
                    count += 0
                else:
                    count += 1
        return count
    
    def __eq__(self, other):
        """ returns True if the called object and the argument 
        have the same values for the tiles attribute,
        and False otherwise
        """
        return self.tiles == other.tiles 
    
    def distance_from_goal(self):
        """ calculates the 'Manhantten Distance' between the current 
        coordinates of each board tile and the goal 
        coordinates of the board tile 
        """
        distance = 0
        for x in range(3):
            for y in range(3):
                tile_value = self.tiles[x][y]
                x_goal = tile_value % 3
                y_goal = tile_value // 3
                distance += abs(x - x_goal) + abs(y - y_goal)
        return distance
            
            
                                        
    
   
   
                
            
        
    
    
    
    
    
    
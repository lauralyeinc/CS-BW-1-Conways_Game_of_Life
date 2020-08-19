class Cell:
    def __init__(self):
        # inital state dead
        # able to set and fetch new stats w/ functions
        self._status= 'Dead'

    def set_dead(self):
        self._status = 'Dead'

    def set_alive(self):
        self._status = 'Alive'
    
    def is_alive(self):
        if self._status == 'Alive':
            return True
        else:
            return False 
    
    def get_print_character(self):
        # returns characters status
        if self.is_alive():
            #alive
            return 'O'
        else:
            #dead
            return '*'
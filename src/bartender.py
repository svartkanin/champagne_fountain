from .visualization import Visualizer


class Glass:

    def __init__(self, capacity):
        """Initialize a new Glass object
        
        Args:
            capacity (int): The total capacity this glass can hold
        """
        self._capacity = capacity
        self._amount_filled = 0

    @property
    def capacity(self):
        """Retrieve the capacity of the glass
        
        Returns:
            int: Capacity
        """
        return self._capacity

    @property
    def amount_filled(self):
        """Retrieve the amount the glass is currently filled
        
        Returns:
            int: Current amount the glass is filled
        """
        return self._amount_filled

    @amount_filled.setter
    def amount_filled(self, amount):
        """Fill the glass by this amount
        
        Args:
            amount (int): New glass filling
        """
        self._amount_filled = amount

    def filled_rounded(self):
        """Retrieve the filling of the glass rounded by 2 decimals
        
        Returns:
            str: Rounded filling of the glass
        """
        return str(round(self._amount_filled, 2))

    def fillup(self, fill):
        """Add a certain amount to the current filling
        
        Args:
            fill (int): Amount to be added to the filling
        """
        self._amount_filled += fill

    def glass_repr(self, max_length):
        """Generate an ASCII representation of the glass
        
        Args:
            max_length (int): Specifies the maximum length the 
                              representation has to be scaled to,
                              so that all glasses have the same width
        
        Returns:
            str: Beautiful representation of the glass
        """
        str_amount = self.filled_rounded()
        total_fillers = ' ' * (max_length - len(str_amount))

        if len(total_fillers) % 2 == 0:
            right_filler = left_filler = total_fillers[int(
                len(total_fillers) / 2):]
        else:
            right_filler = total_fillers[:int(len(total_fillers) / 2)]
            left_filler = total_fillers[len(right_filler):]

        rim = '-' * (max_length + 2)
        str_glass = f'| {left_filler}{str_amount}{right_filler} |'

        return str_glass


class Fountain:

    def __init__(self, num_bottom_glasses, glass_capacity):
        """Create a new fountain
        
        Args:
            num_bottom_glasses (int): Specifies the number of glasses
                                      on the bottom of the fountain
            glass_capacity (int): Specifies the capacity each glass can hold
        """
        self._glass_capacity = glass_capacity
        self._total_levels = num_bottom_glasses
        self._tower = dict()
        self._overflow_table = 0

    @property
    def tower(self):
        """Return the full glass fountain
        
        Returns:
            dict: Glass fountain in dictionary representation
        """
        return self._tower

    @property
    def overflow_table(self):
        """Retrieve the amount that was spilled on the table 
           during the pouring
        
        Returns:
            int: Milliliter poured onto the table
        """
        return self._overflow_table

    def total_glasses(self):
        """Total number of glasses the fountain consists of
        
        Returns:
            int: Number of glasses in the fountain
        """
        return sum(range(1, self._total_levels + 1))

    def stack_glasses(self):
        """Build the fountain
        """
        for level in range(self._total_levels):
            self._tower[level] = []

            for position in range(level + 1):
                glass = Glass(self._glass_capacity)
                self._tower[level].append(glass)

    def pour(self, milliliter):
        """Start pouring x amount of milliliter
        
        Args:
            milliliter (int): Amount to be poured
        """
        # pour everything into the first glass and then
        # calculate the overflow from top to bottom
        self._tower[0][0].amount_filled += milliliter

        for level in range(self._total_levels):
            for position in range(level + 1):
                glass = self._tower[level][position]
                overflow = glass.amount_filled - glass.capacity

                if overflow > 0:  # overflow
                    glass.amount_filled = glass.capacity

                    # check if it's the last level of the fountain
                    if level + 1 < self._total_levels:
                        self._tower[level + 1][position].fillup(overflow / 2)
                        self._tower[level + 1][position + 1].fillup(overflow / 2)
                    else:
                        self._overflow_table += overflow


class Bartender:

    def __init__(self, num_bottom_glasses, glass_capacity):
        """Create a new bartender
        
        Args:
            num_bottom_glasses (int): Number bottom glasses to be used
            glass_capacity (int): Size of the glasses to be used
        """
        self._fountain = Fountain(num_bottom_glasses, glass_capacity)
        self._fountain.stack_glasses()
        self._visualizer = Visualizer()

    def place_order(self, milliliter):
        """Tell the bartender how many milliliter to pour
        
        Args:
            milliliter (int): Milliliters ordered and to be poured
        """
        self._milliliter = milliliter
        self._fountain.pour(milliliter)

    def display_order(self):
        """Display the result of the placed order and the 
            theoretical mess that was created on the table
        """
        tower = self._fountain.tower
        graph_fountain = self._visualizer.visualize(tower)

        text = f'\nOrder was: {self._milliliter}\n'
        text += f'Fountain total glasses: {self._fountain.total_glasses()}\n'

        overflow_table = self._fountain.overflow_table
        overflow = f'{overflow_table} milliliter were poured on the table\n'

        print(f'{text}\n{graph_fountain}\n{overflow}')

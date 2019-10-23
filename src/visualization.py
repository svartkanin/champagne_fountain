class Visualizer:

    def max_glass_length(self, tower):
        """Calculate the glass with the largest width
            so other glasses can be adjusted accordingly
        
        Args:
            tower (dict): Fountain tower
        
        Returns:
            int: Length of widest glass
        """
        glass_lengths = []
        for level in tower:
            for glass in tower[level]:
                glass_lengths.append(len(glass.filled_rounded()))

        return max(glass_lengths)

    def visualize(self, tower):
        """Build the fountain visualization
        
        Args:
            tower (dict): Fountain tower
        
        Returns:
            str: ASCII representation of the fountain
        """
        max_level = len(tower.keys())
        max_glass_length = self.max_glass_length(tower)
        output = ''

        for level in tower:
            right_shift = (max_level - len(tower[level])) / 2
            spaces = ' ' * int(right_shift * (max_glass_length + 4))
            row = spaces

            for glass in tower[level]:
                row += glass.glass_repr(max_glass_length)

            _open = False
            bottom = ''
            for s in row:
                if s == '|':
                    _open = not _open
                    if _open:
                        bottom += ' '
                        continue

                bottom += '-' if _open else ' '

            output += f'{row}\n{bottom}\n'

        return output

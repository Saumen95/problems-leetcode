class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        # directions = ['N', 'E', 'S', 'W']
        # 0 - N, 1 - E, 2 - S, 3 - W
        position_offset, obstacles = [(0, 1), (1, 0), (0, -1), (-1, 0)], set(map(tuple, obstacles))
        x, y, direction, max_distance = 0, 0, 0, 0
        for command in commands:
            if command == -2: direction = (direction - 1) % 4
            elif command == -1: direction = (direction + 1) % 4
            else:
                x_off, y_off = position_offset[direction][0], position_offset[direction][1]
                while command > 0:
                    if (x+x_off, y+y_off) not in obstacles:
                        x, y = x+x_off, y+y_off
                    command -= 1
                max_distance = max(max_distance, x**2 + y**2)
        return max_distance
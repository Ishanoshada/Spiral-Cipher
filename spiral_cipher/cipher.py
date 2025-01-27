import math
from enum import Enum
from typing import List, Tuple

class Direction(Enum):
    CLOCKWISE = 1
    COUNTERCLOCKWISE = 2

class SpiralType(Enum):
    INWARD = 1
    OUTWARD = 2

class SpiralCipher:
    def __init__(self, key: int = 1, padding_char: str = 'X'):
        self.key = key
        self.padding_char = padding_char

    def _get_grid_size(self, text: str) -> int:
        """Calculate the smallest square grid that can contain the text."""
        length = len(text)
        return math.ceil(math.sqrt(length))

    def _create_grid(self, size: int) -> List[List[str]]:
        """Create an empty grid of given size."""
        return [['' for _ in range(size)] for _ in range(size)]

    def _get_next_position(self, x: int, y: int, direction: Direction, 
                          visited: set, size: int) -> Tuple[int, int]:
        """Get next position based on direction and visited cells."""
        if direction == Direction.CLOCKWISE:
            moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        else:
            moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # left, down, right, up

        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < size and 0 <= new_y < size and 
                (new_x, new_y) not in visited):
                return new_x, new_y
        return -1, -1

    def _shift_char(self, char: str, shift: int) -> str:
        """Shift a character by the given key."""
        if char.isalpha():
            shift %= 26
            if char.islower():
                return chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                return chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        return char

    def encode(self, text: str, direction: Direction = Direction.CLOCKWISE,
               spiral_type: SpiralType = SpiralType.INWARD) -> str:
        """Encrypt text using spiral writing."""
        size = self._get_grid_size(text)
        grid = self._create_grid(size)
        visited = set()
        
        # Pad text if necessary
        text = text + self.padding_char * (size * size - len(text))
        
        # Determine starting position
        if spiral_type == SpiralType.INWARD:
            x, y = 0, 0
        else:
            x, y = size - 1, size - 1
            
        text_pos = 0
        
        # Fill the grid in spiral order
        while text_pos < len(text):
            grid[x][y] = self._shift_char(text[text_pos], self.key)
            visited.add((x, y))
            text_pos += 1
            
            next_x, next_y = self._get_next_position(x, y, direction, visited, size)
            if next_x == -1:
                break
            x, y = next_x, next_y
        
        # Generate ciphertext
        return ''.join(''.join(row) for row in grid)

    def decode(self, ciphertext: str, direction: Direction = Direction.CLOCKWISE,
               spiral_type: SpiralType = SpiralType.INWARD) -> str:
        """Decrypt spiral-encrypted text."""
        size = int(math.sqrt(len(ciphertext)))
        if size * size != len(ciphertext):
            raise ValueError("Ciphertext length must be a perfect square")
            
        # Create grid from ciphertext
        grid = [['' for _ in range(size)] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                grid[i][j] = ciphertext[i * size + j]
                
        # Read grid in spiral pattern
        result = []
        visited = set()
        
        if spiral_type == SpiralType.INWARD:
            x, y = 0, 0
        else:
            x, y = size - 1, size - 1
            
        while len(result) < len(ciphertext):
            result.append(self._shift_char(grid[x][y], -self.key))
            visited.add((x, y))
            
            next_x, next_y = self._get_next_position(x, y, direction, visited, size)
            if next_x == -1:
                break
            x, y = next_x, next_y
            
        # Remove padding and return
        return ''.join(result).rstrip(self.padding_char)

    def encrypt_file(self, input_file: str, output_file: str):
        """Encrypt a file."""
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
        encrypted = self.encode(text)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(encrypted)

    def decrypt_file(self, input_file: str, output_file: str):
        """Decrypt a file."""
        with open(input_file, 'r', encoding='utf-8') as f:
            ciphertext = f.read()
        decrypted = self.decode(ciphertext)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(decrypted)

# Helper functions for direct usage
def encode(text: str, key: int = 1) -> str:
    return SpiralCipher(key).encode(text)

def decode(ciphertext: str, key: int = 1) -> str:
    return SpiralCipher(key).decode(ciphertext)
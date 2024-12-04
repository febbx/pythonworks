def print_hollow_pyramid(height):
    for i in range(height):
        # Print leading spaces
        print(' ' * (height - i - 1), end='')

        # Print the stars and hollow spaces
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i or i == height - 1:
                print('*', end='')
            else:
                print(' ', end='')
        
        print()  # Move to the next line

# Example usage
height = 5
print_hollow_pyramid(height)

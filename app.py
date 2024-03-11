def calculate_square_tree_areas(side_lengths):
    """
    Calculate the area of square trees given their side lengths.
    
    Args:
        side_lengths (List[int]): A list of integers representing the side lengths of square trees.
    
    Returns:
        List[int]: A list of integers representing the areas of the square trees.
    """
    # Using a list comprehension to calculate areas
    return [length**2 for length in side_lengths]

# Example usage
side_lengths = [20]
areas = calculate_square_tree_areas(side_lengths)
print(areas)

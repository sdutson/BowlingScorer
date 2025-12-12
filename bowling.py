
def is_valid(delivery_value: str) -> bool:
    """
    Checks if the provided str is valid. 
    Valid being defined as, an integer in the range [0, 10]
    
    :param delivery_value: The value to check.
    :type delivery_value: str
    :return: True if the param string is valid, false otherwise. 
    :rtype: bool
    """
    return delivery_value.isdigit() and 0 <= int(delivery_value) <= 10

def is_strike(frame: tuple[int, int]) -> bool:
    """
    Checks to see if the provided frame represents a strike. 
    
    :param frame: The frame to check
    :type frame: tuple[int, int]
    :return: True is the frame represents a strike and false otherwise. 
    :rtype: bool
    """
    return frame[0] == 10

def is_spare(frame: tuple[int, int]) -> bool:
    """
   Checks to see if the provided frame represents a spare. 
    
    :param frame: The frame to check. 
    :type frame: tuple[int, int]
    :return: True if the frame represents a spare, and false otherwise. 
    :rtype: bool
    """
    return (frame[0] + frame[1]) == 10

def get_frame_values(frame_num: int) -> tuple[int, int]:
    """
    Gets the values for the provided frame number. This method 
    enforces that delivery values are integers in the range [0, 10]
    
    :param frame_num: The frame number to get from the user. 
    :type frame_num: int
    :return: The frame entered by the user. 
    :rtype: tuple[int, int]
    """
    print(f"\n\nFrame: #{frame_num}")
    # Get first delivery value. 
    delivery_one = input("\nEnter number of pins knocked down on first bowl: ")
    while not is_valid(delivery_one): 
        print("Invalid input. Input must be an integer in the range [0, 10].")
        delivery_one = input("Enter number of pins knocked down on first bowl: ")
    
    delivery_one = int(delivery_one)
    if(delivery_one == 10):
        print("You bowled a strike!")
        return (delivery_one, 0) # Strike!
    
    # Get second delivery value.
    delivery_two = input("\nEnter number of pins knocked down on second bowl: ")
    while not is_valid(delivery_two) or int(delivery_two) > 10 - delivery_one: # TODO: Make sure this cast won't cause any errors.  
        print(f"Invalid input. Input must be an integer in the range [0, {10 - delivery_one}].")
        delivery_two = input("Enter number of pins knocked down on second bowl: ")
    delivery_two = int(delivery_two)

    # Return results. 
    if(delivery_one + delivery_two == 10):
        print("Nice spare!")
    return (delivery_one, delivery_two)

def compute_game_score(frame_values: list[tuple[int, int]]) -> int:
    """
    Given the frames for a game, compute the game score. 
    
    :param frame_values: The frames from a game of bowling. 
    :type frame_values: list[tuple[int, int]]
    :return: The score of the game. 
    :rtype: int
    """
    score = 0

    for index in range(10):
        frame = frame_values[index] # Get the frame. 
        score += frame[0] + frame[1]
        if is_strike(frame) : # Strike 
            score += frame_values[index + 1][0] + frame_values[index + 1][1]
            if is_strike(frame_values[index + 1]):
                score += frame_values[index + 2][0]
        elif is_spare(frame): # Spare
            score += frame_values[index + 1][0]

    return score

if __name__ == "__main__":
    running = True
    while(running):
        print("\nLets play a game of bowling!")
        frame_values = [(0, 0)] * 12
        # Get frame values. 
        for frame in range(1, 11):
            frame_values[frame - 1] = get_frame_values(frame)

        # Get frame 11 if frame 10 was a strike or spare. 
        if is_spare(frame_values[9] or is_strike(frame_values[9])):
            frame_values[10] = get_frame_values(11)

        # Get frame 12 if frame 10 was a strike. 
        if is_strike(frame_values[9]):
            frame_values[11] = get_frame_values(12)

        print(f"\n\nYour game score is: {compute_game_score(frame_values)}")
        # Ask the user if they want to play another game. 
        response = input("Would you like to play another game?(y for yes, n for no): ")
        running = (response == "n")
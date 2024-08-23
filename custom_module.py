def generate_time_travel_message(year, destination, cost):
    """
    Generate a time travel message based on the provided year, destination, and cost.

    Parameters:
    - year (int): The target year for time travel.
    - destination (str): The destination of the time travel.
    - cost (Decimal): The cost of the time travel.

    Returns:
    - str: A formatted message about the time travel experience.
    """
    # Format and return the message
    message = (
        f"Get ready for your time travel adventure!\n"
        f"Destination: {destination}\n"
        f"Year: {year}\n"
        f"Total Cost: ${cost:.2f}"
    )
    return message

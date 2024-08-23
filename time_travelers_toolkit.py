# Import the datetime module with an alias
import datetime as dt

# Import Decimal from the decimal module
from decimal import Decimal

# Import randint and choice from the random module
from random import randint, choice

# Import the custom module (assuming it's in the same directory)
import custom_module

# Get today's date
today_date = dt.date.today()

# Print today's date using f-string
print(f"Today's date: {today_date}")

# Get the current time
current_time = dt.datetime.now().time()

# Print the current time using f-string
print(f"Current time: {current_time}")

# Define the base cost of time travel as a Decimal object
base_cost = Decimal('100.00')  # Example base cost in currency

# Define the range for the random target year
start_year = 2025
end_year = 2100

# Generate a random target year within the specified range
target_year = randint(start_year, end_year)

# Get the current year
current_year = dt.datetime.now().year

# Calculate the difference between the target year and the current year
year_difference = target_year - current_year

# Define a cost multiplier per year of travel (e.g., 10 units of currency per year)
cost_per_year = Decimal('10.00')

# Calculate the total cost multiplier
total_cost_multiplier = cost_per_year * year_difference

# Calculate the final cost
final_cost = base_cost + total_cost_multiplier

# Format the final cost to two decimal places
final_cost = final_cost.quantize(Decimal('0.01'))

# Define a list of possible destinations
destinations = [
    "Ancient Egypt",
    "Medieval Europe",
    "The Renaissance",
    "The American Revolution",
    "The Moon Landing",
    "The Industrial Revolution",
    "Future Mars Colony",
    "The Great Wall of China",
    "Victorian London",
    "The Jurassic Period"
]

# Use the choice() function to randomly select one destination
selected_destination = choice(destinations)

# Call the generate_time_travel_message() function from custom_module
message = custom_module.generate_time_travel_message(target_year, selected_destination, final_cost)

# Print the generated message
print(message)

# Print a congratulatory message
print("Congratulations on completing your time travel project!")

# Time Travel Cost Calculator

This project is a fun and interactive Python script that simulates the cost calculation for a hypothetical time travel journey. It uses various Python modules to generate a random target year, calculate the cost of the journey based on the year difference, and select a random historical or futuristic destination. Finally, it combines these elements to generate a time travel message using a custom module.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Testing](#testing) 
- [Example Output](#example-output)
- [Learning Outcomes](#learning-outcomes)
- [Custom Module](#custom-module)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The Time Travel Cost Calculator simulates a scenario where you can calculate the cost of traveling to a random year in the future. The project demonstrates the use of various Python features, including working with dates and times, performing calculations with the `Decimal` module for accurate financial operations, and random selection of data.

## Features

- **Date and Time Handling**: Get the current date and time using the `datetime` module.
- **Random Year Generation**: Generate a random target year within a specified range.
- **Cost Calculation**: Calculate the total cost of time travel based on the difference between the current year and the target year.
- **Random Destination Selection**: Randomly select a destination from a predefined list.
- **Custom Message Generation**: Generate a time travel message using a custom module.

## Technologies Used

- **Python**: The core programming language.
- **datetime Module**: For handling dates and times.
- **decimal Module**: For precise financial calculations.
- **random Module**: For generating random numbers and selecting random choices.
- **Custom Module**: A user-defined module to generate custom messages.

## Setup and Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/time-travel-cost-calculator.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd time-travel-cost-calculator
   ```

3. **Ensure you have Python installed**. This project was developed using Python 3.x.

4. **Run the script**:

   ```bash
   python time_travel_calculator.py
   ```

5. ## Run the tests

To ensure everything is working correctly, run the tests using:

```bash
python -m unittest test.py
```
## How It Works

1. **Import Required Modules**: The script begins by importing necessary modules, including a custom module for generating time travel messages.
2. **Date and Time Calculation**: It calculates the current date and time using the `datetime` module.
3. **Random Year and Cost Calculation**: A random target year is generated, and the cost of traveling to that year is calculated based on a predefined cost per year.
4. **Destination Selection**: A random destination is selected from a list of historical and futuristic places.
5. **Message Generation**: The custom module is used to generate a final message that includes the target year, destination, and calculated cost.
6. **Output**: The generated message and a congratulatory note are printed to the console.

## Usage

- **Run the script** to simulate a time travel cost calculation.
- **Input**: The script doesn't require any input; it operates automatically to generate results.
- **Output**: The script prints the calculated cost, selected destination, and final time travel message.

## Example Output

```plaintext
Today's date: 2024-09-02
Current time: 14:22:45.678912
Randomly selected target year: 2075
Year difference: 51 years
Base cost: 100.00
Cost per year: 10.00
Total cost multiplier: 510.00
Final cost: 610.00
Selected destination: The Moon Landing
Generated message: Congratulations! Your time travel adventure to the year 2075 is set to visit The Moon Landing. The total cost for this journey is 610.00 units of currency.
Congratulations on completing your time travel project!
```

## Learning Outcomes

By working on this project, you will:

- **Understand Date and Time Manipulation**: Learn how to use the `datetime` module to handle dates and times effectively in Python.
- **Perform Financial Calculations**: Gain experience using the `Decimal` module for precise financial calculations, avoiding common issues with floating-point arithmetic.
- **Generate Random Data**: Learn how to generate random numbers and make random selections using the `random` module, which is useful for creating dynamic and unpredictable outputs.
- **Work with Custom Modules**: Understand how to create and use custom Python modules to organize code and promote reusability.
- **Enhance Problem-Solving Skills**: Apply logical thinking to calculate the time travel cost based on year differences and to combine multiple elements (dates, costs, destinations) into a cohesive output.

## Custom Module

The `custom_module` is a user-defined Python module that contains a function `generate_time_travel_message(target_year, selected_destination, final_cost)`. This function takes in the target year, destination, and calculated cost, then returns a formatted message that simulates a time travel confirmation.

### Example of `custom_module.py`

```python
def generate_time_travel_message(target_year, selected_destination, final_cost):
    return f"Congratulations! Your time travel adventure to the year {target_year} is set to visit {selected_destination}. The total cost for this journey is {final_cost} units of currency."
```

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---


# Terminal Calculator

A simple and interactive Python-based calculator that supports basic arithmetic operations. Designed for use in the terminal, this calculator is user-friendly and handles edge cases gracefully.

---

## Features

- **Basic Arithmetic Operations**: Addition, Subtraction, Multiplication, and Division.
- **Flexible Input**: Accepts both operation names (e.g., `add`) and symbols (e.g., `+`).
- **Error Handling**: Handles invalid inputs and division by zero with appropriate messages.
- **Calculation History**: Automatically logs all calculations to a history file (`calculation_history.txt`).
- **Interactive Interface**: Fully terminal-based for ease of use.
- **Extensible Design**: Easily extendable to include more operations.

---

## File Structure

```
├── calculator/          # Core calculator functions
│   ├── __init__.py      # Package initialization
│   ├── calculator.py    # Arithmetic operations
├── tests/               # Unit tests
│   ├── test_calculator.py
├── docs/README.md       # Documentation
├── main.py              # Terminal-based interface
├── requirements.txt     # Dependencies
└── calculation_history.txt # Logs calculation history
```

---

## Testing Command

python3 -m unittest discover -s tests
python3 main.py        

## Setup Instructions

Follow these steps to set up and run the calculator:

1. **Clone the Repository**:

   ```bash
   git clone <repo_url>
   cd calculator
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.6+ installed. Then, install the required dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

3. **Run the Calculator**:
   Launch the terminal-based calculator:
   ```bash
   python3 main.py
   ```

---

## Usage

1. **Choose an Operation**:

   - Enter the operation name (e.g., `add`) or symbol (e.g., `+`).
   - Supported operations: `add (+)`, `subtract (-)`, `multiply (*)`, `divide (/)`.

2. **Enter Numbers**:

   - Provide two numbers when prompted.

3. **View Results**:

   - The result will be displayed in the terminal.
   - The calculation will also be logged in `calculation_history.txt`.

4. **Exit**:
   - Type `exit` to quit the calculator.

---

## Example

```bash
Welcome to Terminal Calculator!
Choose operation (add, subtract, multiply, divide, +, -, *, /) or 'exit' to quit: add
Enter first number: 5
Enter second number: 3
Result of Addition: 8.0
----------------------------------------
```

---

## Future Enhancements

- Add support for advanced mathematical operations (e.g., exponentiation, square root).
- Implement a graphical user interface (GUI).
- Add support for multiple languages.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the calculator.

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description.

---

## Contact

For questions or feedback, please contact [ankit.rai@bypeopletechnologies.com].

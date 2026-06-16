# SMART BUDGET PLANNER
#### Video Demo: [YouTube Video URL Here]
#### Description:
The Smart Budget Planner is a feature-rich, command-line interface (CLI) application built using Python. It is designed to act as a lightweight personal finance companion, allowing users to take full control of their financial health. Managing personal expenses can quickly become overwhelming, and standard spreadsheets often lack the immediacy and validations required to maintain accuracy. This software bridges that gap by offering a fast, intuitive system to log income, record multi-category expenses, track current balances, and export records for downstream analysis.

By enforcing clean user-input loops and structural integrity via custom functions, the application ensures that financial reporting remains accurate and robust. Users can categorize entries under standardized fields like Food, Salary, Utilities, and Entertainment, making it incredibly simple to identify exactly where money is being spent. The software serves as a great digital alternative to physical ledgers or complex banking software for individuals seeking programmatic financial management.
---

## Architecture and File Descriptions
The project adheres strictly to the architectural constraints outlined by the CS50P specification, dividing structural logic, verification suites, and external states into three critical root-level components:

### 1. `project.py`
This file contains the main operational engine of the application. It begins with an infinite `while True` main game loop that renders an interactive ASCII dashboard menu. Users can pick options numbered from 1 to 6 to execute specific behaviors. The file isolates core computational operations into independent, non-nested global functions:
*   `add_transaction()`: Standardizes incoming values by generating a dictionary structure containing keys for type, float-enforced amounts, categorized names, and formatted date-strings before safely pushing them onto the active state stack.
*   `calculate_balance()`: Iterates through the stored transaction history to isolate gross income and gross expenditures, calculating the final net balance through simple mathematical deductions ($Balance = Income - Expenses$).
*   `get_category_total()`: Implements structural case-insensitivity to iterate over all active expenses and cleanly isolate spending metrics associated with single target categories like "Food" or "Rent".
*   `export_csv()`: Leverages Python's native `csv` library to write stored dictionaries to human-readable sheets for Excel or tracking tools.
*   `load_data()` and `save_data()`: Helper utilities that look for a local `data.json` database layer to automatically pull or write data changes between sessions.

### 2. `test_project.py`
This file contains the automated testing pipeline executed via `pytest`. To guarantee strict technical separation from user terminal elements, these test functions never invoke `main()` or trigger active CLI printouts. Instead, they isolate individual core logic blocks. It utilizes a `pytest.fixture` to generate reproducible mockup financial transactions. Testing cases ensure that calculation margins match exactly, zero-state edge cases function correctly, user-input text variations (like inputting "food" instead of "Food") automatically standardize gracefully, and CSV file writes successfully trigger true boolean flags.

### 3. `requirements.txt`
This file contains the external dependencies necessary to execute the testing components of the app. Because the budget planner utilizes built-in Python modules for file writing (`json`, `csv`, `os`, and `datetime`), this dependency manifest cleanly lists `pytest` to set up development operations smoothly.

---

## Design Choices and Philosophy
Several key design tradeoffs were evaluated during development:

*   **JSON Over Plain Text Storage:** Early iterations experimented with writing logs directly into a simple `.txt` string format. However, this required regex patterns or string splitting to separate amounts from dates, which felt brittle. Transitioning to a structured JSON database layout allowed data to load seamlessly back into Python as intuitive dictionaries, preserving clean variable types effortlessly.
*   **Decoupled CLI Processing:** A major architectural choice was separating data manipulation from visual interfaces. Functions like `add_transaction` and `calculate_balance` strictly accept variables and return raw values without performing `input()` or `print()` prompts internally. This made writing robust `pytest` workflows straightforward, as functions didn't block execution waiting for user terminal inputs.
*   **Fail-Safe Date Parsing:** Manual date management often breaks due to user typos. The design incorporates a fallback mechanism where if a user enters an unparseable date structure or hits "Enter", the app utilizes Python's `datetime` library to capture the current system date automatically, preventing code crashes.
---

## Installation and Execution Instructions
To interact with the Smart Budget Planner locally, install the necessary dependencies and spin up the script via terminal controls:

```bash
# Install required testing libraries
pip install -r requirements.txt

# Run the automated pytest suite to ensure code health
pytest test_project.py

# Launch the primary budget planner application
python project.py

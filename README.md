# KIU Test

Python version recommended 3.10

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-project.git
   cd your-project
    ```

2. **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    ```

    **Activate the virtual environment:**

    * On Windows



        ```bash
        venv\Scripts\activate
        ```

    * On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
3. **Install project dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Run __main__.py

Run the main script using the following command:

```bash
python __main__.py
```

### Run tests with coverage report

Make sure you have **pytest** and **pytest-cov** installed:

```bash
pytest --cov=app
```

For a detailed report in html
```bash
pytest --cov=app --cov-report=html
```

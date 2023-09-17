# Vigenere Cipher Analysis Tool

Vigenere Cipher Tool is a Python-based utility that allows users to encrypt, decrypt, and analyze text using the Vigenere cipher method.

## Table of Contents
- [Vigenere Cipher Analysis Tool](#vigenere-cipher-analysis-tool)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Testing](#testing)
  - [Contributing](#contributing)
  - [License](#license)

## Features

1. **Encryption**: Encrypt plaintext with a user-provided key using the Vigenere cipher method.
2. **Decryption**: Decrypt ciphertext using a known key.
3. **Analysis Tools**:
    - **Kasiski Examination**: Deduce potential key lengths based on repeated sequences in the ciphertext.
    - **Index of Coincidence (IoC)**: Utilize statistical properties to suggest potential key lengths.
    - **Key Deduction**: Attempt to deduce the key using frequency analysis based on potential key lengths.

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/bbienvenu/Vigenere-Cipher-Analysis-Tool.git
    ```
2. Change directory:
    ```
    cd vigenere-cipher-tool
    ```
3. (Optional) Create a virtual environment:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

## Usage

1. Execute the main script:
    ```
    python main.py
    ```

2. Follow the interactive CLI instructions. Choose between `encrypt`, `decrypt`, or `analyze` actions, and provide the necessary input.

## Testing

To ensure the Vigenere Cipher tool's functionality, tests have been provided:

1. Run the test suite:
    ```
    python -m unittest -v
    ```

2. Ensure all tests pass to validate that the core functionality of the Vigenere cipher is working correctly.

## Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository on GitHub.
2. **Clone** your fork and create a new branch: 
    ```
    git checkout -b your-branch-name
    ```
3. Make your changes, and then push them back to your repository.
4. Submit a **pull request** detailing your changes.

## License

Vigenere Cipher Tool is open source and available under the MIT License. See `LICENSE` file for more details.

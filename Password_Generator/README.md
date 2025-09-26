# Random Password Generator

## Description
This script generates a secure random password of a specified length.  
You can optionally include digits, uppercase letters, and special symbols.

## Features
- Custom password length
- Include or exclude digits
- Include or exclude uppercase letters
- Include or exclude special symbols
- Command-line interface (CLI)

## Requirements
- Python 3.x

## Usage

Run the script from the command line:

```bash
python password_gen.py --length 12 --use_digits --use_uppercase --use_special_symbols
```

### Arguments
- `--length` (required): Length of the password (integer)
- `--use_digits` (optional): Include digits in the password
- `--use_uppercase` (optional): Include uppercase letters
- `--use_special_symbols` (optional): Include special symbols

### Example

Generate a 12-character password with all character types:

```bash
python password_gen.py --length 12 --use_digits --use_uppercase --use_special_symbols
```

Generate an 8-character password with only lowercase letters:

```bash
python password_gen.py --length 8
```

## Output
The password will be printed directly in the console.

## Notes
- If no optional flags are specified, the password will contain lowercase letters only.
- Make sure to run the script from the folder where `password_gen.py` is located or provide the full path.

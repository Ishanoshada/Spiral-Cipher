# Spiral Cipher Documentation

![PyPI](https://img.shields.io/pypi/v/spiral-cipher)

The **Spiral Cipher** is a Python package for text encryption and decryption using a spiral pattern. It writes text in a spiral pattern within a square matrix and reads it back row by row for encoding. The reverse process is used for decoding. The package also supports file-based encryption/decryption and customizable encryption keys.

---

## Features

- **Text Encryption/Decryption**: Encrypt and decrypt text using a spiral pattern.
- **File Encryption/Decryption**: Encrypt and decrypt files.
- **Customizable Key**: Use a key to shift characters for additional security.
- **UTF-8 Support**: Works with Unicode characters.
- **Command-Line Interface (CLI)**: Easy-to-use CLI for text and file operations.
- **Python API**: Programmatic access to encryption/decryption functions.

---

## Installation

Install the package using `pip`:

```bash
pip install spiral-cipher
```

---

## Usage

### Python API

The package provides a Python API for programmatic usage.

#### 1. **Encoding and Decoding Text**

```python
from spiral_cipher import encode, decode

# Encode text
encoded_text = encode("Hello, World!", key=1111) # any key : int , ex : 9999999
print(encoded_text)  # Output: "AxeeQQQhew!,khP"

# Decode text
decoded_text = decode(encoded_text, key=1111)
print(decoded_text)  # Output: "Hello, World!"
```

#### 2. **Using the `SpiralCipher` Class**

```python
from spiral_cipher import SpiralCipher

# Initialize the cipher with a key
cipher = SpiralCipher(key=3)

# Encode text
encoded_text = cipher.encode("Hello, World!")
print(encoded_text)  # Output: "KhooAAArog!,urZ"

# Decode text
decoded_text = cipher.decode(encoded_text)
print(decoded_text)  # Output: "Hello, World!"

# Encrypt a file
cipher.encrypt_file("input.txt", "encrypted.txt")

# Decrypt a file
cipher.decrypt_file("encrypted.txt", "decrypted.txt")
```

---

### Command-Line Interface (CLI)

The package provides a CLI for easy text and file processing.

#### 1. **Text Processing**

```bash
# Encode text
spiral-cipher encode "Hello, World!" -k 3

# Decode text
spiral-cipher decode "KhooAAArog!,urZ " -k 3 #don't miss space +_+
```

#### 2. **File Processing**

```bash
# Encrypt a file
spiral-cipher encode input.txt -f -o encrypted.txt -k 3

# Decrypt a file
spiral-cipher decode encrypted.txt -f -o decrypted.txt -k 3
```

#### 3. **CLI Options**

| Argument | Description |
|----------|-------------|
| `action` | Action to perform (`encode` or `decode`) |
| `input`  | Text to process or input file path |
| `-k, --key` | Encryption key (default: `1`) |
| `-f, --file` | Treat input as a file path |
| `-o, --output` | Output file path (required for file operations) |
| `-h, --help` | Show help message |

---

## How It Works

### Encryption Process

1. **Create a Square Matrix**:
   - The input text is padded (if necessary) to fit into the smallest square matrix.

2. **Write Text in Spiral Pattern**:
   - The text is written in a spiral pattern (clockwise or counterclockwise) within the matrix.

3. **Shift Characters**:
   - Each character is shifted by the key value for additional security.

4. **Read Row by Row**:
   - The matrix is read row by row to generate the encrypted text.

### Decryption Process

1. **Create a Square Matrix**:
   - The encrypted text is placed into a square matrix.

2. **Read Text in Spiral Pattern**:
   - The text is read in the reverse spiral pattern.

3. **Unshift Characters**:
   - Each character is unshifted by the key value.

4. **Remove Padding**:
   - Padding characters are removed to retrieve the original text.

---

## Examples

### Example 1: Encoding and Decoding Text

```python
from spiral_cipher import encode, decode

# Encode text
encoded = encode("Hello, World!", key=3)
print(encoded)  # Output: "Khoog$ro/urZ#"

# Decode text
decoded = decode(encoded, key=3)
print(decoded)  # Output: "Hello, World!"
```

### Example 2: File Encryption and Decryption

```python
from spiral_cipher import SpiralCipher

# Initialize the cipher
cipher = SpiralCipher(key=3)

# Encrypt a file
cipher.encrypt_file("input.txt", "encrypted.txt")

# Decrypt a file
cipher.decrypt_file("encrypted.txt", "decrypted.txt")
```

### Example 3: CLI Usage

```bash
# Encode text
spiral-cipher encode "Hello, World!" -k 3

# Decode text
spiral-cipher decode "Khoog$ro/urZ#" -k 3

# Encrypt a file
spiral-cipher encode input.txt -f -o encrypted.txt -k 3

# Decrypt a file
spiral-cipher decode encrypted.txt -f -o decrypted.txt -k 3
```

---

## Development

### 1. **Clone the Repository**

```bash
git clone https://github.com/ishanoshada/spiral-cipher.git
cd spiral-cipher
```

### 2. **Install in Development Mode**

```bash
pip install -e .
```

### 3. **Run Tests**

```bash
python -m unittest discover tests
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

- **Ishan Oshada** - [GitHub Profile](https://github.com/ishanoshada)

---

## Links

- **GitHub Repository**: [https://github.com/ishanoshada/spiral-cipher](https://github.com/ishanoshada/spiral-cipher)
- **PyPI Package**: [https://pypi.org/project/spiral-cipher/](https://pypi.org/project/spiral-cipher/)
- **Bug Reports**: [https://github.com/ishanoshada/spiral-cipher/issues](https://github.com/ishanoshada/spiral-cipher/issues)

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

**Repository Views** ![Views](https://profile-counter.glitch.me/spiral-cipher/count.svg)

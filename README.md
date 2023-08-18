# DES Encryption and Decryption Demo using Streamlit

This is a simple application that demonstrates the encryption and decryption of data using the Data Encryption Standard (DES) algorithm. It utilizes the Streamlit framework to provide a user-friendly interface for performing encryption and decryption operations.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python: Make sure you have Python installed on your system. The code is written in Python 3.


## Installation

Install the required packages using pip:

```bash
pip install -r requirements.txt

```

## Usage
1. Run the Streamlit app using the following command:
```bash
streamlit run app.py
```
2. The app will open in your default web browser, presenting you with an interface to choose between encryption and decryption operations.

3. For Encryption:
- Enter an 8-character key in the sidebar input.
- Enter the data you want to encrypt in the provided text area.
- Click the "Perform Operation" button.
- Encrypted data will be displayed along with a success message.

4. For Decryption:
- Choose the decryption operation in the sidebar.
- Enter the 8-character key used for encryption.
- Enter the encrypted data (in hexadecimal format) in the text area.
- Click the "Perform Operation" button.
- Decrypted data will be displayed along with a success message if decryption is successful.

Note: The app uses ECB mode for DES encryption and decryption.

## Contributing

Contributions are welcome! If you find any issues or improvements, feel free to open a pull request or create an issue.

## License

[MIT](https://github.com/it-TranKhaiHoang/DES-Encrypt-Decrypt-Demo/blob/main/LICENSE)
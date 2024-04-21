# Caesar Cipher Implementation

The Caesar Cipher Implementation is a Python program that demonstrates the Caesar Cipher algorithm, a simple and widely used encryption technique. This implementation allows users to encrypt and decrypt messages using the Caesar Cipher with a specified key.

## What is the Caesar Cipher?

The Caesar Cipher, named after Julius Caesar, is one of the earliest and simplest encryption techniques. It works by shifting each letter in the plaintext by a fixed number of positions down or up the alphabet. For example, with a key of 3, 'A' would be replaced by 'D', 'B' would become 'E', and so on. The Caesar Cipher is a type of substitution cipher where each letter is replaced with another letter in the alphabet.

## How does the program work?

The Caesar Cipher Implementation program provides a user-friendly interface where users can choose between encryption and decryption modes. Upon selecting the desired mode, users are prompted to enter a key (an integer between 1 and 26) and the text to encrypt or decrypt. The program then processes the input text according to the selected mode and key, and displays the resulting ciphertext or decrypted plaintext.

## Features:

- **Encryption and Decryption**: Users can encrypt and decrypt messages using the Caesar Cipher algorithm.
- **Key Selection**: Users can choose a key (an integer between 1 and 26) for encryption and decryption.
- **User Interface**: The program provides a simple menu-driven interface for ease of use.
- **Error Handling**: The program ensures that the key entered by the user is within the valid range and handles invalid input gracefully.
- **Example and Instructions**: The program includes an example scenario and instructions for usage in the README file.

## Usage:

To use the program, follow these steps:
1. Run the Python script `caesar_cipher.py`.
2. Choose one of the following options:
   - **Encrypt**: Select this option to encrypt text using the Caesar Cipher.
   - **Decrypt**: Select this option to decrypt text encrypted using the Caesar Cipher.
   - **Exit**: Select this option to exit the program.
3. If you chose the **Encrypt** or **Decrypt** option, you will be prompted to enter a key (an integer between 1 and 26) and the text to encrypt or decrypt.
4. The program will then display the resulting ciphertext or decrypted plaintext.

## Example:

To illustrate the usage of the Caesar Cipher Implementation, consider the following example:

1. **Encryption Mode**:
    ```
    ***CAESER CIPHER***

    menu
    1. encrypt
    2. decrypt
    3. exit

    Enter your choice: 1
    Encryption mode selected

    Enter key in range [1,26]: 3
    Enter text to encrypt: hello world
    CIPHERTEXT:  khoor zruog
    ```

2. **Decryption Mode**:
    ```
    ***CAESER CIPHER***

    menu
    1. encrypt
    2. decrypt
    3. exit

    Enter your choice: 2
    Decryption mode selected

    Enter key in range [1,26]: 3
    Enter text to decrypt: khoor zruog
    ORIGINALTEXT:  hello world
    ```

This example demonstrates how users can interact with the Caesar Cipher Implementation program. Users can select between encryption and decryption modes, enter a key, and input the text to be processed. The program then displays the result accordingly.



import streamlit as st
from Crypto.Cipher import DES

# Streamlit UI
st.title("DES Encryption and Decryption Demo")

operation = st.sidebar.radio("Choose Operation", ["Encrypt", "Decrypt"])

# Key input
key = st.sidebar.text_input("Enter 8-character Key:", max_chars=8)

# Data input
if operation == "Encrypt":
    data = st.text_area("Enter Data to Encrypt:")
else:
    data = st.text_area("Enter Data to Decrypt:")

# Padding to ensure data length is a multiple of 8
def pad_data(data):
    padding_len = 8 - (len(data) % 8)
    padded_data = data + chr(padding_len) * padding_len
    return padded_data

# Encryption function
def encrypt_data(key, data):
    cipher = DES.new(key.encode("utf-8"), DES.MODE_ECB)
    padded_data = pad_data(data)
    ciphertext = cipher.encrypt(padded_data.encode("utf-8"))
    return ciphertext

# Decryption function
def decrypt_data(key, ciphertext):
    cipher = DES.new(key.encode("utf-8"), DES.MODE_ECB)
    decrypted_data = cipher.decrypt(ciphertext)
    return decrypted_data.rstrip(b"\0").decode("utf-8")

if st.sidebar.button("Perform Operation"):
    if operation == "Encrypt":
        if key and data:
            encrypted_data = encrypt_data(key, data)
            st.success("Encryption Successful!")
            st.write("Encrypted Data:", encrypted_data.hex())
    else:
        if key and data:
            try:
                decrypted_data = decrypt_data(key, bytes.fromhex(data))
                st.success("Decryption Successful!")
                st.write("Decrypted Data:", decrypted_data)
            except ValueError:
                st.error("Decryption Error. Check your key or input data.")

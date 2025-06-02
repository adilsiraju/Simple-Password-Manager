# 🔐 Simple Password Manager

A secure, command-line password manager built with Python that uses Fernet encryption to safely store and manage your passwords locally.

## ✨ Features

- **🔒 Secure Encryption**: Uses Fernet symmetric encryption from the `cryptography` library
- **💾 Local Storage**: All passwords are stored locally in an encrypted format
- **👤 User-Friendly Interface**: Simple command-line interface for easy interaction
- **🔑 Key Management**: Automatic generation and management of encryption keys
- **📝 Add Passwords**: Store new username/password combinations
- **👀 View Passwords**: Decrypt and display stored passwords securely

## 🛠️ Requirements

- Python 3.6+
- `cryptography` library

## 📦 Installation

1. **Clone or download this repository**
2. **Install required dependencies:**
   ```bash
   pip install cryptography
   ```

3. **Generate encryption key (first-time setup):**
   - Uncomment the key generation code in `password_manager.py` (lines 11-18)
   - Run the script once to generate the key
   - Comment the code back to prevent key regeneration

## 🚀 Usage

Run the password manager:
```bash
python password_manager.py
```

### Available Commands

- **`add`** - Add a new password entry
- **`view`** - View all stored passwords (decrypted)
- **`q`** - Quit the application

### Example Session
```
Do you want to 'add' a new password or 'view' existing ones ? You may also press 'q' to quit.
> add
Username: john@example.com
Password: mySecurePassword123

Do you want to 'add' a new password or 'view' existing ones ? You may also press 'q' to quit.
> view
User:  john@example.com     Password:  mySecurePassword123

Do you want to 'add' a new password or 'view' existing ones ? You may also press 'q' to quit.
> q
```

## 📁 File Structure

```
Simple-Password-Manager/
├── password_manager.py    # Main application file
├── key.key               # Encryption key (generated automatically)
├── passwords.txt         # Encrypted password storage
├── README.md            # This file
├── data/                # Additional data directory
└── src/                 # Source code directory
```

## 🔒 Security Features

- **Fernet Encryption**: Uses AES 128 in CBC mode with PKCS7 padding
- **Local Storage**: No cloud storage - all data remains on your machine
- **Key Separation**: Encryption key is stored separately from password data
- **No Plaintext Storage**: Passwords are never stored in plaintext

## ⚠️ Important Security Notes

1. **Keep `key.key` safe**: If you lose this file, you cannot decrypt your passwords
2. **Backup your key**: Consider securely backing up your `key.key` file
3. **File permissions**: Ensure only you can read the `key.key` and `passwords.txt` files
4. **One-time key generation**: Only generate the key once - regenerating will make existing passwords unreadable

## 🤝 Contributing

This is a simple educational project. Feel free to fork and enhance it with additional features like:
- Password strength checking
- Categories/tags for passwords
- Export/import functionality
- GUI interface
- Password generation

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🎓 Educational Purpose

This project was created as part of a programming tutorial series. It demonstrates:
- File I/O operations in Python
- Encryption/decryption using the `cryptography` library
- Command-line interface design
- Basic password management concepts

---

**⚠️ Disclaimer**: This is an educational project. For production use, consider established password managers with additional security features and professional security audits.
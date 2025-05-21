
# 🔐 SecurePDFVault

**SecurePDFVault** is a lightweight Python tool that allows you to password-protect your PDF files using a simple command-line interface. It’s ideal for quick and offline PDF encryption without relying on third-party online tools.

## 📁 Project Structure

```

SecurePDFVault/
├── pdf\_password\_protector.py   # Main script to apply password protection
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── clcoding.pdf                # Sample PDF for testing (optional)
└── outputs/                    # Stores the password-protected PDFs

````

## 🚀 Features

- Encrypt any PDF file with a password
- Simple and minimal interface
- Saves output in the `outputs/` folder
- No internet connection required — works entirely offline

## 🛠️ How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/Kirankumarvel/SecurePDFVault.git
cd SecurePDFVault
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Script

```bash
python pdf_password_protector.py
```

The script will:

* Ask for the PDF file path (you can test with `clcoding.pdf`)
* Ask for the password
* Save the encrypted version as `protected_file.pdf` in the `outputs/` folder

## 🧪 Example

```bash
Enter path of PDF: clcoding.pdf
Enter password to encrypt the PDF: mysecure123
PDF has been encrypted and saved as 'outputs/protected_file.pdf'
```

## 📦 Dependencies

* `PyPDF2`

Install manually if needed:

```bash
pip install PyPDF2
```

## 📌 Notes

* Only supports basic PDF encryption
* Original PDF remains unaltered
* Encrypted PDF can be opened with any PDF reader using the password

## 👨‍💻 Author

**Kiran Kumar V**
📬 🔗 [GitHub](https://github.com/Kirankumarvel)

---

📁 **Protect your PDFs easily — because your data deserves security.**

```



#  Password Analyzer Tool

A simple Python-based CLI and web tool that:

-  Checks password strength using entropy
-  Suggests stronger alternatives
-  Scans saved passwords and reports weak ones

---

##  Features

- **Entropy-based strength evaluation**
- **Password scanner for JSON files**
- **Smart suggestions** for weak passwords
- Optional **web interface** using Flask (for deployment or local use)

---

##  How It Works

###  Entropy-Based Strength

Passwords are evaluated based on Shannon entropy:

| Entropy Range     | Strength     |
|-------------------|--------------|
| 0 - 28 bits       | Very Weak |
| 28 - 36 bits      | Weak      |
| 36 - 60 bits      | Reasonable |
| 60+ bits          | Strong    |

---

##  Quick Start (CLI)

###  Requirements

- Python 3.8+
- Install dependencies:

```bash
pip install -r requirements.txt

# GUPP

GUPP is a Discord Nitro code generator that allows users to generate random gift codes and check their validity. If a valid code is found, it sends the code to a specified Discord webhook.

## Features

- **Random Nitro Code Generation**: Generates random 18-character alphanumeric strings.
- **Code Validation**: Checks if the generated codes are valid Discord Nitro gift codes.
- **Webhook Notification**: Sends valid codes to a specified Discord webhook.
- **User-Friendly Interface**: Interactive menu with colorful ASCII art and smooth rainbow effects.

## Requirements

- Python 3.12.6
- A Discord Webhook
- Required libraries:
  - `requests`
  - `pyfiglet`
  - `colorama`

You can install the required libraries using pip:

```bash
pip install requests pyfiglet colorama
```
## Usage
- Clone the repository:

```bash
git clone https://github.com/yourusername/gupp.git
cd gupp
```
- Run the script:

```bash
python gupp.py
```
- Follow the on-screen instructions:

Select "Start" to begin generating codes.
Enter your Discord webhook URL to receive valid codes.
Choose options to open My Instagram page or exit.

## Disclaimer
This tool is intended for educational purposes only. Please use responsibly and respect the terms of service of Discord.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

import random
import string
import requests
import time
import pyfiglet
import webbrowser
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

def generate_code():
    """Generate a random 18-character alphanumeric string."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(18))

def check_code(code):
    """Send a GET request to the specified URL."""
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    response = requests.get(url)
    return response.status_code

def send_webhook(code, webhook_url):
    """Send the generated code to the provided Discord webhook."""
    data = {"content": f"https://discord.gift/{code}"}
    requests.post(webhook_url, json=data)

def print_large_text(text):
    """Print text in large ASCII format with the 'Bloody' style."""
    ascii_art = pyfiglet.figlet_format(text, font='bloody')
    print(smooth_rainbow_text(ascii_art))

def smooth_rainbow_text(text):
    """Create a smooth rainbow gradient effect for the text."""
    colors = [
        Fore.RED, Fore.YELLOW, Fore.GREEN,
        Fore.CYAN, Fore.BLUE, Fore.MAGENTA
    ]
    rainbow = ''.join(colors[i % len(colors)] + char for i, char in enumerate(text))
    return rainbow + Fore.RESET  # Reset color after the rainbow text

def display_menu():
    """Display the GUPP menu."""
    print(smooth_rainbow_text("Welcome to GUPP"))
    print(smooth_rainbow_text(pyfiglet.figlet_format("GUPP", font='bloody')))
    print(smooth_rainbow_text("1. Start"))
    print(smooth_rainbow_text("2. Instagram"))
    print(smooth_rainbow_text("3. Exit"))

def main():
    display_menu()
    
    choice = input(smooth_rainbow_text("Select an option: "))
    
    if choice == '1':
        webhook_url = input(smooth_rainbow_text("Enter your webhook URL: "))
        while True:
            code = generate_code()
            print(smooth_rainbow_text(f"Generated code: {code}"))

            if check_code(code) == 200:
                print_large_text("VALID CODE")
                send_webhook(code, webhook_url)
                break  # Stop the script after finding a valid code
            
            time.sleep(0)  # Minimize sleep time for maximum speed

    elif choice == '2':
        webbrowser.open("https://instagram.com/pythonpromotesmusic")
        print(smooth_rainbow_text("Opening Instagram..."))
    elif choice == '3':
        print(smooth_rainbow_text("Exiting..."))
    else:
        print(smooth_rainbow_text("Invalid option. Please try again."))

if __name__ == "__main__":
    main()

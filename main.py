from blessed import Terminal
from rich.markdown import Markdown
from rich import print as mr_print
from dotenv import load_dotenv
import subprocess

from app.ai import get_sky_response
from app.utility import get_location_from_ip

load_dotenv()

term = Terminal()





def run_terminal_mode():
    term = Terminal()
    location = get_location_from_ip()

    print(term.enter_fullscreen())
    print(term.clear())
    
    print(term.bold(term.blue("Sky Terminal Mode")))
    print(term.green(f"Location: {location}"))
    print(term.yellow("Type your questions below. Type 'exit' or 'quit' to leave."))
    print()
    
    try:
        while True:
            user_question = input(term.bold("Ask your question: ")).strip()
            if user_question.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break

            sky_response = get_sky_response(user_question, location)
            print(term.bold("Sky says:"))
            mr_print(Markdown(sky_response))
            print()
    finally:
        print(term.exit_fullscreen())


menu_items = ['Run in Terminal Mode', 'Run Streamlit App', 'Exit']
selected_index = 0

def print_menu(selected_index):
    print(term.clear())
    print(term.bold(term.blue("SKY")))
    print(term.bold(term.blue("Welcome to SKY - AI Tutor")))
    print()
    for i, item in enumerate(menu_items):
        if i == selected_index:
            print(term.reverse(item))
        else:
            print(item)

def main():
    term = Terminal()
    selected_index = 0

    print(term.enter_fullscreen())
    print_menu(selected_index)

    try:
        while True:
            print_menu(selected_index)
            user_input = input(term.bold("Press 'n' to navigate, 'Enter' to select: ")).strip().lower()
            
            if user_input == 'n':
                selected_index = (selected_index + 1) % len(menu_items)
            elif user_input == '':
                if menu_items[selected_index] == 'Exit':
                    break
                elif menu_items[selected_index] == 'Run in Terminal Mode':
                    print(term.exit_fullscreen())
                    run_terminal_mode()
                    break
                elif menu_items[selected_index] == 'Run Streamlit App':
                    print(term.exit_fullscreen())
                    subprocess.run(["streamlit", "run", "web.py"])
                    break
            else:
                print("Invalid input. Please press 'n' to navigate or 'Enter' to select.")
    finally:
        print(term.exit_fullscreen())

if __name__ == "__main__":
    main()
import os
import argparse
import openai
import curses
from Sticker_Generator.generators.dalle.dalle import generate_dalle
from Transformer.remove_background import backround_remover
from Selenium.driver import redbubble_upload

#############################################################################
#
# ARGS
#
#############################################################################

# Deprecated command-line arguments
# parser = argparse.ArgumentParser()
# parser.add_argument(
#     "-generator", "--generator", help="Generator must be dalle (for now)", type=str
# )
# parser.add_argument("-size", "--size", help="Size must be 256, 512, 1024", type=str)
# parser.add_argument("-n", "--n", help="Number of stickers to generate", type=int)
# args = parser.parse_args()

#############################################################################
#
# PATHS
#
#############################################################################

# Define the root directory of the project
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Set the current working directory to the project root
os.chdir(ROOT_DIR)

#############################################################################
#
# ENVIRONMENT VARIABLES
#
#############################################################################

# Set OpenAI organization and API key using environment variables
openai.organization = os.environ.get("ENV_OPENAI_ORG")
openai.api_key = os.environ.get("ENV_OPENAI_KEY")

#############################################################################
#
# Runtime
#
#############################################################################


def main(stdscr):
    """
    The main function of the program, executed in the terminal interface.
    Allows the user to input text, select a sticker generator and size,
    and upload the resulting sticker to RedBubble.

    Args:
    stdscr (curses window): A curses window object representing the terminal screen.

    Returns:
    None
    """
    # Hide cursor
    curses.curs_set(0)

    # Print initial prompt for user input
    stdscr.addstr(0, 0, "Enter the type of sticker you want to create: ")
    stdscr.refresh()

    # Read user input
    curses.echo()
    user_input = stdscr.getstr().decode("utf-8")
    curses.noecho()

    # Clear screen and display user input
    stdscr.clear()
    stdscr.addstr(0, 0, "You entered: " + user_input)
    stdscr.refresh()

    # Define options for sticker generator
    options_generator = ["Dalle", "Other Generator"]
    selected_option_generator = 0

    # Print options and allow user to select one
    while True:
        # Clear screen and print options
        stdscr.clear()
        stdscr.addstr(0, 0, "You entered: " + user_input)
        stdscr.addstr(2, 0, "Select a generator type:")
        for i in range(len(options_generator)):
            if i == selected_option_generator:
                stdscr.addstr(i + 4, 2, "> " + options_generator[i])
            else:
                stdscr.addstr(i + 4, 4, options_generator[i])
        stdscr.refresh()

        # Wait for user input
        key = stdscr.getch()

        # Update selected option based on user input
        if key == curses.KEY_UP:
            selected_option_generator = (selected_option_generator - 1) % len(
                options_generator
            )
        elif key == curses.KEY_DOWN:
            selected_option_generator = (selected_option_generator + 1) % len(
                options_generator
            )
        elif key == curses.KEY_ENTER or key == 10:
            break

    options_sticker = ["256", "512", "1024"]
    selected_option_sticker = 0

    # Print options and allow user to select one
    while True:
        # Clear screen and print options
        stdscr.clear()
        stdscr.addstr(0, 0, "You entered: " + user_input)
        stdscr.addstr(2, 0, "Select a sticker size:")
        for i in range(len(options_sticker)):
            if i == selected_option_sticker:
                stdscr.addstr(i + 4, 2, "> " + options_sticker[i])
            else:
                stdscr.addstr(i + 4, 4, options_sticker[i])
        stdscr.refresh()

        # Wait for user input
        key = stdscr.getch()

        # Update selected option based on user input
        if key == curses.KEY_UP:
            selected_option_sticker = (selected_option_sticker - 1) % len(
                options_sticker
            )
        elif key == curses.KEY_DOWN:
            selected_option_sticker = (selected_option_sticker + 1) % len(
                options_sticker
            )
        elif key == curses.KEY_ENTER or key == 10:
            break

    # Clear screen and print final message
    stdscr.clear()
    stdscr.refresh()
    stdscr.addstr(0, 0, "You entered: " + user_input)
    stdscr.clear()
    stdscr.refresh()
    # loading_bar("Generating the sticker...", False)
    # loading_bar(user_input)
    if selected_option_generator == 0:
        sticker = generate_dalle(
            ROOT_DIR, user_input, options_sticker[selected_option_sticker]
        )
        backround_remover(sticker, ROOT_DIR)
        stdscr.refresh()
        # Clear screen and print final message
        stdscr.clear()
        stdscr.addstr(0, 0, "Your Sticker is: " + user_input)
        stdscr.addstr(
            2,
            0,
            "Sticker generated in /Acadia/Sticker_Generator/data! Uploading to RedBubble...",
        )
        stdscr.refresh()
        #redbubble_upload()
    else:
        stdscr.refresh()
        stdscr.clear()
        stdscr.addstr(0, 0, "Invalid Generator. Please try again.")

    # Wait for user input before closing the program
    stdscr.getch()


if __name__ == "__main__":
    curses.wrapper(main)

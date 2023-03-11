import os
import argparse
import openai
import curses
import sys
import select
import time
import tty
import termios
from generators.dalle.dalle import generate_dalle
from transformer.remove_background import backround_remover
from ..Selenium.driver import redbubble_upload

#############################################################################
#
# Args
#
#############################################################################

# What generator are you running? What image size is desired?

# Parser
parser = argparse.ArgumentParser()

# Parser Arguements
parser.add_argument(
    "-generator", "--generator", help="Generator must be dalle (for now)", type=str
)
parser.add_argument("-size", "--size", help="Size must be 256, 512, 1024", type=str)
parser.add_argument("-n", "--n", help="Number of stickers to generate", type=int)
args = parser.parse_args()

#############################################################################
#
# PATHS
#
#############################################################################

# What is the base directory of the project?

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#############################################################################
#
# ENVIRONMENT VARIABLES
#
#############################################################################

# What are the environment variables?

openai.organization = os.environ.get("ENV_OPENAI_ORG")
openai.api_key = os.environ.get("ENV_OPENAI_KEY")

#############################################################################
#
# Runtime
#
#############################################################################

# sticker_generator.py
# def loading_bar(text="Loading", flag=None):
#     dots = ""
#     while flag is None or not flag:
#         for i in range(4):
#             if flag is not None and flag:
#                 break
#             time.sleep(0.2)
#             dots = dots + "." if i < 3 else ""
#             sys.stdout.write("\r" + text + dots)
#             sys.stdout.flush()
#         if flag is not None and flag:
#             break
#         dots = ""
#         sys.stdout.write("\r" + text + "   ")
#         sys.stdout.flush()
#     # Clear the loading bar and display the "Sticker generated!" message
#     sys.stdout.write("\r" + " " * (len(text) + 102))
#     sys.stdout.flush()
#     sys.stdout.write("\r" + "Sticker generated!")
#     sys.stdout.flush()


def main(stdscr):
    # Hide cursor
    curses.curs_set(0)

    # Print initial prompt for user input
    stdscr.addstr(0, 0, "Enter the text for the sticker: ")
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
                stdscr.addstr(i+4, 2, "> " + options_generator[i])
            else:
                stdscr.addstr(i+4, 4, options_generator[i])
        stdscr.refresh()

        # Wait for user input
        key = stdscr.getch()

        # Update selected option based on user input
        if key == curses.KEY_UP:
            selected_option_generator = (selected_option_generator - 1) % len(options_generator)
        elif key == curses.KEY_DOWN:
            selected_option_generator = (selected_option_generator + 1) % len(options_generator)
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
                stdscr.addstr(i+4, 2, "> " + options_sticker[i])
            else:
                stdscr.addstr(i+4, 4, options_sticker[i])
        stdscr.refresh()

        # Wait for user input
        key = stdscr.getch()

        # Update selected option based on user input
        if key == curses.KEY_UP:
            selected_option_sticker = (selected_option_sticker - 1) % len(options_sticker)
        elif key == curses.KEY_DOWN:
            selected_option_sticker = (selected_option_sticker + 1) % len(options_sticker)
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
        sticker = generate_dalle(user_input, options_sticker[selected_option_sticker])
        backround_remover(sticker)
        stdscr.refresh()
        # Clear screen and print final message
        stdscr.clear()
        stdscr.addstr(0, 0, "Your Sticker is: " + user_input)
        stdscr.addstr(2, 0, "Sticker generated in /Acadia/Sticker_Generator/data! Uploading to RedBubble...")
        stdscr.refresh()
        redbubble_upload()
    else:
        stdscr.refresh()
        stdscr.clear()
        stdscr.addstr(0, 0, "Invalid Generator. Please try again.")

    # Wait for user input before closing the program
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)

# if __name__ == "__main__":
#     # What is the generator?
#     if args.generator == "dalle":
#         generate_dalle(args.size, args.n)
#     else:
#         print("Please specify a generator with -generator, defaulting to dalle")
#         generate_dalle(args.size, args.n)



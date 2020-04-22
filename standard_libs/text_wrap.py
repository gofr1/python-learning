#!/usr/bin/env python3

import textwrap

loremIpsum = """    Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia 
deserunt mollit anim id est laborum"""

def main():
    print("No dedent:")
    print(textwrap.fill(loremIpsum))
    print()

    print("Dedent:")
    print()

    dedentText = textwrap.dedent(loremIpsum).strip()
    print(dedentText)
    print()

    print("Fill:")
    print()
    print(textwrap.fill(dedentText, width=50))
    print(textwrap.fill(dedentText, width=100))
    print()

    print("Controlling indent:")
    print()
    print(textwrap.fill(dedentText, initial_indent="    ", subsequent_indent=""))
    print(textwrap.fill(dedentText, initial_indent="    ", subsequent_indent="     "))
    print()

    print("Shortening text:")
    print()
    print(textwrap.shorten("Something is great!", width=12, placeholder="..."))

if __name__ == '__main__':
    main()
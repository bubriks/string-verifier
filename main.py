import os
import sys
import re


def main():
    expression = os.environ["INPUT_EXPRESSION"]
    strings = os.environ["INPUT_STRINGS"]

    groups = None
    match = None
    for i in strings.split(" "):
        match = re.match(expression, i)
        if match:
            if groups is None:
                groups = match.groups()
            elif groups != match.groups():
                sys.exit("Groups dont match" +
                         "\nGroup 1: " + str(groups) +
                         "\nGroup 2: " + str(match.groups()))
        else:
            sys.exit("String doesnt match the pattern" +
                     "\nString: " + i)
    print(f"::set-output name=groups::{' '.join(match.groups())}")
    print(f"::set-output name=result::{match.group(0)}")


if __name__ == "__main__":
    main()
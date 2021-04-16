import os
import sys
import re

def main():
    expression = os.environ["INPUT_EXPRESSION"]
    strings = os.environ["INPUT_STRINGS"]
    
    groups = None
    for i in strings.split(" "):
        m = re.match(expression, i)
        if m:
            if groups is None:
                groups = m.groups
            elif groups != m.groups:
                sys.exit("Groups dont match" +
                         "\nGroup 1: " + str(groups()) +
                         "\nGroup 2: " + str(m.groups()))
        else:
            sys.exit("String doesnt match the pattern" +
                     "\nString: " + i)
    print(f"::set-output name=groups::{groups}")
    
if __name__ == "__main__":
    main()
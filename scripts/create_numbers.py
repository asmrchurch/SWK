#!/usr/bin/env python3

import subprocess

applescript = '''
tell application "Numbers"
    set newDoc to make new document
    tell newDoc
        tell the first table of the first sheet
            add row below
            set value of cell 1 of row 1 to "Name"
            set value of cell 2 of row 1 to "Age"
            set value of cell 3 of row 1 to "City"
            add row below
            set value of cell 1 of row 2 to "Alice"
            set value of cell 2 of row 2 to 25
            set value of cell 3 of row 2 to "New York"
            add row below
            set value of cell 1 of row 3 to "Bob"
            set value of cell 2 of row 3 to 30
            set value of cell 3 of row 3 to "San Francisco"
        end tell
    end tell
    save newDoc in (POSIX file "/Users/suganolab/Desktop/test.numbers")
end tell
'''

# Run AppleScript via subprocess
subprocess.run(["osascript", "-e", applescript])

print("Numbers file created on Desktop!")

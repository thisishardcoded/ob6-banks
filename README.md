# ob6-banks
Python script to set bank of OB6 patch sysex dumps.

Presets for the Sequential OB-6 synthesiser are typically supplied as MIDI sysex files with a fixed bank number. This Python script takes such a file and renumbers the bank of each patch with the given value. This saves you writing over banks you wish to keep intact.

If Python3 isn't running on your system you'll need to download and install it as described here:

https://www.python.org/downloads/

You will also need to know how to run Python from the command line. There's a beginner's guide here:

https://wiki.python.org/moin/BeginnersGuide

Either check out this repo or simply create a blank python file called bank.py and paste the code in bank.py into it.

Make sure bank.py and the sysex file you want to process are in the same directory.

Use as follows:

> python3 bank.py [filename: a sysex file of OB-6 patches in the correct format] [new bank number, a number in the range 0 to 4]

All being well the script should reply with a success message noting the previous bank number and confirming the new bank number

Caveats:

** THIS WAS THROWN TOGETHER QUICKLY *** USE AT YOUR OWN RISK *** BACK UP YOUR DATA FIRST **

** FEED THE SCRIPT JUNK AND IT'LL GIVE JUNK BACK *** DON'T SEND JUNK TO YOUR OB-6 *** I DON'T KNOW WHAT WILL HAPPEN **

** BANKS ARE ZERO INDEXED *** NUMBERED FROM 0 TO 4, NOT 1 to 5 IN OTHER WORDS **

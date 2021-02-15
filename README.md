# IOT-Inspector HomeWork

This is the homework assignment of Tamás Dobi for the company IoT-Inspector

## Installation

No need to install anything other than python 3

## Usage

Open the folder, then locate "input.txt". You have to provide the numbers you want the program to check.

You have to place these numbers under eachother without any extra space

For example:

```python

             _  _  _  _  _  _  _  _  _
            |_||_||_||_||_||_||_||_||_|
            |_||_||_||_||_||_||_||_||_|

                _  _  _  _  _  _     _
            |_||_|| || ||_   |  |  | _
              | _||_||_||_|  |  |  | _|

```

Then all you have to do is run the write_to_file.py file.

## Output

If the program ran it created an "output.txt" file which contains all the checked numbers.
There are 3 types of output for a number:

    If there were no fix found: the number will get a plus " ILL" keyword after the number for example : ['4', '9', '0', '0', '6', '7', '7', '1', '?'] ILL

    If there is only 1 possible fix: the number will get printed without any additional keywords for example: ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    If there are multiple fixes: the number will get printed and then all the possible fixes following it for example: ['5', '5', '5', '5', '5', '5', '5', '5', '5'] AMB[['5', '5', '9', '5', '5', '5', '5', '5', '5'], ['5', '5', '5', '6', '5', '5', '5', '5', '5']]

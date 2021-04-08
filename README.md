
# Register Machine Simulator

[![GitHub](https://img.shields.io/github/license/informaticfreak/vectometry)](LICENSE.txt)&nbsp;
[![Python Version](https://img.shields.io/badge/python-3-blue)](https://www.python.org/downloads/)&nbsp;

A simulator for a simple register machine as an code interpreter written in Python. The register machine language defines 29 different commands for basic input, output and arithmetic operations.

## How to use

Execute the Python file `rm_interpreter.py` via the console/terminal and as a first command line parameter pass the path to the `.rm` code file. Optionally add a `-p` as second command line parameter to get the status of the accumulator and the instruction counter after each instruction or `-w` for the status and an additional wait for pressing the enter key to continue after each instruction.

```
py rm_interpreter.py [path] [optional -p or -w]
```

## An example: calculation of the faculty of an integer

The file `examples/faculty.rm` contains the code for the calculation, click [here](examples/faculty.rm) to open it. Because the source file `rm_interpreter.py` is located in the directory `src` the relative path to the example file is `../examples/faculty.rm`. To see the status of the register machine while the program is running, the last parameter is `-p`.

```
py rm_interpreter.py ../examples/faculty.rm -p
```

So after the start of the program, the program waits with printing `INP: `&nbsp;for the input of a number to calculate its faculty. You can also enter a decimal number or a negative number, but an integer is required. This wrong inputs are intercepted by the register machine program code in [line 13](examples/faculty.rm#L13) and [line 17](examples/faculty.rm#L17). In this case the input number is `3`.

```
STATUS: accu: 0 | cind: 1
INP: 3
STATUS: accu: 0 | cind: 2
STATUS: accu: 3.0 | cind: 3
STATUS: accu: 3.0 | cind: 4
STATUS: accu: 2.0 | cind: 5
STATUS: accu: 2.0 | cind: 6
STATUS: accu: 3.0 | cind: 7
STATUS: accu: 3.0 | cind: 8
STATUS: accu: 3.0 | cind: 9
STATUS: accu: 3.0 | cind: 10
STATUS: accu: 3.0 | cind: 11
STATUS: accu: 3.0 | cind: 12
STATUS: accu: 2.0 | cind: 13
STATUS: accu: 2.0 | cind: 14
STATUS: accu: 2.0 | cind: 10
STATUS: accu: 2.0 | cind: 11
STATUS: accu: 2.0 | cind: 12
STATUS: accu: 1.0 | cind: 13
STATUS: accu: 1.0 | cind: 14
STATUS: accu: 1.0 | cind: 10
STATUS: accu: 1.0 | cind: 11
STATUS: accu: 1.0 | cind: 12
STATUS: accu: 0.0 | cind: 13
STATUS: accu: 0.0 | cind: 14
STATUS: accu: 0.0 | cind: 15
STATUS: accu: 0.0 | cind: 16
STATUS: accu: 3.0 | cind: 17
STATUS: accu: 3.0 | cind: 18
STATUS: accu: 3.0 | cind: 19
STATUS: accu: 3.0 | cind: 20
STATUS: accu: 2.0 | cind: 21
STATUS: accu: 2.0 | cind: 22
STATUS: accu: 2.0 | cind: 23
STATUS: accu: 6.0 | cind: 24
STATUS: accu: 6.0 | cind: 25
STATUS: accu: 6.0 | cind: 18
STATUS: accu: 6.0 | cind: 19
STATUS: accu: 2.0 | cind: 20
STATUS: accu: 1.0 | cind: 21
STATUS: accu: 1.0 | cind: 22
STATUS: accu: 1.0 | cind: 23
STATUS: accu: 6.0 | cind: 24
STATUS: accu: 6.0 | cind: 25
STATUS: accu: 6.0 | cind: 18
STATUS: accu: 6.0 | cind: 19
STATUS: accu: 1.0 | cind: 20
STATUS: accu: 0.0 | cind: 21
STATUS: accu: 0.0 | cind: 29
STATUS: accu: 0.0 | cind: 30
OUT: 6.0
STATUS: accu: 0.0 | cind: 31
Program finished
```

After the program is finished, the calculated faculty of the input number `3` is `6`. If a wrong number is entered, no output will be printed.

## Documentation

### The syntax

* A command is composed of a three character long keyword and a number as parameter separated by a space character&nbsp;` `
* A comment starts with an hashtag character&nbsp;`#`&nbsp;at the beginning of a line or behind a command, separated by a space character&nbsp;` `
* Only one command per line and any number of blank lines are allowed
* The keywords are not case sensitve
* A Parameter is always a number, it can contain underscores&nbsp;`_`&nbsp;and any number of zeros&nbsp;`0`, a dot&nbsp;`.`&nbsp;as decimal point works only for constants, inputs and anchor points
* A program is terminated with the command&nbsp;`HLT 99`, if this command is not in the last line of the program at the latest, it is terminated, but with an error

### All 29 commands

#### Start and terminate the program

Command | Parameter | Description
------- | ---------- | -----------
`INI` | 00 | No functionality (internal use only)
`HTL` | 99 | Terminate the program

#### Load and store values

Command | Parameter | Description
------- | --------- | -----------
`LDK` | *number* | Load value *number* in accumulator
`LDA` | *addresse* | Load value from *addresse* in accumulator
`LDP` | *addresse* | Load value from address to which *address* points into accumulator
`STA` | *addresse* | Store value from accumulator in *addresse*
`STP` | *addresse* | Store value from accumulator in addresse, where *address* points to

#### Anchor points and jumps to them

Command | Parameter | Description
------- | --------- | -----------
`ANC` | *anchor* | Anchor point with *anchor* as id
`JMP` | *anchor* | Unconditional jump to *anchor*
`JEZ` | *anchor* | Conditional jump to *anchor*, if value from accumulator is equal to zero
`JLZ` | *anchor* | Conditional jump to *anchor*, if value from accumulator is less than zero
`JGZ` | *anchor* | Conditional jump to *anchor*, if value from accumulator is greater than zero
`JNE` | *anchor* | Conditional jump to *anchor*, if value from accumulator is not equal to zero
`JLE` | *anchor* | Conditional jump to *anchor*, if value from accumulator is less than or equal to zero
`JGE` | *anchor* | Conditional jump to *anchor*, if value from accumulator is greater than or equal to zero

#### Read input and print output

Command | Parameter | Description
------- | --------- | -----------
`INP` | *addresse* | Wait for user input with `INP: `&nbsp;and store the entered number in *addresse*
`OUT` | *addresse* | Print value from *addresse*

#### Arithmetic operations

Command | Parameter | Description
------- | --------- | -----------
`ADK` | *number* | Add value *number* to value from accumulator
`ADA` | *addresse* | Add value from *addresse* to value from accumulator
`ADP` | *addresse* | Add value from addresse to which *addresse* points to value from accumulator
`SUK` | *number* | Subtract value *number* from value from accumulator
`SUA` | *addresse* | Subtract value from *addresse* from value from accumulator
`SUP` | *addresse* | Subtract value from addresse to which *addresse* points from value from accumulator
`MUK` | *number* | Multiply value *number* by value from accumulator
`MUA` | *addresse* | Multiply value from *addresse* by value from accumulator
`MUP` | *addresse* | Multiply value from addresse to which *addresse* points by value from accumulator
`DIK` | *number* | Divide value from accumulator by value *number*
`DIA` | *addresse* | Divide value from accumulator by value from *addresse*
`DIP` | *addresse* | Divide value from accumulator by value from addresse to which *addresse* points to

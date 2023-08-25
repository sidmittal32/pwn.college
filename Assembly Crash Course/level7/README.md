# Level Description
```
hacker@assembly-crash-course-level-7:~$ /challenge/run

Welcome to ASMLevel7
==================================================

To interact with any level you will send raw bytes over stdin to this program.
To efficiently solve these problems, first run it once to see what you need
then craft, assemble, and pipe your bytes to this program.

In this level you will be working with registers. You will be asked to modify
or read from registers_use.

We will now set some values in memory dynamically before each run. On each run
the values will change. This means you will need to do some type of formulaic
operation with registers_use. We will tell you which registers_use are set beforehand
and where you should put the result. In most cases, its rax.

In this level you will be working with bit logic and operations. This will involve heavy use of
directly interacting with bits stored in a register or memory location. You will also likely
need to make use of the logic instructions in x86: and, or, not, xor.



Shifting in assembly is another interesting concept! x86 allows you to 'shift'
bits around in a register. Take for instance, rax. For the sake of this example
say rax only can store 8 bits (it normally stores 64). The value in rax is:
rax = 10001010
If we shift the value once to the left:
shl rax, 1
The new value is:
rax = 00010100
As you can see, everything shifted to the left and the highest bit fell off and
a new 0 was added to the right side. You can use this to do special things to
the bits you care about. It also has the nice side affect of doing quick multiplication,
division, and possibly modulo.
Here are the important instructions:
shl reg1, reg2       <=>     Shift reg1 left by the amount in reg2
shr reg1, reg2       <=>     Shift reg1 right by the amount in reg2
Note: all 'regX' can be replaced by a constant or memory location

Using only the following instructions:
mov, shr, shl
Please perform the following:
Set rax to the 5th least significant byte of rdi
i.e.
rdi = | B7 | B6 | B5 | B4 | B3 | B2 | B1 | B0 |
Set rax to the value of B4

We will now set the following in preparation for your code:
rdi = 0x62de7e71bc6a889e

Please give me your assembly in bytes (up to 0x1000 bytes): 
```

# Solution
```py
import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
mov rax, rdi
shl rax, 24
shr rax, 56
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())
```

```
@assembly-crash-course-level-7:~$ ipython
Python 3.8.10 (default, May 26 2023, 14:05:08) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.2 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pwn
   ...: pwn.context.update(arch="amd64")
   ...: code = pwn.asm("""
   ...: mov rax, rdi
   ...: shl rax, 24
   ...: shr rax, 56
   ...: """ )
   ...: process = pwn.process("/challenge/run")
   ...: process.write(code)
   ...: print(process.readall())
[x] Starting local process '/challenge/run'
[+] Starting local process '/challenge/run': pid 999
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 962B
[x] Receiving all data: 2.12KB
[x] Receiving all data: 2.18KB
[x] Receiving all data: 2.24KB
[x] Receiving all data: 2.30KB
[x] Receiving all data: 2.36KB
[+] Receiving all data: Done (2.36KB)
[*] Process '/challenge/run' stopped with exit code 0 (pid 999)
b"\nWelcome to ASMLevel7\n==================================================\n\nTo interact with any level you will send raw bytes over stdin to this program.\nTo efficiently solve these problems, first run it once to see what you need\nthen craft, assemble, and pipe your bytes to this program.\n\nIn this level you will be working with registers. You will be asked to modify\nor read from registers_use.\n\nWe will now set some values in memory dynamically before each run. On each run\nthe values will change. This means you will need to do some type of formulaic\noperation with registers_use. We will tell you which registers_use are set beforehand\nand where you should put the result. In most cases, its rax.\n\nIn this level you will be working with bit logic and operations. This will involve heavy use of\ndirectly interacting with bits stored in a register or memory location. You will also likely\nneed to make use of the logic instructions in x86: and, or, not, xor.\n\n\n\nShifting in assembly is another interesting concept! x86 allows you to 'shift'\nbits around in a register. Take for instance, rax. For the sake of this example\nsay rax only can store 8 bits (it normally stores 64). The value in rax is:\nrax = 10001010\nIf we shift the value once to the left:\nshl rax, 1\nThe new value is:\nrax = 00010100\nAs you can see, everything shifted to the left and the highest bit fell off and\na new 0 was added to the right side. You can use this to do special things to\nthe bits you care about. It also has the nice side affect of doing quick multiplication,\ndivision, and possibly modulo.\nHere are the important instructions:\nshl reg1, reg2       <=>     Shift reg1 left by the amount in reg2\nshr reg1, reg2       <=>     Shift reg1 right by the amount in reg2\nNote: all 'regX' can be replaced by a constant or memory location\n\nUsing only the following instructions:\nmov, shr, shl\nPlease perform the following:\nSet rax to the 5th least significant byte of rdi\ni.e.\nrdi = | B7 | B6 | B5 | B4 | B3 | B2 | B1 | B0 |\nSet rax to the value of B4\n\nWe will now set the following in preparation for your code:\nrdi = 0x8a1298e2623e8b1e\n\nPlease give me your assembly in bytes (up to 0x1000 bytes): \nExecuting your code...\n---------------- CODE ----------------\n0x400000:\tmov   \trax, rdi\n0x400003:\tshl   \trax, 0x18\n0x400007:\tshr   \trax, 0x38\n--------------------------------------\npwn.college{wrB-DHL6MsTSZpVn-kEvPc5V5wC.0FMwIDL5IDOzMzW}\n\n"
```

# Flag
`pwn.college{wrB-DHL6MsTSZpVn-kEvPc5V5wC.0FMwIDL5IDOzMzW}`

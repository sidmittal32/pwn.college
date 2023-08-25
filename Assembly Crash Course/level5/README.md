# Problem Description
```
hacker@assembly-crash-course-level-5:~$ /challenge/run

Welcome to ASMLevel5
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



Modulo in assembly is another interesting concept! x86 allows you to get the
remainder after doing a division on something. For instance:
10 / 3  ->  remainder = 1
You can get the remainder of a division using the instructions introduced earlier
through the div instruction.
In most programming languages we refer to mod with the symbol '%'.

Please compute the following:
rdi % rsi
Place the value in rax.

We will now set the following in preparation for your code:
rdi = 0x11857d73
rsi = 0x3fff

Please give me your assembly in bytes (up to 0x1000 bytes): 
```

# Solution
```py
import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
mov rax, rdi
div rsi
mov rax, rdx
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())
```

```
hacker@assembly-crash-course-level-5:~$ ipython
Python 3.8.10 (default, May 26 2023, 14:05:08) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.2 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pwn
   ...: pwn.context.update(arch="amd64")
   ...: code = pwn.asm("""
   ...: mov rax, rdi
   ...: div rsi
   ...: mov rax, rdx
   ...: """ )
   ...: process = pwn.process("/challenge/run")
   ...: process.write(code)
   ...: print(process.readall())
[x] Starting local process '/challenge/run'
[+] Starting local process '/challenge/run': pid 1023
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 702B
[x] Receiving all data: 1.23KB
[x] Receiving all data: 1.29KB
[x] Receiving all data: 1.34KB
[x] Receiving all data: 1.40KB
[x] Receiving all data: 1.46KB
[+] Receiving all data: Done (1.46KB)
[*] Process '/challenge/run' stopped with exit code 0 (pid 1023)
b"\nWelcome to ASMLevel5\n==================================================\n\nTo interact with any level you will send raw bytes over stdin to this program.\nTo efficiently solve these problems, first run it once to see what you need\nthen craft, assemble, and pipe your bytes to this program.\n\nIn this level you will be working with registers. You will be asked to modify\nor read from registers_use.\n\nWe will now set some values in memory dynamically before each run. On each run\nthe values will change. This means you will need to do some type of formulaic\noperation with registers_use. We will tell you which registers_use are set beforehand\nand where you should put the result. In most cases, its rax.\n\n\n\nModulo in assembly is another interesting concept! x86 allows you to get the\nremainder after doing a division on something. For instance:\n10 / 3  ->  remainder = 1\nYou can get the remainder of a division using the instructions introduced earlier\nthrough the div instruction.\nIn most programming languages we refer to mod with the symbol '%'.\n\nPlease compute the following:\nrdi % rsi\nPlace the value in rax.\n\nWe will now set the following in preparation for your code:\nrdi = 0x2d7393a\nrsi = 0x7\n\nPlease give me your assembly in bytes (up to 0x1000 bytes): \nExecuting your code...\n---------------- CODE ----------------\n0x400000:\tmov   \trax, rdi\n0x400003:\tdiv   \trsi\n0x400006:\tmov   \trax, rdx\n--------------------------------------\npwn.college{EmeYv7WHfqvdQp7z2HrdaS_C-Iy.0FO5EDL5IDOzMzW}\n\n"
```

# Flag
`pwn.college{EmeYv7WHfqvdQp7z2HrdaS_C-Iy.0FO5EDL5IDOzMzW}`

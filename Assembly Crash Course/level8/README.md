# Level Description
```
hacker@assembly-crash-course-level-8:~$ /challenge/run

Welcome to ASMLevel8
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



Bitwise logic in assembly is yet another interesting concept!
x86 allows you to perform logic operation bit by bit on registers.
For the sake of this example say registers only store 8 bits.
The values in rax and rbx are:
rax = 10101010
rbx = 00110011
'If we were to perform a bitwise AND of rax and rbx using the and rax, rbx instruction'
the result would be calculated by ANDing each pair bits 1 by 1 hence why
it's called a bitwise logic. So from left to right:
1 AND 0 = 0, 0 AND 0 = 0, 1 AND 1 = 1, 0 AND 1 = 0 ...
Finally we combine the results together to get:
rax = 00100010
Here are some truth tables for reference:
    AND          OR           XOR
 A | B | X    A | B | X    A | B | X
---+---+---  ---+---+---  ---+---+---
 0 | 0 | 0    0 | 0 | 0    0 | 0 | 0
 0 | 1 | 0    0 | 1 | 1    0 | 1 | 1
 1 | 0 | 0    1 | 0 | 1    1 | 0 | 1
 1 | 1 | 1    1 | 1 | 1    1 | 1 | 0

Without using the following instructions:
mov, xchg
Please perform the following:
rax = rdi AND rsi
i.e. Set rax to the value of (rdi AND rsi)

We will now set the following in preparation for your code:
rdi = 0x6d62b24e248376c4
rsi = 0x71d0046113d7c199

Please give me your assembly in bytes (up to 0x1000 bytes): 
```

# Solution
```py
import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
and rax, rdi
and rax, rsi
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())
```

```
hacker@assembly-crash-course-level-8:~$ ipython
Python 3.8.10 (default, May 26 2023, 14:05:08) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.2 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pwn
   ...: pwn.context.update(arch="amd64")
   ...: code = pwn.asm("""
   ...: and rax, rdi
   ...: and rax, rsi
   ...: """ )
   ...: process = pwn.process("/challenge/run")
   ...: process.write(code)
   ...: print(process.readall())
[x] Starting local process '/challenge/run'
[+] Starting local process '/challenge/run': pid 753
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 962B
[x] Receiving all data: 2.11KB
[x] Receiving all data: 2.17KB
[x] Receiving all data: 2.20KB
[x] Receiving all data: 2.26KB
[x] Receiving all data: 2.32KB
[+] Receiving all data: Done (2.32KB)
[*] Process '/challenge/run' stopped with exit code 0 (pid 753)
b"\nWelcome to ASMLevel8\n==================================================\n\nTo interact with any level you will send raw bytes over stdin to this program.\nTo efficiently solve these problems, first run it once to see what you need\nthen craft, assemble, and pipe your bytes to this program.\n\nIn this level you will be working with registers. You will be asked to modify\nor read from registers_use.\n\nWe will now set some values in memory dynamically before each run. On each run\nthe values will change. This means you will need to do some type of formulaic\noperation with registers_use. We will tell you which registers_use are set beforehand\nand where you should put the result. In most cases, its rax.\n\nIn this level you will be working with bit logic and operations. This will involve heavy use of\ndirectly interacting with bits stored in a register or memory location. You will also likely\nneed to make use of the logic instructions in x86: and, or, not, xor.\n\n\n\nBitwise logic in assembly is yet another interesting concept!\nx86 allows you to perform logic operation bit by bit on registers.\nFor the sake of this example say registers only store 8 bits.\nThe values in rax and rbx are:\nrax = 10101010\nrbx = 00110011\n'If we were to perform a bitwise AND of rax and rbx using the and rax, rbx instruction'\nthe result would be calculated by ANDing each pair bits 1 by 1 hence why\nit's called a bitwise logic. So from left to right:\n1 AND 0 = 0, 0 AND 0 = 0, 1 AND 1 = 1, 0 AND 1 = 0 ...\nFinally we combine the results together to get:\nrax = 00100010\nHere are some truth tables for reference:\n    AND          OR           XOR\n A | B | X    A | B | X    A | B | X\n---+---+---  ---+---+---  ---+---+---\n 0 | 0 | 0    0 | 0 | 0    0 | 0 | 0\n 0 | 1 | 0    0 | 1 | 1    0 | 1 | 1\n 1 | 0 | 0    1 | 0 | 1    1 | 0 | 1\n 1 | 1 | 1    1 | 1 | 1    1 | 1 | 0\n\nWithout using the following instructions:\nmov, xchg\nPlease perform the following:\nrax = rdi AND rsi\ni.e. Set rax to the value of (rdi AND rsi)\n\nWe will now set the following in preparation for your code:\nrdi = 0x60d594140088b940\nrsi = 0x94ee988bf33bd4ee\n\nPlease give me your assembly in bytes (up to 0x1000 bytes): \nExecuting your code...\n---------------- CODE ----------------\n0x400000:\tand   \trax, rdi\n0x400003:\tand   \trax, rsi\n--------------------------------------\npwn.college{4loQeJsqnotY6LaH5tvSoCa9A8f.0VMwIDL5IDOzMzW}\n\n"
```

# Flag
`pwn.college{4loQeJsqnotY6LaH5tvSoCa9A8f.0VMwIDL5IDOzMzW}`

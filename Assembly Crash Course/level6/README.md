# Level Description
```
hacker@assembly-crash-course-level-6:~$ /challenge/run

Welcome to ASMLevel6
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



Another cool concept in x86 is the independent access to lower register bytes.
Each register in x86 is 64 bits in size, in the previous levels we have accessed
the full register using rax, rdi or rsi. We can also access the lower bytes of
each register using different register names. For example the lower
32 bits of rax can be accessed using eax, lower 16 bits using ax,
lower 8 bits using al, etc.
MSB                                    LSB
+----------------------------------------+
|                   rax                  |
+--------------------+-------------------+
                     |        eax        |
                     +---------+---------+
                               |   ax    |
                               +----+----+
                               | ah | al |
                               +----+----+
Lower register bytes access is applicable to all registers_use.

Using only the following instruction(s)
mov
Please compute the following:
rax = rdi modulo 256
rbx = rsi modulo 65536

We will now set the following in preparation for your code:
rdi = 0x42d8
rsi = 0x5d2dc86f

Please give me your assembly in bytes (up to 0x1000 bytes): 
```

# Solution
```py
import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
mov al, dil
mov bx, si
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())
```

```
hacker@assembly-crash-course-level-6:~$ ipython
Python 3.8.10 (default, May 26 2023, 14:05:08) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.2 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pwn
   ...: pwn.context.update(arch="amd64")
   ...: code = pwn.asm("""
   ...: mov al, dil
   ...: mov bx, si
   ...: """ )
   ...: process = pwn.process("/challenge/run")
   ...: process.write(code)
   ...: print(process.readall())
[x] Starting local process '/challenge/run'
[+] Starting local process '/challenge/run': pid 1494
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 702B
[x] Receiving all data: 1.83KB
[x] Receiving all data: 1.89KB
[x] Receiving all data: 1.91KB
[x] Receiving all data: 1.97KB
[x] Receiving all data: 2.03KB
[+] Receiving all data: Done (2.03KB)
[*] Process '/challenge/run' stopped with exit code 0 (pid 1494)
b'\nWelcome to ASMLevel6\n==================================================\n\nTo interact with any level you will send raw bytes over stdin to this program.\nTo efficiently solve these problems, first run it once to see what you need\nthen craft, assemble, and pipe your bytes to this program.\n\nIn this level you will be working with registers. You will be asked to modify\nor read from registers_use.\n\nWe will now set some values in memory dynamically before each run. On each run\nthe values will change. This means you will need to do some type of formulaic\noperation with registers_use. We will tell you which registers_use are set beforehand\nand where you should put the result. In most cases, its rax.\n\n\n\nAnother cool concept in x86 is the independent access to lower register bytes.\nEach register in x86 is 64 bits in size, in the previous levels we have accessed\nthe full register using rax, rdi or rsi. We can also access the lower bytes of\neach register using different register names. For example the lower\n32 bits of rax can be accessed using eax, lower 16 bits using ax,\nlower 8 bits using al, etc.\nMSB                                    LSB\n+----------------------------------------+\n|                   rax                  |\n+--------------------+-------------------+\n                     |        eax        |\n                     +---------+---------+\n                               |   ax    |\n                               +----+----+\n                               | ah | al |\n                               +----+----+\nLower register bytes access is applicable to all registers_use.\n\nUsing only the following instruction(s)\nmov\nPlease compute the following:\nrax = rdi modulo 256\nrbx = rsi modulo 65536\n\nWe will now set the following in preparation for your code:\nrdi = 0xc186\nrsi = 0xf9a82140\n\nPlease give me your assembly in bytes (up to 0x1000 bytes): \nExecuting your code...\n---------------- CODE ----------------\n0x400000:\tmov   \tal, dil\n0x400003:\tmov   \tbx, si\n--------------------------------------\npwn.college{MFV-J6y57UCDXxym3ZMtIhCpfaa.0VO5EDL5IDOzMzW}\n\n'
```

# Flag
`pwn.college{MFV-J6y57UCDXxym3ZMtIhCpfaa.0VO5EDL5IDOzMzW}`

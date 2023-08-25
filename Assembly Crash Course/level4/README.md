# Level Description
```
hacker@assembly-crash-course-level-4:~$ /challenge/run

Welcome to ASMLevel4
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



Recall division in x86 is more special than in normal math. Math in here is
called integer math. This means everything, as it is now, is in the realm
of whole looking numbers. As an example:
10 / 3 = 3 in integer math. Why? Because 3.33 gets rounded down to an integer.
The relevant instructions for this level are:
mov rax, reg1; div reg2
Notice: to use this instruction you need to first load rax with the desired register
you intended to be the divided. Then run div reg2, where reg2 is the divisor. This
results in:
rax = rdi / rsi; rdx = remainder
The quotient is placed in rax, the remainder is placed in rdx.
Please compute the following:
speed = distance / time, where:
distance = rdi
time = rsi
Place the value of speed into rax given the above.
We will now set the following in preparation for your code:
rdi = 0x1285
rsi = 0x1e

Please give me your assembly in bytes (up to 0x1000 bytes): 
```

# Solution
```py
import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
mov rax, rdi
div rsi
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())
```

```
hacker@assembly-crash-course-level-4:~$ ipython
Python 3.8.10 (default, May 26 2023, 14:05:08) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.2 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pwn
   ...: pwn.context.update(arch="amd64")
   ...: code = pwn.asm("""
   ...: mov rax, rdi
   ...: div rsi
   ...: """ )
   ...: process = pwn.process("/challenge/run")
   ...: process.write(code)
   ...: print(process.readall())
[x] Starting local process '/challenge/run'
[+] Starting local process '/challenge/run': pid 806
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 702B
[x] Receiving all data: 1.57KB
[x] Receiving all data: 1.63KB
[x] Receiving all data: 1.65KB
[x] Receiving all data: 1.71KB
[x] Receiving all data: 1.77KB
[+] Receiving all data: Done (1.77KB)
[*] Process '/challenge/run' stopped with exit code 0 (pid 806)
b'\nWelcome to ASMLevel4\n==================================================\n\nTo interact with any level you will send raw bytes over stdin to this program.\nTo efficiently solve these problems, first run it once to see what you need\nthen craft, assemble, and pipe your bytes to this program.\n\nIn this level you will be working with registers. You will be asked to modify\nor read from registers_use.\n\nWe will now set some values in memory dynamically before each run. On each run\nthe values will change. This means you will need to do some type of formulaic\noperation with registers_use. We will tell you which registers_use are set beforehand\nand where you should put the result. In most cases, its rax.\n\n\n\nRecall division in x86 is more special than in normal math. Math in here is\ncalled integer math. This means everything, as it is now, is in the realm\nof whole looking numbers. As an example:\n10 / 3 = 3 in integer math. Why? Because 3.33 gets rounded down to an integer.\nThe relevant instructions for this level are:\nmov rax, reg1; div reg2\nNotice: to use this instruction you need to first load rax with the desired register\nyou intended to be the divided. Then run div reg2, where reg2 is the divisor. This\nresults in:\nrax = rdi / rsi; rdx = remainder\nThe quotient is placed in rax, the remainder is placed in rdx.\nPlease compute the following:\nspeed = distance / time, where:\ndistance = rdi\ntime = rsi\nPlace the value of speed into rax given the above.\nWe will now set the following in preparation for your code:\nrdi = 0x2263\nrsi = 0x2f\n\nPlease give me your assembly in bytes (up to 0x1000 bytes): \nExecuting your code...\n---------------- CODE ----------------\n0x400000:\tmov   \trax, rdi\n0x400003:\tdiv   \trsi\n--------------------------------------\npwn.college{kZwVCW5RvWoQKwEg75ISsrAs34e.01N5EDL5IDOzMzW}\n\n'
```

# Flag
`pwn.college{kZwVCW5RvWoQKwEg75ISsrAs34e.01N5EDL5IDOzMzW}`

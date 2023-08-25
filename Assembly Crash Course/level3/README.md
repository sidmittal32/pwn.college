# Level Description
```
hacker@assembly-crash-course-level-3:~$ /challenge/run

Welcome to ASMLevel3
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



Using your new knowledge, please compute the following:
f(x) = mx + b, where:
m = rdi
x = rsi
b = rdx
Place the value into rax given the above.
We will now set the following in preparation for your code:
rdi = 0xf38
rsi = 0x18aa
rdx = 0x22a9

Please give me your assembly in bytes (up to 0x1000 bytes): 
```

# Solution
```py
import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
imul rdi, rsi
add rdi, rdx
mov rax, rdi
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())
```

```
hacker@assembly-crash-course-level-3:~$ ipython
Python 3.8.10 (default, May 26 2023, 14:05:08) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.2 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pwn
   ...: pwn.context.update(arch="amd64")
   ...: code = pwn.asm("""
   ...: imul rdi, rsi
   ...: add rdi, rdx
   ...: mov rax, rdi
   ...: """ )
   ...: process = pwn.process("/challenge/run")
   ...: process.write(code)
   ...: print(process.readall())
[x] Starting local process '/challenge/run'
[+] Starting local process '/challenge/run': pid 453
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 702B
[x] Receiving all data: 1007B
[x] Receiving all data: 1.04KB
[x] Receiving all data: 1.09KB
[x] Receiving all data: 1.16KB
[x] Receiving all data: 1.21KB
[+] Receiving all data: Done (1.21KB)
[*] Process '/challenge/run' stopped with exit code 0 (pid 453)
b'\nWelcome to ASMLevel3\n==================================================\n\nTo interact with any level you will send raw bytes over stdin to this program.\nTo efficiently solve these problems, first run it once to see what you need\nthen craft, assemble, and pipe your bytes to this program.\n\nIn this level you will be working with registers. You will be asked to modify\nor read from registers_use.\n\nWe will now set some values in memory dynamically before each run. On each run\nthe values will change. This means you will need to do some type of formulaic\noperation with registers_use. We will tell you which registers_use are set beforehand\nand where you should put the result. In most cases, its rax.\n\n\n\nUsing your new knowledge, please compute the following:\nf(x) = mx + b, where:\nm = rdi\nx = rsi\nb = rdx\nPlace the value into rax given the above.\nWe will now set the following in preparation for your code:\nrdi = 0x1133\nrsi = 0x2038\nrdx = 0x32b\n\nPlease give me your assembly in bytes (up to 0x1000 bytes): \nExecuting your code...\n---------------- CODE ----------------\n0x400000:\timul  \trdi, rsi\n0x400004:\tadd   \trdi, rdx\n0x400007:\tmov   \trax, rdi\n--------------------------------------\npwn.college{0XnTkQV33a8TNE3Ax432MeZ6P5-.0lN5EDL5IDOzMzW}\n\n'
```

# Flag
`pwn.college{0XnTkQV33a8TNE3Ax432MeZ6P5-.0lN5EDL5IDOzMzW}`

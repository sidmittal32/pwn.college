# Level Description
```
hacker@assembly-crash-course-level-9:~$ /challenge/run

Welcome to ASMLevel9
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



Using only the following instructions:
and, or, xor
Implement the following logic:

if x is even then
  y = 1
else
  y = 0
where:
x = rdi
y = rax

We will now set the following in preparation for your code:
rdi = 0x2a9aa105

Please give me your assembly in bytes (up to 0x1000 bytes): 
```

# Solution
```py
import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
xor rax, rax
and rdi, 1
or rax, rdi
xor rax, 1
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())
```

```
hacker@assembly-crash-course-level-9:~$ ipython
Python 3.8.10 (default, May 26 2023, 14:05:08) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.2 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pwn
   ...: pwn.context.update(arch="amd64")
   ...: code = pwn.asm("""
   ...: xor rax, rax
   ...: and rdi, 1
   ...: or rax, rdi
   ...: xor rax, 1
   ...: """ )
   ...: process = pwn.process("/challenge/run")
   ...: process.write(code)
   ...: print(process.readall())
[x] Starting local process '/challenge/run'
[+] Starting local process '/challenge/run': pid 1276
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 962B
[x] Receiving all data: 1.22KB
[x] Receiving all data: 1.28KB
[x] Receiving all data: 1.31KB
[x] Receiving all data: 1.42KB
[x] Receiving all data: 1.47KB
[+] Receiving all data: Done (1.47KB)
[*] Process '/challenge/run' stopped with exit code 0 (pid 1276)
b'\nWelcome to ASMLevel9\n==================================================\n\nTo interact with any level you will send raw bytes over stdin to this program.\nTo efficiently solve these problems, first run it once to see what you need\nthen craft, assemble, and pipe your bytes to this program.\n\nIn this level you will be working with registers. You will be asked to modify\nor read from registers_use.\n\nWe will now set some values in memory dynamically before each run. On each run\nthe values will change. This means you will need to do some type of formulaic\noperation with registers_use. We will tell you which registers_use are set beforehand\nand where you should put the result. In most cases, its rax.\n\nIn this level you will be working with bit logic and operations. This will involve heavy use of\ndirectly interacting with bits stored in a register or memory location. You will also likely\nneed to make use of the logic instructions in x86: and, or, not, xor.\n\n\n\nUsing only the following instructions:\nand, or, xor\nImplement the following logic:\n\nif x is even then\n  y = 1\nelse\n  y = 0\nwhere:\nx = rdi\ny = rax\n\nWe will now set the following in preparation for your code:\nrdi = 0x121ad8a8\n\nPlease give me your assembly in bytes (up to 0x1000 bytes): \nExecuting your code...\n---------------- CODE ----------------\n0x400000:\txor   \trax, rax\n0x400003:\tand   \trdi, 1\n0x400007:\tor    \trax, rdi\n0x40000a:\txor   \trax, 1\n--------------------------------------\npwn.college{UJzvQrNpJ41g3sYYdGdfn0U6vyO.0lMwIDL5IDOzMzW}\n\n'
```

# Flag
`pwn.college{UJzvQrNpJ41g3sYYdGdfn0U6vyO.0lMwIDL5IDOzMzW}`

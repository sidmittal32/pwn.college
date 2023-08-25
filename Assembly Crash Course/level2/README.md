# Level Description
```
hacker@assembly-crash-course-level-2:~$ /challenge/run

Welcome to ASMLevel2
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



Many instructions exist in x86 that allow you to do all the normal
math operations on registers_use and memory. For shorthand, when we say
A += B, it really means, A = A + B. Here are some useful instructions:
add reg1, reg2       <=>     reg1 += reg2
sub reg1, reg2       <=>     reg1 -= reg2
imul reg1, reg2      <=>     reg1 *= reg2
div  is a littler harder, we will discuss it later.
Note: all 'regX' can be replaced by a constant or memory location

Do the following:
* add 0x331337 to rdi

We will now set the following in preparation for your code:
rdi = 0xc78

Please give me your assembly in bytes (up to 0x1000 bytes): 
```

# Solution
```py
import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
add rdi, 0x331337
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())
```

```
hacker@assembly-crash-course-level-2:~$ ipython
Python 3.8.10 (default, May 26 2023, 14:05:08) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.2 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pwn
   ...: pwn.context.update(arch="amd64")
   ...: code = pwn.asm("""
   ...: add rdi, 0x331337
   ...: """ )
   ...: process = pwn.process("/challenge/run")
   ...: process.write(code)
   ...: print(process.readall())
[x] Starting local process '/challenge/run'
[+] Starting local process '/challenge/run': pid 754
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 702B
[x] Receiving all data: 1.30KB
[x] Receiving all data: 1.36KB
[x] Receiving all data: 1.43KB
[x] Receiving all data: 1.49KB
[+] Receiving all data: Done (1.49KB)
[*] Process '/challenge/run' stopped with exit code 0 (pid 754)
b"\nWelcome to ASMLevel2\n==================================================\n\nTo interact with any level you will send raw bytes over stdin to this program.\nTo efficiently solve these problems, first run it once to see what you need\nthen craft, assemble, and pipe your bytes to this program.\n\nIn this level you will be working with registers. You will be asked to modify\nor read from registers_use.\n\nWe will now set some values in memory dynamically before each run. On each run\nthe values will change. This means you will need to do some type of formulaic\noperation with registers_use. We will tell you which registers_use are set beforehand\nand where you should put the result. In most cases, its rax.\n\n\n\nMany instructions exist in x86 that allow you to do all the normal\nmath operations on registers_use and memory. For shorthand, when we say\nA += B, it really means, A = A + B. Here are some useful instructions:\nadd reg1, reg2       <=>     reg1 += reg2\nsub reg1, reg2       <=>     reg1 -= reg2\nimul reg1, reg2      <=>     reg1 *= reg2\ndiv  is a littler harder, we will discuss it later.\nNote: all 'regX' can be replaced by a constant or memory location\n\nDo the following:\n* add 0x331337 to rdi\n\nWe will now set the following in preparation for your code:\nrdi = 0x8f6\n\nPlease give me your assembly in bytes (up to 0x1000 bytes): \nExecuting your code...\n---------------- CODE ----------------\n0x400000:\tadd   \trdi, 0x331337\n--------------------------------------\npwn.college{sbiZ757QscQikoZ8piCLeVjUyd3.0VN5EDL5IDOzMzW}\n\n"
```

# Flag
`pwn.college{sbiZ757QscQikoZ8piCLeVjUyd3.0VN5EDL5IDOzMzW}`

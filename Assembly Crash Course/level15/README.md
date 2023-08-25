# Level Description
```
hacker@assembly-crash-course-level-15:~$ /challenge/run

Welcome to ASMLevel15
==================================================

To interact with any level you will send raw bytes over stdin to this program.
To efficiently solve these problems, first run it once to see what you need
then craft, assemble, and pipe your bytes to this program.

We will now set some values in memory dynamically before each run. On each run
the values will change. This means you will need to do some type of formulaic
operation with registers_use. We will tell you which registers_use are set beforehand
and where you should put the result. In most cases, its rax.

In this level you will be working with the Stack, the memory region that dynamically expands
and shrinks. You will be required to read and write to the Stack, which may require you to use
the pop & push instructions. You may also need to utilize rsp to know where the stack is pointing.



In this level we are going to explore the last in first out (LIFO) property of the stack.

Using only following instructions:
push, pop
Swap values in rdi and rsi.
i.e.
If to start rdi = 2 and rsi = 5
Then to end rdi = 5 and rsi = 2

We will now set the following in preparation for your code:
rdi = 0x956c063
rsi = 0x1b7b15bd

Please give me your assembly in bytes (up to 0x1000 bytes): 
```

# Solution
```py
import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
push rdi
push rsi
pop rdi
pop rsi
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())
```

```
hacker@assembly-crash-course-level-15:~$ ipython
Python 3.8.10 (default, May 26 2023, 14:05:08) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.2 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pwn
   ...: pwn.context.update(arch="amd64")
   ...: code = pwn.asm("""
   ...: push rdi
   ...: push rsi
   ...: pop rdi
   ...: pop rsi
   ...: """ )
   ...: process = pwn.process("/challenge/run")
   ...: process.write(code)
   ...: print(process.readall())
[x] Starting local process '/challenge/run'
[+] Starting local process '/challenge/run': pid 1113
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 884B
[x] Receiving all data: 1.40KB
[x] Receiving all data: 1.46KB
[x] Receiving all data: 1.50KB
[x] Receiving all data: 1.58KB
[x] Receiving all data: 1.64KB
[+] Receiving all data: Done (1.64KB)
[*] Process '/challenge/run' stopped with exit code 0 (pid 1113)
b'\nWelcome to ASMLevel15\n==================================================\n\nTo interact with any level you will send raw bytes over stdin to this program.\nTo efficiently solve these problems, first run it once to see what you need\nthen craft, assemble, and pipe your bytes to this program.\n\nWe will now set some values in memory dynamically before each run. On each run\nthe values will change. This means you will need to do some type of formulaic\noperation with registers_use. We will tell you which registers_use are set beforehand\nand where you should put the result. In most cases, its rax.\n\nIn this level you will be working with the Stack, the memory region that dynamically expands\nand shrinks. You will be required to read and write to the Stack, which may require you to use\nthe pop & push instructions. You may also need to utilize rsp to know where the stack is pointing.\n\n\n\nIn this level we are going to explore the last in first out (LIFO) property of the stack.\n\nUsing only following instructions:\npush, pop\nSwap values in rdi and rsi.\ni.e.\nIf to start rdi = 2 and rsi = 5\nThen to end rdi = 5 and rsi = 2\n\nWe will now set the following in preparation for your code:\nrdi = 0xad488a3\nrsi = 0x19bfff16\n\nPlease give me your assembly in bytes (up to 0x1000 bytes): \n\nWARNING: It looks like your input might not be assembled binary\ncode, but actual assembly source. This challenge needs the\nraw binary assembled code as input.\n\nExecuting your code...\n---------------- CODE ----------------\n0x400000:\tpush  \trdi\n0x400001:\tpush  \trsi\n0x400002:\tpop   \trdi\n0x400003:\tpop   \trsi\n--------------------------------------\npwn.college{UJIJnpy6QuIQxJxtLb2ySEVX7vb.0FOwIDL5IDOzMzW}\n\n'
```

# Flag
`pwn.college{UJIJnpy6QuIQxJxtLb2ySEVX7vb.0FOwIDL5IDOzMzW}`

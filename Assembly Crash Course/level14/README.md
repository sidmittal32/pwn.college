# Level Description
```
hacker@assembly-crash-course-level-14:~$ /challenge/run

Welcome to ASMLevel14
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



In these levels we are going to introduce the stack.
The stack is a region of memory, that can store values for later.
To store a value a on the stack we use the push instruction, and to retrieve a value we use pop.
The stack is a last in first out (LIFO) memory structure this means
the last value pushed in the first value popped.
Imagine unloading plates from the dishwasher let's say there are 1 red, 1 green, and 1 blue.
First we place the red one in the cabinet, then the green on top of the red, then the blue.
Out stack of plates would look like:
Top ----> Blue
          Green
Bottom -> Red
Now if we wanted a plate to make a sandwich we would retrieve the top plate from the stack
which would be the blue one that was last into the cabinet, ergo the first one out.

Replace the top value of the stack with (top value of the stack - rdi).

We will now set the following in preparation for your code:
rdi = 0x111c1
(stack) [0x7fffff1ffff8] = 0xf20c0ae

Please give me your assembly in bytes (up to 0x1000 bytes): 
```

# Solution
```py
import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
pop rax
sub rax, rdi
push rax
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())
```

```
hacker@assembly-crash-course-level-14:~$ ipython
Python 3.8.10 (default, May 26 2023, 14:05:08) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.2 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pwn
   ...: pwn.context.update(arch="amd64")
   ...: code = pwn.asm("""
   ...: pop rax
   ...: sub rax, rdi
   ...: push rax
   ...: """ )
   ...: process = pwn.process("/challenge/run")
   ...: process.write(code)
   ...: print(process.readall())
[x] Starting local process '/challenge/run'
[+] Starting local process '/challenge/run': pid 689
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 884B
[x] Receiving all data: 1.86KB
[x] Receiving all data: 1.92KB
[x] Receiving all data: 1.97KB
[x] Receiving all data: 2.03KB
[x] Receiving all data: 2.08KB
[+] Receiving all data: Done (2.08KB)
[*] Process '/challenge/run' stopped with exit code 0 (pid 689)
b"\nWelcome to ASMLevel14\n==================================================\n\nTo interact with any level you will send raw bytes over stdin to this program.\nTo efficiently solve these problems, first run it once to see what you need\nthen craft, assemble, and pipe your bytes to this program.\n\nWe will now set some values in memory dynamically before each run. On each run\nthe values will change. This means you will need to do some type of formulaic\noperation with registers_use. We will tell you which registers_use are set beforehand\nand where you should put the result. In most cases, its rax.\n\nIn this level you will be working with the Stack, the memory region that dynamically expands\nand shrinks. You will be required to read and write to the Stack, which may require you to use\nthe pop & push instructions. You may also need to utilize rsp to know where the stack is pointing.\n\n\n\nIn these levels we are going to introduce the stack.\nThe stack is a region of memory, that can store values for later.\nTo store a value a on the stack we use the push instruction, and to retrieve a value we use pop.\nThe stack is a last in first out (LIFO) memory structure this means\nthe last value pushed in the first value popped.\nImagine unloading plates from the dishwasher let's say there are 1 red, 1 green, and 1 blue.\nFirst we place the red one in the cabinet, then the green on top of the red, then the blue.\nOut stack of plates would look like:\nTop ----> Blue\n          Green\nBottom -> Red\nNow if we wanted a plate to make a sandwich we would retrieve the top plate from the stack\nwhich would be the blue one that was last into the cabinet, ergo the first one out.\n\nReplace the top value of the stack with (top value of the stack - rdi).\n\nWe will now set the following in preparation for your code:\nrdi = 0x14f84\n(stack) [0x7fffff1ffff8] = 0x2708465c\n\nPlease give me your assembly in bytes (up to 0x1000 bytes): \nExecuting your code...\n---------------- CODE ----------------\n0x400000:\tpop   \trax\n0x400001:\tsub   \trax, rdi\n0x400004:\tpush  \trax\n--------------------------------------\npwn.college{sSeEh7VIAXMN5lNfBSuhpf0Kb17.01NwIDL5IDOzMzW}\n\n"
```

# Flag
`pwn.college{sSeEh7VIAXMN5lNfBSuhpf0Kb17.01NwIDL5IDOzMzW}`

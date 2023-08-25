# Level Description
```
hacker@assembly-crash-course-level-17:~$ /challenge/run

Welcome to ASMLevel17
==================================================

To interact with any level you will send raw bytes over stdin to this program.
To efficiently solve these problems, first run it once to see what you need
then craft, assemble, and pipe your bytes to this program.

We will now set some values in memory dynamically before each run. On each run
the values will change. This means you will need to do some type of formulaic
operation with registers_use. We will tell you which registers_use are set beforehand
and where you should put the result. In most cases, its rax.

In this level you will be working with control flow manipulation. This involves using instructions
to both indirectly and directly control the special register `rip`, the instruction pointer.
You will use instructions like: jmp, call, cmp, and the like to implement requests behavior.



Earlier, you learned how to manipulate data in a pseudo-control way, but x86 gives us actual
instructions to manipulate control flow directly. There are two major ways to manipulate control
flow: 1. through a jump; 2. through a call. In this level, you will work with jumps. There are
two types of jumps:
1. Unconditional jumps
2. Conditional jumps
Unconditional jumps always trigger and are not based on the results of earlier instructions.
As you know, memory locations can store data and instructions. You code will be stored
at 0x400077 (this will change each run).
For all jumps, there are three types:
1. Relative jumps
2. Absolute jumps
3. Indirect jumps
In this level we will ask you to do both a relative jump and an absolute jump. You will do a relative
jump first, then an absolute one. You will need to fill space in your code with something to make this
relative jump possible. We suggest using the `nop` instruction. It's 1 byte and very predictable.
Useful instructions for this level is:
jmp (reg1 | addr | offset) ; nop
Hint: for the relative jump, lookup how to use `labels` in x86.

Using the above knowledge, perform the following:
Create a two jump trampoline:
1. Make the first instruction in your code a jmp
2. Make that jmp a relative jump to 0x51 bytes from its current position
3. At 0x51 write the following code:
4. Place the top value on the stack into register rdi
5. jmp to the absolute address 0x403000

We will now set the following in preparation for your code:
- Loading your given code at: 0x400077
- (stack) [0x7fffff1ffff8] = 0x58

Please give me your assembly in bytes (up to 0x1000 bytes): 
```

# Solution
```py
import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
jmp label
"""
+
"nop\n" * 0x51
+
"""
label:
pop rdi
mov rax, 0x403000
jmp rax
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())
```

```
hacker@assembly-crash-course-level-17:~$ ipython
Python 3.8.10 (default, May 26 2023, 14:05:08) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.2 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pwn
   ...: pwn.context.update(arch="amd64")
   ...: code = pwn.asm("""
   ...: jmp label
   ...: """
   ...: +
   ...: "nop\n" * 0x51
   ...: +
   ...: """
   ...: label:
   ...: pop rdi
   ...: mov rax, 0x403000
   ...: jmp rax
   ...: """ )
   ...: process = pwn.process("/challenge/run")
   ...: process.write(code)
   ...: print(process.readall())
[x] Starting local process '/challenge/run'
[+] Starting local process '/challenge/run': pid 2421
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 882B
[x] Receiving all data: 2.46KB
[x] Receiving all data: 2.52KB
[x] Receiving all data: 2.56KB
[x] Receiving all data: 2.73KB
[x] Receiving all data: 2.86KB
[x] Receiving all data: 3.00KB
[x] Receiving all data: 3.16KB
[x] Receiving all data: 3.28KB
[x] Receiving all data: 3.40KB
[x] Receiving all data: 3.54KB
[x] Receiving all data: 3.67KB
[x] Receiving all data: 3.82KB
[x] Receiving all data: 3.95KB
[x] Receiving all data: 4.07KB
[x] Receiving all data: 4.13KB
[+] Receiving all data: Done (4.13KB)
[*] Process '/challenge/run' stopped with exit code 0 (pid 2421)
b"\nWelcome to ASMLevel17\n==================================================\n\nTo interact with any level you will send raw bytes over stdin to this program.\nTo efficiently solve these problems, first run it once to see what you need\nthen craft, assemble, and pipe your bytes to this program.\n\nWe will now set some values in memory dynamically before each run. On each run\nthe values will change. This means you will need to do some type of formulaic\noperation with registers_use. We will tell you which registers_use are set beforehand\nand where you should put the result. In most cases, its rax.\n\nIn this level you will be working with control flow manipulation. This involves using instructions\nto both indirectly and directly control the special register `rip`, the instruction pointer.\nYou will use instructions like: jmp, call, cmp, and the like to implement requests behavior.\n\n\n\nEarlier, you learned how to manipulate data in a pseudo-control way, but x86 gives us actual\ninstructions to manipulate control flow directly. There are two major ways to manipulate control\nflow: 1. through a jump; 2. through a call. In this level, you will work with jumps. There are\ntwo types of jumps:\n1. Unconditional jumps\n2. Conditional jumps\nUnconditional jumps always trigger and are not based on the results of earlier instructions.\nAs you know, memory locations can store data and instructions. You code will be stored\nat 0x400021 (this will change each run).\nFor all jumps, there are three types:\n1. Relative jumps\n2. Absolute jumps\n3. Indirect jumps\nIn this level we will ask you to do both a relative jump and an absolute jump. You will do a relative\njump first, then an absolute one. You will need to fill space in your code with something to make this\nrelative jump possible. We suggest using the `nop` instruction. It's 1 byte and very predictable.\nUseful instructions for this level is:\njmp (reg1 | addr | offset) ; nop\nHint: for the relative jump, lookup how to use `labels` in x86.\n\nUsing the above knowledge, perform the following:\nCreate a two jump trampoline:\n1. Make the first instruction in your code a jmp\n2. Make that jmp a relative jump to 0x51 bytes from its current position\n3. At 0x51 write the following code:\n4. Place the top value on the stack into register rdi\n5. jmp to the absolute address 0x403000\n\nWe will now set the following in preparation for your code:\n- Loading your given code at: 0x400021\n- (stack) [0x7fffff1ffff8] = 0x7e\n\nPlease give me your assembly in bytes (up to 0x1000 bytes): \nExecuting your code...\n---------------- CODE ----------------\n0x400021:\tjmp   \t0x400074\n0x400023:\tnop   \t\n0x400024:\tnop   \t\n0x400025:\tnop   \t\n0x400026:\tnop   \t\n0x400027:\tnop   \t\n0x400028:\tnop   \t\n0x400029:\tnop   \t\n0x40002a:\tnop   \t\n0x40002b:\tnop   \t\n0x40002c:\tnop   \t\n0x40002d:\tnop   \t\n0x40002e:\tnop   \t\n0x40002f:\tnop   \t\n0x400030:\tnop   \t\n0x400031:\tnop   \t\n0x400032:\tnop   \t\n0x400033:\tnop   \t\n0x400034:\tnop   \t\n0x400035:\tnop   \t\n0x400036:\tnop   \t\n0x400037:\tnop   \t\n0x400038:\tnop   \t\n0x400039:\tnop   \t\n0x40003a:\tnop   \t\n0x40003b:\tnop   \t\n0x40003c:\tnop   \t\n0x40003d:\tnop   \t\n0x40003e:\tnop   \t\n0x40003f:\tnop   \t\n0x400040:\tnop   \t\n0x400041:\tnop   \t\n0x400042:\tnop   \t\n0x400043:\tnop   \t\n0x400044:\tnop   \t\n0x400045:\tnop   \t\n0x400046:\tnop   \t\n0x400047:\tnop   \t\n0x400048:\tnop   \t\n0x400049:\tnop   \t\n0x40004a:\tnop   \t\n0x40004b:\tnop   \t\n0x40004c:\tnop   \t\n0x40004d:\tnop   \t\n0x40004e:\tnop   \t\n0x40004f:\tnop   \t\n0x400050:\tnop   \t\n0x400051:\tnop   \t\n0x400052:\tnop   \t\n0x400053:\tnop   \t\n0x400054:\tnop   \t\n0x400055:\tnop   \t\n0x400056:\tnop   \t\n0x400057:\tnop   \t\n0x400058:\tnop   \t\n0x400059:\tnop   \t\n0x40005a:\tnop   \t\n0x40005b:\tnop   \t\n0x40005c:\tnop   \t\n0x40005d:\tnop   \t\n0x40005e:\tnop   \t\n0x40005f:\tnop   \t\n0x400060:\tnop   \t\n0x400061:\tnop   \t\n0x400062:\tnop   \t\n0x400063:\tnop   \t\n0x400064:\tnop   \t\n0x400065:\tnop   \t\n0x400066:\tnop   \t\n0x400067:\tnop   \t\n0x400068:\tnop   \t\n0x400069:\tnop   \t\n0x40006a:\tnop   \t\n0x40006b:\tnop   \t\n0x40006c:\tnop   \t\n0x40006d:\tnop   \t\n0x40006e:\tnop   \t\n0x40006f:\tnop   \t\n0x400070:\tnop   \t\n0x400071:\tnop   \t\n0x400072:\tnop   \t\n0x400073:\tnop   \t\n0x400074:\tpop   \trdi\n0x400075:\tmov   \trax, 0x403000\n0x40007c:\tjmp   \trax\n--------------------------------------\npwn.college{4v6i0mtYIX-IlQiPFqEeccx4MSM.0FMxIDL5IDOzMzW}\n\n"
```

# Flag
`pwn.college{4v6i0mtYIX-IlQiPFqEeccx4MSM.0FMxIDL5IDOzMzW}`

# Level Description
```
hacker@assembly-crash-course-level-16:~$ /challenge/run

Welcome to ASMLevel16
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



In the previous levels you used push and pop to store and load data from the stack
however you can also access the stack directly using the stack pointer.
The stack pointer is stored in the special register rsp.
rsp always stores the memory address to the top of the stack,
i.e. the memory address of the last value pushed.
Similar to the memory levels we can use [rsp] to access the value at the memory address in rsp.

Without using pop please calculate the average of 4 consecutive quad words stored on the stack.
Store the average on the top of the stack. Hint:
RSP+0x?? Quad Word A
RSP+0x?? Quad Word B
RSP+0x?? Quad Word C
RSP      Quad Word D
RSP-0x?? Average

We will now set the following in preparation for your code:
(stack) [0x7fffff200000:0x7fffff1fffe0]
= ['0x8f0b0f3', '0x17f03ee8', '0x32bfdce4', '0x3688eb03'] (list of things)

Please give me your assembly in bytes (up to 0x1000 bytes): 
```

# Solution
```py
import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
mov rax, [rsp]
add rax, [rsp+8]
add rax, [rsp+16]
add rax, [rsp+24]
shr rax, 2
push rax 
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())
```

```
hacker@assembly-crash-course-level-16:~$ ipython
Python 3.8.10 (default, May 26 2023, 14:05:08) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.2 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pwn
   ...: pwn.context.update(arch="amd64")
   ...: code = pwn.asm("""
   ...: mov rax, [rsp]
   ...: add rax, [rsp+8]
   ...: add rax, [rsp+16]
   ...: add rax, [rsp+24]
   ...: shr rax, 2
   ...: push rax 
   ...: """ )
   ...: process = pwn.process("/challenge/run")
   ...: process.write(code)
   ...: print(process.readall())
[x] Starting local process '/challenge/run'
[+] Starting local process '/challenge/run': pid 836
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 884B
[x] Receiving all data: 1.75KB
[x] Receiving all data: 1.81KB
[x] Receiving all data: 1.84KB
[x] Receiving all data: 2.06KB
[x] Receiving all data: 2.11KB
[+] Receiving all data: Done (2.11KB)
[*] Process '/challenge/run' stopped with exit code 0 (pid 836)
b"\nWelcome to ASMLevel16\n==================================================\n\nTo interact with any level you will send raw bytes over stdin to this program.\nTo efficiently solve these problems, first run it once to see what you need\nthen craft, assemble, and pipe your bytes to this program.\n\nWe will now set some values in memory dynamically before each run. On each run\nthe values will change. This means you will need to do some type of formulaic\noperation with registers_use. We will tell you which registers_use are set beforehand\nand where you should put the result. In most cases, its rax.\n\nIn this level you will be working with the Stack, the memory region that dynamically expands\nand shrinks. You will be required to read and write to the Stack, which may require you to use\nthe pop & push instructions. You may also need to utilize rsp to know where the stack is pointing.\n\n\n\nIn the previous levels you used push and pop to store and load data from the stack\nhowever you can also access the stack directly using the stack pointer.\nThe stack pointer is stored in the special register rsp.\nrsp always stores the memory address to the top of the stack,\ni.e. the memory address of the last value pushed.\nSimilar to the memory levels we can use [rsp] to access the value at the memory address in rsp.\n\nWithout using pop please calculate the average of 4 consecutive quad words stored on the stack.\nStore the average on the top of the stack. Hint:\nRSP+0x?? Quad Word A\nRSP+0x?? Quad Word B\nRSP+0x?? Quad Word C\nRSP      Quad Word D\nRSP-0x?? Average\n\nWe will now set the following in preparation for your code:\n(stack) [0x7fffff200000:0x7fffff1fffe0]\n= ['0xb15456b', '0x34f26897', '0x372f00ad', '0x63c0ff3'] (list of things)\n\nPlease give me your assembly in bytes (up to 0x1000 bytes): \nExecuting your code...\n---------------- CODE ----------------\n0x400000:\tmov   \trax, qword ptr [rsp]\n0x400004:\tadd   \trax, qword ptr [rsp + 8]\n0x400009:\tadd   \trax, qword ptr [rsp + 0x10]\n0x40000e:\tadd   \trax, qword ptr [rsp + 0x18]\n0x400013:\tshr   \trax, 2\n0x400017:\tpush  \trax\n--------------------------------------\npwn.college{k9vtMdNf4Xc4GcD4RFBFYOFuGLJ.0VOwIDL5IDOzMzW}\n\n"
```

# Flag
`pwn.college{k9vtMdNf4Xc4GcD4RFBFYOFuGLJ.0VOwIDL5IDOzMzW}`

# Level Description
```
hacker@assembly-crash-course-level-11:~$ /challenge/run

Welcome to ASMLevel11
==================================================

To interact with any level you will send raw bytes over stdin to this program.
To efficiently solve these problems, first run it once to see what you need
then craft, assemble, and pipe your bytes to this program.

We will now set some values in memory dynamically before each run. On each run
the values will change. This means you will need to do some type of formulaic
operation with registers_use. We will tell you which registers_use are set beforehand
and where you should put the result. In most cases, its rax.

In this level you will be working with memory. This will require you to read or write
to things stored linearly in memory. If you are confused, go look at the linear
addressing module in 'ike. You may also be asked to dereference things, possibly multiple
times, to things we dynamically put in memory for your use.



Recall that registers in x86_64 are 64 bits wide, meaning they can store 64 bits in them.
Similarly, each memory location is 64 bits wide. We refer to something that is 64 bits
(8 bytes) as a quad word. Here is the breakdown of the names of memory sizes:
* Quad Word = 8 Bytes = 64 bits
* Double Word = 4 bytes = 32 bits
* Word = 2 bytes = 16 bits
* Byte = 1 byte = 8 bits
In x86_64, you can access each of these sizes when dereferencing an address, just like using
bigger or smaller register accesses:
mov al, [address]        <=>         moves the least significant byte from address to rax
mov ax, [address]        <=>         moves the least significant word from address to rax
mov eax, [address]        <=>         moves the least significant double word from address to rax
mov rax, [address]        <=>         moves the full quad word from address to rax
Remember that moving only into al for instance does not fully clear the upper bytes.

Please perform the following:
1) Set rax to the byte at 0x404000
2) Set rbx to the word at 0x404000
3) Set rcx to the double word at 0x404000
4) Set rdx to the quad word at 0x404000

We will now set the following in preparation for your code:
[0x404000] = 0x1d68de

Please give me your assembly in bytes (up to 0x1000 bytes):
```

# Solution
```py
import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
mov al, [0x404000]
mov bx, [0x404000]
mov ecx, [0x404000]
mov rdx, [0x404000]
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())
```

```
hacker@assembly-crash-course-level-11:~$ ipython
Python 3.8.10 (default, May 26 2023, 14:05:08) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.2 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pwn
   ...: pwn.context.update(arch="amd64")
   ...: code = pwn.asm("""
   ...: mov al, [0x404000]
   ...: mov bx, [0x404000]
   ...: mov ecx, [0x404000]
   ...: mov rdx, [0x404000]
   ...: """ )
   ...: process = pwn.process("/challenge/run")
   ...: process.write(code)
   ...: print(process.readall())
[x] Starting local process '/challenge/run'
[+] Starting local process '/challenge/run': pid 368
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 913B
[x] Receiving all data: 2.14KB
[x] Receiving all data: 2.20KB
[x] Receiving all data: 2.28KB
[x] Receiving all data: 2.40KB
[x] Receiving all data: 2.46KB
[+] Receiving all data: Done (2.46KB)
[*] Process '/challenge/run' stopped with exit code 0 (pid 368)
b"\nWelcome to ASMLevel11\n==================================================\n\nTo interact with any level you will send raw bytes over stdin to this program.\nTo efficiently solve these problems, first run it once to see what you need\nthen craft, assemble, and pipe your bytes to this program.\n\nWe will now set some values in memory dynamically before each run. On each run\nthe values will change. This means you will need to do some type of formulaic\noperation with registers_use. We will tell you which registers_use are set beforehand\nand where you should put the result. In most cases, its rax.\n\nIn this level you will be working with memory. This will require you to read or write\nto things stored linearly in memory. If you are confused, go look at the linear\naddressing module in 'ike. You may also be asked to dereference things, possibly multiple\ntimes, to things we dynamically put in memory for your use.\n\n\n\nRecall that registers in x86_64 are 64 bits wide, meaning they can store 64 bits in them.\nSimilarly, each memory location is 64 bits wide. We refer to something that is 64 bits\n(8 bytes) as a quad word. Here is the breakdown of the names of memory sizes:\n* Quad Word = 8 Bytes = 64 bits\n* Double Word = 4 bytes = 32 bits\n* Word = 2 bytes = 16 bits\n* Byte = 1 byte = 8 bits\nIn x86_64, you can access each of these sizes when dereferencing an address, just like using\nbigger or smaller register accesses:\nmov al, [address]        <=>         moves the least significant byte from address to rax\nmov ax, [address]        <=>         moves the least significant word from address to rax\nmov eax, [address]        <=>         moves the least significant double word from address to rax\nmov rax, [address]        <=>         moves the full quad word from address to rax\nRemember that moving only into al for instance does not fully clear the upper bytes.\n\nPlease perform the following:\n1) Set rax to the byte at 0x404000\n2) Set rbx to the word at 0x404000\n3) Set rcx to the double word at 0x404000\n4) Set rdx to the quad word at 0x404000\n\nWe will now set the following in preparation for your code:\n[0x404000] = 0x1521a7\n\nPlease give me your assembly in bytes (up to 0x1000 bytes): \nExecuting your code...\n---------------- CODE ----------------\n0x400000:\tmov   \tal, byte ptr [0x404000]\n0x400007:\tmov   \tbx, word ptr [0x404000]\n0x40000f:\tmov   \tecx, dword ptr [0x404000]\n0x400016:\tmov   \trdx, qword ptr [0x404000]\n--------------------------------------\npwn.college{kdQU13wc8peZAJcrOgFTG-uv4Xa.0FNwIDL5IDOzMzW}\n\n"
```

# Flag
`pwn.college{kdQU13wc8peZAJcrOgFTG-uv4Xa.0FNwIDL5IDOzMzW}`

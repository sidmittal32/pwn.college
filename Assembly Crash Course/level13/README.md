# Level Description
```
hacker@assembly-crash-course-level-13:~$ /challenge/run

Welcome to ASMLevel13
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



Recall that memory is stored linearly. What does that mean? Say we access the quad word at 0x1337:
[0x1337] = 0x00000000deadbeef
The real way memory is layed out is byte by byte, little endian:
[0x1337] = 0xef
[0x1337 + 1] = 0xbe
[0x1337 + 2] = 0xad
...
[0x1337 + 7] = 0x00
What does this do for us? Well, it means that we can access things next to each other using offsets,
like what was shown above. Say you want the 5th *byte* from an address, you can access it like:
mov al, [address+4]
Remember, offsets start at 0.

Perform the following:
1. load two consecutive quad words from the address stored in rdi
2. calculate the sum of the previous steps quad words.
3. store the sum at the address in rsi

We will now set the following in preparation for your code:
[0x404308] = 0xc307a
[0x404310] = 0xd9a25
rdi = 0x404308
rsi = 0x404700

Please give me your assembly in bytes (up to 0x1000 bytes):
```

# Solution
```py
import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
mov rax, [rdi]
add rax, [rdi + 8]
mov [rsi], rax
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())
```

```
hacker@assembly-crash-course-level-13:~$ ipython
Python 3.8.10 (default, May 26 2023, 14:05:08) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.2 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pwn
   ...: pwn.context.update(arch="amd64")
   ...: code = pwn.asm("""
   ...: mov rax, [rdi]
   ...: add rax, [rdi + 8]
   ...: mov [rsi], rax
   ...: """ )
   ...: process = pwn.process("/challenge/run")
   ...: process.write(code)
   ...: print(process.readall())
[x] Starting local process '/challenge/run'
[+] Starting local process '/challenge/run': pid 762
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 913B
[x] Receiving all data: 1.77KB
[x] Receiving all data: 1.83KB
[x] Receiving all data: 1.87KB
[x] Receiving all data: 1.99KB
[x] Receiving all data: 2.04KB
[+] Receiving all data: Done (2.04KB)
[*] Process '/challenge/run' stopped with exit code 0 (pid 762)
b"\nWelcome to ASMLevel13\n==================================================\n\nTo interact with any level you will send raw bytes over stdin to this program.\nTo efficiently solve these problems, first run it once to see what you need\nthen craft, assemble, and pipe your bytes to this program.\n\nWe will now set some values in memory dynamically before each run. On each run\nthe values will change. This means you will need to do some type of formulaic\noperation with registers_use. We will tell you which registers_use are set beforehand\nand where you should put the result. In most cases, its rax.\n\nIn this level you will be working with memory. This will require you to read or write\nto things stored linearly in memory. If you are confused, go look at the linear\naddressing module in 'ike. You may also be asked to dereference things, possibly multiple\ntimes, to things we dynamically put in memory for your use.\n\n\n\nRecall that memory is stored linearly. What does that mean? Say we access the quad word at 0x1337:\n[0x1337] = 0x00000000deadbeef\nThe real way memory is layed out is byte by byte, little endian:\n[0x1337] = 0xef\n[0x1337 + 1] = 0xbe\n[0x1337 + 2] = 0xad\n...\n[0x1337 + 7] = 0x00\nWhat does this do for us? Well, it means that we can access things next to each other using offsets,\nlike what was shown above. Say you want the 5th *byte* from an address, you can access it like:\nmov al, [address+4]\nRemember, offsets start at 0.\n\nPerform the following:\n1. load two consecutive quad words from the address stored in rdi\n2. calculate the sum of the previous steps quad words.\n3. store the sum at the address in rsi\n\nWe will now set the following in preparation for your code:\n[0x404238] = 0xd2344\n[0x404240] = 0xf29f6\nrdi = 0x404238\nrsi = 0x404710\n\nPlease give me your assembly in bytes (up to 0x1000 bytes): \nExecuting your code...\n---------------- CODE ----------------\n0x400000:\tmov   \trax, qword ptr [rdi]\n0x400003:\tadd   \trax, qword ptr [rdi + 8]\n0x400007:\tmov   \tqword ptr [rsi], rax\n--------------------------------------\npwn.college{8-ucbvquhqjQne_Rx9AV9Yh5X12.0lNwIDL5IDOzMzW}\n\n"
```

# Flag
`pwn.college{8-ucbvquhqjQne_Rx9AV9Yh5X12.0lNwIDL5IDOzMzW}`

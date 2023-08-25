# Level Description
```
hacker@assembly-crash-course-level-12:~$ /challenge/run

Welcome to ASMLevel12
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



It is worth noting, as you may have noticed, that values are stored in reverse order of how we
represent them. As an example, say:
[0x1330] = 0x00000000deadc0de
If you examined how it actually looked in memory, you would see:
[0x1330] = 0xde 0xc0 0xad 0xde 0x00 0x00 0x00 0x00
This format of storing things in 'reverse' is intentional in x86, and its called Little Endian.

For this challenge we will give you two addresses created dynamically each run. The first address
will be placed in rdi. The second will be placed in rsi.
Using the earlier mentioned info, perform the following:
1. set [rdi] = 0xdeadbeef00001337
2. set [rsi] = 0xc0ffee0000
Hint: it may require some tricks to assign a big constant to a dereferenced register. Try setting
a register to the constant then assigning that register to the derefed register.

We will now set the following in preparation for your code:
[0x404350] = 0xffffffffffffffff
[0x4048e8] = 0xffffffffffffffff
rdi = 0x404350
rsi = 0x4048e8

Please give me your assembly in bytes (up to 0x1000 bytes): 
```

# Solution
```py
import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
movq rax, 0xdeadbeef00001337
movq [rdi], rax
movq rax, 0xc0ffee0000
movq [rsi], rax
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())
```

```
hacker@assembly-crash-course-level-12:~$ ipython
Python 3.8.10 (default, May 26 2023, 14:05:08) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.2 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pwn
   ...: pwn.context.update(arch="amd64")
   ...: code = pwn.asm("""
   ...: movq rax, 0xdeadbeef00001337
   ...: movq [rdi], rax
   ...: movq rax, 0xc0ffee0000
   ...: movq [rsi], rax
   ...: """ )
   ...: process = pwn.process("/challenge/run")
   ...: process.write(code)
   ...: print(process.readall())
[x] Starting local process '/challenge/run'
[+] Starting local process '/challenge/run': pid 442
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 913B
[x] Receiving all data: 1.91KB
[x] Receiving all data: 1.97KB
[x] Receiving all data: 2.01KB
[x] Receiving all data: 2.16KB
[x] Receiving all data: 2.22KB
[+] Receiving all data: Done (2.22KB)
[*] Process '/challenge/run' stopped with exit code 0 (pid 442)
b"\nWelcome to ASMLevel12\n==================================================\n\nTo interact with any level you will send raw bytes over stdin to this program.\nTo efficiently solve these problems, first run it once to see what you need\nthen craft, assemble, and pipe your bytes to this program.\n\nWe will now set some values in memory dynamically before each run. On each run\nthe values will change. This means you will need to do some type of formulaic\noperation with registers_use. We will tell you which registers_use are set beforehand\nand where you should put the result. In most cases, its rax.\n\nIn this level you will be working with memory. This will require you to read or write\nto things stored linearly in memory. If you are confused, go look at the linear\naddressing module in 'ike. You may also be asked to dereference things, possibly multiple\ntimes, to things we dynamically put in memory for your use.\n\n\n\nIt is worth noting, as you may have noticed, that values are stored in reverse order of how we\nrepresent them. As an example, say:\n[0x1330] = 0x00000000deadc0de\nIf you examined how it actually looked in memory, you would see:\n[0x1330] = 0xde 0xc0 0xad 0xde 0x00 0x00 0x00 0x00\nThis format of storing things in 'reverse' is intentional in x86, and its called Little Endian.\n\nFor this challenge we will give you two addresses created dynamically each run. The first address\nwill be placed in rdi. The second will be placed in rsi.\nUsing the earlier mentioned info, perform the following:\n1. set [rdi] = 0xdeadbeef00001337\n2. set [rsi] = 0xc0ffee0000\nHint: it may require some tricks to assign a big constant to a dereferenced register. Try setting\na register to the constant then assigning that register to the derefed register.\n\nWe will now set the following in preparation for your code:\n[0x4041e8] = 0xffffffffffffffff\n[0x404d48] = 0xffffffffffffffff\nrdi = 0x4041e8\nrsi = 0x404d48\n\nPlease give me your assembly in bytes (up to 0x1000 bytes): \nExecuting your code...\n---------------- CODE ----------------\n0x400000:\tmovabs\trax, 0xdeadbeef00001337\n0x40000a:\tmov   \tqword ptr [rdi], rax\n0x40000d:\tmovabs\trax, 0xc0ffee0000\n0x400017:\tmov   \tqword ptr [rsi], rax\n--------------------------------------\npwn.college{MLu2ClPY3GC0aDKYwrYU3u-kMMH.0VNwIDL5IDOzMzW}\n\n"
```

# Flag
`pwn.college{MLu2ClPY3GC0aDKYwrYU3u-kMMH.0VNwIDL5IDOzMzW}`

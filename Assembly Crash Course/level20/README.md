# Level Description
```
hacker@assembly-crash-course-level-20:~$ /challenge/run

Welcome to ASMLevel20
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



In  a previous level you computed the average of 4 integer quad words, which
was a fixed amount of things to compute, but how do you work with sizes you get when
the program is running? In most programming languages a structure exists called the
for-loop, which allows you to do a set of instructions for a bounded amount of times.
The bounded amount can be either known before or during the programs run, during meaning
the value is given to you dynamically. As an example, a for-loop can be used to compute
the sum of the numbers 1 to n:
sum = 0
i = 1
for i <= n:
    sum += i
    i += 1

Please compute the average of n consecutive quad words, where:
rdi = memory address of the 1st quad word
rsi = n (amount to loop for)
rax = average computed

We will now set the following in preparation for your code:
- [0x4040c0:0x404318] = {n qwords]}
- rdi = 0x4040c0
- rsi = 75


Please give me your assembly in bytes (up to 0x1000 bytes): 
```

# Solution
```py
import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
xor rax, rax
xor rcx, rcx
mov rbx, rsi
loop:
sub rbx, 1
mov ecx, [rdi+rbx*8]
add rax, rcx
cmp rbx, 0
jne loop
div rsi
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())
```

```
hacker@assembly-crash-course-level-20:~$ ipython
Python 3.8.10 (default, May 26 2023, 14:05:08) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.2 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pwn
   ...: pwn.context.update(arch="amd64")
   ...: code = pwn.asm("""
   ...: xor rax, rax
   ...: xor rcx, rcx
   ...: mov rbx, rsi
   ...: loop:
   ...: sub rbx, 1
   ...: mov ecx, [rdi+rbx*8]
   ...: add rax, rcx
   ...: cmp rbx, 0
   ...: jne loop
   ...: div rsi
   ...: """ )
   ...: process = pwn.process("/challenge/run")
   ...: process.write(code)
   ...: print(process.readall())
[x] Starting local process '/challenge/run'
[+] Starting local process '/challenge/run': pid 331
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 882B
[x] Receiving all data: 1.78KB
[x] Receiving all data: 1.84KB
[x] Receiving all data: 1.91KB
[x] Receiving all data: 2.11KB
[x] Receiving all data: 2.17KB
[+] Receiving all data: Done (2.17KB)
[*] Process '/challenge/run' stopped with exit code 0 (pid 331)
b'\nWelcome to ASMLevel20\n==================================================\n\nTo interact with any level you will send raw bytes over stdin to this program.\nTo efficiently solve these problems, first run it once to see what you need\nthen craft, assemble, and pipe your bytes to this program.\n\nWe will now set some values in memory dynamically before each run. On each run\nthe values will change. This means you will need to do some type of formulaic\noperation with registers_use. We will tell you which registers_use are set beforehand\nand where you should put the result. In most cases, its rax.\n\nIn this level you will be working with control flow manipulation. This involves using instructions\nto both indirectly and directly control the special register `rip`, the instruction pointer.\nYou will use instructions like: jmp, call, cmp, and the like to implement requests behavior.\n\n\n\nIn  a previous level you computed the average of 4 integer quad words, which\nwas a fixed amount of things to compute, but how do you work with sizes you get when\nthe program is running? In most programming languages a structure exists called the\nfor-loop, which allows you to do a set of instructions for a bounded amount of times.\nThe bounded amount can be either known before or during the programs run, during meaning\nthe value is given to you dynamically. As an example, a for-loop can be used to compute\nthe sum of the numbers 1 to n:\nsum = 0\ni = 1\nfor i <= n:\n    sum += i\n    i += 1\n\nPlease compute the average of n consecutive quad words, where:\nrdi = memory address of the 1st quad word\nrsi = n (amount to loop for)\nrax = average computed\n\nWe will now set the following in preparation for your code:\n- [0x404078:0x404378] = {n qwords]}\n- rdi = 0x404078\n- rsi = 96\n\n\nPlease give me your assembly in bytes (up to 0x1000 bytes): \nExecuting your code...\n---------------- CODE ----------------\n0x400000:\txor   \trax, rax\n0x400003:\txor   \trcx, rcx\n0x400006:\tmov   \trbx, rsi\n0x400009:\tsub   \trbx, 1\n0x40000d:\tmov   \tecx, dword ptr [rdi + rbx*8]\n0x400010:\tadd   \trax, rcx\n0x400013:\tcmp   \trbx, 0\n0x400017:\tjne   \t0x400009\n0x400019:\tdiv   \trsi\n--------------------------------------\npwn.college{IzX0BTMKYg2rx57jUY_k0ACe5i0.01MxIDL5IDOzMzW}\n\n'
```

# Flag
`pwn.college{IzX0BTMKYg2rx57jUY_k0ACe5i0.01MxIDL5IDOzMzW}`

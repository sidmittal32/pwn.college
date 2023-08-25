# Level Description
```
hacker@assembly-crash-course-level-21:~$ /challenge/run

Welcome to ASMLevel21
==================================================

To interact with any level you will send raw bytes over stdin to this program.
To efficiently solve these problems, first run it once to see what you need
then craft, assemble, and pipe your bytes to this program.

In this level you will be working with control flow manipulation. This involves using instructions
to both indirectly and directly control the special register `rip`, the instruction pointer.
You will use instructions like: jmp, call, cmp, and the like to implement requests behavior.

We will be testing your code multiple times in this level with dynamic values! This means we will
be running your code in a variety of random ways to verify that the logic is robust enough to
survive normal use. You can consider this as normal dynamic value se



In previous levels you discovered the for-loop to iterate for a *number* of times, both dynamically and
statically known, but what happens when you want to iterate until you meet a condition? A second loop
structure exists called the while-loop to fill this demand. In the while-loop you iterate until a
condition is met. As an example, say we had a location in memory with adjacent numbers and we wanted
to get the average of all the numbers until we find one bigger or equal to 0xff:
average = 0
i = 0
while x[i] < 0xff:
    average += x[i]
    i += 1
average /= i

Using the above knowledge, please perform the following:
Count the consecutive non-zero bytes in a contiguous region of memory, where:
rdi = memory address of the 1st byte
rax = number of consecutive non-zero bytes
Additionally, if rdi = 0, then set rax = 0 (we will check)!
An example test-case, let:
rdi = 0x1000
[0x1000] = 0x41
[0x1001] = 0x42
[0x1002] = 0x43
[0x1003] = 0x00
then: rax = 3 should be set

We will now run multiple tests on your code, here is an example run:
- (data) [0x404000] = {10 random bytes},
- rdi = 0x404000

Please give me your assembly in bytes (up to 0x1000 bytes): 
```

# Solution
```py
import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
mov rax,0
cmp rdi,0
je done
mov rsi,-1
loop:
add rsi,1
mov rbx,[rdi+rsi]
cmp rbx,0
jne loop
mov rax,rsi
done:
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())
```

```
hacker@assembly-crash-course-level-21:~$ ipython
Python 3.8.10 (default, May 26 2023, 14:05:08) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.2 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pwn
   ...: pwn.context.update(arch="amd64")
   ...: code = pwn.asm("""
   ...: mov rax,0
   ...: cmp rdi,0
   ...: je done
   ...: mov rsi,-1
   ...: loop:
   ...: add rsi,1
   ...: mov rbx,[rdi+rsi]
   ...: cmp rbx,0
   ...: jne loop
   ...: mov rax,rsi
   ...: done:
   ...: """ )
   ...: process = pwn.process("/challenge/run")
   ...: process.write(code)
   ...: print(process.readall())
[x] Starting local process '/challenge/run'
[+] Starting local process '/challenge/run': pid 872
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 839B
[x] Receiving all data: 1.96KB
[x] Receiving all data: 2.02KB
[x] Receiving all data: 2.07KB
[x] Receiving all data: 2.31KB
[x] Receiving all data: 2.37KB
[+] Receiving all data: Done (2.37KB)
[*] Process '/challenge/run' stopped with exit code 0 (pid 872)
b'\nWelcome to ASMLevel21\n==================================================\n\nTo interact with any level you will send raw bytes over stdin to this program.\nTo efficiently solve these problems, first run it once to see what you need\nthen craft, assemble, and pipe your bytes to this program.\n\nIn this level you will be working with control flow manipulation. This involves using instructions\nto both indirectly and directly control the special register `rip`, the instruction pointer.\nYou will use instructions like: jmp, call, cmp, and the like to implement requests behavior.\n\nWe will be testing your code multiple times in this level with dynamic values! This means we will\nbe running your code in a variety of random ways to verify that the logic is robust enough to\nsurvive normal use. You can consider this as normal dynamic value se\n\n\n\nIn previous levels you discovered the for-loop to iterate for a *number* of times, both dynamically and\nstatically known, but what happens when you want to iterate until you meet a condition? A second loop\nstructure exists called the while-loop to fill this demand. In the while-loop you iterate until a\ncondition is met. As an example, say we had a location in memory with adjacent numbers and we wanted\nto get the average of all the numbers until we find one bigger or equal to 0xff:\naverage = 0\ni = 0\nwhile x[i] < 0xff:\n    average += x[i]\n    i += 1\naverage /= i\n\nUsing the above knowledge, please perform the following:\nCount the consecutive non-zero bytes in a contiguous region of memory, where:\nrdi = memory address of the 1st byte\nrax = number of consecutive non-zero bytes\nAdditionally, if rdi = 0, then set rax = 0 (we will check)!\nAn example test-case, let:\nrdi = 0x1000\n[0x1000] = 0x41\n[0x1001] = 0x42\n[0x1002] = 0x43\n[0x1003] = 0x00\nthen: rax = 3 should be set\n\nWe will now run multiple tests on your code, here is an example run:\n- (data) [0x404000] = {10 random bytes},\n- rdi = 0x404000\n\nPlease give me your assembly in bytes (up to 0x1000 bytes): \nExecuting your code...\n---------------- CODE ----------------\n0x400000:\tmov   \trax, 0\n0x400007:\tcmp   \trdi, 0\n0x40000b:\tje    \t0x400025\n0x40000d:\tmov   \trsi, 0xffffffffffffffff\n0x400014:\tadd   \trsi, 1\n0x400018:\tmov   \trbx, qword ptr [rdi + rsi]\n0x40001c:\tcmp   \trbx, 0\n0x400020:\tjne   \t0x400014\n0x400022:\tmov   \trax, rsi\n--------------------------------------\npwn.college{M6ITubuC1gixMFG6yn0_9xtMk8E.0FNxIDL5IDOzMzW}\n\n'
```

# Flag
`pwn.college{M6ITubuC1gixMFG6yn0_9xtMk8E.0FNxIDL5IDOzMzW}`

# Level Description
```
hacker@assembly-crash-course-level-10:~$ /challenge/run

Welcome to ASMLevel10
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



Up until now you have worked with registers as the only way for storing things, essentially
variables like 'x' in math. Recall that memory can be addressed. Each address contains something
at that location, like real addresses! As an example: the address '699 S Mill Ave, Tempe, AZ 85281'
maps to the 'ASU Campus'. We would also say it points to 'ASU Campus'.  We can represent this like:
['699 S Mill Ave, Tempe, AZ 85281'] = 'ASU Campus'
The address is special because it is unique. But that also does not mean other address cant point to
the same thing (as someone can have multiple houses). Memory is exactly the same! For instance,
the address in memory that your code is stored (when we take it from you) is 0x400000.
In x86 we can access the thing at a memory location, called dereferencing, like so:
mov rax, [some_address]        <=>     Moves the thing at 'some_address' into rax
This also works with things in registers:
mov rax, [rdi]         <=>     Moves the thing stored at the address of what rdi holds to rax
This works the same for writing:
mov [rax], rdi         <=>     Moves rdi to the address of what rax holds.
So if rax was 0xdeadbeef, then rdi would get stored at the address 0xdeadbeef:
[0xdeadbeef] = rdi
Note: memory is linear, and in x86, it goes from 0 - 0xffffffffffffffff (yes, huge).

Please perform the following:
1. Place the value stored at 0x404000 into rax
2. Increment the value stored at the address 0x404000 by 0x1337
Make sure the value in rax is the original value stored at 0x404000 and make sure
that [0x404000] now has the incremented value.

We will now set the following in preparation for your code:
[0x404000] = 0x16fbc6

Please give me your assembly in bytes (up to 0x1000 bytes):
```

# Solution
```py
import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
mov rax, [0x404000]
addq [0x404000], 0x1337
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())
```

```
hacker@assembly-crash-course-level-10:~$ ipython
Python 3.8.10 (default, May 26 2023, 14:05:08) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.2 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pwn
   ...: pwn.context.update(arch="amd64")
   ...: code = pwn.asm("""
   ...: mov rax, [0x404000]
   ...: addq [0x404000], 0x1337
   ...: """ )
   ...: process = pwn.process("/challenge/run")
   ...: process.write(code)
   ...: print(process.readall())
[x] Starting local process '/challenge/run'
[+] Starting local process '/challenge/run': pid 394
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 913B
[x] Receiving all data: 2.58KB
[x] Receiving all data: 2.65KB
[x] Receiving all data: 2.69KB
[x] Receiving all data: 2.77KB
[x] Receiving all data: 2.83KB
[+] Receiving all data: Done (2.83KB)
[*] Process '/challenge/run' stopped with exit code 0 (pid 394)
b"\nWelcome to ASMLevel10\n==================================================\n\nTo interact with any level you will send raw bytes over stdin to this program.\nTo efficiently solve these problems, first run it once to see what you need\nthen craft, assemble, and pipe your bytes to this program.\n\nWe will now set some values in memory dynamically before each run. On each run\nthe values will change. This means you will need to do some type of formulaic\noperation with registers_use. We will tell you which registers_use are set beforehand\nand where you should put the result. In most cases, its rax.\n\nIn this level you will be working with memory. This will require you to read or write\nto things stored linearly in memory. If you are confused, go look at the linear\naddressing module in 'ike. You may also be asked to dereference things, possibly multiple\ntimes, to things we dynamically put in memory for your use.\n\n\n\nUp until now you have worked with registers as the only way for storing things, essentially\nvariables like 'x' in math. Recall that memory can be addressed. Each address contains something\nat that location, like real addresses! As an example: the address '699 S Mill Ave, Tempe, AZ 85281'\nmaps to the 'ASU Campus'. We would also say it points to 'ASU Campus'.  We can represent this like:\n['699 S Mill Ave, Tempe, AZ 85281'] = 'ASU Campus'\nThe address is special because it is unique. But that also does not mean other address cant point to\nthe same thing (as someone can have multiple houses). Memory is exactly the same! For instance,\nthe address in memory that your code is stored (when we take it from you) is 0x400000.\nIn x86 we can access the thing at a memory location, called dereferencing, like so:\nmov rax, [some_address]        <=>     Moves the thing at 'some_address' into rax\nThis also works with things in registers:\nmov rax, [rdi]         <=>     Moves the thing stored at the address of what rdi holds to rax\nThis works the same for writing:\nmov [rax], rdi         <=>     Moves rdi to the address of what rax holds.\nSo if rax was 0xdeadbeef, then rdi would get stored at the address 0xdeadbeef:\n[0xdeadbeef] = rdi\nNote: memory is linear, and in x86, it goes from 0 - 0xffffffffffffffff (yes, huge).\n\nPlease perform the following:\n1. Place the value stored at 0x404000 into rax\n2. Increment the value stored at the address 0x404000 by 0x1337\nMake sure the value in rax is the original value stored at 0x404000 and make sure\nthat [0x404000] now has the incremented value.\n\nWe will now set the following in preparation for your code:\n[0x404000] = 0x10e122\n\nPlease give me your assembly in bytes (up to 0x1000 bytes): \nExecuting your code...\n---------------- CODE ----------------\n0x400000:\tmov   \trax, qword ptr [0x404000]\n0x400008:\tadd   \tqword ptr [0x404000], 0x1337\n--------------------------------------\npwn.college{czNV4xphoqb2E2qBTuPJkK0K7Nu.01MwIDL5IDOzMzW}\n\n"
```

# Flag
`pwn.college{czNV4xphoqb2E2qBTuPJkK0K7Nu.01MwIDL5IDOzMzW}`

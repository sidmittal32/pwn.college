# Level Description
```
hacker@assembly-crash-course-level-19:~$ /challenge/run

Welcome to ASMLevel19
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



The last set of jump types is the indirect jump, which is often used for switch statements in the
real world. Switch statements are a special case of if-statements that use only numbers to
determine where the control flow will go. Here is an example:
switch(number):
    0: jmp do_thing_0
    1: jmp do_thing_1
    2: jmp do_thing_2
    default: jmp do_default_thing
The switch in this example is working on `number`, which can either be 0, 1, or 2. In the case that
`number` is not one of those numbers, default triggers. You can consider this a reduced else-if
type structure.
In x86, you are already used to using numbers, so it should be no suprise that you can make if
statements based on something being an exact number. In addition, if you know the range of the numbers,
a switch statement works very well. Take for instance the existence of a jump table. A jump table
is a contiguous section of memory that holds addresses of places to jump. In the above example, the
jump table could look like:
[0x1337] = address of do_thing_0
[0x1337+0x8] = address of do_thing_1
[0x1337+0x10] = address of do_thing_2
[0x1337+0x18] = address of do_default_thing
Using the jump table, we can greatly reduce the amount of cmps we use. Now all we need to check
is if `number` is greater than 2. If it is, always do:
jmp [0x1337+0x18]
Otherwise:
jmp [jump_table_address + number * 8]
Using the above knowledge, implement the following logic:
if rdi is 0:
    jmp 0x40301c
else if rdi is 1:
    jmp 0x4030f7
else if rdi is 2:
    jmp 0x4031f1
else if rdi is 3:
    jmp 0x40329e
else:
    jmp 0x403363
Please do the above with the following constraints:
- assume rdi will NOT be negative
- use no more than 1 cmp instruction
- use no more than 3 jumps (of any variant)
- we will provide you with the number to 'switch' on in rdi.
- we will provide you with a jump table base address in rsi.

Here is an example table:
    [0x4041d0] = 0x40301c (addrs will change)
    [0x4041d8] = 0x4030f7
    [0x4041e0] = 0x4031f1
    [0x4041e8] = 0x40329e
    [0x4041f0] = 0x403363

Please give me your assembly in bytes (up to 0x1000 bytes):
```

# Solution
```py
import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
mov rax,rdi
and rax,0xfffffffffffffffc
je down
jmp [rsi+32]
down:
jmp [rsi+rdi*8]
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())
```

```
hacker@assembly-crash-course-level-19:~$ ipython
Python 3.8.10 (default, May 26 2023, 14:05:08) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.2 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pwn
   ...: pwn.context.update(arch="amd64")
   ...: code = pwn.asm("""
   ...: mov rax,rdi
   ...: and rax,0xfffffffffffffffc
   ...: je down
   ...: jmp [rsi+32]
   ...: down:
   ...: jmp [rsi+rdi*8]
   ...: """ )
   ...: process = pwn.process("/challenge/run")
   ...: process.write(code)
   ...: print(process.readall())
[x] Starting local process '/challenge/run'
[+] Starting local process '/challenge/run': pid 1364
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 839B
[x] Receiving all data: 2.89KB
[x] Receiving all data: 2.95KB
[x] Receiving all data: 2.97KB
[x] Receiving all data: 3.16KB
[x] Receiving all data: 3.21KB
[+] Receiving all data: Done (3.21KB)
[*] Process '/challenge/run' stopped with exit code 0 (pid 1364)
b"\nWelcome to ASMLevel19\n==================================================\n\nTo interact with any level you will send raw bytes over stdin to this program.\nTo efficiently solve these problems, first run it once to see what you need\nthen craft, assemble, and pipe your bytes to this program.\n\nIn this level you will be working with control flow manipulation. This involves using instructions\nto both indirectly and directly control the special register `rip`, the instruction pointer.\nYou will use instructions like: jmp, call, cmp, and the like to implement requests behavior.\n\nWe will be testing your code multiple times in this level with dynamic values! This means we will\nbe running your code in a variety of random ways to verify that the logic is robust enough to\nsurvive normal use. You can consider this as normal dynamic value se\n\n\n\nThe last set of jump types is the indirect jump, which is often used for switch statements in the\nreal world. Switch statements are a special case of if-statements that use only numbers to\ndetermine where the control flow will go. Here is an example:\nswitch(number):\n    0: jmp do_thing_0\n    1: jmp do_thing_1\n    2: jmp do_thing_2\n    default: jmp do_default_thing\nThe switch in this example is working on `number`, which can either be 0, 1, or 2. In the case that\n`number` is not one of those numbers, default triggers. You can consider this a reduced else-if\ntype structure.\nIn x86, you are already used to using numbers, so it should be no suprise that you can make if\nstatements based on something being an exact number. In addition, if you know the range of the numbers,\na switch statement works very well. Take for instance the existence of a jump table. A jump table\nis a contiguous section of memory that holds addresses of places to jump. In the above example, the\njump table could look like:\n[0x1337] = address of do_thing_0\n[0x1337+0x8] = address of do_thing_1\n[0x1337+0x10] = address of do_thing_2\n[0x1337+0x18] = address of do_default_thing\nUsing the jump table, we can greatly reduce the amount of cmps we use. Now all we need to check\nis if `number` is greater than 2. If it is, always do:\njmp [0x1337+0x18]\nOtherwise:\njmp [jump_table_address + number * 8]\nUsing the above knowledge, implement the following logic:\nif rdi is 0:\n    jmp 0x40302d\nelse if rdi is 1:\n    jmp 0x40311a\nelse if rdi is 2:\n    jmp 0x40319b\nelse if rdi is 3:\n    jmp 0x403261\nelse:\n    jmp 0x40337b\nPlease do the above with the following constraints:\n- assume rdi will NOT be negative\n- use no more than 1 cmp instruction\n- use no more than 3 jumps (of any variant)\n- we will provide you with the number to 'switch' on in rdi.\n- we will provide you with a jump table base address in rsi.\n\nHere is an example table:\n    [0x404155] = 0x40302d (addrs will change)\n    [0x40415d] = 0x40311a\n    [0x404165] = 0x40319b\n    [0x40416d] = 0x403261\n    [0x404175] = 0x40337b\n\nPlease give me your assembly in bytes (up to 0x1000 bytes): \nExecuting your code...\n---------------- CODE ----------------\n0x400000:\tmov   \trax, rdi\n0x400003:\tand   \trax, 0xfffffffffffffffc\n0x400007:\tje    \t0x40000c\n0x400009:\tjmp   \tqword ptr [rsi + 0x20]\n0x40000c:\tjmp   \tqword ptr [rsi + rdi*8]\n--------------------------------------\npwn.college{kdz4cbH2oYpHq4vOFxB1QJBXvFc.0lMxIDL5IDOzMzW}\n\n"
```

# Flag
`pwn.college{kdz4cbH2oYpHq4vOFxB1QJBXvFc.0lMxIDL5IDOzMzW}`

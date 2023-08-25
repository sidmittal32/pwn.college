# Level Description
```
hacker@assembly-crash-course-level-18:~$ /challenge/run

Welcome to ASMLevel18
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



We will now introduce you to conditional jumps--one of the most valuable instructions in x86.
In higher level programming languages, an if-else structure exists to do things like:
if x is even:
   is_even = 1
else:
   is_even = 0
This should look familiar, since its implementable in only bit-logic. In these structures, we can
control the programs control flow based on dynamic values provided to the program. Implementing the
above logic with jmps can be done like so:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
; assume rdi = x, rax is output
; rdx = rdi mod 2
mov rax, rdi
mov rsi, 2
div rsi
; remainder is 0 if even
cmp rdx, 0
; jump to not_even code is its not 0
jne not_even
; fall through to even code
mov rbx, 1
jmp done
; jump to this only when not_even
not_even:
mov rbx, 0
done:
mov rax, rbx
; more instructions here
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Often though, you want more than just a single 'if-else'. Sometimes you want two if checks, followed
by an else. To do this, you need to make sure that you have control flow that 'falls-through' to the
next `if` after it fails. All must jump to the same `done` after execution to avoid the else.
There are many jump types in x86, it will help to learn how they can be used. Nearly all of them rely
on something called the ZF, the Zero Flag. The ZF is set to 1 when a cmp is equal. 0 otherwise.

Using the above knowledge, implement the following:
if [x] is 0x7f454c46:
   y = [x+4] + [x+8] + [x+12]
else if [x] is 0x00005A4D:
   y = [x+4] - [x+8] - [x+12]
else:
   y = [x+4] * [x+8] * [x+12]
where:
x = rdi, y = rax. Assume each dereferenced value is a signed dword. This means the values can start as
a negative value at each memory position.
A valid solution will use the following at least once:
jmp (any variant), cmp

We will now run multiple tests on your code, here is an example run:
- (data) [0x404000] = {4 random dwords]}
- rdi = 0x404000

Please give me your assembly in bytes (up to 0x1000 bytes): 
```

# Solution
```py
import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
mov ebx,[rdi+4]
mov ecx,[rdi+8]
mov edx,[rdi+12]
mov eax,[rdi]
cmp eax,0x7f454c46
je con1
nop
mov eax,[rdi]
cmp eax,0x00005A4D
je con2
nop
imul ebx,ecx
imul ebx,edx
jmp done
nop
con1:
add ebx,ecx
add ebx,edx
jmp done
nop
con2:
sub ebx,ecx
sub ebx,edx
done:
mov eax,ebx
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())
```

```
hacker@assembly-crash-course-level-18:~$ ipython
Python 3.8.10 (default, May 26 2023, 14:05:08) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.2 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pwn
   ...: pwn.context.update(arch="amd64")
   ...: code = pwn.asm("""
   ...: mov ebx,[rdi+4]
   ...: mov ecx,[rdi+8]
   ...: mov edx,[rdi+12]
   ...: mov eax,[rdi]
   ...: cmp eax,0x7f454c46
   ...: je con1
   ...: nop
   ...: mov eax,[rdi]
   ...: cmp eax,0x00005A4D
   ...: je con2
   ...: nop
   ...: imul ebx,ecx
   ...: imul ebx,edx
   ...: jmp done
   ...: nop
   ...: con1:
   ...: add ebx,ecx
   ...: add ebx,edx
   ...: jmp done
   ...: nop
   ...: con2:
   ...: sub ebx,ecx
   ...: sub ebx,edx
   ...: done:
   ...: mov eax,ebx
   ...: """ )
   ...: process = pwn.process("/challenge/run")
   ...: process.write(code)
   ...: print(process.readall())
[x] Starting local process '/challenge/run'
[+] Starting local process '/challenge/run': pid 2162
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 839B
[x] Receiving all data: 2.78KB
[x] Receiving all data: 2.84KB
[x] Receiving all data: 2.88KB
[x] Receiving all data: 3.26KB
[x] Receiving all data: 3.48KB
[x] Receiving all data: 3.54KB
[+] Receiving all data: Done (3.54KB)
[*] Process '/challenge/run' stopped with exit code 0 (pid 2162)
b"\nWelcome to ASMLevel18\n==================================================\n\nTo interact with any level you will send raw bytes over stdin to this program.\nTo efficiently solve these problems, first run it once to see what you need\nthen craft, assemble, and pipe your bytes to this program.\n\nIn this level you will be working with control flow manipulation. This involves using instructions\nto both indirectly and directly control the special register `rip`, the instruction pointer.\nYou will use instructions like: jmp, call, cmp, and the like to implement requests behavior.\n\nWe will be testing your code multiple times in this level with dynamic values! This means we will\nbe running your code in a variety of random ways to verify that the logic is robust enough to\nsurvive normal use. You can consider this as normal dynamic value se\n\n\n\nWe will now introduce you to conditional jumps--one of the most valuable instructions in x86.\nIn higher level programming languages, an if-else structure exists to do things like:\nif x is even:\n   is_even = 1\nelse:\n   is_even = 0\nThis should look familiar, since its implementable in only bit-logic. In these structures, we can\ncontrol the programs control flow based on dynamic values provided to the program. Implementing the\nabove logic with jmps can be done like so:\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n; assume rdi = x, rax is output\n; rdx = rdi mod 2\nmov rax, rdi\nmov rsi, 2\ndiv rsi\n; remainder is 0 if even\ncmp rdx, 0\n; jump to not_even code is its not 0\njne not_even\n; fall through to even code\nmov rbx, 1\njmp done\n; jump to this only when not_even\nnot_even:\nmov rbx, 0\ndone:\nmov rax, rbx\n; more instructions here\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nOften though, you want more than just a single 'if-else'. Sometimes you want two if checks, followed\nby an else. To do this, you need to make sure that you have control flow that 'falls-through' to the\nnext `if` after it fails. All must jump to the same `done` after execution to avoid the else.\nThere are many jump types in x86, it will help to learn how they can be used. Nearly all of them rely\non something called the ZF, the Zero Flag. The ZF is set to 1 when a cmp is equal. 0 otherwise.\n\nUsing the above knowledge, implement the following:\nif [x] is 0x7f454c46:\n   y = [x+4] + [x+8] + [x+12]\nelse if [x] is 0x00005A4D:\n   y = [x+4] - [x+8] - [x+12]\nelse:\n   y = [x+4] * [x+8] * [x+12]\nwhere:\nx = rdi, y = rax. Assume each dereferenced value is a signed dword. This means the values can start as\na negative value at each memory position.\nA valid solution will use the following at least once:\njmp (any variant), cmp\n\nWe will now run multiple tests on your code, here is an example run:\n- (data) [0x404000] = {4 random dwords]}\n- rdi = 0x404000\n\nPlease give me your assembly in bytes (up to 0x1000 bytes): \nExecuting your code...\n---------------- CODE ----------------\n0x400000:\tmov   \tebx, dword ptr [rdi + 4]\n0x400003:\tmov   \tecx, dword ptr [rdi + 8]\n0x400006:\tmov   \tedx, dword ptr [rdi + 0xc]\n0x400009:\tmov   \teax, dword ptr [rdi]\n0x40000b:\tcmp   \teax, 0x7f454c46\n0x400010:\tje    \t0x400026\n0x400012:\tnop   \t\n0x400013:\tmov   \teax, dword ptr [rdi]\n0x400015:\tcmp   \teax, 0x5a4d\n0x40001a:\tje    \t0x40002d\n0x40001c:\tnop   \t\n0x40001d:\timul  \tebx, ecx\n0x400020:\timul  \tebx, edx\n0x400023:\tjmp   \t0x400031\n0x400025:\tnop   \t\n0x400026:\tadd   \tebx, ecx\n0x400028:\tadd   \tebx, edx\n0x40002a:\tjmp   \t0x400031\n0x40002c:\tnop   \t\n0x40002d:\tsub   \tebx, ecx\n0x40002f:\tsub   \tebx, edx\n0x400031:\tmov   \teax, ebx\n--------------------------------------\npwn.college{MuwyjDEthWFQVL0RRW9bHZPlBK9.0VMxIDL5IDOzMzW}\n\n"
```

# Flag
`pwn.college{MuwyjDEthWFQVL0RRW9bHZPlBK9.0VMxIDL5IDOzMzW}`

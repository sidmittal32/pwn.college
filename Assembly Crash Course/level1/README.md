# Level Description
```
hacker@assembly-crash-course-level-1:~$ /challenge/run

Welcome to ASMLevel1
==================================================

To interact with any level you will send raw bytes over stdin to this program.
To efficiently solve these problems, first run it once to see what you need
then craft, assemble, and pipe your bytes to this program.

In this level you will be working with registers. You will be asked to modify
or read from registers_use.



In this level you will work with registers_use! Please set the following:
* rdi = 0x1337

Please give me your assembly in bytes (up to 0x1000 bytes): 
```

# Solution
```py
import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
mov rdi, 0x1337
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())
```
```
hacker@assembly-crash-course-level-1:~$ ipython
Python 3.8.10 (default, May 26 2023, 14:05:08) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.2 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import pwn
   ...: pwn.context.update(arch="amd64")
   ...: code = pwn.asm("""
   ...: mov rdi, 0x1337
   ...: """ )
   ...: process = pwn.process("/challenge/run")
   ...: process.write(code)
   ...: print(process.readall())
[x] Starting local process '/challenge/run'
[+] Starting local process '/challenge/run': pid 847
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 397B
[x] Receiving all data: 549B
[x] Receiving all data: 611B
[x] Receiving all data: 640B
[x] Receiving all data: 679B
[x] Receiving all data: 737B
[+] Receiving all data: Done (737B)
[*] Process '/challenge/run' stopped with exit code 0 (pid 847)
b'\nWelcome to ASMLevel1\n==================================================\n\nTo interact with any level you will send raw bytes over stdin to this program.\nTo efficiently solve these problems, first run it once to see what you need\nthen craft, assemble, and pipe your bytes to this program.\n\nIn this level you will be working with registers. You will be asked to modify\nor read from registers_use.\n\n\n\nIn this level you will work with registers_use! Please set the following:\n* rdi = 0x1337\n\nPlease give me your assembly in bytes (up to 0x1000 bytes): \nExecuting your code...\n---------------- CODE ----------------\n0x400000:\tmov   \trdi, 0x1337\n--------------------------------------\npwn.college{k1VLKbk1PBPzuz9O4IZhzmBx674.0FN5EDL5IDOzMzW}\n\n'
```

# Flag
`pwn.college{k1VLKbk1PBPzuz9O4IZhzmBx674.0FN5EDL5IDOzMzW}`

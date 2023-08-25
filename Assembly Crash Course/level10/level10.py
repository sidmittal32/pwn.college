import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
mov rax, [0x404000]
addq [0x404000], 0x1337
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())

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

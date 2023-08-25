import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
mov al, dil
mov bx, si
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())

import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
mov rax, rdi
shl rax, 24
shr rax, 56
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())

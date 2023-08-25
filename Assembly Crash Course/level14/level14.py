import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
pop rax
sub rax, rdi
push rax
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())

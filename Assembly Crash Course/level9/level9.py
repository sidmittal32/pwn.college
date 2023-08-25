import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
xor rax, rax
and rdi, 1
or rax, rdi
xor rax, 1
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())

import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
mov rax, rdi
div rsi
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())

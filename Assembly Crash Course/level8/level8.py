import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
and rax, rdi
and rax, rsi
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())

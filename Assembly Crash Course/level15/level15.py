import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
push rdi
push rsi
pop rdi
pop rsi
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())

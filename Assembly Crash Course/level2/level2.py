import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
add rdi, 0x331337
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())

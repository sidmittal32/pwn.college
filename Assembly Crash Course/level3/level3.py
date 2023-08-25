import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
imul rdi, rsi
add rdi, rdx
mov rax, rdi
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())

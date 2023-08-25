import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
mov rax, [rdi]
add rax, [rdi + 8]
mov [rsi], rax
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())

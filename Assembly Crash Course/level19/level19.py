import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
mov rax,rdi
and rax,0xfffffffffffffffc
je down
jmp [rsi+32]
down:
jmp [rsi+rdi*8]
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())

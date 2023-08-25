import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
mov rax, [rsp]
add rax, [rsp+8]
add rax, [rsp+16]
add rax, [rsp+24]
shr rax, 2
push rax 
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())

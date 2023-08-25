import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
xor rax, rax
xor rcx, rcx
mov rbx, rsi
loop:
sub rbx, 1
mov ecx, [rdi+rbx*8]
add rax, rcx
cmp rbx, 0
jne loop
div rsi
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())

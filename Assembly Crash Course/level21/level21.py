import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
mov rax,0
cmp rdi,0
je done
mov rsi,-1
loop:
add rsi,1
mov rbx,[rdi+rsi]
cmp rbx,0
jne loop
mov rax,rsi
done:
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())

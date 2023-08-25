import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
movq rax, 0xdeadbeef00001337
movq [rdi], rax
movq rax, 0xc0ffee0000
movq [rsi], rax
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())

import pwn
pwn.context.update(arch="amd64")
code = pwn.asm("""
mov ebx,[rdi+4]
mov ecx,[rdi+8]
mov edx,[rdi+12]
mov eax,[rdi]
cmp eax,0x7f454c46
je con1
nop
mov eax,[rdi]
cmp eax,0x00005A4D
je con2
nop
imul ebx,ecx
imul ebx,edx
jmp done
nop
con1:
add ebx,ecx
add ebx,edx
jmp done
nop
con2:
sub ebx,ecx
sub ebx,edx
done:
mov eax,ebx
""" )
process = pwn.process("/challenge/run")
process.write(code)
print(process.readall())

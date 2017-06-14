# port 53

# 套接字边界问题

"""
套接字封帧问题

- 一次过发送完数据后close套接字
- 单个方向上关闭通道
- 定长传输
- 设定边界
- 为每个消息设置长度
- 长度不定的，为每个传输块设定长度


HTTP协议采用了多种封帧方法

例如：

\r\n\r\n0

Content-Length

Connection: close

"""
  
  import socket

  socket.getaddrinfo # socket.gaierror45
  socket.gethostbyaddr
  socket.gethostbyname 
  socket.gethostname 
  socket.getservbyname
  socket.getservbyport 

"""
hex(4235)
'0x108b'

struct.pack('>i', 4235)
b'\x00\x00\x10\x8b'
大端-高尾端

struct.pack('<i', 4235)
b'\x8b\x10\x00\x00'
小端-低

"""


"""
BOM b'\xff\xfe'
BOM_BE b'\xfe\xff'
BOM_LE b'\xff\xfe'
BOM32_BE b'\xfe\xff'
BOM32_LE b'\xff\xfe'
BOM64_BE b'\x00\x00\xfe\xff'
BOM64_LE b'\xff\xfe\x00\x00'
BOM_UTF8 b'\xef\xbb\xbf'
BOM_UTF16 b'\xff\xfe'
BOM_UTF16_LE b'\xff\xfe'
BOM_UTF16_BE b'\xfe\xff'
BOM_UTF32 b'\xff\xfe\x00\x00'
BOM_UTF32_LE b'\xff\xfe\x00\x00'
BOM_UTF32_BE b'\x00\x00\xfe\xff'
"""
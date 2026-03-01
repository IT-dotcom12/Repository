import struct

a,b = float(input("a: ")), float(input("b: "))
ba = struct.unpack('>Q', struct.pack('>d', a))[0]
bb = struct.unpack('>Q', struct.pack('>d', b))[0]

print(f"{a} = {ba:064b}")
print(f"{b} = {bb:064b}")
print(f"Различий: {sum((ba>>i)&1 != (bb>>i)&1 for i in range(64))}")
print(f"{'=' if a==b else '!='}")


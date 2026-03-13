import base64

encoded = "3d3d516343746d4d6d6c315669563362"

step1 = bytes.fromhex(encoded).decode()
step2 = step1[::-1]
step3 = base64.b64decode(step2).decode()

print(step3)
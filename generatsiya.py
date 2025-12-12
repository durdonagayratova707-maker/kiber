
from Crypto.PublicKey import RSA

def generate_rsa_keypair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Kalitlarni faylga saqlash
private_key, public_key = generate_rsa_keypair()
with open("private.pem", "wb") as f:
    f.write(private_key)
with open("public.pem", "wb") as f:
    f.write(public_key)

print("Kalitlar yaratildi: private.pem va public.pem")

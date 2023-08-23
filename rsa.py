from Crypto.Util.number import*



# - - RSA Numbers - -

Message = "Hello"  # can be the flag for CTF

print("The message is ", Message)

m = bytes_to_long(b"Hello") # Convert to long ( number )



p=getPrime(512) #random 512 bit prime num

q=getPrime(512) #random 512 bit prime num

print("p = " , p )

n=p*q # the modulus 



phi=(p-1)*(q-1) 



print("- Encrypted:")# - - Encrypt - -



e=65537 # encrypt key 

c=pow(m,e,n) # encryption formula



print(c) # Cipher text ( Encrypted message )



print("- Decrypted:")# - - Decrypt - -

d=inverse(e,phi) # decrypt key

msg=pow(c,d,n) # decryption formula

print(msg) # the message in bits (numbers)

print(long_to_bytes(msg)) # numbers to TEXT to read the message


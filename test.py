'''import uuid

print(uuid.uuid4().hex)'''

import argon2

ph = argon2.PasswordHasher(time_cost=2, memory_cost=2**15,parallelism=8, hash_len=16, salt_len=16)

hash = ph.hash("user")

print(hash)
print(ph.verify(hash, "user"))
print(ph.check_needs_rehash(hash))

print(len("4$lgqSJTGhVc0AF8vq+wgZcw$HUc5g3J95+h6FFiySxhQmQ"))
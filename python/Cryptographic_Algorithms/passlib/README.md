---------Encrypting passwords in Python with passlib---------

Installation:

pip install passlib

passlib is a library which is mainly used for encrypting the paseword with the use of hashing algorithm PDKDF2.


Context - Passlib works by defining a context. In it, we specify what algorithm we will use for hashing, as well as any configuration parameters.

What are rounds?
A round is a part of the algorithm that runs many times in order to reduce "crackability". Different algorithms recommend using different numbers of rounds.


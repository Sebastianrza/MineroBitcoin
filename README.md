# MineroBitcoin
This project is only for hobby
We are going to try to "emulate" at a local level what would be a blockchain node where each of the students in the class will be a bitcoin miner.

Each bitcoin miner will generate a file (which is the equivalent of a block) with the following structure: you must put your full name and surname, the hash of the previous block and the nonce that makes the hash (sha1) of your file start with 00 .
File:

Name and Surname: ******************
Previous hash: 00000000000000000000000000000000000000000000
Nonce: ****

Hash:

SHA1 (block) = *********************************************

It's necessary have installing pip,re and hashlib (pip3 install re, pip3 install hashlib)
this program is written for sha1, but it can be modified for the algorithm you need.
sha1, sha224, sha256, sha384, sha512, blake2b, and blake2s. md5, sha3_224, sha3_256, 
sha3_384, sha3_512, shake_128, shake_256.

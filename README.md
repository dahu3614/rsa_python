# rsa_python

The Rivest-Shamir-Adleman (RSA) cryptosystem is the most widely used system for securely transmitting data currently in use today. It was originally developed independently, once by by Clifford Cocks in 1973, and again by Rivest, Shamir, and Adleman in 1977. The usefulness of the RSA system is that it enables public-key cryptography, which means that messages can be sent and received securely without previously having a secure key exchange between the sender and receipient. Instead, the system relies on a pair of keys: one public and one private. The public key is sent out to anyone who wishes to send a message to the receipient, while the recipient holds the private key secretly. In this way, anyone with the public key can encrypt a message and send the resulting ciphertext to the recipient, but only the recipient (who holds the private key) can decode the encrypted messages back into plaintext.

The code in this repository is a working system for generating public and private keys, and using these keys to encrypt and decrypt messages. The way this works is as follows. First, two distinct prime numbers $p$ and $q$ are chosen. In practice, these are between 2048 - 4096 bits (in decimal, these values are between 616 digits and 1234 digits long), but in this project, shorter numbers are chosen for ease of use of the system. Then, the product of these two primes is computed

$$
n = p * q 
$$

Next, a number $e$ is found such that it is relatively prime to $(p - 1) * (q - 1)$. Finally, a number $d$ is found such that it is inverse to $e$, modulo $(p - 1) * (q - 1)$. The pair $(e, n)$ is sent out as the public key and used to encrypt a message $M$. The ciphertext $C$ is generated with the public key by computing 

$$
C = M ^ {e} \, mod \, n
$$

and then sent to the recipient. Finally, the ciphertext is decrypted by the recipient with the private key $(d, n)$ by computing 

$$
M = C ^ {d} \, mod \, n
$$

In my project, I define the basic tools required for implementing the RSA system, including functions for implementing Fast Modular Exponentiation, Euclid's Algorithm and Extended Euclid's Algorithm, functions for finding the public and private keys for the RSA Algorithm, and finally functions for encoding and decoding encrypted messages.

Additionally, I also discuss how to break codes with small key values, and why it becomes more difficult to break the codes as the keys get large.

Finally, I implemented three custom features:
1. A main() function so that anyone using this code can take advantage of the functionality in a very easy way.
2. An improved factorization algorithm using a list of the first 100,008 primes to factor keys up to 12 digits long
3. Pollard's Rho factorization algorithm to factor keys up to 27 digits long within ~1 minute

Note that since each character is encrypted individually, this encryption method is susceptible to known plaintext attack or character frequency analysis attack. I am currently working on code for a character frequency analysis attack against this implementation - stay tuned!

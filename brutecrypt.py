import time

class crack_hash:
   def __init__(self, hash_value, default_passwords):
       self.hash_value = hash_value
       self.default_passwords = default_passwords

   # main function for md5
   def MD5(self, MD5_hash):
       print("\n\033[2;34mMD5 Hash Detected...\n")

       # iterate the md5 hash and default passwords   
       for passwd,md5 in zip(self.default_passwords.readlines(), MD5_hash.readlines()):

          # check if the value is matched
          if self.hash_value == md5.strip():
            print("\n\033[2;38mChecking  |  {0}  |  \033[2;32mFound".format(passwd.strip()))
            break
          else:
            time.sleep(1)
            print("\033[2;38mChecking  |  {0}  |  \033[2;31mNot Found".format(passwd.strip()))

   # duplicated function for sha1
   def SHA1(self, SHA1_hash):
       print("\n\033[2;34mSHA-1 hash Detected...\n")

       # iterate the sha1 hash and default passwords
       for passwd,sha1 in zip(self.default_passwords.readlines(), SHA1_hash.readlines()):

          # check if the value is matched
          if self.hash_value == sha1.strip():
            print("\n\033[2;38mChecking  |  {0}  |  \033[2;32mFound".format(passwd.strip()))
            break
          else:
            time.sleep(1)
            print("\033[2;38mChecking  |  {0}  |  \033[2;31mNot Found".format(passwd.strip()))

   # duplicated function for sha256
   def SHA256(self, SHA256_hash):
       print("\n\033[2;34mSHA-256 Hash Detected...\n")

       # iterate the sha256 and default passwords
       for passwd,sha256 in zip(self.default_passwords.readlines(), SHA256_hash.readlines()):

          # check if the value is matched
          if self.hash_value == sha256.strip():
            print("\n\033[2;38mChecking  |  {0}  |  \033[2;32mFound".format(passwd.strip()))
            break
          else:
            time.sleep(1)
            print("\033[2;38mChecking  |  {0}  |  \033[2;31mNot Found".format(passwd.strip()))

   # duplicated function for sha512
   def SHA512(self, SHA512_hash):
       print("\n\033[2;34mSHA-512 Hash Detected...\n")

       # iterate the sha512 and default passwords
       for passwd,sha512 in zip(self.default_passwords.readlines(), SHA512_hash.readlines()):

          # check if the value is matched
          if self.hash_value == sha512.strip():
            print("\n\033[2;38mChecking  |  {0}  |  \033[2;32mFound".format(passwd.strip()))
            break
          else:
            time.sleep(1)
            print("\033[2;38mChecking  |  {0}  |  \033[2;31mNot Found".format(passwd.strip()))

   # duplicated function for crc32
   def CRC32(self, CRC32_hash):
       print("\n\033[2;34mCRC-32 Hash Detected...\n")

       # iterate the crc32 and default passwords
       for passwd,crc32 in zip(self.default_passwords.readlines(), CRC32_hash.readlines()):

          # check if the value is matched
          if self.hash_value == crc32.strip():
            print("\n\033[2;38mChecking  |  {0}  |  \033[2;32mFound".format(passwd.strip()))
            break
          else:
            time.sleep(1)
            print("\033[2;38mChecking  |  {0}  |  \033[2;31mNot Found".format(passwd.strip()))

   class hash_set:
      def execute(self):

          #logo
          banner = '''\033[1;31m
                        @@@@@@@  @@@@@@@  @@@  @@@ @@@@@@@ @@@@@@@@       @@@@@@@ @@@@@@@  @@@ @@@ @@@@@@@  @@@@@@@
                        @@!  @@@ @@!  @@@ @@!  @@@   @@!   @@!           !@@      @@!  @@@ @@! !@@ @@!  @@@   @@!  
                        @!@!@!@  @!@!!@!  @!@  !@!   @!!   @!!!:!        !@!      @!@!!@!   !@!@!  @!@@!@!    @!!  
                        !!:  !!! !!: :!!  !!:  !!!   !!:   !!:           :!!      !!: :!!    !!:   !!:        !!:  
                        :: : ::   :   : :  :.:: :     :    : :: :::       :: :: :  :   : :   .:     :          :
                        
                        [+] CODED BY: REV
                   '''

          # file for hash and default passwords to implement in duplicated functions and object
          default_passwords = open("password.txt", "r")
          MD5_hash = open("MD5.txt", "r")
          SHA1_hash = open("SHA-1.txt", "r")
          SHA256_hash = open("SHA-256.txt", "r")
          SHA512_hash = open("SHA-512.txt", "r")
          CRC32_hash = open("CRC-32.txt", "r")

          print(banner)

          # check the type and length of hash
          hash_value = input("\033[2;34m[+] Enter Hash:")
          start = crack_hash(hash_value, default_passwords)
             
          # check the hash type
          if hash_value == "":
            print("\n\033[2;31mEnter a Hash Value...")
          else:
            # check if hash is 32 length execute the md5 function
            if len(hash_value) == 32:
              start.MD5(MD5_hash)

            # check if hash is 40 length execute the sha1 function
            elif len(hash_value) == 40:
              start.SHA1(SHA1_hash)

            # check if hash is 64 length execute the sha256 function
            elif len(hash_value) == 64:
              start.SHA256(SHA256_hash)

            # check if hash is 128 length execute the sha512 function
            elif len(hash_value) == 128:
              start.SHA512(SHA512_hash)

            # check if hash is 8 length excute the crc32 function
            elif len(hash_value) == 8:
              start.CRC32(CRC32_hash)
            else:
              print("\n\033[2;31mHash not identified...")

run = crack_hash.hash_set()
run.execute()          
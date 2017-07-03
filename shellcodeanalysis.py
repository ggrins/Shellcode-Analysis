import os

shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80"

f = open("shellcode.bin", "w+")
f.write(shellcode)
f.close()


print "\n[+]Printing Shellcode Strings[+]"
print "---------------------------------------"
os.system("strings shellcode.bin")
print "---------------------------------------"

print "\n"

print "[+]Disassembling Binary[+]"
print "---------------------------------------"
os.system("ndisasm -b 32 shellcode.bin")
print "---------------------------------------"

os.system("rm shellcode.bin")

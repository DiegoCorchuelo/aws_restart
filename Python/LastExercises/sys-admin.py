import os
import subprocess

os.system("ls")

print()

subprocess.run(["ls", "-l", "README.md"])

print()
#Recuperación de información del sistema
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

print()
#Recuperación de información sobre el espacio en disco
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
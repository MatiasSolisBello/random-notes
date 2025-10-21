# Bandit

Connectar con bandit via ssh
```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

**Level 0 → Level 1**
```bash
cat readme
```

**Level 1 → Level 2**
```bash
bandit1@bandit:~$ ls
-
bandit1@bandit:~$ cat ./-*
```

**Level 2 → Level 3**
```bash
bandit2@bandit:~$ ls
--spaces in this filename--
bandit2@bandit:~$ cat ./*
```

**Level 3 → Level 4**
```bash
bandit3@bandit:~$ ls
inhere
bandit3@bandit:~$ cd inhere
bandit3@bandit:~/inhere$ ls
bandit3@bandit:~/inhere$ ls -la
total 12
drwxr-xr-x 2 root    root    4096 Oct 14 09:26 .
drwxr-xr-x 3 root    root    4096 Oct 14 09:26 ..
-rw-r----- 1 bandit4 bandit3   33 Oct 14 09:26 .. Hiding-From-You
bandit3@bandit:~/inhere$ cat ./ ...*
```

**Level 4 → Level 5**
```bash
bandit4@bandit:~/inhere$ cat ./-file*
```

**Level 5 → Level 6**
```bash
# Lista recursivamente todos los archivos con detalles de permisos.
ls -lR

file */{.,}* | grep "ASCII text" | grep -v ', with very long lines'

find . -type f -size 1033c ! -executable -exec file '{}' \; | grep ASCII ./maybehere07/.file2

cat ./maybehere07/.file2

```

`file {}` → Identifica el tipo de contenido del archivo.

`grep "text"` → Filtra los archivos que contienen "text" en su descripción (archivos de texto).

`-type f` → Busca solo archivos (no directorios).

`-readable` → Filtra solo los archivos que el usuario tiene permisos de lectura.


**Level 6 → Level 7**

Se almacena en algún lugar del servidor y tiene las siguientes propiedades:
* Pertenece al usuario bandit7
* Pertenece al grupo bandit6
* Tamaño: 33 bytes
```bash
find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
```

`-type f` → Solo busca archivos (no directorios).

`-user bandit7` → Filtra archivos que pertenezcan al usuario bandit7.

`-group bandit6` → Filtra archivos que pertenezcan al grupo bandit6.

`-size 33c` → Busca archivos de exactamente 33 bytes (c significa "bytes", sin c serían bloques de 512B).

`2>/dev/null` → Oculta los errores de "Permiso denegado".


**Level 7 → Level 8**

La contraseña se almacena en el archivo data.txt junto a la palabra millonésimo.

```bash
grep "millionth" data.txt
```

**Level 8 → Level 9**

La contraseña se almacena en el archivo data.txt y es la única línea de texto que aparece solo una vez.
```bash
sort data.txt | uniq -u
```

`sort archivo.txt` → Ordena las líneas del archivo (necesario para que uniq funcione correctamente).

`uniq -u` → Muestra solo las líneas que aparecen una única vez en el archivo.

**Level 9 → Level 10**

La contraseña se almacena en el archivo data.txt en una de las pocas cadenas legibles por humanos, precedida por varios caracteres ‘=’.

```bash
strings data.txt | grep =
```


**Level 10 → Level 11**

La contraseña se almacena en el archivo data.txt, que contiene datos codificados en base64.
```bash
base64 -d data.txt

#imagen o documento, debes redirigir la salida a un archivo:
base64 -d archivo.txt > salida.bin
```
`-d o --decode` → Indica que queremos decodificar en lugar de codificar.


**Level 11 → Level 12**

La contraseña almacena en el archivo data.txt, donde todas las letras minúsculas (a-z) y mayúsculas (A-Z) se han rotado 13 posiciones.
```bash
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

**Level 12 → Level 13**

La contraseña se almacena en el archivo data.txt, que es un **volcado hexadecimal** de un archivo comprimido repetidamente.
```bash
```
` ` → 


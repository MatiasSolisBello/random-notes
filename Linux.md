# Apuntes de Linux

## Indice

[Comandos basicos](#comandos-basicos)

[Información del sistema](#información-del-sistema)

[Find](#find)

[Gestión de archivos y directorios](#gestión-de-archivos-y-directorios)

[Usuarios](#usuarios)

[Contraseñas](#contraseñas)

[Permisos](#permisos)

[Iptables](#iptables)

---

## Comandos basicos

Comando  | Descripción
------------- | -------------
pwd  | Directorio actual
cd | Mover a escritorio
cd .. | Volver
man ls  | Info detallada
ls | Listar
ls -l  | Muestra detalles como permisos, propietario, grupo, tamaño y fecha de modificación.
ls -R | (recursive) Muestra el contenido de todos los subdirectorios de manera recursiva
ls -a  | Muestra todos los archivos, incluidos los ocultos (que comienzan con .)
rwx  |  Permisos del directorio (Conexiones, Propietaio, Grupo del propietario)
d rwx  | Directorio
-rwx | Fichero o archivo
touch  | Crea archivos masivos
cat  | Visualizar contenido
cat *file1* *file2* > *file3*  | Leer file1 y unirlo a file2, que se unira a file3
cat -n | Mostrar fichero enumerado
more  | Visualizar parcializado
head *file*  | Visualizar primeras 10 lineas
head -n5 *file*  | Visualizar primeras 5 lineas
tail *file*   | Visualizar ultimas lineas
tail -n5 *file*  | Visualizar ultimas 5 lineas
tail -f *file* | Ver modificaciones en tiempo real
less | Ver contenido paginado
cp   | Copiar ficheros o directorios(cp opcion /ruta_origen /destino)
sort *archivo* | Ordena líneas de texto alfabética o numéricamente
sort -r *archivo*  | Ordena en orden inverso
sort -n *archivo*  | Ordena números (en lugar de alfabéticamente)
sort -k2,2 *archivo*  | Ordena por la segunda columna
grep | Busca texto dentro de archivos o entrada estándar
grep "error" logs.txt  | Busca la palabra "error" en logs.txt
grep -i "error" logs.txt  | Búsqueda sin distinguir mayúsculas/minúsculas
grep -r "error" /var/logs  | Busca recursivamente en una carpeta
grep -E "error|warning" logs.txt  | Busca varias palabras con expresiones regulares
tar | Empaqueta múltiples archivos en uno solo.
tar -cvf backup.tar carpeta/  | Crea un archivo tar de una carpeta
tar -xvf backup.tar  | Extrae el contenido de un archivo tar
tar -tvf backup.tar  | Lista los archivos dentro de un tar
tar -cvzf backup.tar.gz carpeta/  | Crea un tar y lo comprime con gzip
tar -xvzf backup.tar.gz  | Extrae un archivo tar.gz
gzip | comprime archivos individuales
gunzip | descomprime archivos
gzip archivo.txt  | Comprime archivo.txt a archivo.txt.gz
gunzip archivo.txt.gz  | Descomprime archivo.txt.gz a archivo.txt
gzip -d archivo.txt.gz  | Alternativa a gunzip para descomprimir
gzip -9 archivo.txt  | Máxima compresión
mv */ruta* */destino* | Mover o renombrar
rm | Eliminar
rm -rf | Forzar eliminacion de directorio
mkdir | Crear directorio
rmdir | Eliminar directorio vacio


## Información del sistema

Comando  | Descripción
------------- | -------------
who  | Muestra usuarios conectados 
who -u | Lista de usuarios
su *username* | Cambia al usuario indicado. Sino se indica, cambia a root
su -l *username* | Logear con usuario indicado
uname -a | Muestra información completa del sistema.
df -h  |  Muestra el espacio disponible en el disco.
du -sh *  | Muestra el tamaño de un directorio y su contenido.
free -h  |  Muestra el uso de memoria RAM.
top o htop  |  Muestra procesos en ejecución y uso de CPU/RAM.
ps aux  |  Lista todos los procesos en ejecución.
uptime  |  Muestra el tiempo de actividad del sistema.

## Find

Comando  | Descripción
------------- | -------------
find / | Busca en todo el sistema de archivos (puedes especificar otro directorio en lugar de / si lo deseas).
find / -type f | Filtra solo archivos (excluye directorios).
find -name "*.mp4" | Busca archivos con extensión .mp4
find -name "*.mp4" -size +100M | Filtra archivos mp4 con un tamaño mayor a 100MB
find / -type d | lista de todos los directorios presentes en tu sistema de archivo
find / -type f -name *fichero* | Busca fichero por nombre 


## Gestión de archivos y directorios

Comando  | Descripción
------------- | -------------
grep "texto" archivo.txt | Busca "texto" dentro de un archivo.
tar -cvf archivo.tar carpeta/ | Comprime una carpeta en un archivo .tar.
tar -xvf archivo.tar | Extrae un archivo .tar.
zip -r archivo.zip carpeta/ | Comprime una carpeta en .zip.
unzip archivo.zip | Extrae un archivo .zip.

## Usuarios

Comando  | Descripción
------------- | -------------
useradd *username* | Crea usuario
userdel *username* | Elimina usuario
addgroup *groupname* | Crea grupo
groupdel *groupname*  | Elimina grupo
usermod -l | Cambia nombre de usuario
usermod -d | Cambia el directorio de inicio del usuario
usermod -g | Cambia grupo del usuario
usermod -G | Añade usuario a grupos secundarios
chsh -l |
cat /etc/passwd | Usuarios creados
cat /etc/group | Lista de grupos

useradd -c "comentario" -u *id_user* -m -d *ruta*


Comando  | Descripción
------------- | -------------
-d  | Directorio 
-e<YYYMMMDD> | Fecha de deshabilitacion de cuenta
-f<dias> | Exira en x dias
-g | Grupo
-G *grupo1 grupo2* | 
-m | Crea directorio si no existe
-M  | No crea directorio
-p | 
-s | 
-u <id>| Id de usuario
-L | Bloquear usuario
-n | Cambia el nombre


## Contraseñas

Comando  | Descripción
------------- | -------------
passwd | Cambia contraseña del usuario actual
passwd *username* | Crea contraseña para usuario indicado
passwd -n 60  | Tiempo de vida minima de 60 dias 
passwd -x 90  | Tiempo de vida maxima de 90 dias 
passwd -w 10  | Advertencia de 10 dias antes de expiración
passwd -i 5 | Desactiva la cuenta 5 dias despues de caducidad
passwd -l *username* | Solo root. Bloquea usuario
passwd -u *username* | Solo root. Desbloquea usuario
passwd -d | Solo root. Elimina password
passwd -s | Solo root. Muestra información sobre el estado de la contraseña
cat /etc/shadow | Información de contraseñas
chage -l *username* | Ver info. valiosa del password


## Permisos

* R=4(Leer)
* W=2(Escribir)
* X=1(Ejecutar)

Comando  | Descripción
------------- | -------------
chmod 777 *archivo* | Otorga todos los permisos 
chmod -x *archivo* | Quita permiso de ejecución
chmod g-w *archivo* | Quita permiso de escribir al **grupo**
chmod g+rwx | Otorga permisos de lectura, escritura y ejecución al **grupo**
chmod a+rwx | Otorga todos los permisos a todos(a=all)

![Permisos](https://computernewage.com/wp-content/uploads/2015/06/representacion-permisos-en-linux1.png)

Comando  | Descripción
------------- | -------------
chown *username* *fichero* | Cambia propietario del fichero segun el usuario indicado (*chown = change owner*)
chown -R usuario:grupo carpeta/ | Cambia recursivamente el dueño de una carpeta y su contenido.
chgrp *group* *fichero* | Cambia grupo de archivo o directorio (*chgrp = change group*)
passwd -S usuario | Muestra el estado de la contraseña de un usuario.


## Iptables

Iptables es un sistema de firewall (bloquear acceso a usuarios no autorizados) vinculado al kernel de linux

* INPUT → Maneja paquetes dirigidos a la máquina.
* OUTPUT → Maneja paquetes salientes.
* FORWARD → Maneja tráfico que atraviesa la máquina (por ejemplo, en un router).

Comando  | Descripción
------------- | -------------
iptables -A | Agrega nueva regla
iptables -L | Lista reglas actuales
iptables -j *Acción* | ACCEPT/DROP/REJECT
iptables -D | Elimina regla
-i | Interfaz de entrada
-o | Interfaz de salida


Comando  | Descripción
------------- | -------------
ip a | Muestra las interfaces de red y direcciones IP.
netstat -tulnp | Muestra los puertos en uso y servicios activos.
iptables -L -v -n | Lista las reglas de firewall activas.
iptables -A INPUT -p tcp --dport 22 -j ACCEPT | Permite conexiones SSH en el puerto 22.
iptables -A INPUT -p tcp --dport 80 -j DROP | Bloquea conexiones en el puerto 80.
iptables -F | Borra todas las reglas activas.

```shell
iptables -A INPUT -p tcp --dport 22 -j ACCEPT  # Permite SSH
iptables -A INPUT -p icmp -j ACCEPT  # Permite ping
iptables -A OUTPUT -p tcp --dport 443 -j ACCEPT  # Permite tráfico HTTPS saliente
iptables -A FORWARD -p tcp --dport 80 -j ACCEPT  # Permite tráfico web que atraviesa la máquina


iptables -P INPUT DROP   # Bloquear todo el tráfico entrante por defecto
iptables -P FORWARD DROP  # Bloquear todo el tráfico reenviado
iptables -P OUTPUT ACCEPT  # Permitir todo el tráfico saliente


iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT  # Permite tráfico relacionado
```










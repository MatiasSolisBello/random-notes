# Apuntes de Linux

## Indice

[Comandos basicos](#comandos-basicos)

[Información del sistema](#información-del-sistema)

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
ls | Listar
man ls  | Info detallada
ls -l  | Usuario, grupo, archivo
ls -a  | Muestra todo
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
mv */ruta* */destino* | Mover o renombrar
rm | Eliminar
rm -rf | Forzar eliminacion de directorio
mkdir | Crear directorio
rmdir | Eliminar directorio vacio
chmod | Cambia los permisos de un archivo
chown *usuario:grupo fich* | chown *usuario:grupo fich*

opciones de find, lspci, uname


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

## Gestión de archivos y directorios

Comando  | Descripción
------------- | -------------
find /ruta -name "*.txt" | Busca archivos con extensión .txt.
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
chmod | Modifica permisos
chmod g+rwx | Otorga permisos de lectura, escritura y ejecución al grupo
chgrp | Cambia grupo de archivo o directorio
chown | Cambia usuario y grupo de archivo
chmod 755 archivo | Asigna permisos en formato numérico.
chown -R usuario:grupo carpeta/ | Cambia recursivamente el dueño de una carpeta y su contenido.
passwd -S usuario | Muestra el estado de la contraseña de un usuario.

![Permisos](https://computernewage.com/wp-content/uploads/2015/06/representacion-permisos-en-linux1.png)


## Iptables

Firewall: Bloquear acceso a usuarios no autorizados

Comando  | Descripción
------------- | -------------
ip a | Muestra las interfaces de red y direcciones IP.
netstat -tulnp | Muestra los puertos en uso y servicios activos.
iptables -L -v -n | Lista las reglas de firewall activas.
iptables -A INPUT -p tcp --dport 22 -j ACCEPT | Permite conexiones SSH en el puerto 22.
iptables -A INPUT -p tcp --dport 80 -j DROP | Bloquea conexiones en el puerto 80.
iptables -F | Borra todas las reglas activas.





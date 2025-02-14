# Apuntes de Linux

## Indice

[Comandos basicos](#comandos-basicos)

[Usuarios](#usuarios)

---

## Comandos basicos

Comando  | Descripción
------------- | -------------
pwd  | Directorio actual
cd | Mover a escritorio
cd .. | Volver
ls | Listar
man ls  | Info detallada
ls -L  | Usuarios y sus permisos
ls -l  | Usuario, grupo, archivo
ls -a  | Muestra todo
rwx  |  Permisos del directorio (Conexiones, Propietaio, Grupo del propietario)
d rwx  | Directorio
-rwx | Fichero o archivo
touch  | Crea archivos masivos
cat  | Visualizar contenido
more  | Visualizar parcializado
head  | Visualizar cabecera
tail   | Visualizar ultimas lineas
cp   | Copiar ficheros o drectorios(cp opcion /ruta_origen /destino)
mv | Mover o renombrar (v /ruta /destino)
rm | Eliminar
rm rf | Forzar, Solo root
rmdir | Eimminar directorio
chmod | Cambia los permisos de un archivo
chown *usuario:grupo fich* | Cambia el dueño un archivo

opciones de find, lspci, uname


## Usuarios

Comando  | Descripción
------------- | -------------
useradd *username* | Crea usuario
passwd *username* | Crea contraseña
userdel *username* | Elimimna usuario
addgroup *groupname* | Crea grupo
groupdel *groupname*  | Elimina grupo
usermod -g | Cambia grupo del usuario
usermod -G | Añade grupo a otro usuario


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
-u <id>|
-L | Bloquear usuario
-n | Cambia el nombre






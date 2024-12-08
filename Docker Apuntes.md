# Apuntes de Docker

## Indice

[¿Qué es docker?](#qué-es-docker)

[¿Por que usar Docker?](#por-que-usar-docker)

[Qué es una maquina virtual](#qué-es-una-maquina-virtual)

[Docker vs Maquinas virtuales](#docker-vs-maquinas-virtuales)

[¿Qué es un contenedor?](#qué-es-un-contenedor)

[Instalar docker](#instalar-docker)

[Gestión de contenedores](#gestión-de-contenedores)

[ Arquitectura de Docker](#arquitectura-de-docker)

## ¿Qué es docker?

Proyecto de codigo abierto que **automatiza el despliegue de aplicaciones dentro de contenedores**. Por contenedor, nos referimos a un "recipiente" que contiene todas las librerias y componentes necesarios de manera aislada para ejecutar el sofware y que puede ser transportado a cualquier computador.

## ¿Por que usar Docker?

* Portabilidad

* Aislamiento

* Eficiencia de recursos (en comparación con una maquina virtual)

## ¿Qué es una maquina virtual?

Una VM son **entornos de computación** (Sistema operativo, RAM, CPU, entre otros) completamente independientes y virtualizados que se ejecutan dentro de un **hipervisor**(supervisor encargado de crear VM) en un servidor fisico.

Por **virtualizacion** se entiende por la capacidad de crear varios entornos virtuales(VM)

## Docker vs Maquinas virtuales

La principal diferencia es el *uso del sistema operatiivo y el uso de recursos*:

![docker-vs-virtual-machine](https://guias.donweb.com/wp-content/uploads/2022/01/docker-vs-virtual-machine.png)

## ¿Qué es un contenedor?

Es una unidad de software ligera y portatil que encapsula una aplicación junto con todas sus dependencias y bibliotecas.

## Instalar docker

* **Requerimientos:**
  
  * WSL2
  
  * 64 bit de procesardor / 4 de RAM
  
  * Activar virtualización en BIOS: Admin. de tareas / Rendimiento / Virtualización
  
  * Panel de Control / Activar o desac. caract. de Windows / 
    
    * Habilitar *Subsistema de Windows para Linux* y *Virtual Machine Platform*

**Ejecutar primer contenedor**

* Los **contenedores** es una instancia en ejecución de una imagen. Es el entorno activo donde la aplicación funciona. Permite ejecutar procesos basados en la configuración de la imagen.

* Una **imagen** es una *plantilla* estática e inmutable que contiene todo lo necesario para ejecutar una aplicación, incluyendo el sistema operativo, las bibliotecas, las dependencias y el código de la aplicación. Sirve como base para crear contenedores. Las imagenes se almacenan en dockerHub.

Ejecutar imagen hello-world

```shell
docker run hello-world
```

Listar los contenedores

```shell
docker ps -a
```

**Gestión de imagenes en docker**

Lista de imagenes

```shell
docker images
```

Buscar una imagen

```shell
docker search nginx
```

Descargar imagen

```shell
docker pull nginx
```

Eliminar contenedor llamado hello-world

```shell
docker rm (nombre o id de contenedor)
docker rmi hello-world
```

## Gestión de contenedores

Poner "nombre" a contenedor

```shell
docker run --name contenedor1 hello-world
```

Inspeccionar contenedor

```shell
docker inspect hello-world
```

* Los nombres de los contenedores son unicos

Eliminar todos los contenedores

```shell
docker container prune
```

Trabaja de modo interativo y podras interactuar con el contenedor

```shell
docker run -it ubuntu
```

Siempre activo el contenedor(segundo plano)

```shell
docker run --name alwaysup -d ubuntu tail -f /dev/null
```

puerto de maquina:puerto de contenedor y eliminalo si se detiene

```shell
docker run -it --rm -d -p 8080:80 --name web nginx:latest
```

```shell
docker stop container-id
```

## Arquitectura de Docker

Docker daemon: Es el corazón de docker, gracias a el podemos administrar los contenedores, Esta herramienta tiene una REST API que se conecta con docker CLI. De esta forma podemos administrar los contenedores.

<img title="" src="https://arquitectoit.com/images/dockers/docker-engine-components.png" alt="https://arquitectoit.com/images/dockers/docker-engine-components.png" data-align="center" width="363">

**¿Qué es Dockerfile?**

Es un archivo de texto plano que contiene un conjunto de instrucciones que Docker utiliza para construir una imagen.

<img title="" src="https://miro.medium.com/v2/resize:fit:1400/0*CP98BIIBgMG2K3u5.png" alt="" data-align="center" width="613">

```dockerfile
# Indicamos la imagen que vamos a utilizar
FROM ubuntu:latest

# Ejecuta un comando para instaaer herramientas
RUN apt-get update && apt-get install -y curl wget vim git

# Carpeta de trabajo
WORKDIR /app

#Creamos un archivo de texto dentro del contenedor
RUN echo "¡Hola Docker!" > saludo.txt

# Ejecuta puerto 80
EXPOSE 80

# Solo puede existir un CMD 
CMD ["echo","Este es un contenedor de ejemplo"]
```

```shell
docker build -t ubuntu-new .
```

```shell
docker run -it -p 7070:70 ubuntu-new
/bin/bash
```

**Ejecutar contenedor**

```shell
docker run -d --name my-wea nginx:latest
docker exec -it my-wea ls /usr/share/nginx/html
```

**Docker Hub**

Es un repositorio de imagenes en Docker es un lugar donde puedes almacenar y compartir imagenes de contenedores de Docker

```shell
docker login
docker images

# Publicar repo
docker tag ubuntu-new my-username/repo-name
docke push my-username/repo-name


# Descargar repo
docker pull redis:latest
```

**Inspección y monitoreo de contenedores**

```shell
docker inspect container-name

# Ver logs en tiempo real
docker logs -f container-name

# Ver estadisticas de consumo de recursos
docker stats container-name
```

**Redes en Docker**

Las redes son una funcionalidad que permite la comuncación entre contenedores y/o el mundo exterior.

Listar redes (de la computadora)

```shell
docker network ls
```

Crear nueva red

```shell
docker network create my-network
```

```shell
docker network disconnect my-network
```

```shell
docker network rm my-network
```

**Volumenes y Bind Mounts**

En caso de que el contenedor tenga datos importantes que no queremos perder, y por error eliminamos el contenedor, debemos usar volumenes o Bind Mounts.

Los **volumenes** son el mecanismo preferido en producción para conservar los datos generados y utilizados por los contenedores Docker para guardarlos en un area de docker. 

Los **Bind Mounts** o montajes vinculados tienen una funcionalidad limitada en comparacion con los volumenes. Cuando utiliza un montaje de enlace, archivo o directorio en la maquina host se monta en el sistema de archivos (*Filesystem*) de contenedor, lo malo de esto, es que los datos quedan expuestos. Son perfectos para practicar.

<img title="" src="https://miro.medium.com/v2/resize:fit:746/1*bViAujGNZjJQrmhfN6IRsQ.png" alt="https://miro.medium.com/v2/resize:fit:746/1*bViAujGNZjJQrmhfN6IRsQ.png" data-align="center" width="520">

Ejemplo con mongo:

```shell
mkdir mongodb_data

# -v: crea volumen en x carpeta
docker run -d --name my-mongodb-container -v "/mongodb_data/:/datadb" mongo:latest

# Ejecutar comandos en el contenedor
docker exec -it my-mongodb-container bash

# Acceder a consola de mongo
mongosh

show databases
use dbprueba
db.users.insert({"name": "Frederick"})
db.users.find()
exit

# Detener y borrar contenedor
docker stop my-mongodb-container
docker rm my-mongodb-container
```

Ejemplo con MySQL:

```shell
docker run --name mysql-container -v "/mysql_bd:/var/lib/mysql" -e MYSQL_ROOT_PASSWORD -D mysql
docker exec -it mysql-container bash
mysql -u root -p
create database test1;
show databases;
exit
```

Ejemplo de volumen con mongo

```shell
docker volume create db_mongo
docker volume ls


docker run -d --name my-mongodb-container -mount src=db_mongo, dst=/data
```

**Docker Compose**

Herramienta que permite trabajar con multiples contenedores al mismo tiempo

docker-compse.yaml

```yaml
version: '3.8'

services:

  #Servicio para la base de datos
  db:
    image: mysql:latest
    environment:
      MYSQL_ROOT_PASSWORD: example
      MYSQL_DATABASE: my_database
      MYSQL_USER: user
    volumes:
      - db_data:/var/lib/mysql
    networks:
      - backend

  #Servicio para la aplicación web
  web:
    image: nginx:alpine
    depends_on:
      - db
    ports:
      - "8080:80"
    volumes:
      - html_volume:/usr/share/nginx/html
      - config_volume:/etc/nginx/conf.d
    networks:
      - frontend
      - backend

volumes:
  html_volume:
  config_volume:
  db_data:

networks:
  frontend:
  backend:
```

```shell
# Ejecutar en carpeta del proyecto
docker-compose up -d
```

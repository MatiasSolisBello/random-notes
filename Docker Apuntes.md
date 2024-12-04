# Apuntes de Docker

**¿Qué es docker?**

Proyecto de codigo abierto que **automatiza el despliegue de aplicaciones dentro de contenedores**. Por contenedor, nos referimos a un "recipiente" que contiene todas las librerias y componentes necesarios de manera aislada para ejecutar el sofware y que puede ser transportado a cualquier computador.

**¿Por que usar Docker?**

* Portabilidad

* Aislamiento

* Eficiencia de recursos (en comparación con una maquina virtual)

**Antes de empezar ¿Qué es una maquina virtual?**

Una VM son **entornos de computación** (Sistema operativo, RAM, CPU, entre otros) completamente independientes y virtualizados que se ejecutan dentro de un **hipervisor**(supervisor encargado de crear VM) en un servidor fisico.

Por **virtualizacion** se entiende por la capacidad de crear varios entornos virtuales(VM)

**Docker vs Maquinas virtuales**

La principal diferencia es el *uso del sistema operatiivo y el uso de recursos*:

![docker-vs-virtual-machine](https://guias.donweb.com/wp-content/uploads/2022/01/docker-vs-virtual-machine.png)

**¿Qué es un contenedor?**

Es una unidad de software ligera y portatil que encapsula una aplicación junto con todas sus dependencias y bibliotecas.

**Instalar docker**

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

**Gestión de contenedores**

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
docker stop alwaysup
```

**Arquitectura de Docker**

Docker daemon: Es el corazón de docker, gracias a el podemos administrar los contenedores, Esta herramienta tiene una REST API que se conecta con docker CLI. De esta forma podemos administrar los contenedores.

![https://arquitectoit.com/images/dockers/docker-engine-components.png](https://arquitectoit.com/images/dockers/docker-engine-components.png)



**¿Qué es Dockerfile?**

Es un archivo de texto plano que contiene un conjunto de instrucciones que Docker utiliza para construir una imagen.

![](https://miro.medium.com/v2/resize:fit:1400/0*CP98BIIBgMG2K3u5.png)

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







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



```shell

```



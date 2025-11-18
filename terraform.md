# ¿Qué es Terraform?

Herramienta de infraestructura como código (IaC)  para **automatizar** la creación, gestión y configuración de **infraestructura** de manera declarativa.

[![Diagram](https://www.howtonetwork.com/wp-content/uploads/2024/09/1_ATNMu1nQTnIXauJYXlDDGw.png "Diagram")](https://www.howtonetwork.com/wp-content/uploads/2024/09/1_ATNMu1nQTnIXauJYXlDDGw.png "Diagram")

**Ejemplo:**
* Levantar servidor en EC2
* Instalar servidor don NGINX, abrir puerto 80 y 22 a todo el mundo

# Descargar Terraform
    winget install Hashicorp.Terraform
    terraform --version

Herramientas:
* AWS CLI
* Repositorio de GitHub
* Extensión de Terraform para VS Code (opcional)

Terraform lee automaticamente tods los archivos .tf del directorio. Es buena practica que el archivo se llame main.tf


# Provider
Un proveedor es un plugin que interactua con un servicio  API especifica de un proveedor de infraestructura (AWS, Azure, etc.).
```
provider "aws" {
	region = "us-east-1"
}
```
# Resource
Son la unidad basica de cinfiguración de Terraform
```
resource "aws_instance" "nginx-server" {
	ami = "ami-0440d3b780d96b29d"	#Amazon Linux 2023 AMI
	instance_type = "t3.micro"
}
```
# Comandos
```
terraform init	# Crea carpeta terraform con plugin para servidor
terraform plan 	# Genera plan de ejecución y muestra cambios
terraform apply	 # Aplica los cambios
terraform destroy
```

# Modificaciones

## NGINX
```
resource "aws_instance" "nginx-server" {
  ...
  
  # Instalar nginx
  user_data = <<-EOF
              #!/bin/bash
              sudo yum install -y nginx
              sudo systemctl enable nginx
              sudo systemctl start nginx
              EOF
}
```

## SSH KEY
```
ssh-keygen -t rsa -b 2048 -f "nginx-server.key"
```

```
resource "aws_instance" "nginx-server" {
  ...
  key_name = aws_key_pair.nginx-server-ssh.key_name
}

resource "aws_key_pair" "nginx-server-ssh" {
	key_name   = "nginx-server-ssh"
	public_key = file("nginx-server.key.pub")
}
```

## Security Group
```
resource "aws_security_group" "nginx-server-sg" {
	 name = "nginx-server-sg"
	 description = "Security group allowing SSH and HTTP access"
	
	# Reglas de entrada al puerto 22 y 80
	 ingress {
	 	from_port   = 22
		to_port     = 22
		protocol    = "tcp"
		cidr_blocks = ["0.0.0.0/0"]
	}

	ingress {
		from_port   = 80
		to_port     = 80
		protocol    = "tcp"
		cidr_blocks = ["0.0.0.0/0"]
	}
	
	# Regla de salida (0 = Todos los puertos)
	egress {
		from_port        = 0
		to_port          = 0
		protocol         = "-1"
		cidr_blocks      = ["0.0.0.0/0"]
	}
}
```

Recuerda asignar security group a la maquina
```
resource "aws_instance" "nginx-server" {
	...
	vpc_security_group_ids = [
		aws_security_group.nginx-server-sg.id
	]
}
```

## Tags

Agrega tags a todos los recursos y cambiales el nombre
```
resource "aws_instance" "nginx-server" {
	 tags = {
	 	Name        = "nginx-server-XX"
		Environment = "test"
		Owner       = "ariel.molina@caosbinario.com"
		Team        = "DevOps"
		Project     = "webinar"
	}
}
```

# Output
Mostrar información resultante por consola
```
output "server_public_ip" {
 	description = "Dirección IP pública de la instancia EC2"
 	value       = aws_instance.nginx-server.public_ip
}

output "server_public_dns" {
 	description = "DNS público de la instancia EC2"
 	value       = aws_instance.nginx-server.public_dns
}
```
Mostrar solo outputs
```
terraform output [output_name]
```

# Variables

Ejemplo: Crear variable para el ID de AMI
```
# Crea variable con  decrpción y valor por defecto
variable "ami_id" {
	description = "ID de la AMI para la instancia EC2"
	default     = "ami-0440d3b780d96b29d"
}

resource "aws_instance" "nginx-server" {
	ami = var.ami_id
	...
}
```

Concatenación:
```
variable "server_name" {
	description = "Nombre del servidor web"
	default     = "nginx-server"
}

resource "aws_key_pair" "nginx-server-ssh" {
	key_name = "${var.server_name}-ssh"
}
```

# Archivos
Todo codigo se debe dividir en archivos para mantenerlo limpio y ordenado.
Los archivos pueden ser:

* variables.tf
* providers.tf
* ec2.tf
* key.tf
* sg.tf
* outputs.tf
* terraform.tfvars: Asigna valores a variables distintas a la que estan por defecto

Pero ¿Que sucede si tengo variables distintas si es qa o produccion?

Debe existir un qa.tfvars ya que terraform.tfvars aplica solo para prod.
Si se quiere ejecutar la infraestructura para QA se debe ejecutar:

```
terraform plan --var-file=qa.tfvars
```

Pero **OJO**: Aun *NO* creamos 2 instancias (qa y prod). Eso se hace a continuación:

# Modulos
Forma de encapsular y reutilizar bloques de configuración

A partir de ahora, todos los archivos estaran dentro de a carpeta nginx_server_module

main.tf
```
terraform {
	backend "s3" {
		bucket         = "webinar-terraform-caosbinario-123asd123ad123asd"
		key            = "webinar-terraform/terraform.tfstate"
		region         = "us-east-1"
	}
}

####### modulos #######
module "nginx_server_dev" {
    source = "./nginx_server_module"

    ami_id           = "ami-0440d3b780d96b29d"
    instance_type    = "t3.medium"
    server_name      = "nginx-server-dev"
    environment      = "dev"
}

module "nginx_server_qa" {
    source = "./nginx_server_module"

    ami_id           = "ami-0440d3b780d96b29d"
    instance_type    = "t3.small"
    server_name      = "nginx-server-qa"
    environment      = "qa"
}

#######  output ####### 
output "nginx_dev_ip" {
	description = "Dirección IP pública de la instancia EC2"
	value       = module.nginx_server_dev.server_public_ip
}

output "nginx_dev_dns" {
	description = "DNS público de la instancia EC2"
	value       = module.nginx_server_dev.server_public_dns
}

output "nginx_qa_ip" {
	description = "Dirección IP pública de la instancia EC2"
	value       = module.nginx_server_qa.server_public_ip
}

output "nginx_qa_dns" {
	description = "DNS público de la instancia EC2"
	value       = module.nginx_server_qa.server_public_dns
}
```
**OJO: POR CADA MODULO CREADO HAY QUE EJECUTAR 'terraform init'**

# Archivo de estado
Es un archivo .tfstatee que registra el estado actual de la infraestructura.
**No es bueno almacenarla en tu maquina local, sino que en S3**

* Crear bucket S3

main.tf
```
terraform {
	backend "s3" {
		bucket         = "bucket_name"
		key            = "project_name/terraform.tfstate"
		region         = "us-east-1"
	}
}
```
**OJO: POR CADA MODULO CREADO HAY QUE EJECUTAR 'terraform init'**

# Importar
Podemos importar recursos ya existentes (EC2) para gestionarlos desde Terraform
```
terraform import [nombre] [instance_id]
terraform state show [nombre]
```
Hace aproximadamente un mes, comencé a estudiar para rendir el examen AWS Certified Cloud Practitioner CLF-C02. Durante este proceso, encontré múltiples conceptos que pueden prestarse a confusión, ya sea por sus nombres similares o porque sus nombres no reflejan con precisión su funcionalidad. Este post tiene como objetivo resumir brevemente los conceptos que, desde mi experiencia, resultaron más difíciles de entender o memorizar.

## Security Groups vs NACL

Vamos con un concepto de seguridad de red, los security groups y los NACL (Listas de Control de Acceso a la Red) son muy fáciles de confundir puesto que cumplen la misma función, pero en realidad operan en distintos niveles de la red.

Por un lado, los **Security Group** son firewalls virtuales, que se aplican a nivel de <u>instancia</u> y solo permiten reglas de permitir. No requieren configurar denegaciones ni salidas manuales para respuestas.

En cambio, los **NACLs** son firewalls a nivel de <u>subred</u>, es decir, permiten tanto reglas de permitir como de denegar tráfico. Son útiles para bloquear direcciones IP específicas de forma general para todos los recursos dentro de una subred.


## GuardDuty vs Amazon Inspector

Vamos con conceptos de seguridad nativos de AWS, GuardDuty y Amazon Inspector son muy similares, ambos realizan análisis automatizados, pero se diferencian en lo que analizan.

Por un lado, **GuardDuty** hace análisis de los registros de AWS para <u>identificar comportamientos sospechosos (amenazas)</u>, por ejemplo, detecta un escaneo de puertos desde una IP externa hacia una instancia EC2 y genera una alerta automática para investigar el incidente.

En cambio, **Amazon Inspector** hace análisis automatizados de <u>vulnerabilidades en recursos desplegados en AWS</u>, por  ejemplo, una organización detecta y corrige una vulnerabilidad crítica en una imagen de contenedor antes de su paso a producción.

## CloudTrail vs CloudWatch vs CloudFront

CloudTrail, CloudWatch y CloudFront son tres servicios cuyos nombres similares pueden llevar a confusión, aunque sus propósitos son muy distintos:

**CloudTrail** se encarga de <u>registrar todas las acciones realizadas en una cuenta de AWS</u>, como llamadas a la API, indicando quién hizo qué, cuándo y desde dónde. Por ejemplo: registrar quién eliminó una instancia EC2 o modificó una política IAM.

**CloudWatch** se enfoca en el <u>monitoreo de métricas, logs, alarmas y eventos en los recursos de AWS</u>. Por ejemplo, puede generar una alerta si el uso de CPU de una instancia EC2 supera el 80%.

**CloudFront** es un servicio de distribución de contenido (CDN) que mejora el rendimiento al entregar contenido desde ubicaciones geográficas cercanas al usuario final, mediante el almacenamiento en caché, ya sea desde buckets S3 u orígenes personalizados como servidores web.


## AWS Site-to-Site vs AWS Direct Connect

Ambos conceptos son formas de conectarse y acceder a los servicios de AWS en un entorno de nube híbrida.

Por un lado, **VPN (AWS Site-to-Site)** es un túnel cifrado que conecta una red local con una VPC (Virtual Private Cloud) <u>mediante internet</u>, lo que implica mayor latencia e inseguridad inherente al medio.

Por otro lado, **AWS Direct Connect** es una conexión entre una red local y los servicios de AWS mediante un cable de <u>fibra óptica, es decir, sin internet</u>. Especialmente útil para flujos críticos de datos por su conexión dedicada, más estable y con menor latencia.


##Conclusión

A la hora de preparar el examen AWS Cloud Practitioner, no basta con memorizar definiciones: muchos conceptos suenan parecidos, hacen cosas diferentes o sus nombres no reflejan claramente su propósito. 

Personalmente, estos fueron algunos de los que más me costó diferenciar y que más fácilmente se olvidan si no se entienden a fondo.

Mi recomendación es que no te limites a estudiar con tarjetas de memoria (flashcards), sino que busques entender el "para qué" de cada servicio, lo relaciones con casos de uso reales, y sobre todo, lo compares activamente con otros servicios similares. Eso ayuda no solo a aprobar el examen, sino también a aplicar ese conocimiento en proyectos reales en la nube.

Si este resumen te fue útil, compártelo con quienes también estén preparando la certificación. ¡Y no dudes en comentar qué conceptos se te hicieron más difíciles!

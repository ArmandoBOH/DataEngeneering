# Primera Entraga
[Volver](../README.md)

## Como Ejecutar:

### Ejecutar con Docker Compose (RECOMENDADO)
  ##### Se requiere tener instalado docker y docker compose.
  
  Ubicarse en el directorio PrimeraEntrega y ejecutar el siguiente comando: 
  
  ```Bash
    docker compose up
  ```
  Recuerde borrar las imagenes con `docker rmi <image_name> -f` para liberar recursos.

### Ejecutar script 
Para ejecutar el script directamente se deben realizar los siguientes pasos:

1. Instalar las librerias
```Bash
  pip install --no-cache-dir -r requirements.txt 
```

2. Agregar las variables de entorno dependiendo de su ambiente:
   - Linux:
     ```Bash
       export DB_HOST=data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com DB_NAME=data-engineer-database DB_PASSWORD=25eE08PxcY DB_PORT=5439 DB_USER=armandorafaelbohorquez_coderhouse DEBUG=FALSE
     ```
   - Windows(PowerShell):
       ```PowerShell
             $env:DB_HOST = "data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com" 
             $env:DB_NAME = "data-engineer-database" 
             $env:DB_PASSWORD = "25eE08PxcY" 
             $env:DB_PORT = "5439" 
             $env:DB_USER = "armandorafaelbohorquez_coderhouse" 
             $env:DEBUG = "FALSE"
       ```
   - Pycharm
       ```
         DB_HOST=data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com;DB_NAME=data-engineer-database;DB_PASSWORD=25eE08PxcY;DB_PORT=5439;DB_USER=armandorafaelbohorquez_coderhouse
       ```

3. Ejecutar el script dentro del direcotorio ./PrimeraEntrega/app/src/

    ```Bash
      python main.py
    ```
    Tambien puede utilizar Pycharm. 




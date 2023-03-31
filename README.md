# 🐍 supermetrics_apis: Automatización de las APIS de SuperMetrics (Python / Flask)

## 💻 Instalación

Recomiendo utilizar un entorno virtual (virtualenv) para ejecturar este proyecto y no tener problemas de dependencias.

Para ejecutar el proyecto, es necesario clonar el repositorio:

```
git clone https://github.com/oscarwol/supermetrics_apis
cd supermetrics_apis
virtualenv -p python3 .
cd Scripts
activate
cd..
```

Despues, es necesario utilizar el gestor de paquetes de Python (PIP) [pip](https://pip.pypa.io/en/stable/) para instalar todas las dependencias y requerimientos necesarios para ejecutar el proyecto, estos se encuentran en el archivo "requirements.txt".

```
pip install -r requirements.txt
```

## 💾 Creando la Base de datos:
Para este proyecto se utilizo 'SQLAlchemy' un ORM desiñado para flask, el ORM apunta a una base de datos ya creada, en este repositorio encontrarás un backup de la esctructura de la DB, puedes montarla en el localhost y funcionará correctamente.

Se debe configurar a donde apuntará la DB, eso se hace en la siguiente línea de código:

```
12. url = url = "mysql+pymysql://root:pass@localhost:3306/supermetrics_api"
```
Para configurar la base de datos, ver el ejemplo de arriba y seguir la nomenclatura de datos descrita a continuación:

Usuario: root
Contraseña: pass
Servidor: localhost
Base de datos: supermetrics_api"


## 🚀 Iniciar el Proyecto
Una vez creado el entorno virtual, ejecutado e instaladas todas las dependencias y requerimientos, el proyecto puede ser ejecutado simplemente con la siguiente línea:
```
python api.py 
```


## ⚙️ Uso:

```
localhost:5000 (El puerto puede cambiarse de ser necesario)
```

El sistema cuenta con 7 'Endpoints' diferentes: 

| HTTP Type | Path | Used For |
| --- | --- | --- |
| `GET` | /google | Registra los datos del endpoint de Google en la base de datos|
| `GET` | /linkedin | Registra los datos del endpoint de Linkedin en la base de datos|
| `GET` | /fb-campana | Registra los datos del endpoint de FB-CAMPANA en la base de datos|
| `GET` | /fb-region | Registra los datos del endpoint de FB-REGION en la base de datos|
| `GET` | /fb-edad-gen | Registra los datos del endpoint de FB-EDAD-GEN en la base de datos|
| `GET` | /fb-platafomra | Registra los datos del endpoint de FB-PLATAFORMA en la base de datos|
| `GET` | /fb-anuncio | Registra los datos del endpoint de FB-ANUNCIO en la base de datos|
| `GET` | /bulk | (SOLO TEST) Registra Todos los datos anteriores al mismo tiempo|
| `GET` | /reverse | (SOLO TEST) Borra todos los datos de la DB correspondientes al dia de hoy|

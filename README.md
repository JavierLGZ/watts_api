# Watts app

Es un Entrypoint diseñado para medir tu consumo neto de tu factura eléctrica.
Tomando los datos que genera tu medidor inteligente podrás llevar al detalle cuánta electricidad utilizas a lo largo del día, a la semana o al mes.


## tecnologías Empleadas

**Server:** Python: django, django REST framework

**DataBases:** PostgresQL, Sqlite3

## Caracteristicas incluidas

- un despliegue por medio de docker-compose utilizando como base de  datos postgres
- un revisor de estilo automatico integrado a git para antes de cada commit


## API Reference

#### Get Consumo de electricidad

```http
  GET /consume/?date=yyyy-mm-dd&period=[daily, weekly, monthly]
```

| Parameter | Type     | Description                |
| :-------- | :------- | -------------------------- |
| `date`    | `string` | **Optional**. se toma como referencia para devolver los datos del consumo del dia por horas o diario si es semanal o mensualmente **Default:** la fecha actual|
| `period`  | `string` | **Optional**. escoge el periodo de consumo. Si es diario devolverá el consumo por horas. semanal y mensualmente el consumo será por dia **Default:** Daily|


## Pruebas en local

clona el proyecto

```bash
  git clone https://github.com/JavierLGZ/watts_api.git
```

ve al directorio del proyecto

```bash
  cd watts_api
```

Instalar la librería de entornos virtuales

```bash
  python -m pip install venv
```

generar un entorno virtual

```bash
  python -m venv venv
```

iniciar el entorno virtual

```bash
  source venv/bin/activate
```

isntalar las dependencias necesarias

```bash
  pip install -r requirements.txt
```

iniciar el proyecto

```bash
  python manage.py makemigrations
  python manage.py migrate
  python excel_to_json.py
  python manage.py loadddata fixture.json
  python manage.py runserver
```

en la direcion **127.0.0.1:8000/consume** se podran hacer las cosultas.

detener el proyecto y el entorno virtual

```bash
  Ctrl + c
  deactivate
```

## Testing

para correr las pruebas  se debe usar el siguiente comando

```bash
  python manage.py test
```

de manera automática cargará los datos proporcionados en el excel


## Variables de entorno

Para iniciar el proyecto en docker y poder utilizar la base de datos de postgres se requieren de variables que deben guardarse en un archivo .env

`SECRET_KEY`

`SQL_ENGINE`

`SQL_DATABASE`

`SQL_USER`

`SQL_PASSWORD`

`SQL_HOST`

`SQL_PORT`


## Despliegue

Para el Despliegue se requiere tener instalado docker y docker-compose, en un entorno de windows estos dos componentes vienen incluidos en la aplicación de Docker Desktop así que solo con instalar esta ya es suficiente.

al ubicarnos en la carpeta del proyecto y en el archivo .env retiramos los comentarios de las variablesque requiere postgres para funcionar

Luego de eso ejecutamos en siguiente comando;

```bash
  docker-compose up
```
 el programa ya se encargará de la construcción de la imagen para el proyecto y de la descarga de la imagen de postgresql para usarla como base de datos

## Ejemplos

para obtener el consumo mensual basta con poner como fecha cualquier día del mes y poner como periodo monthly

```bash
  curl http://127.0.0.1:8000/consume/?date=2022-10-31&period=monthly
  >>>   [{"meter_date":"2022-10-31 00:00:00","value":1.7099600000001374},{"meter_date":"2022-10-31 01:00:00","value":1.8408199999994395},   {"meter_date":"2022-10-31 02:00:00","value":2.35157000000072},
        {"meter_date":"2022-10-31 03:00:00","value":3.4833999999991647},{"meter_date":"2022-10-31 04:00:00","value":3.068360000001121},{"meter_date":"2022-10-31 05:00:00","value":3.125},
        {"meter_date":"2022-10-31 06:00:00","value":3.1474600000001374},{"meter_date":"2022-10-31 07:00:00","value":3.285149999999703},{"meter_date":"2022-10-31 08:00:00","value":2.8623099999986152},{"meter_date":"2022-10-31 09:00:00","value":3.50097999999889},
        {"meter_date":"2022-10-31 10:00:00","value":2.9208999999991647},{"meter_date":"2022-10-31 11:00:00","value":4.088869999999588},{"meter_date":"2022-10-31 12:00:00","value":3.092769999999291},{"meter_date":"2022-10-31 13:00:00","value":4.0898400000005495},
        {"meter_date":"2022-10-31 14:00:00","value":3.8339900000009948},{"meter_date":"2022-10-31 15:00:00","value":4.331060000000434},{"meter_date":"2022-10-31 16:00:00","value":0},{"meter_date":"2022-10-31 17:00:00","value":0},{"meter_date":"2022-10-31 18:00:00","value":0},{"meter_date":"2022-10-31 19:00:00","value":0},{"meter_date":"2022-10-31 20:00:00","value":0},
        {"meter_date":"2022-10-31 21:00:00","value":0},{"meter_date":"2022-10-31 22:00:00","value":0},{"meter_date":"2022-10-31 23:00:00","value":0}]
```

por defecto la api devolverá el consumo del dia de la fecha de hoy

```bash
  curl http://127.0.0.1:8000/consume/
  >>>>  [{"meter_date":"2022-12-08 00:00:00","value":0},{"meter_date":"2022-12-08 01:00:00","value":0},{"meter_date":"2022-12-08 02:00:00","value":0},{"meter_date":"2022-12-08 03:00:00","value":0},{"meter_date":"2022-12-08 04:00:00","value":0},{"meter_date":"2022-12-08 05:00:00","value":0},{"meter_date":"2022-12-08 06:00:00","value":0},
        {"meter_date":"2022-12-08 07:00:00","value":0},{"meter_date":"2022-12-08 08:00:00","value":0},{"meter_date":"2022-12-08 09:00:00","value":0},{"meter_date":"2022-12-08 10:00:00","value":0},{"meter_date":"2022-12-08 11:00:00","value":0},{"meter_date":"2022-12-08 12:00:00","value":0},{"meter_date":"2022-12-08 13:00:00","value":0},
        {"meter_date":"2022-12-08 14:00:00","value":0},{"meter_date":"2022-12-08 15:00:00","value":0},{"meter_date":"2022-12-08 16:00:00","value":0},{"meter_date":"2022-12-08 17:00:00","value":0},{"meter_date":"2022-12-08 18:00:00","value":0},{"meter_date":"2022-12-08 19:00:00","value":0},{"meter_date":"2022-12-08 20:00:00","value":0},
        {"meter_date":"2022-12-08 21:00:00","value":0},{"meter_date":"2022-12-08 22:00:00","value":0},{"meter_date":"2022-12-08 23:00:00","value":0}]
```

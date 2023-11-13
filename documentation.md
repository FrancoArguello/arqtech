creamos el entorno virtual con virtualenv
pip install virtualenv
virtualenv env
desde la consola entramos a la carpara env, ahi a la carpeta scripts y ahi colocamos activate y enter

###########################################################################################################################
instalamos todas las dependencias que vamos a utilizar que estan listados en requirements.txt
desde nuestra raiz ejecutamos
pip install -r requirements.txt

###########################################################################################################################
creamos un archivo git ignore y vamos a ir colocando ahi los elementos de nuestro proyecto que no queremos que se pusheen a nuestro repo de github

###########################################################################################################################
creamos el proyecto de django con django-admin startprojects arqtech
creamos las apps que necesitemos

###########################################################################################################################
creamos una carpeta llamada templates que ahi es donde vamos a alojar todos los templates de nuestro proyecto
dentro de esa carpeta creamos el archivo base.html
modificamos en el archivo setting.py en el apartado de template colocamos 'DIRS': [os.path.join(BASE_DIR,'templates')],

###########################################################################################################################
instalamos postgresSql
creamos una base de datos con el nombre de nuestro proyecto
en el archivo setting.py en el apartado de databases modificamos los datos colocando
DATABASES = {
'default': env.db("DATABASE_URL", default="postgres://arqtech"),
}
DATABASES['default']["ATOMIC_REQUESTS"] = True
que va a hacer referencia a nuestra base de datos PostgresSql, y DATABASE_URL es la variable que va a contener nuestros datos sensibles de ingreso a la DB que eso lo vamos a colocar en el archivo .env
DATABASE_URL=postgres://postgres:password@127.0.0.1:5432/nombreDB

###########################################
instalamos argon2-cffi y argon2-cffi-bindings para el encriptado de contraseñas, y en setting.py agregamos lo siguiente par poder trabar con contraseñas seguras

PASSWORD_HASHERS = [
"django.contrib.auth.hashers.Argon2PasswordHasher",
"django.contrib.auth.hashers.PBKDF2PasswordHasher",
"django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
"django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

#################################################3
instalamos pip install openpyxl para poder trabajar el formulario y luego poder descargarlo en un archivo de excel

###########################################
agregamos LOGIN_REDIRECT_URL = 'nombre de la url del template que queremos que ir' en nuestro archivo de setting para que una vez logueado el usuario lo re dirija automaticamente al template del index.

###########################################


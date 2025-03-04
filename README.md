# Proyecto de ciberseguridad (phishing en correos electronicos)
El phishing es una técnica utilizada por los ciberdelincuentes que consiste en engañar a las personas haciéndose pasar por una empresa o servicio de confianza
Existen múltiples tipos de Phishing, uno de los más comunes es aquel realizado a través de emails
Los estafadores se hacen pasar por compañias reales y suelen engañar al usuario a través del envio de enlaces maliciosos, suelen preguntar por datos personales o datos bancarios, que al ingresarlos son robados


# Design Thinking

## Empatizar

#### 1. ¿Quienes son los usuarios?
Los usuarios pueden dividirse en varios grupos según su perfil y nivel de riesgo:

1. ```Empleados de empresas``` - Especialmente aquellos que manejan información sensible (ejecutivos, recursos humanos, finanzas, TI).
2. ```Usuarios de correo personal``` - Personas que usan servicios de correo como Gmail, Outlook o Yahoo y pueden ser víctimas de ataques de phishing.
3. ```Administradores de seguridad informática``` - Profesionales encargados de proteger la infraestructura tecnológica de una organización contra ataques.
4. ```Pequeñas y medianas empresas (PyMEs)``` - Negocios con menos recursos en ciberseguridad y mayor riesgo de caer en fraudes.
5. ```Instituciones gubernamentales y educativas``` - Objetivo frecuente de ataques dirigidos para robo de información o fraude.

#### 2. ¿Que les importa?
Estar comodos y seguros al momento de usar sus dispositivos:

1. ```Protección de datos personales y financieros``` - Evitar el robo de información sensible o acceso no autorizado.
2. ```Evitar fraudes y pérdidas económicas``` - Phishing puede llevar a estafas con consecuencias financieras graves.
3. ```Seguridad en su entorno laboral``` - Empresas buscan proteger a sus empleados y prevenir brechas de seguridad.
4. ```Conciencia y educación sobre phishing``` - Muchas personas desconocen los riesgos y cómo identificar correos fraudulentos.
5. ```Facilidad y accesibilidad de la solución``` - Herramientas o capacitaciones deben ser intuitivas y fáciles de implementar.

#### 3. ¿Como me identifico?
Somos un equipo comprometido con la seguridad digital y la educación interactiva. Nos identificamos como un grupo de diseñadores, desarrolladores y expertos en ciberseguridad que buscamos crear una solución accesible y efectiva para ayudar a las personas a identificar intentos de phishing.

Nuestro enfoque es centrado en el usuario, entendiendo sus preocupaciones y necesidades para diseñar una experiencia de aprendizaje dinámica y práctica. Trabajamos de manera colaborativa, combinando diferentes habilidades para construir una solución innovadora y funcional.



## Definir

#### 1. ¿Que quieren los usuarios?
Los usuarios buscan una solución que les permita aprender a identificar intentos de phishing de manera clara, práctica y sin complicaciones. 
Los Usuarios Quieren:

1. ```Un método de aprendizaje interactivo y accesible que no requiera conocimientos técnicos avanzados.```
2. ```Simulaciones de correos fraudulentos para practicar en un entorno seguro.```
3. ```Guías y recomendaciones en tiempo real para mejorar su capacidad de identificación.```
4. ```Protección y confianza en el uso de sus dispositivos personales y corporativos.```
5. ```Una plataforma intuitiva y fácil de usar, con elementos de gamificación para hacer el aprendizaje más dinámico y motivador.```

#### 2. ¿Qué podemos construir?
Podemos desarrollar una plataforma educativa interactiva que enseñe a los usuarios a identificar y responder correctamente a intentos de phishing. La plataforma podría incluir:

1. ```Correos cebo``` - Simulación de correos de phishing para que los usuarios practiquen su detección.
2. ```Evaluaciones interactivas``` - Cuestionarios y retos para medir el aprendizaje.
3. ```Recomendaciones en tiempo real``` - Explicaciones sobre qué elementos analizar en un correo sospechoso.
4. ```Reportes y seguimiento``` - Historial de respuestas para ver el progreso del usuario.
5. ```Gamificación``` - Puntos y recompensas para motivar el aprendizaje.

#### 3. ¿Cómo interpreto?
1. ```Patrones de error``` - Analizar en qué tipos de correos los usuarios fallan más.
2. ```Evolución del aprendizaje``` - Comparar respuestas antes y después de la capacitación.
3. ```Tiempo de respuesta``` - Evaluar si el usuario identifica rápidamente señales de phishing.


# Firebase4
Uso de la libreria P4


## 0.1 Crear ambiente virtual

```bash
python3 -m venv .hola
```

```gitignore
*.pyc
_pycache_/
.venv/
```

## 1. Activar el ambiente virtual

```bash
source .hola/bin/activate
```

```bash
deactivate
```

## 1.5 Instalar librerias

```shell
python -m pip install --upgrade pip
```

```shell
pip install pyrebase4
pip install setuptools
```

```shell
pip freeze > requirements.txt
```

```shell
python -V > runtime.txt
```

### Manejo de Gits

```shell
git add .
git commit -m  ""
git push -u  origin main

git pull origin main
git pull --rebase origin main
```

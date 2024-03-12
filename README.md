# DESAFIO CODE LEAP

Desafio de back end da codeleap

# Como rodar

Você primeiramente deve criar um virtual env:

```shell
//windows
virtualenv env

//Linux
python -m venv env
``` 

Agora ative:

```shell
//linux
source env/bin/activate

//Windows
env/Scripts/Activate
```

Baixe as dependencias:

```shell
pip install -r poetry.lock
```

Entre na pasta codeleap e rode:

```shell
python manage.py runserver
```

Qualquer problema ocorrido pode ser problema com a compatibilidade entre OS, esse script foi feito em Linux, caso tenha problemas no windows, rode no linux, por favor! :) 
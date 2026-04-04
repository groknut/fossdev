
# mini-http

Минимальный HTTP-сервер на порту 8080.

## Установка
```bash
pip install --index-url https://test.pypi.org/simple/ mini-http
```

## Использование
```bash
python -c "import mini_http; print('OK')"
```

## Самостоятельная сборка пакета

Для автоматической публикации проекта на [test.pypi](https://test.pypi.org/) необходимо создать `.pypirc` файл и заполнить следующим содержимым:
```
[distutils]
index-servers =
    testpypi

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-token
```

Затем выполните
```bash
make publish
```

Проект автоматически опубликуется в репозитории.

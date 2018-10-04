# IdentificacaoVeicular

API Restful desenvolvida em Flask para reconhecimento de placas.

## Estrutura do repositorio

`datase_utils/`: Diretorio contendo notebooks para auxilio no desenvolvimento do dataset
`IV-Flask/`: Principal diretorio do repositorio, onde se encontra o projeto da API

`api_post.ipynb`: Notebook com exemplo de acesso a API

## Python Version

Python 3.6.3

## Build Python Env (local)

```
cd IV-Flask

pip3 install -r requirements.txt
```
## Executar a aplicacao

```
cd IV-Flask

invoke iv
```

### Bugs conhecidos

A API conta com o uso do Swagger, entretanto o post de imagens via swagger possui um bug que impossibilita seu uso 
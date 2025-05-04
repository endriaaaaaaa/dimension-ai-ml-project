# Documentación del Entorno de Desarrollo

## Requisitos del Sistema
- Python 3.9+
- Docker (opcional para contenedores)
- macOS (ambos desarrolladores)

## Entorno Virtual
Este proyecto utiliza `venv` para gestionar dependencias. Para configurar:

```bash
python -m venv env
source env/bin/activate  # En macOS/Linux
pip install -r requirements.txt
```

## Dependencias
Todas las dependencias están especificadas en `requirements.txt` con versiones exactas para garantizar la replicabilidad. Las principales bibliotecas utilizadas son:

- **Análisis de Datos**: numpy, pandas
- **Machine Learning**: scikit-learn, tensorflow
- **NLP**: nltk, spacy, transformers
- **API y Web**: flask, fastapi
- **Base de Datos**: sqlalchemy, pymongo

## Validación del Entorno
Para verificar que el entorno está correctamente configurado:

```bash
python scripts/validate_environment.py
```

## Variables de Entorno
Las variables de entorno se configuran en un archivo `.env` local. Ver `.env.example` para ejemplos.


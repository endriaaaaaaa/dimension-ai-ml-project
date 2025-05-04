# DIMENSION.AI ML Project

## Descripción
Este repositorio contiene el código e infraestructura para el proyecto de Machine Learning de DIMENSION.AI, enfocado en el análisis y predicciones para contenido en YouTube mediante técnicas avanzadas de análisis de datos y modelos predictivos.

## Objetivos del Proyecto
- Desarrollar modelos predictivos para analizar tendencias en YouTube
- Implementar pipeline de datos desde APIs externas
- Crear dashboard interactivo para visualización de resultados
- Automatizar procesos de reentrenamiento y actualización de modelos

## Estructura del Proyecto
```
dimension-ai-ml-project/
├── .github/           # Configuración de GitHub
├── config/            # Archivos de configuración
├── docs/              # Documentación
├── notebooks/         # Jupyter Notebooks
├── scripts/           # Scripts útiles
├── src/               # Código fuente
│   ├── data/          # Módulos para manejo de datos
│   ├── models/        # Modelos de ML
│   ├── visualization/ # Visualización de datos
│   └── api/           # APIs y endpoints
├── tests/             # Tests
├── .gitignore         # Archivos ignorados por Git
├── Dockerfile         # Configuración de Docker
├── requirements.txt   # Dependencias
└── setup.py           # Instalación del paquete
```

## Configuración del Entorno de Desarrollo

### Requisitos previos
- Python 3.9+
- Conda o venv para gestión de entornos virtuales
- Git para control de versiones
- Docker (opcional)

### Pasos para configurar el entorno

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/usuario/dimension-ai-ml-project.git
   cd dimension-ai-ml-project
   ```

2. Configurar entorno virtual:
   ```bash
   # Con Conda:
   conda create -n dimension-ai python=3.9
   conda activate dimension-ai
   
   # O con venv:
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

4. Configurar variables de entorno:
   ```bash
   cp .env.example .env
   # Editar .env con tus credenciales
   ```

5. Verificar instalación:
   ```bash
   python scripts/validate_env.py
   ```

## Plan de Fases del Proyecto

### Fase 1: Preparación Técnica e Infraestructura (1-14 mayo)
- Configuración del entorno de desarrollo
- Implementación de sistemas de almacenamiento
- Configuración de acceso a APIs

### Fase 2: Recolección y Análisis de Datos (15-28 mayo)
- Desarrollo de pipeline ETL
- Análisis exploratorio
- Creación de dashboard inicial

### Fase 3: Desarrollo de Modelos Predictivos (29 mayo - 11 junio)
- Feature engineering
- Entrenamiento de modelos
- Optimización de hiperparámetros

### Fase 4: Operacionalización y Automatización (12-25 junio)
- Implementación de API
- Automatización de reentrenamiento
- Despliegue de dashboard interactivo

### Fase 5: Documentación y Presentación (26 junio - 7 julio)
- Documentación técnica
- Manual de usuario
- Presentación final

## Flujo de Trabajo con Git

- La rama principal es `main`
- El desarrollo se realiza en la rama `develop`
- Para nuevas funciones, crear ramas desde `develop` con el formato `feature/nombre-funcionalidad`
- Los pull requests requieren revisión de código antes del merge

## Herramientas y Tecnologías

- **Análisis de Datos**: Pandas, NumPy, SciPy
- **Visualización**: Matplotlib, Seaborn, Plotly, Tableau/Power BI
- **Machine Learning**: Scikit-learn, XGBoost, TensorFlow/PyTorch
- **APIs**: YouTube Data API, SocialBlade API
- **Backend**: FastAPI, Flask
- **Bases de Datos**: PostgreSQL, MongoDB
- **Orquestación**: Apache Airflow
- **Tracking de Experimentos**: MLflow
- **Despliegue**: Docker, GitHub Actions

## Colaboradores
- Desarrollador 1 (Enfoque en Infraestructura)
- Desarrollador 2 (Enfoque en APIs y Data)

## Licencia
Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

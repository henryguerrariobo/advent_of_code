# 📊 Proyecto de Ciencia de Datos: advent_of_code

<div align="center">

  <!-- Estado del Proyecto -->
  <a href="#">
    <img src="https://img.shields.io/badge/Estado-En%20desarrollo-yellow" alt="Estado del Proyecto">
  </a>

  <!-- Porcentaje de Avance -->
  <a href="#">
    <img src="https://img.shields.io/badge/Progreso-0%25-red" alt="Porcentaje de Avance">
  </a>

  <!-- Documentación -->
  <a href="#">
    <img src="https://img.shields.io/badge/Documentación-Pendiente-orange" alt="Estado de la Documentación">
  </a>
</div>

<div align="center">
   <!-- Checked with mypy -->
  <a href="https://mypy-lang.org/">
    <img src="https://www.mypy-lang.org/static/mypy_badge.svg" alt="Checked with mypy">
  </a>

  <!-- Code style: black -->
  <a href="https://github.com/psf/black">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black">
  </a>

  <!-- Linting: Ruff -->
  <a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json" alt="Linting: Ruff">
  </a>

 <!-- Security: Bandit -->
  <a href="https://bandit.readthedocs.io/en/latest/">
    <img src="https://img.shields.io/badge/security-bandit-green" alt="Security: Bandit">
  </a>

</div>

## 1. Descripción General del Proyecto

**Descripción del proyecto**: Añadir aquí la descripción específica de tu proyecto de análisis de datos.

- **Responsable del Desarrollo**: Henry Guerra

- **Auditor/Cliente Responsable**: _[Nombre del responsable]_

- **Última Actualización**: _[Fecha de última actualización]_

---

## 2. Reportes Utilizados

Descripción de los reportes que se utilizan regularmente para realizar el análisis.

| Nombre del Reporte | Descripción | Origen de Datos | Frecuencia de Actualización |
| ------------------ | ----------- | --------------- | --------------------------- |
| **[Nombre]**       | [Descripción del reporte] | _[Sistema origen]_ | [Frecuencia] |

---

## 3. Funcionamiento Básico

A continuación, se detalla el funcionamiento básico del proyecto:

- **Herramientas/Software**: Python, uv, Polars, Pydantic
- **Flujo de Trabajo**:
  1. **Carga de Datos**: Se cargan los datos desde las fuentes configuradas.
  2. **Procesamiento y Limpieza**: Se procesan y limpian los datos usando los módulos en `src/advent_of_code/process/`.
  3. **Análisis**: Se ejecuta el análisis principal usando los módulos en `src/advent_of_code/analyze/`.
  4. **Exportación**: Se generan los reportes finales usando `src/advent_of_code/export/`.
  5. **Validación**: Se validan los resultados y se entregan al responsable.

---

## 4. Reportes de Resultados Generados

Descripción de los reportes generados después de completar el análisis.

**Reportes de Análisis**

| Nombre del Reporte | Descripción | Formato |
| ------------------ | ----------- | ------- |
| **[nombre].xlsx**  | [Descripción del análisis] | Excel |

---

## 5. 🚀 Configuración y Uso

### Prerrequisitos

- Python >= 3.11
- [uv](https://docs.astral.sh/uv/) para gestión de dependencias

### Instalación

1. Clona el repositorio:
```bash
git clone <tu-repositorio>
cd advent_of_code
```

2. Instala las dependencias:
```bash
just install
```

### Comandos disponibles

```bash
just                    # Lista todos los comandos disponibles
just install           # Instala dependencias y configura pre-commit
just check             # Ejecuta todas las verificaciones (linting, tests, etc.)
just test_unit         # Ejecuta pruebas unitarias
just test_integration  # Ejecuta pruebas de integración
just run               # Ejecuta la aplicación principal
```

---

## 6. 📁 Estructura del Proyecto

```
advent_of_code/
├── config/                 # Archivos de configuración
│   └── main.json          # Configuración principal (rutas, parámetros)
├── data/                  # Datos del proyecto
│   ├── raw/              # Datos sin procesar
│   ├── process/          # Datos procesados
│   ├── final/            # Datos finales
│   └── results/          # Resultados y reportes generados
├── docs/                 # Documentación del proyecto
├── notebooks/            # Jupyter notebooks para exploración
├── src/                  # Código fuente
│   └── advent_of_code/
│       ├── analyze/      # Módulos de análisis
│       ├── export/       # Módulos de exportación
│       ├── load/         # Módulos de carga de datos
│       ├── process/      # Módulos de procesamiento
│       ├── config.py     # Gestión de configuración
│       ├── errors.py     # Manejo de errores personalizados
│       └── result.py     # Implementación de Result pattern
└── tests/               # Pruebas
    ├── unit/           # Pruebas unitarias
    └── integration/    # Pruebas de integración
```

---

## 7. ⚙️ Configuración

Edita `config/main.json` para ajustar:

- **Rutas de datos**: Configurar ubicaciones de archivos de entrada y salida
- **Parámetros del análisis**: Ajustar criterios y filtros específicos
- **Configuraciones del reporte**: Personalizar formato y contenido de salidas

---

## 8. 🧪 Desarrollo y Testing

### Ejecutar pruebas

```bash
just test_unit          # Solo pruebas unitarias
just test_integration   # Solo pruebas de integración
```

### Control de calidad

Este proyecto incluye:
- **Linting**: Ruff para formato y estilo de código
- **Type checking**: MyPy para verificación de tipos estática
- **Pre-commit hooks**: Verificaciones automáticas antes de cada commit
- **Testing**: Pytest para pruebas unitarias e integración
- **Security**: Bandit para análisis de seguridad

---

## 9. 📝 Contribuir

1. Crea un branch para tu funcionalidad: `git checkout -b feature/nueva-funcionalidad`
2. Realiza tus cambios siguiendo las guías en `docs/coding-guidelines/`
3. Ejecuta `just check` para verificar calidad del código
4. Commit siguiendo el formato en `docs/coding-guidelines/style/COMMITS.md`
5. Crea un Pull Request

---

**Contacto**: Henry Guerra (hg2866066@gmail.com)

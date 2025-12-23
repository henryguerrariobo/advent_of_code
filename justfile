# Muestra la lista de comandos disponibles
default:
    @just --list

# Instalar dependencias del proyecto
install:
    @echo "🚀 Creating virtual environment using uv"
    @uv sync --all-packages
    @uv run pre-commit install

check: install
    @echo "🚀 Checking lock file consistency with 'pyproject.toml'"
    @uv lock --locked
    @echo "🚀 Linting code: Running pre-commit"
    @uv run pre-commit run --all-files

# Ejecutar pruebas
test_unit *args:
    @echo "🚀 Testing code: Running pytest"
    @uv run pytest tests/year_2025 {{args}}


# Ejecutar entorno de desarrollo
run *args:
    @echo "🚀 Running development cli"
    @uv run src/advent_of_code/__init__.py {{args}}

# Listar variables globales de proyecto
list_global_vars:
    @grep -r "^[A-Z_][A-Z0-9_]*\s*\(:\s*[^=]*\)\?=" --include="*.py" src

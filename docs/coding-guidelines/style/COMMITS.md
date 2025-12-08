# Guía de estilo para Commits y Documentación

> Tomados parcialmente de [Contributing to Atom](https://github.com/atom/atom/blob/master/CONTRIBUTING.md)

En esta sección, hablaremos de como documentar los commits. El propósito de estas normas es asegurar que el desarrollo pueda ser mantenible en el tiempo, se pueda hacer trazabilidad de cambios y el conocimiento del desarrollo pueda ser transferido.

## Mensajes de Commit de Git

Así como la nomenclatura en código, los mensajes de commit es preferible escribirlos en inglés, para poder facilitar que cualquier persona, independiente de su lengua materna pueda entender el historial de cambios, y asegurarse de que puedan continuar con un desarrollo.

Los lineamientos de estilo son los siguientes:

- Utilice en el mensaje del commit un emoji descriptivo:


| Emoji | Tipo      | Descripción                                                                                                                                                                                                                             |
| ----- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🎨    | refactor  | cuando mejore la lógica/forma/estructura del código                                                                                                                                                                                     |
| 🛠️    | feat      | cuando agregue alguna nueva funcionalidad                                                                                                                                                                                               |
| 📝    | docs      | cuando escriba o modifique documentación                                                                                                                                                                                                            |
| 🐛    | bug       | cuando arregle un bug                                                                                                                                                                                                                   |
| 🧪    | test      | cuando agregue las pruebas al código                                                                                                                                                                                                    |
| ✨    | beauty    | Cuando haga cambios con respecto al import linter <span style="font-size:12px"><strong><em>Nota: no aplicar esta convención cuando agregue nuevas funcionalidades<br>y estas pasen por la revisión del pre-commit.</em></strong></span> |
| 🗑️    | remove    | cuando elimine archivos o lineas de código que no se usan en el proyecto.                                                                                                                                                                                   |
| 🔖    | bump      | cuando actualice el versionamiento semántico                                                                                                                                                                                            |
| 📌    | todo     | cuando agregue tareas a los archivos                                                                                                                                                                                                                   |
| 💄    | style     | cuando haga ajustes de formato o estilo al código. Ej: agregar cabeceras de funciones, docstrings, etc.                                                                                                                                                                                                                    |
| ⬆️    | deps-up   | cuando actualice dependencias                                                                                                                                                                                                           |
| ⬇️    | deps_down | cuando desactualice dependencias                                                                                                                                                                                                        |
| 🔀    | merge     | cuando fusione ramas                                                                                                                                                                                                                    |

- Haga uso del _present tense_ (_"Add feature"_, no _"Added feature"_)
- Haga uso del _imperative mood_ (_"Move cursor to..."_, no _"Moves cursor to..."_)
- Limite la primera línea a 72 caracteres o menos.
- Refiérase a Pull Requests o Issues libremente después de la primera línea.
- Cuando cambie documentación únicamente, incluya en el título del commit las palabras `[ci skip]`. Esto con el fin de no integrar continuamente este cambio.

Por lo tanto, un buen nombramiento del commit sería de la manera:

```
git commit -m "AB#312 :bug: IS-S1-030: Fix bug in class Student"
```

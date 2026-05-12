# Makefile para Proyecto Integrador T9
# Autor: Bryan Borges
# Descripción: Compilación y gestión del proyecto

CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra
TARGET = main
SOURCE = main.cpp
OBJECTS = main.o

# Colores para output
GREEN = \033[0;32m
RED = \033[0;31m
YELLOW = \033[0;33m
NC = \033[0m # No Color

.PHONY: all build clean run test help install

# Target por defecto
all: build

# Compilar el proyecto
build: $(TARGET)
	@echo "$(GREEN)Compilación exitosa$(NC)"

$(TARGET): $(SOURCE)
	@echo "$(YELLOW)Compilando...$(NC)"
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SOURCE)

# Ejecutar el programa
run: build
	@echo "$(GREEN)▶  Ejecutando...$(NC)"
	./$(TARGET)

# Compilación rápida (sin dependencias)
debug: CXXFLAGS += -g -O0
debug: build
	@echo "$(GREEN) Modo debug activado$(NC)"

# Compilación optimizada
release: CXXFLAGS += -O3
release: build
	@echo "$(GREEN)⚡ Compilación optimizada$(NC)"

# Limpiar archivos generados
clean:
	@echo "$(YELLOW)  Limpiando...$(NC)"
	rm -f $(TARGET) $(OBJECTS) *.o *.out test_input.txt
	@echo "$(GREEN) Limpieza completada$(NC)"

# Limpiar y reconstruir
rebuild: clean build
	@echo "$(GREEN)Reconstrucción completada$(NC)"

# Ejecutar pruebas automáticas
test: build
	@echo "$(YELLOW) Ejecutando pruebas...$(NC)"
	@chmod +x test_automatico.sh
	@./test_automatico.sh

# Mostrar información del archivo
info:
	@echo "$(GREEN)═══════════════════════════════════$(NC)"
	@echo "$(GREEN) INFORMACIÓN DEL PROYECTO$(NC)"
	@echo "$(GREEN)═══════════════════════════════════$(NC)"
	@wc -l $(SOURCE)
	@echo ""
	@echo "Fecha de modificación:"
	@ls -lh $(SOURCE) | awk '{print $$6, $$7, $$8}'
	@echo ""
	@echo "Tamaño del archivo:"
	@ls -lh $(SOURCE) | awk '{print $$5}'

# Mostrar estadísticas
stats: $(SOURCE)
	@echo "$(GREEN)═══════════════════════════════════$(NC)"
	@echo "$(GREEN) ESTADÍSTICAS DEL CÓDIGO$(NC)"
	@echo "$(GREEN)═══════════════════════════════════$(NC)"
	@echo "Líneas de código:"
	@wc -l $(SOURCE)
	@echo ""
	@echo "Funciones implementadas:"
	@grep -c "void\|map\|int\|string" $(SOURCE)
	@echo ""
	@echo "Comentarios:"
	@grep -c "//" $(SOURCE)
	@echo ""
	@echo "Clases:"
	@grep -c "class" $(SOURCE)

# Instalar documentación
install: build
	@echo "$(GREEN) Instalando...$(NC)"
	@mkdir -p bin
	@cp $(TARGET) bin/
	@cp *.md bin/
	@echo "$(GREEN) Instalación completada en ./bin$(NC)"

# Desinstalar
uninstall:
	@echo "$(YELLOW)  Desinstalando...$(NC)"
	@rm -rf bin/ $(TARGET)
	@echo "$(GREEN) Desinstalación completada$(NC)"

# Mostrar ayuda
help:
	@echo "$(GREEN)═══════════════════════════════════════════════════════$(NC)"
	@echo "$(GREEN) MAKE - AYUDA DEL PROYECTO$(NC)"
	@echo "$(GREEN)═══════════════════════════════════════════════════════$(NC)"
	@echo ""
	@echo "Targets disponibles:"
	@echo ""
	@echo "  $(YELLOW)make build$(NC)   - Compilar el proyecto (default)"
	@echo "  $(YELLOW)make run$(NC)     - Compilar y ejecutar"
	@echo "  $(YELLOW)make debug$(NC)   - Compilar en modo debug"
	@echo "  $(YELLOW)make release$(NC) - Compilar optimizado"
	@echo "  $(YELLOW)make clean$(NC)   - Limpiar archivos generados"
	@echo "  $(YELLOW)make rebuild$(NC) - Limpiar y recompilar"
	@echo "  $(YELLOW)make test$(NC)    - Ejecutar pruebas automáticas"
	@echo "  $(YELLOW)make info$(NC)    - Ver información del archivo"
	@echo "  $(YELLOW)make stats$(NC)   - Mostrar estadísticas del código"
	@echo "  $(YELLOW)make install$(NC) - Instalar en ./bin"
	@echo "  $(YELLOW)make uninstall$(NC) - Desinstalar"
	@echo "  $(YELLOW)make help$(NC)    - Mostrar esta ayuda"
	@echo ""
	@echo "Ejemplos de uso:"
	@echo ""
	@echo "  Compilar:        $(YELLOW)make$(NC)"
	@echo "  Ejecutar:        $(YELLOW)make run$(NC)"
	@echo "  Pruebas:         $(YELLOW)make test$(NC)"
	@echo "  Limpiar:         $(YELLOW)make clean$(NC)"
	@echo ""
	@echo "$(GREEN)═══════════════════════════════════════════════════════$(NC)"

# Compilación silenciosa
compile-silent:
	@$(CXX) $(CXXFLAGS) -o $(TARGET) $(SOURCE) 2>/dev/null && echo "Compilado" || echo "Error de compilación"

# Check de sintaxis
syntax-check:
	@echo "$(YELLOW) Verificando sintaxis...$(NC)"
	@$(CXX) $(CXXFLAGS) -fsyntax-only $(SOURCE)
	@echo "$(GREEN) Sintaxis correcta$(NC)"

# Ver archivos generados
files:
	@echo "$(GREEN) Archivos del proyecto:$(NC)"
	@ls -lh

# Formater (si está disponible)
format:
	@echo "$(YELLOW) Formateando código...$(NC)"
	@if command -v clang-format &> /dev/null; then \
		clang-format -i $(SOURCE); \
		echo "$(GREEN) Código formateado$(NC)"; \
	else \
		echo "$(RED) clang-format no está instalado$(NC)"; \
	fi

.SILENT: syntax-check

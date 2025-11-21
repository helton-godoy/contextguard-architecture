#!/bin/bash
# contextguard-activate.sh

PROJECT_PATH="${1:-.}"
PROJECT_TYPE="${2:-auto}"

echo "🚀 Ativando ContextGuard Global para projeto: $PROJECT_PATH"

# Detectar tipo de projeto se necessário
if [ "$PROJECT_TYPE" = "auto" ]; then
    PROJECT_TYPE=$(python3 -c "
import sys, os, glob
sys.path.append('$(dirname $0)')
from auto_detector import ProjectTypeDetector
detector = ProjectTypeDetector()
print(detector.detect_project_type('$PROJECT_PATH'))
")
    echo "📋 Tipo de projeto detectado: $PROJECT_TYPE"
fi

# Criar estrutura ContextGuard
mkdir -p "$PROJECT_PATH/.contextguard"
mkdir -p "$PROJECT_PATH/.contextguard/modules"
mkdir -p "$PROJECT_PATH/.contextguard/extensions"
mkdir -p "$PROJECT_PATH/.contextguard/state"

# Copiar template apropriado
if [ "$PROJECT_TYPE" != "general" ]; then
    cp "$(dirname $0)/templates/${PROJECT_TYPE}-project.yaml" \
       "$PROJECT_PATH/.contextguard/project-config.yaml"
else
    cp "$(dirname $0)/templates/general-project.yaml" \
       "$PROJECT_PATH/.contextguard/project-config.yaml"
fi

echo "✅ ContextGuard ativado com sucesso!"
echo "📊 Monitoramento silencioso iniciado"
echo "🔄 Preservação de estado habilitada"
echo "⚡ Otimização automática ativa"

#!/usr/bin/env python
# scripts/validate_environment.py

import sys
import importlib
import pkg_resources

def check_dependencies():
    """Verifica que todas las dependencias requeridas estén instaladas con las versiones correctas."""
    
    required = {}
    with open("requirements.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "==" in line:
                package, version = line.split("==")
                required[package] = version
    
    print(f"Verificando {len(required)} dependencias...")
    
    missing = []
    incorrect_version = []
    
    for package, required_version in required.items():
        try:
            # Intenta importar el paquete
            imported = importlib.import_module(package.replace("-", "_"))
            
            # Verifica la versión
            try:
                installed_version = pkg_resources.get_distribution(package).version
                if installed_version != required_version:
                    incorrect_version.append((package, installed_version, required_version))
                    print(f"✗ {package} tiene versión {installed_version}, pero se requiere {required_version}")
                else:
                    print(f"✓ {package} {installed_version}")
            except:
                print(f"✓ {package} (versión no verificada)")
                
        except ImportError:
            missing.append(package)
            print(f"✗ {package} no está instalado")
    
    if missing or incorrect_version:
        print(f"
¡Atención! Hay problemas con el entorno:")
        if missing:
            print(f"- Faltan {len(missing)} dependencias: {", ".join(missing)}")
        if incorrect_version:
            print(f"- Hay {len(incorrect_version)} paquetes con versiones incorrectas")
        
        print("
Solución: ejecuta el siguiente comando:")
        print("pip install -r requirements.txt")
        return False
    else:
        print("
✅ ¡Todas las dependencias están correctamente instaladas!")
        return True

if __name__ == "__main__":
    sys.exit(0 if check_dependencies() else 1)


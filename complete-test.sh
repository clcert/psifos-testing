# Limpiar elección previa
python main.py -c

# Configurar elección
python api-script.py config

# Generar claves
python main.py -g

# Abrir elección
python api-script.py start

# Enviar votos
python main.py -v

# Cerrar elección y computar tally
python api-script.py end
python api-script.py tally

# Enviar desencriptación parcial
python main.py -d

# Imprimir resultados
python main.py -p

# Liberar resultados
python api-script.py release

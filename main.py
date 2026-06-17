# Importa a função principal que contém o loop do jogo
from src.jogo import executar_jogo

# Verifica se o arquivo está sendo executado diretamente (e não importado como módulo)
if __name__ == "__main__":
    # Inicia o jogo
    executar_jogo()

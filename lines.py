import sys

def main():
    # Verificar o número de argumentos
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments" if len(sys.argv) < 2 else "Too many command-line arguments")

    filename = sys.argv[1]

    # Verificar se o arquivo tem a extensão .py
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        # Abrir o arquivo
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Contar linhas de código
    code_lines = 0
    in_docstring = False
    for line in lines:
        stripped = line.lstrip()

        # Ignorar linhas em branco
        if not stripped:
            continue

        # Verificar docstrings (abrindo ou fechando)
        if stripped.startswith('"""') or stripped.startswith("'''"):
            if in_docstring:
                in_docstring = False
            else:
                in_docstring = True
            # Se a linha contém apenas a abertura/fechamento, continue
            if stripped.strip() == '"""' or stripped.strip() == "'''":
                continue
        if in_docstring:
            continue

        # Ignorar linhas que são apenas comentários
        if stripped.startswith("#"):
            continue

        # Remover comentários do final das linhas de código
        if "#" in stripped:
            stripped = stripped.split("#")[0].rstrip()

        # Se a linha ainda contém código após a limpeza, conta como válida
        if stripped:
            code_lines += 1

    print(code_lines)


main()

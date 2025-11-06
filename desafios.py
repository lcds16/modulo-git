"""
Desafio Módulo Git

Neste arquivo você encontrará funções **incompletas** que representam
tarefas relacionadas ao aprendizado de Git e GitHub.

Seu objetivo é:
- Criar uma issue para cada função.
- Implementar a função em uma branch específica.
- Fazer commit, criar tag e abrir Pull Request.
- Repetir o processo até concluir todas as funções.

Boa sorte e bons commits! 🚀
"""
import re

#OUTRA BRANCH _ REPETINDO O EXERCICIO

def mostrar_mensagem_inicial():
    print("BEM VINDA AO GIT \\O//")

def listar_comandos_git_basicos():
    return ["git init", "git add", "git commit", "git status", "git push"]

def criar_mensagem_commit(funcao_nome):
    return f"Implementa função {funcao_nome}"


def verificar_tag_valida(tag):
    padrao = r"^v\d+\.\d+$"
    return bool(re.match(padrao, tag))


def gerar_relatorio_final(funcoes_concluidas):
    total = len(funcoes_concluidas)
    return f"Desafio concluído! {total} funções implementadas no projeto."

#bla
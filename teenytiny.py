from lex import *
from parse import *
import sys


def lexerMain():
    # source = "+- */>>==!="
    # source = "+-# This is a comment!\n */"
    # source = '+- "This is a string" # This is a comment!\n */'
    # source = "+-123 9.8654*/"
    source = "IF+-123 foo*THEN/"
    lexer = Lexer(source)

    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()


def parserMain():
    print("Teeny Tiny Compiler")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1], "r") as inputFile:
        source = inputFile.read()

    # Inititalize the lexer and parser.
    lexer = Lexer(source)
    parser = Parser(lexer)

    parser.program()  # Start the parser.
    print("Parsing completed.")


def main():
    parserMain()


main()

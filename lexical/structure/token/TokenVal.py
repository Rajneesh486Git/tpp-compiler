from enum import Enum


class TokenVal(Enum):
    IF = 'SE'
    ELSE = 'SENAO'
    THEN = "ENTAO"
    END = "FIM"
    FOR = "REPITA"
    RETURN = "RETORNA"
    UNTIL = "ATE"
    READ = "LEIA"
    WRITE = "ESCREVE"
    FLOAT_TYPE = "TIPO_FLUTUANTE"
    INTEGER_TYPE = "TIPO_INTEIRO"
    PLUS = "SOMA"
    MINUS = "MENOS"
    TIMES = "VEZES"
    DIVISION = "DIVIDE"
    LOGIC_EQUALS = "IGUAL"
    COMMA = "VIRGULA"
    ASSIGNMENT = "ATRIBUICAO"
    LESS = "MENOR"
    LESS_EQUALS = "MENOR_IGUAL"
    HIGHER = "MAIOR"
    HIGHER_EQUALS = "MAIOR_IGUAL"
    OPEN_PARENTHESES = "ABRE_PARENTESES"
    CLOSE_PARENTHESES = "FECHA_PARENTESES"
    TWO_DOTS = "DOIS PONTOS"
    OPEN_BRACKETS = "ABRE_COLCHETES"
    CLOSE_BRACKETS = "FECHA_COLCHETES"
    LOGIC_AND = "E_LOGICO"
    LOGIC_OR = "OU_LOGICO"
    LOGIC_NOT = "NAO_LOGICO"
    INTEGER_NUMBER = "NUMERO_INTEIRO"
    FLOAT_NUMBER = "NUMERO_FLUTUANTE"
    IDENTIFICATOR = "IDENTIFICADOR"
    SCIENTIFIC_NOTATION = "NOTACAO_CIENTIFICA"

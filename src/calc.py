from dataclasses import dataclass
from typing import Any, Optional

# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER, PLUS, MINUS, MUL, DIV, EOF = "INTEGER", "PLUS", "MINUS", "MUL", "DIV", "EOF"


@dataclass(frozen=True)
class Token:
    """
    Examples:
        Token(INTEGER, 3)
        Token(PLUS '+')
    """

    type: str
    value: Any


ops = {
    "+": Token(PLUS, "+"),
    "-": Token(MINUS, "-"),
    "*": Token(MUL, "*"),
    "/": Token(DIV, "/"),
}


class Interpreter:
    def __init__(self, text: str):
        # client string input, e.g. "3+5"
        self.text = text
        # self.position is an index into self.text
        self._position: int = 0
        # current token instance
        self._current_token: Optional[Token] = None
        self._current_char = text[self._position]

    def error(self) -> None:
        raise Exception("Error parsing input")

    def _advance_position(self) -> None:
        # is self.pos index past the end of the self.text ?
        # if so, then return EOF token because there is no more
        # input left to convert into tokens
        self._position += 1
        if self._position > len(self.text) - 1:
            self._current_char = None
        else:
            self._current_char = self.text[self._position]

    def _get_integer(self) -> int:
        """
        Return multiple digit integer by joining subsequent digit characters.
        """
        result = ""
        while self._current_char is not None and self._current_char.isdigit():
            result += self._current_char
            self._advance_position()
        return int(result)

    def _get_next_token(
        self,
    ):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        # if the character is a digit then convert it to
        # integer, create an INTEGER token, increment self.pos
        # index to point to the next character after the digit,
        # and return the INTEGER token
        while self._current_char is not None:
            if self._current_char == " ":
                self._advance_position()
                continue
            if self._current_char.isdigit():
                return Token(type=INTEGER, value=self._get_integer())
            if self._current_char in ops:
                token = ops[self._current_char]
                self._advance_position()
                return token
        return Token(type=EOF, value=None)

    def _eat(self, token_type: str) -> None:
        """Compare the current token type with the passed token
        type and if they match then "eat" the current token
        and assign the next token to the self.current_token,
        otherwise raise an exception."""
        if self._current_token.type == token_type:
            self._current_token = self._get_next_token()
        else:
            self.error()

    def _term(self) -> Any:
        token = self._current_token
        self._eat(token.type)
        return token.value

    def expr(self) -> int:
        """
        Arithmetic expression interprter / parser
        """
        self._current_token = self._get_next_token()
        result = self._term()
        while self._current_token.type != EOF:
            if self._current_token.type in (MINUS, PLUS, DIV, MUL):
                if self._current_token.type == PLUS:
                    self._eat(PLUS)
                    result = result + self._term()
                elif self._current_token.type == MINUS:
                    self._eat(MINUS)
                    result = result - self._term()
                elif self._current_token.type == MUL:
                    self._eat(MUL)
                    result = result * self._term()
                else:
                    self._eat(DIV)
                    result = result / self._term()
        return result


def main():
    while True:
        try:
            text = input("calc> ")
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == "__main__":
    main()

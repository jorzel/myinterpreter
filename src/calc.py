from typing import Any, Optional

# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER, PLUS, EOF = "INTEGER", "PLUS", "EOF"


class Token(object):
    def __init__(self, type_: str, value: Any):
        # token type: INTEGER, PLUS, or EOF
        self.type = type_
        # token value: 0, 1, 2. 3, 4, 5, 6, 7, 8, 9, '+', or None
        self.value = value

    def __str__(self) -> str:
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return f"Token({self.type}, {repr(self.value)})"

    def __repr__(self) -> str:
        return self.__str__()


class Interpreter(object):
    def __init__(self, text: str):
        # client string input, e.g. "3+5"
        self.text = text
        # self.position is an index into self.text
        self._position: int = 0
        # current token instance
        self._current_token: Optional[Token] = None
        self._current_char = text[self._position]

    def error(self):
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
                return Token(INTEGER, self._get_integer())
            if self._current_char == "+":
                self._advance_position()
                return Token(PLUS, "+")
            self.error()
        return Token(EOF, None)

    def _eat(self, token_type: str) -> None:
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self._current_token.type == token_type:
            self._current_token = self._get_next_token()
        else:
            self.error()

    def expr(self) -> int:
        # set current token to the first token taken from the input
        self._current_token = self._get_next_token()

        # we expect the current token to be a single-digit integer
        left = self._current_token
        self._eat(INTEGER)

        # we expect the current token to be a '+' token
        _ = self._current_token
        self._eat(PLUS)

        # we expect the current token to be a single-digit integer
        right = self._current_token
        self._eat(INTEGER)
        # after the above call the self.current_token is set to
        # EOF token

        # at this point INTEGER PLUS INTEGER sequence of tokens
        # has been successfully found and the method can just
        # return the result of adding two integers, thus
        # effectively interpreting client input
        result = left.value + right.value
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

from enum import Enum
from typing import List

class Morse(Enum):
    DOT = 0
    DASH = 1
    SPACE = 2

class Translate():
    """
    Class containing all methods pertaining to translation of data to morse, to characters, and to actions.
    """

    MORSE_CODE_DICT = {
        (Morse.DOT, Morse.DASH): 'A',        # .-
        (Morse.DASH, Morse.DOT, Morse.DOT, Morse.DOT): 'B',   # -...
        (Morse.DASH, Morse.DOT, Morse.DASH, Morse.DOT): 'C',  # -.-.
        (Morse.DASH, Morse.DOT, Morse.DOT): 'D',   # -..
        (Morse.DOT,): 'E',                         # .
        (Morse.DOT, Morse.DOT, Morse.DASH, Morse.DOT): 'F',   # ..-.
        (Morse.DASH, Morse.DASH, Morse.DOT): 'G',  # --.
        (Morse.DOT, Morse.DOT, Morse.DOT, Morse.DOT): 'H',    # ....
        (Morse.DOT, Morse.DOT): 'I',               # ..
        (Morse.DOT, Morse.DASH, Morse.DASH, Morse.DASH): 'J', # .---
        (Morse.DASH, Morse.DOT, Morse.DASH): 'K',  # -.-
        (Morse.DOT, Morse.DASH, Morse.DOT, Morse.DOT): 'L',   # .-..
        (Morse.DASH, Morse.DASH): 'M',             # --
        (Morse.DASH, Morse.DOT): 'N',              # -.
        (Morse.DASH, Morse.DASH, Morse.DASH): 'O', # ---
        (Morse.DOT, Morse.DASH, Morse.DASH, Morse.DOT): 'P',  # .--.
        (Morse.DASH, Morse.DASH, Morse.DOT, Morse.DASH): 'Q', # --.-
        (Morse.DOT, Morse.DASH, Morse.DOT): 'R',   # .-.
        (Morse.DOT, Morse.DOT, Morse.DOT): 'S',    # ...
        (Morse.DASH,): 'T',                        # -
        (Morse.DOT, Morse.DOT, Morse.DASH): 'U',   # ..-
        (Morse.DOT, Morse.DOT, Morse.DOT, Morse.DASH): 'V',   # ...-
        (Morse.DOT, Morse.DASH, Morse.DASH): 'W',  # .--
        (Morse.DASH, Morse.DOT, Morse.DOT, Morse.DASH): 'X',  # -..-
        (Morse.DASH, Morse.DOT, Morse.DASH, Morse.DASH): 'Y', # -.--
        (Morse.DASH, Morse.DASH, Morse.DOT, Morse.DOT): 'Z',  # --..
        (Morse.DOT, Morse.DASH, Morse.DASH, Morse.DASH, Morse.DASH): '1', # .----
        (Morse.DOT, Morse.DOT, Morse.DASH, Morse.DASH, Morse.DASH): '2',  # ..---
        (Morse.DOT, Morse.DOT, Morse.DOT, Morse.DASH, Morse.DASH): '3',   # ...--
        (Morse.DOT, Morse.DOT, Morse.DOT, Morse.DOT, Morse.DASH): '4',    # ....-
        (Morse.DOT, Morse.DOT, Morse.DOT, Morse.DOT, Morse.DOT): '5',     # .....
        (Morse.DASH, Morse.DOT, Morse.DOT, Morse.DOT, Morse.DOT): '6',    # -....
        (Morse.DASH, Morse.DASH, Morse.DOT, Morse.DOT, Morse.DOT): '7',   # --...
        (Morse.DASH, Morse.DASH, Morse.DASH, Morse.DOT, Morse.DOT): '8',  # ---..
        (Morse.DASH, Morse.DASH, Morse.DASH, Morse.DASH, Morse.DOT): '9', # ----.
        (Morse.DASH, Morse.DASH, Morse.DASH, Morse.DASH, Morse.DASH): '0' # -----
    }

    @staticmethod
    def convert_stream_to_morse(stream: List[int], prev_morse: List[Morse]) -> List[Morse]:
        """
        Converts a stream of amplitude-time data (represented as integers) into a list of Morse code enums.
        
        :param stream: A list of integers representing the amplitude-time data.
        :param prev_morse: A list of previously converted morse code enums.
        :return: A list of MorseEnum representing the morse code (DOT, DASH, SPACE).
        """
        pass

    @staticmethod
    def split_morse_seq_to_words(morse_stream: List[Morse]) -> List[List[Morse]]:
        """
        Splits a list of Morse symbols (DOT, DASH, SPACE) into separate morse code sequences using SPACE as a divider.
        
        :param morse_stream: A list of Morse enums representing the full morse code stream.
        :return: List[List[Morse]], where each list represents a morse code character (DOT/DASH sequence).
        """
        result = [] # sentence full of lists of morse symbols
        letter = []

        for symbol in morse_stream:
            if symbol == Morse.SPACE:
                if letter:  # Only add non-empty words
                    result.append(letter)
                    current_word = []
            else:
                result.append(symbol)
        
        if current_word:  # Append the last word if any
            result.append(current_word)

        return result

    @staticmethod
    def convert_morse_word_to_english(morse_stream: List[Morse]) -> List[str]:
        """
        Converts a morse code stream (DOT/DASH/SPACE) into corresponding characters.
        
        :param morse_stream: A list of Morse enums representing the full morse code stream.
        :return: A string of translated characters.
        """
        # Split the morse stream by spaces into individual morse sequences
        morse_words = Translate.split_morse_by_spaces(morse_stream)
        result = []
        
        for word in morse_words:
            # Convert each morse "word" (sequence of dots/dashes) into a character
            character = Translate.MORSE_CODE_DICT.get(tuple(word), '?')  # '?' for unknown sequences
            result.append(character)
        
        return ''.join(result)

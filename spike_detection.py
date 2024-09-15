from enum import Enum
from typing import List, Tuple

class Morse(Enum):
    DOT = 0
    DASH = 1
    SPACE = 2

class Translate():
    """
    Class containing all methods pertaining to translation of data to morse, to characters, and to actions.

    Key Terms:
    Dot: single morse code dot
    Dash: single morse code dash
    Space: pause that distingushes between clusters of dots and dashes. Each go to form a letter.
    """
    
    # CONSTANTS
    DASH_INDEX_THRESHOLD = 5_000             # index offset between first spike and second spike that if less than is a dash, otherwise two dots.
    SPACE_INDEX_THRESHOLD = 10_000    # index offset between two spikes representing a space seperating two clusters of morse symbols

    INVALID_MAGNITUDE_THRESHOLD = 20_000        # All spikes in a stream that occur after and including a spike that exceeds this threshold will not be considered as morse

    FIRST_SPIKE_MAGNITUDE_THRESHOLD = 8_000    # This is the threshold needed to start a new symbol with a spike
    SECOND_SPIKE_MAGNITUDE_THRESHOLD = 6_000    # This is the threshold needed by a spike that follows a dot to make it into a dash

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
    def convert_stream_to_morse(stream: List[Tuple[int, int]], prev_symbols: List[Morse], last_spike_offset: int) -> List[Morse]:
        """
        Converts a stream of amplitude-time data (represented as integers) into a list of Morse code enums.
        
        :param stream: A list of tuples (int, int) representing the (index, amplitude) of every speak.
        :param prev_morse: Tuple(A list of previously converted morse code enums, the index offset between the last spike and the end of the interval).
        :return: A list of MorseEnum representing the cumulative morse code (DOT, DASH, SPACE). new_morse + prev_morse
        """
        result = []

        prev_symbol, prev_index = None, float('inf')

        if prev_symbols:
            prev_symbol, prev_index = prev_symbols[-1], -last_spike_offset
            result.append(prev_symbols[-1])
            del prev_symbols[-1]

        # Once first element has properly been merged with prev_morse, continue stream as normal

        for index, magnitude in stream:
            
            print((index, magnitude), (prev_index, prev_symbol), result)

            # if magnitude exceeds invalid threshold do not consider any spike which occurs after in this stream chunk
            if (magnitude >= Translate.INVALID_MAGNITUDE_THRESHOLD):
                break

            # Convert spikes to morse symbols
            if (prev_symbol is Morse.DOT) and (index - prev_index < Translate.DASH_INDEX_THRESHOLD) and (magnitude >= Translate.SECOND_SPIKE_MAGNITUDE_THRESHOLD):  # Previous Dot is now a Dash
                del result[-1]              # delete dot
                result.append(Morse.DASH)   # replace w dash
                
                prev_symbol, prev_index = result[-1], index
                print("real")
            else:
                if (magnitude >= Translate.FIRST_SPIKE_MAGNITUDE_THRESHOLD):  # Gap between two dots is a space
                    # if last dot was so long ago that there should be a space, put a space, then a dot.
                    if (index - prev_index >= Translate.SPACE_INDEX_THRESHOLD):
                        result.append(Morse.SPACE)
                        print("true")
                    result.append(Morse.DOT)
                    print("based")
                    prev_symbol, prev_index = result[-1], index

        return prev_symbols + result if prev_symbols else result
    

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
                    letter = []
            else:
                letter.append(symbol)
        
        if letter:  # Append the last word if any
            result.append(letter)

        return result

    @staticmethod
    def convert_morse_word_to_english(morse_stream: List[Morse]) -> List[str]:
        """
        Converts a morse code stream (DOT/DASH/SPACE) into corresponding characters.
        
        :param morse_stream: A list of Morse enums representing the full morse code stream.
        :return: A string of translated characters.
        """
        # Split the morse stream by spaces into individual morse sequences
        morse_words = Translate.split_morse_seq_to_words(morse_stream)
        print(morse_words)
        result = []
        
        for word in morse_words:
            # Convert each morse "word" (sequence of dots/dashes) into a character
            character = Translate.MORSE_CODE_DICT.get(tuple(word), '?')  # '?' for unknown sequences
            result.append(character)
        
        return ''.join(result)
<<<<<<< Updated upstream
=======


# data = [(4, 1913), (47, 1616), (91, 1939), (94, 1901), (108, 2002), (153, 2363), (198, 2270), (287, 1904), (355, 1050), (370, 1894)]
# morse = Translate.convert_stream_to_morse(data, None)
# english = Translate.convert_morse_word_to_english(morse)
# print(morse)
# print(english)
>>>>>>> Stashed changes

#################################################################
# FILE : wordsearch.py
# WRITER : Ran Houdine , ranho , 313261133
# EXERCISE : intro2cs2 ex5 2021
# DESCRIPTION: A program that finds words in a words matrix
# STUDENTS I DISCUSSED THE EXERCISE WITH: none.
# WEB PAGES I USED: none
#################################################################
import sys
from os import path

# region Constants
LACKING_ARGUMENTS = "Please enter words list and matrix file directories, directions input and output file directory"
MATRIX_NOT_FOUND = "The matrix file can't be found"
WORD_LIST_NOT_FOUND = "The word list file can't be found"
INVALID_DIRECTIONS = "Please enter only valid search directions"
# endregion


def read_wordlist(filename):
    """
    The function gets a words-containing file's location and returns a list of the file's words
    :param filename: The file's location
    :return: A list of words from the file
    """
    words_list = []
    with open(filename) as file:
        for line in file:
            words_list.append(line.replace('\n', ''))  # deleting unwanted \n's from the given words
    return words_list


# region read matrix
def read_matrix(filename):
    """

    :param filename:
    :return:
    """
    matrix = []
    with open(filename) as matrix_file:
        init_matrix(matrix, matrix_file)
    return matrix


# region functions used by read_matrix
def add_row(empty_row, line_to_add):
    """
    Gets an empty row and fills it with letters
    :param empty_row: The empty row to which letters are to be inserted
    :param line_to_add: the current line of the matrix file to be inserted to the matrix row
    :return: None
    """
    for cell in line_to_add.split(","):
        empty_row.append(cell.replace("\n", ""))


def init_matrix(matrix_to_init, matrix_file):
    """
    Initializes the matrix from the given matrix file
    :param matrix_to_init: and empty list making the row-less empty matrix
    :param matrix_file: The matrix file to initialize
    :return: Initialized matrix
    """
    for line in matrix_file:
        matrix_to_init.append([])
        add_row(matrix_to_init[-1], line)
    return matrix_to_init
# endregion
# endregion


# region find words
def find_words(word_list, matrix, directions):
    """
        Gets a list of words and searches them in a matrix
    :param word_list: list of words to be searched
    :param matrix: word matrix
    :param directions: directions to search along
    :return: a list of (word, count) tuples denoting the number of appearances of each word in the matrix
    """
    words_count_list = []
    search_directions = set(directions)
    for word in word_list:
        count = search(word, matrix, search_directions)
        if count:
            words_count_list.append((word, count))
    return words_count_list


# region functions used by find_words
def search(word, matrix, directions):
    """
    The function searches for a word in a matrix in the given directions
    :param word: word to search
    :param directions: directions to search
    :param matrix: matrix to search in
    :return: number of appearances of the word in the matrix
    """
    count = 0
    for direction in directions:
        if direction == 'u':
            count += search_up(word, matrix)
        if direction == 'd':
            count += search_down(word, matrix)
        if direction == 'r':
            count += search_right(word, matrix)
        if direction == 'l':
            count += search_left(word, matrix)
        if direction == 'w':
            count += search_up_right(word, matrix)
        if direction == 'x':
            count += search_up_left(word, matrix)
        if direction == 'y':
            count += search_down_right(word, matrix)
        if direction == 'z':
            count += search_down_left(word, matrix)
    return count


# region direction-specific search functions
# region searching up
def search_up(word, matrix):
    """
    Searches for a word in the matrix in the up direction
    :param word: the word to be searched for
    :param matrix: the matrix to search
    :return: the numbers of appearances of the given word upwards in the matrix
    """
    count = 0
    for row in range(len(word)-1, len(matrix)):
        for col in range(len(matrix[row])):
            if word[0] == matrix[row][col]:
                if word_appears_up(word, row, col, matrix):
                    count += 1
    return count


def word_appears_up(word, row, col, matrix):
    """
    Determines whether an appearance of the first letter of a word continues to be the actual word
    in the up direction
    :param word: Current word searched for
    :param row: row of current cell searched in the matrix
    :param col: column of current cell searched in the matrix
    :param matrix: matrix searched
    :return: True if the word appears. False otherwise
    """
    for letter in range(1, len(word)):
        if word[letter] != matrix[row-letter][col]:
            return False
    return True
# endregion


def search_down(word, matrix):
    """
    Searches for a word in the matrix in the up direction
    :param word: The current word searched for
    :param matrix: The matrix searched
    :return: the number of appearances of the word in the matrix in the down direction
    """
    return search_up(word[::-1], matrix)


# region searching right
def search_right(word, matrix):
    """
    Searches for a word in the matrix in the right direction
    :param word: The current word searched for
    :param matrix: The matrix searched
    :return: the number of appearances of the word in the matrix in the right direction
    """
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])-len(word)+1):
            if word[0] == matrix[row][col]:
                if word_appears_right(word, row, col, matrix):
                    count += 1
    return count


def word_appears_right(word, row, col, matrix):
    """
    Determines whether an appearance of the first letter of a word continues to be the actual word
    in the right direction
    :param word: Current word searched for
    :param row: row of current cell searched in the matrix
    :param col: column of current cell searched in the matrix
    :param matrix: matrix searched
    :return: True if the word appears. False otherwise
    """
    for letter in range(1, len(word)):
        if word[letter] != matrix[row][col+letter]:
            return False
    return True

# endregion


def search_left(word, matrix):
    """
    Searches for a word in the matrix in the left direction
    :param word: The current word searched for
    :param matrix: The matrix searched
    :return: the number of appearances of the word in the matrix in the left direction
    """
    return search_right(word[::-1], matrix)


# region searching up right
def search_up_right(word, matrix):
    """
    Searches for a word in the matrix in the up-right direction
    :param word: The current word searched for
    :param matrix: The matrix searched
    :return: the number of appearances of the word in the matrix in the up-right direction
    """
    count = 0
    for row in range(len(word)-1, len(matrix)):
        for col in range(len(matrix[0])-len(word)+1):
            if word[0] == matrix[row][col]:
                if word_appears_up_right(word, row, col, matrix):
                    count += 1
    return count


def word_appears_up_right(word, row, col, matrix):
    """
    Determines whether an appearance of the first letter of a word continues to be the actual word
    in the up-right direction
    :param word: Current word searched for
    :param row: row of current cell searched in the matrix
    :param col: column of current cell searched in the matrix
    :param matrix: matrix searched
    :return: True if the word appears. False otherwise
    """
    for letter in range(1, len(word)):
        if word[letter] != matrix[row-letter][col+letter]:
            return False
    return True
# endregion


# region searching up left
def search_up_left(word, matrix):
    """
    Searches for a word in the matrix in the up-left direction
    :param word: The current word searched for
    :param matrix: The matrix searched
    :return: the number of appearances of the word in the matrix in the up-left direction
    """
    count = 0
    for row in range(len(word)-1, len(matrix)):
        for col in range(len(word)-1, len(matrix[0])):
            if word[0] == matrix[row][col]:
                if word_appears_up_left(word, row, col, matrix):
                    count += 1
    return count


def word_appears_up_left(word, row, col, matrix):
    """
    Determines whether an appearance of the first letter of a word continues to be the actual word
    in the up-left direction
    :param word: Current word searched for
    :param row: row of current cell searched in the matrix
    :param col: column of current cell searched in the matrix
    :param matrix: matrix searched
    :return: True if the word appears. False otherwise
    """
    for letter in range(1, len(word)):
        if word[letter] != matrix[row-letter][col-letter]:
            return False
    return True
# endregion


def search_down_right(word, matrix):
    """
    Searches for a word in the matrix in the down-right direction
    :param word: The current word searched for
    :param matrix: The matrix searched
    :return: the number of appearances of the word in the matrix in the down-right direction
    """
    return search_up_left(word[::-1], matrix)


def search_down_left(word, matrix):
    """
    Searches for a word in the matrix in the down-left direction
    :param word: The current word searched for
    :param matrix: The matrix searched
    :return: the number of appearances of the word in the matrix in the down-left direction
    """
    return search_up_right(word[::-1], matrix)
# endregion
# endregion
# endregion


# region write output
def write_output(results, filename):
    """
    Creates the file of the search results
    :param results: list of tuples (pairs) of words and their number of appearances
    :param filename: The name of the file to be created
    :return: None
    """
    with open(filename, 'w') as file:
        for pair in results:
            file.writelines([str(pair[0]) + ',' + str(pair[1]) + "\n"])
# endregion


def input_ok():
    """
    Checks the command line input
    :return: True if input is valid. Falst otherwise
    """
    if len(sys.argv) < 5:
        print(LACKING_ARGUMENTS)
        return False
    if not path.exists(sys.argv[1]):
        print(WORD_LIST_NOT_FOUND)
        return False
    if not path.exists(sys.argv[2]):
        print(MATRIX_NOT_FOUND)
        return False
    for letter in sys.argv[4]:
        if letter not in {'u', 'd', 'l', 'r', 'w', 'x', 'y', 'z'}:
            print(INVALID_DIRECTIONS)
            return False
    return True


def main():
    if input_ok():
        words_list = read_wordlist(sys.argv[1])
        matrix = read_matrix(sys.argv[2])
        results = find_words(words_list, matrix, sys.argv[4])
        write_output(results, sys.argv[3])


if __name__ == '__main__':
    main()

from tailor.types.location import Location
from tailor.utils.sourcefile import file_too_long, num_lines_in_file


class FileListener:
    # pylint: disable=too-few-public-methods

    def __init__(self, printer, filepath):
        self.__printer = printer
        self.__filepath = filepath

    def verify(self, max_lines):
        self.__verify_file_length(max_lines)

    def __verify_file_length(self, max_lines):
        if file_too_long(self.__filepath, max_lines):
            self.__printer.error('File is over maximum line limit (' +
                                 str(num_lines_in_file(self.__filepath)) +
                                 '/' + str(max_lines) + ')',
                                 loc=Location(max_lines, 1))

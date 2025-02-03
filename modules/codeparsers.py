class CBCodeParsers:
    def get_classes_in_file(self, file):
        """
        Retrieves the classes in a given file.
        :param file: The file to parse for classes.
        """
        print('Code parsers initialized')

    def get_functions_in_class(self, file, class_name):
        """
        Retrieves the functions in a given class within a file.
        :param file: The file containing the class.
        :param class_name: The name of the class to parse for functions.
        """
        print('Code parsers initialized')

    def get_ast_tree_in_file(self, file, class_name):
        """
        Generates an Abstract Syntax Tree (AST) for a given file.
        :param file: The file to generate an AST for.
        :param class_name: The name of the class to focus the AST generation on.
        """
        pass

cbcodeparsers = CBCodeParsers()

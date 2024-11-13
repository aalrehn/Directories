
class DirectoryStructure:

    def __init__(self):
        self.root = {}

    def create_directory(self, path: str) -> str:
        """
        Creates a new directory.

        Args:
            path (str): The full directory path to create, e.g., 'fruits/apples/fuji'.

        Returns:
            str: A message indicating the result of the operation.
        """

        current = self.root
        for folder in path.strip('/').split('/'):
            if folder not in current:
                current[folder] = {}
            current = current[folder]
        return f"CREATE {path}"

    def locate_directory(self, path: str) -> (bool, dict):
        """
        Locates a directory within the directory tree.

        Args:
            path (str): The full path of the directory to locate, e.g., 'fruits/apples'.

        Returns:
            tuple: A tuple containing:
                - bool: True if the directory exists, False otherwise.
                - dict or str: The parent directory (dict) if found, or the missing directory name (str) if not found.
        """

        parent, current = None, self.root
        for folder in path.strip('/').split('/'):
            if folder not in current:
                return False, folder
            parent = current
            current = current[folder]
        return True, parent

    def delete_directory(self, path: str) -> str:
        """
        Deletes a specified directory from the directory tree.

        Args:
            path (str): The full path of the directory to delete, e.g., 'fruits/apples'.

        Returns:
            str: A message indicating the result of the delete operation. If the directory
                 does not exist, returns an error message specifying that it was not found.
        """

        messages = [f"DELETE {path}"]
        exists, parent = self.locate_directory(path)
        if not exists:
            messages.append(f"Cannot delete {path} - {parent} does not exist")
            return "\n".join(messages)
        directory = path.strip('/').split('/')[-1]
        parent.pop(directory)
        return "\n".join(messages)

    def move_directory(self, src: str, dest: str) -> str:
        """
        Moves a directory from a source path to a destination path within the directory tree.

        Args:
            src (str): The full path of the directory to move, e.g., 'fruits/apples'.
            dest (str): The full path of the destination directory, e.g., 'vegetables'.

        Returns:
            str: A message indicating the result of the move operation. If the source or
                 destination does not exist, returns an error message specifying which
                 path was not found.
        """

        messages = [f"MOVE {src} {dest}"]
        # Locate source directory
        exists_src, parent_src = self.locate_directory(src)
        if not exists_src:
            messages.append(f"Cannot move {src} - {parent_src} does not exist")
            return "\n".join(messages)
        # Locate destination directory
        exists_dest, parent_dest = self.locate_directory(dest)
        if not exists_dest:
            messages.append(f"Cannot move {src} - {parent_dest} does not exist")
            return "\n".join(messages)
        # Move the directory
        directory_name = src.strip('/').split('/')[-1]
        directory_to_move = parent_src.pop(directory_name)
        dest_directory = dest.strip('/').split('/')[-1]
        parent_dest[dest_directory][directory_name] = directory_to_move
        return "\n".join(messages)

    def show_structure(self) -> str:
        """
        Displays the current directory structure in a hierarchical format.

        Returns:
            str: A formatted string representing the directory tree structure,
                 with each level indented to show hierarchy.
        """

        messages = ["LIST"]

        def recurse_display(directory: dict, level=0):

            for key in sorted(directory.keys()):
                messages.append('  ' * level + key)
                recurse_display(directory[key], level + 1)

        recurse_display(directory=self.root)
        return "\n".join(messages)

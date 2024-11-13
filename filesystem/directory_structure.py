
class DirectoryStructure:

    def __init__(self):
        self.root = {}

    def create_directory(self, path: str) -> str:

        current = self.root
        for folder in path.strip('/').split('/'):
            if folder not in current:
                current[folder] = {}
            current = current[folder]
        return f"CREATE {path}"

    def locate_directory(self, path: str) -> (bool, dict):

        parent, current = None, self.root
        for folder in path.strip('/').split('/'):
            if folder not in current:
                return False, folder
            parent = current
            current = current[folder]
        return True, parent

    def delete_directory(self, path: str) -> str:

        messages = [f"DELETE {path}"]
        exists, parent = self.locate_directory(path)
        if not exists:
            messages.append(f"Cannot delete {path} - {parent} does not exist")
            return "\n".join(messages)
        directory = path.strip('/').split('/')[-1]
        parent.pop(directory)
        return "\n".join(messages)

    def move_directory(self, src: str, dest: str) -> str:

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

        messages = ["LIST"]

        def recurse_display(directory: dict, level=0):

            for key in sorted(directory.keys()):
                messages.append('  ' * level + key)
                recurse_display(directory[key], level + 1)

        recurse_display(directory=self.root)
        return "\n".join(messages)

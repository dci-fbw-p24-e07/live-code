"""Document folder module."""


def get_path(label_name=None):
    """Return the path of a label by its name."""
    return '/path/' + label_name


class DocumentFolder:
    """Document folder class.

    Attributes
    ----------
        - label_name: <str>
        - label_style: <str>

    Methods
    -------
        - get_label() -> <dict>

    """

    label_name = "Folder name"
    label_style = "bold"

    def get_label(self):
        """Return a label dictionary."""
        return {
            "path": get_path(self.label_name),
            "style": self.label_style
        }


document_folder = DocumentFolder()
print(document_folder.get_label())

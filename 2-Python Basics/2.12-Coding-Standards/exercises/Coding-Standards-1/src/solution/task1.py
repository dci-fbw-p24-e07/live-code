def get_path(label_name=None):
    return '/path/' + label_name


class DocumentFolder:
    label_name = "Folder name"
    label_style = "bold"

    def get_label(self):
        return {
            "path": get_path(self.label_name),
            "style": self.label_style
        }


document_folder = DocumentFolder()
print(document_folder.get_label())

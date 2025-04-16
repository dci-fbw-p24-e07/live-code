import os


class FileWorker:


    def rm(self, file_name: str):
        if os.path.isfile(file_name):
            os.remove(file_name)
        
    def create(self, file_name, initial_text):
        with open(file_name, "w") as file:
            file.write(initial_text)

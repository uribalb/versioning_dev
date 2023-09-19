import os
from pathlib import Path

class Directory:
    def __init__(self, project_root):
        self.project_root = project_root

    def tree(self):
        Path(self.project_root+"/data/cleaned").mkdir(parents=True, exist_ok=True)
        Path(self.project_root+"/data/processed").mkdir(parents=True, exist_ok=True)
        Path(self.project_root+"/data/raw").mkdir(parents=True, exist_ok=True)
        Path(self.project_root+"/docs").mkdir(parents=True, exist_ok=True)
        Path(self.project_root+"/models").mkdir(parents=True, exist_ok=True)
        Path(self.project_root+"/notebooks").mkdir(parents=True, exist_ok=True)
        Path(self.project_root+"/reports").mkdir(parents=True, exist_ok=True)
        Path(self.project_root+"/src").mkdir(parents=True, exist_ok=True)

        self.edit_files()

    
    def edit_files(self):
        # Création des fichiers spécifiques avec du contenu générique
        with open(os.path.join(self.project_root, 'data/cleaned', 'data.csv'), 'w') as f:
            f.write("Name,Email,Phone,Description")

        with open(os.path.join(self.project_root, 'data/processed', 'data.csv'), 'w') as f:
            f.write("Name,Email,Phone,Description")

        with open(os.path.join(self.project_root, 'data/raw', 'data.csv'), 'w') as f:
            f.write("Name,Email,Phone,Description")
            
        with open(os.path.join(self.project_root, 'docs', 'docs.txt'), 'w') as f:
            f.write("docs")

        with open(os.path.join(self.project_root, 'models', 'model.json'), 'w') as f:
            f.write('{"1":"0"}')

        with open(os.path.join(self.project_root, 'reports', 'report.txt'), 'w') as f:
            f.write("dummy file")

        with open(os.path.join(self.project_root, 'LICENSE'), 'w') as f:
            f.write("Creative Commons")

        with open(os.path.join(self.project_root, 'Makefile'), 'w') as f:
            f.write("Makefile")

        with open(os.path.join(self.project_root, 'notebooks', 'main.ipynb'), 'w') as f:
            f.write("import numpy as np")

        with open(os.path.join(self.project_root, 'README.md'), 'w') as f:
            f.write("## Template Project")

        with open(os.path.join(self.project_root, 'requirements.txt'), 'w') as f:
            f.write("docopt == 0.6.1")

        # Création du fichier utils.py avec du contenu générique
        dummy_code = """
        import numpy
        
        arr = np.array([1,2,3])
        """
        with open(os.path.join(self.project_root, 'src', 'utils.py'), 'w') as f:
            f.write(dummy_code)
        with open(os.path.join(self.project_root, 'src', 'process.py'), 'w') as f:
            f.write(dummy_code)
        with open(os.path.join(self.project_root, 'src', 'train.py'), 'w') as f:
            f.write(dummy_code)

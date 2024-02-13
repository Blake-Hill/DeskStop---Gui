from PySide6.QtWidgets import QWidget, QMessageBox, QListWidget ,QPushButton, QLineEdit, QLabel, QSizePolicy, QHBoxLayout, QVBoxLayout, QSizePolicy
import os.path

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DeskStop")

        #create QLabels
        sourceLabel = QLabel("Directory to clean: ")
        targetLabel = QLabel("Directory to sort into: ")
        self.targetSuccessLabel = QLabel()
        whitelistLabel = QLabel("Path to files that should not be moved: ")
        #create QListWidgets
        self.sourceList = QListWidget(self)
        self.whitelistList = QListWidget(self)
        #create QlineEdits
        self.sourceEdit = QLineEdit()
        self.targetEdit = QLineEdit()
        self.whitelistEdit = QLineEdit()
        #create QPushButtons 
        sourceButton = QPushButton("Add")
        targetButton = QPushButton("Set")
        whitelistButton = QPushButton("Add")
        cleanButton = QPushButton("Clean!")

        #set SizePolicy's of all labels and buttons, which should not change
        sourceLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        targetLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.targetSuccessLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        whitelistLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sourceButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        targetButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        whitelistButton.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        #set SizePolicy's of LineEdits, which should expand horizontally but not vertically
        self.sourceEdit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.targetEdit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.whitelistEdit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        #connect buttons to click slots
        sourceButton.clicked.connect(self.source_button_clicked)
        targetButton.clicked.connect(self.target_button_clicked)
        whitelistButton.clicked.connect(self.whitelist_button_clicked)
        cleanButton.clicked.connect(self.clean_button_clicked)

        #Layout Group 1
        hLayout1 = QHBoxLayout()
        hLayout1.addWidget(sourceLabel)
        hLayout1.addWidget(self.sourceEdit)
        hLayout1.addWidget(sourceButton)
        #Layout group 2
        hLayout2 = QHBoxLayout()
        hLayout2.addWidget(whitelistLabel)
        hLayout2.addWidget(self.whitelistEdit)
        hLayout2.addWidget(whitelistButton)
        #Layout group 3
        hLayout3 = QHBoxLayout()
        hLayout3.addWidget(targetLabel)
        hLayout3.addWidget(self.targetEdit)
        hLayout3.addWidget(targetButton)
        #add hLayouts to vLayout
        vLayout = QVBoxLayout()
        vLayout.addLayout(hLayout1)
        vLayout.addWidget(self.sourceList)
        vLayout.addLayout(hLayout2)
        vLayout.addWidget(self.whitelistList)
        vLayout.addLayout(hLayout3)
        vLayout.addWidget(self.targetSuccessLabel)
        vLayout.addWidget(cleanButton)
        vLayout.addStretch()

        self.setLayout(vLayout)

    
    def source_button_clicked(self):
        self.checkSource()

    def target_button_clicked(self):
        self.checkTarget()

    def whitelist_button_clicked(self):
        self.checkWhitelist()

    def clean_button_clicked(self):
        self.performClean()

    def checkSource(self):
        if os.path.isdir(self.sourceEdit.text()):
            self.sourceList.addItem(self.sourceEdit.text())
            self.sourceEdit.clear()
        else:
            QMessageBox.information(self, "Whoops", 
                                        "The source path provided does not lead to a valid directory",
                                        QMessageBox.Ok)
    def checkTarget(self):
        if os.path.isdir(self.targetEdit.text()):
            self.targetSuccessLabel.setText(self.targetEdit.text())
            self.targetEdit.clear()
        else:
            QMessageBox.information(self, "Whoops", 
                                        "The source path provided does not lead to a valid directory",
                                        QMessageBox.Ok)

    def checkWhitelist(self):
        if os.path.isfile(self.whitelistEdit.text().strip('"')):
            self.whitelistList.addItem(self.whitelistEdit.text().strip('"'))
            self.whitelistEdit.clear()
        else:
            QMessageBox.information(self, "Whoops", 
                                        "The source path provided does not lead to a valid directory",
                                        QMessageBox.Ok)
    
    def performClean(self):
    #retrieve settings from config files
        sources = [self.sourceList.item(x).text() for x in range(self.sourceList.count())]
        targetDir = self.targetSuccessLabel.text()
        whitelist = [self.whitelistList.item(x).text() for x in range(self.whitelistList.count())]

        #create sub-directories to sort files into
        try:
            os.mkdir(f"{targetDir}\\office")
            os.mkdir(f"{targetDir}\\office\\excel")
            os.mkdir(f"{targetDir}\\office\\word")
            os.mkdir(f"{targetDir}\\office\\powerpoint")
            os.mkdir(f"{targetDir}\\photos")
            os.mkdir(f"{targetDir}\\videos")
            os.mkdir(f"{targetDir}\\text")
            os.mkdir(f"{targetDir}\\audio")
            os.mkdir(f"{targetDir}\\other")
        except FileExistsError:
            pass
        
        #iterate through all the source directories and check the file against the whitelist then sort
        for sourceDir in sources:
            files = os.listdir(sourceDir)
            for file in files:
                if f"{sourceDir}\\{file}" in whitelist:
                    continue
                else:
                    #sort based on extension of file
                    extension = file.split(".")[-1]
                    match extension:
                        case "docx":
                                os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\office\\word\\{file}")
                        case "doc":
                            os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\office\\word\\{file}")
                        case "pptx":
                            os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\office\\powerpoint\\{file}")
                        case "xlsx":
                            os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\office\\excel\\{file}")
                        case "csv":
                            os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\office\\excel\\{file}")
                        case "txt":
                            os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\text\\{file}")
                        case "rtf":
                            os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\text\\{file}")
                        case "mp4":
                            os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\videos\\{file}")
                        case "mov":
                            os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\videos\\{file}")
                        case "wmv":
                            os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\videos\\{file}")
                        case "jpg":
                            os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\photos\\{file}")
                        case "jpeg":
                            os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\photos\\{file}")
                        case "png":
                            os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\photos\\{file}")
                        case "mp3":
                            os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\audio\\{file}")
                        case "wav":
                            os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\audio\\{file}")
                        case _:
                            os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\other\\{file}")  
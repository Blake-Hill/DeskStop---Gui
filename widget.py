from PySide6.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QSizePolicy, QHBoxLayout, QVBoxLayout, QSizePolicy

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DeskStop")

        #create QLabels
        sourceLabel = QLabel("Directory to clean: ")
        targetLabel = QLabel("Directory to sort into: ")
        whitelistLabel = QLabel("File names that should not be moved: ")
        #create lineEdits
        self.sourceEdit = QLineEdit()
        self.targetEdit = QLineEdit()
        self.whitelistEdit = QLineEdit()
        #create QPushButtons 
        sourceButton = QPushButton("Add")
        targetButton = QPushButton("Set")
        whitelistButton = QPushButton("Add")

        #set SizePolicy's of all labels and buttons, which should not change
        sourceLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        targetLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
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

        #Layout Group 1
        hLayout1 = QHBoxLayout()
        hLayout1.addWidget(sourceLabel)
        hLayout1.addWidget(self.sourceEdit)
        hLayout1.addWidget(sourceButton)
        #Layout group 2
        hLayout2 = QHBoxLayout()
        hLayout2.addWidget(targetLabel)
        hLayout2.addWidget(self.targetEdit)
        hLayout2.addWidget(targetButton)
        #Layout group 3
        hLayout3 = QHBoxLayout()
        hLayout3.addWidget(whitelistLabel)
        hLayout3.addWidget(self.whitelistEdit)
        hLayout3.addWidget(whitelistButton)
        #add hLayouts to vLayout
        vLayout = QVBoxLayout()
        vLayout.addLayout(hLayout1)
        vLayout.addLayout(hLayout2)
        vLayout.addLayout(hLayout3)
        vLayout.addStretch()

        self.setLayout(vLayout)

    
    def source_button_clicked(self):
        print(self.sourceEdit.text())

    def target_button_clicked(self):
        print(self.targetEdit.text())

    def whitelist_button_clicked(self):
        print(self.whitelistEdit.text())
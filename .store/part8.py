class window3(QWidget):  # 主程序的代码块（Find a dirty word!）
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 设置窗口内布局
        # self.setUpMainWindow()
        # self.resize(839, 950)
        self.center()
        self.setWindowTitle("A shield")
        self.setFocus()
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        # self.show()
        self.setMinimumSize(0, 0)
        self.setMaximumSize(1640, 978)
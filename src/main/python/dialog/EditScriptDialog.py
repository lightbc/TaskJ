import os
import Script
import TaskJWin
import util.FileUtil as FileUtil
import util.RandomUtil as RandomUtil
import util.OSUtil as OSUtil
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui


class EditScriptDialog(QtWidgets.QDialog, Script.Ui_Form, TaskJWin.Ui_MainWindow):
    """脚本编辑对话框"""

    def __init__(self, parent=None):
        super(EditScriptDialog, self).__init__(parent)
        self.temp_file_path = None
        self.filePath = None
        self.fileName = None
        self.setupUi(self)
        self.open()
        # true：脚本文件非第一次保存，false：脚本文件第一次保存
        self.isSave = False
        # true：显示未保存图标，false：显示已保存图标
        self.isUnSaveIcon = False
        self.toolBarActionListener()

    def toolBarActionListener(self):
        """工具栏事件监听"""
        self.save_action.triggered.connect(self.scriptSave)
        self.run_action.triggered.connect(self.scriptRun)
        self.textEdit.textChanged.connect(self.textChanged)

    def scriptSave(self):
        """编辑脚本内容保存"""
        content = self.textEdit.toPlainText()
        if content:
            if not self.isSave:
                # 打开保存文件对话框，仅支持bat文件保存
                fileDialog = QtWidgets.QFileDialog()
                resp = fileDialog.getSaveFileName(self, "保存", "./", "BAT(*.bat)")
                self.filePath = resp[0]
                # 判断是否选择保存路径和填写保存文件名称
                if self.filePath:
                    self.fileName = os.path.basename(self.filePath)
                    self.isSave = True
                    self.isUnSaveIcon = False
                    self.setSaveIcon()
            else:
                self.isUnSaveIcon = False
                self.setSaveIcon()
            if self.filePath:
                FileUtil.write(self.filePath, content)
                # print("保存路径:%s,保存文件名:%s" % (self.filePath, self.fileName))

    def scriptRun(self):
        """脚本实时效果预览"""
        content = self.textEdit.toPlainText()
        if content:
            # 将编辑的脚本内容保存为临时脚本文件执行，退出后删除临时脚本文件
            temp_dir = OSUtil.getAppTempDir()
            file_name = RandomUtil.getUUID() + ".bat"
            self.temp_file_path = temp_dir + os.sep + file_name
            FileUtil.write(self.temp_file_path, content)
            # 获取路径盘符信息
            drive = os.path.splitdrive(temp_dir)[0]
            # 切换文件保存目录，执行bat文件
            cmd = "cd " + temp_dir + " && " + drive + " && " + file_name
            os.system("chcp 65001")
            os.system(cmd)

    def textChanged(self):
        """文本框文本内容实时监听"""
        content = self.textEdit.toPlainText()
        if content:
            self.isUnSaveIcon = True
        else:
            self.isUnSaveIcon = False
        self.setSaveIcon()

    def setSaveIcon(self):
        """设置保存菜单实时显示图标"""
        icon = self.getSaveIcon()
        self.save_action.setIcon(icon)

    def getSaveIcon(self):
        """获取保存菜单显示图标"""
        res_path = "../resources/images/"
        icon = QtGui.QIcon()
        if self.isUnSaveIcon:
            # 显示未保存图标
            icon.addPixmap(QtGui.QPixmap(res_path + "unsave.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        else:
            # 显示已保存图标
            icon.addPixmap(QtGui.QPixmap(res_path + "save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        return icon

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        """关闭窗体前删除临时文件"""
        if self.temp_file_path:
            FileUtil.removeFile(self.temp_file_path)

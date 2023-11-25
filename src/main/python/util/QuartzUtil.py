import os
from apscheduler.schedulers.background import BackgroundScheduler
from util import FileUtil, LoggerUtil, OSUtil
from entity import NewCreate
from TaskJ import TaskJ


class QuartzUtil:
    """调度任务工具类"""

    def __init__(self, app: TaskJ):
        self.logger = LoggerUtil.getLogger(showLog=app.showLog)
        try:
            self.scheduler = BackgroundScheduler(timezone='Asia/Shanghai')
            self.scheduler.start()
        except Exception as e:
            self.logger.error(e)

    def createJob(self, nid):
        """
        创建Job
        :param nid:识别主键
        :return:
        """
        if self.isAlive(nid):
            self.logger.warning("调度任务已存在，无法重复创建")
            return
        self.logger.info("开始获取调度任务信息")
        task_cfg = getTaskCfg(nid)
        if task_cfg:
            nc = NewCreate.NewCreate()
            try:
                self.task = nc.from_dict(task_cfg)
                self.logger.info("信息反序列化成功")
            except Exception as e:
                self.logger.error("信息反序列化失败")
                self.logger.error(e)
                return
            if self.task.opType == "单次":
                self.runOnce()
            elif self.task.opType == "循环":
                self.runLoop()
        else:
            self.logger.info("未获取到指定的调度任务信息")

    def isAlive(self, nid):
        """
        判断是否已存在相同的Job
        :param nid: 识别主键
        :return:true-存在，false-不存在
        """
        if self.scheduler and self.scheduler.get_job(nid):
            return True
        return False

    def runOnce(self):
        """单次执行"""
        if timeCompare(self.task.runTime) == -1:
            self.logger.warning("当前时间已超过执行开始时间！")
        else:
            self.scheduler.add_job(self.cmd, "date", run_date=self.task.runTime, id=self.task.nId)

    def runLoop(self):
        """循环执行"""
        if timeCompare(self.task.stopTime) == -1:
            self.logger.warning("当前时间已超过执行结束时间！")
        else:
            if self.task.cycleVal:
                cv = int(self.task.cycleVal)
                if self.task.cycleType == "秒":
                    self.scheduler.add_job(self.cmd, "interval", seconds=cv, start_date=self.task.runTime,
                                           end_date=self.task.stopTime, id=self.task.nId)
                elif self.task.cycleType == "分钟":
                    self.scheduler.add_job(self.cmd, "interval", minutes=cv, start_date=self.task.runTime,
                                           end_date=self.task.stopTime, id=self.task.nId)
                elif self.task.cycleType == "小时":
                    self.scheduler.add_job(self.cmd, "interval", hours=cv, start_date=self.task.runTime,
                                           end_date=self.task.stopTime, id=self.task.nId)
                elif self.task.cycleType == "天":
                    self.scheduler.add_job(self.cmd, "interval", days=cv, start_date=self.task.runTime,
                                           end_date=self.task.stopTime, id=self.task.nId)
                elif self.task.cycleType == "周":
                    self.scheduler.add_job(self.cmd, "interval", weeks=cv, start_date=self.task.runTime,
                                           end_date=self.task.stopTime, id=self.task.nId)

    def cmd(self):
        """命令执行"""
        # 设置UTF-8编码输出，防止出现乱码情况
        os.system("chcp 65001")
        self.logger.info("调度任务【%s】开始执行" % self.task.name)
        self.logger.info("调度任务ID:%s" % self.task.nId)
        if self.task.runMode == "命令行":
            self.runCmdCode()
        elif self.task.runMode == "文件":
            self.runCmdFile()
        self.logger.info("调度任务【%s】结束执行" % self.task.name)

    def runCmdCode(self):
        """运行命令行（单行/多行）"""
        ct = os.system(self.task.runCmd)
        self.logger.info("命令行执行返回结果：【%s】" % str(ct))

    def runCmdFile(self):
        """运行bat文件"""
        # 获取文件父级目录路径
        dir_path = os.path.dirname(self.task.runCmd)
        # 获取盘符
        drive = os.path.splitdrive(dir_path)[0]
        # 获取文件名称
        file_name = os.path.basename(self.task.runCmd)
        # 拼接多行命令行，执行bat文件
        cmd = "cd %s && %s && %s" % (dir_path, drive, file_name)
        ct = os.system(cmd)
        self.logger.info("命令文件执行返回结果：【%s】" % str(ct))

    def removeJob(self, nid):
        """
        删除任务Job
        :param nid:识别主键，job_id
        :return:
        """
        if self.scheduler:
            job = self.scheduler.get_job(nid)
            if job:
                job.remove()
                self.logger.info("调度任务【%s】停止执行！" % nid)
            else:
                self.logger.info("无任务ID【%s】任务正在执行！" % nid)

            jobs = self.scheduler.get_jobs()
            if not jobs and len(jobs) == 0:
                LoggerUtil.shutDown()

    def allRunTaskStop(self):
        """全部任务停止，日志处理程序关闭"""
        if self.scheduler:
            jobs = self.scheduler.get_jobs()
            if jobs and len(jobs) > 0:
                self.scheduler.remove_all_jobs()
            self.logger.info("全部调度任务已停止执行，日志处理程序将关闭！")
            LoggerUtil.shutDown()


def getTaskCfg(nid):
    """
    获取指定任务配置数据
    :param nid: 识别主键
    :return: task
    """
    # 获取配置数据
    cfg = FileUtil.getCfg()
    if cfg and len(cfg) > 0:
        for task in cfg:
            if task["nId"] == nid:
                return task
    return None


def timeCompare(t):
    """
    执行开始/结束时间比较
    :param t: 开始/结束时间
    :return: -1-指定时间小于当前时间，0-指定时间等于当前时间，1-指定时间大于当前时间
    """
    rt = OSUtil.strToTimeStamp(t)
    res = OSUtil.compareWithCurrent(rt)
    return res

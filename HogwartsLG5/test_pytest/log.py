#!/usr/bin/python

import logging
import logging.handlers

def mylog():

    # 生成一个日志对象
    # 生成一个Handler。logging支持许多Handler，例如FileHandler, SocketHandler, SMTPHandler等，
    # 我由于要写文件就使用了FileHandler。
    logger = logging.getLogger('test_calc_new')
    # handler = logging.FileHandler("./my_log/mylog.txt")

    # 设置日志信息输出的级别。logging提供多种级别的日志信息，如：NOTSET,
    # DEBUG, INFO, WARNING, ERROR, CRITICAL等。每个级别都对应一个数值。
    # 如果不执行此句，缺省为30(WARNING)。可以执行：logging.getLevelName
    # (logger.getEffectiveLevel())来查看缺省的日志级别。日志对象对于不同
    # 的级别信息提供不同的函数进行输出，如：info(), error(), debug()等。当
    # 写入日志时，小于指定级别的信息将被忽略。因此为了输出想要的日志级别一定
    # 要设置好此参数。这里我设为NOTSET（值为0），也就是想输出所有信息
    logger.setLevel(level = logging.DEBUG)


    # 生成一个格式器，用于规范日志的输出格式。如果没有这行代码，那么缺省的
    # 格式就是："%(message)s"。也就是写日志时，信息是什么日志中就是什么，
    # 没有日期，没有信息级别等信息。logging支持许多种替换值，详细请看
    # Formatter的文档说明。这里有三项：时间，信息级别，日志信息
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # 需要导入import logging.handlers
    # 当工程运行一段时间后，会发现日志文件越来越大，而且也不便于查找某天的错误信息。这就需要我们对日志进行分割，
    # 分割形式有两种：RotatingFileHandler（按照文件大小分割）、TimedRotatingFileHandler（按照时间间隔分割）
    # 其中maxBytes指定每个日志文件的大小，如果文件超过1024KB就分割该日志文件，最大的备份文件个数是40个。到LOG_FILE所在目录下查看，发现除了debug.log文件外，还多了debug.log
    # .1，debug.log.2等文件。
    # handler = logging.handlers.RotatingFileHandler('./my_log/mylog.txt', maxBytes=1024 * 1024, backupCount=40)

    # 需要导入import logging.handlers
    # when参数可设置为S-second（按秒对日志进行分割），
    # M-Minutes（按分钟对日志进行分割），H-Hours（按小时对日志进行分割），D-Days（按天对日志进行分割），
    # midnigh-roll over at midnight（每天半夜对日志进行回滚），W{0-6}-roll over on a certain day;0-Monday（按照指定的日期如0-周一对日志进行回滚）。
    # when参数默认是“h”按小时分割，该参数对大小写不敏感，所以无所谓是H还是h了。
    # interval参数默认“1”，如果when=‘h’，那么就是每一小时对日志进行一次分割，即debug.log所在目录会出现 debug.log.2013-06-28_13，debug.log.2013-06-28_14等日志文件
    handler = logging.handlers.TimedRotatingFileHandler('./mylog/mylog.txt', when='M', interval=1, backupCount=40)
    handler.setLevel(logging.DEBUG)
    # 将格式器设置到处理器上
    handler.setFormatter(formatter)

    # 将处理器加到日志对象上
    logger.addHandler(handler)
    return logger

logging = mylog()
logging.info("Start print log")
logging.debug("Do something")
logging.warning("Something maybe fail.")
logging.info("Finish")
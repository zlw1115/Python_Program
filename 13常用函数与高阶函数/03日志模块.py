'''
日志等级
低-高
debug
info
warnning
error
critical
'''

'''
开发应用程序或部署开发环境时，可以使用DEBUG或INFO级别的日志获取尽可能详细的日志信息来进行开发或部署调试；
应用上线或部署生产环境时，应该使用WARNING或ERROR或CRITICAL级别的日志来降低机器的I/O压力和提高获取错误日志信息的效率。
日志级别的指定通常都是在应用程序的配置文件中进行指定的。
'''

'''
logging模块提供了两种记录日志的方式：
    第一种方式是使用logging提供的模块级别的函数
    第二种方式是使用Logging日志系统的四大组件
    
logging模块定义的模块级别的常用函数
函数	说明
logging.debug(msg, *args, **kwargs)	创建一条严重级别为DEBUG的日志记录
logging.info(msg, *args, **kwargs)	创建一条严重级别为INFO的日志记录
logging.warning(msg, *args, **kwargs)	创建一条严重级别为WARNING的日志记录
logging.error(msg, *args, **kwargs)	创建一条严重级别为ERROR的日志记录
logging.critical(msg, *args, **kwargs)	创建一条严重级别为CRITICAL的日志记录
logging.log(level, *args, **kwargs)	创建一条严重级别为level的日志记录
loggin.basicConfig(**kwargs)	对root logger进行一次性配置

logging.basicConfig(**kwargs)函数用于指定“要记录的日志级别”、“日志格式”、“日志输出位置”、“日志文件的打开模式”等信息，
其他几个都是用于记录各个级别日志的函数。
loggin.basicConfig参数如下
参数名     作用              举例
level      日志输出等级       level=logging.DEBUG
format      日志输出格式      
filename    存储位置        filename='d://back.log'
filemode    输入模式        filemode='w'，该选项要在filename指定的情况下才生效
level	    指定日志器的日志级别

datefmt	    指定日期/时间格式。需要注意的是，该选项要在format中包含时间字段%(asctime)s时才有效
stream	    指定日志输出目标stream，如sys.stdout、sys.stderr以及网络stream。需要说明的是，stream和filename不能同时提供，否则会引发 ValueError异常
style	    Python 3.2中新添加的配置项。指定format格式字符串的风格，可取值为'%'、'{'和'$'，默认为'%'
handlers	Python 3.3中新添加的配置项。该选项如果被指定，它应该是一个创建了多个Handler的可迭代对象，这些handler将会被添加到root logger。需要说明的是：filename、stream和handlers这三个配置项只能有一个存在，不能同时出现2个或3个，否则会引发ValueError异常。

format具体格式
格式符                 含义  
%(levelname)s       日志级别名称
%(pathname)s        执行程序的路径
%(filename)s        执行程序名
%(lineno)d          日志的当前行号
%(asctime)s         打印日志的时间
%(message)s         日志信息

format = '%(asctime)s %(filename)s[line:%lineno)d]%(levelname)s%(message)s'

logging模块的四大组件
组件              说明
loggers        提供应用程序代码直接使用的接口
handlers        用于将日志记录发送到指定的目的位置
filters         提供更细粒度的日志过滤功能，用于决定那些日志记录将会被输出（其他的日志及记录将会被忽略）
formatters      用于控制日志信息的最终输出格式

说明： logging模块提供的模块级别的那些函数实际上也是通过这几个组件的相关实现类来记录日志的，只是在创建这些类的实例时设置了一些默认值。

说明：
    logging.basicConfig()函数是一个一次性的简单配置工具集，也就是说只有在第一次调用该函数时会起作用，
    后续再次调用该函数时完全不会产生任何操作，多次调用的设置并不是雷焦操作
    
    日志器（Logger）是又层级关系的，上面调用的logging模块级别的函数所使用的日志器是RootLogger类的实例，
    其名称为’root‘，他是处于日志器层级关系的最顶层的日子器，且该实例是以单例模式存在的
    
    如果要记录的日志中包含变量数据，可使用一个格式字符串作为这个事件的描述消息（logging.debug、logging.info等函数的第一个参数），
    然后将变量数据作为第二个参数*args的值进行传递，如:logging.warning('%s is %d years old.', 'Tom', 10)，
    输出内容为WARNING:root:Tom is 10 years old.
    
    logging.debug(), logging.info()等方法的定义中，除了msg和args参数外，还有一个**kwargs参数。
    它们支持3个关键字参数: exc_info, stack_info, extra，下面对这几个关键字参数作个说明。
        关于exc_info, stack_info, extra关键词参数的说明:
        exc_info： 其值为布尔值，如果该参数的值设置为True，则会将异常异常信息添加到日志消息中。如果没有异常信息则添加None到日志信息中。
        stack_info： 其值也为布尔值，默认值为False。如果该参数的值设置为True，栈信息将会被添加到日志信息中。
        extra： 这是一个字典（dict）参数，它可以用来自定义消息格式中所包含的字段，但是它的key不能与logging模块定义的字段冲突。
    
'''

import logging
import os
def init_log(path):
    if os.path.exists(path):
        mode = 'a'
    else:
        mode = 'w'
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(filename)s %(lineno)d %(levelname)s %(message)s',
        filename=path,
        filemode=mode
    )
    return logging

current_path = os.getcwd()
path = os.path.join(current_path,'back.log')
log = init_log(path)
log.info('这是第一个记录的日志信息')
log.warning('这是一个警告')
log.error('这是一个错误')
log.debug('这是一个debug')


'''
logging模块日志流处理流程

logging日志模块的四大组件
组件名称	对应类名	功能描述
日志器	Logger	提供了应用程序可一直使用的接口
处理器	Handler	将logger创建的日志记录发送到合适的目的输出
过滤器	Filter	提供了更细粒度的控制工具来决定输出哪条日志记录，丢弃哪条日志记录
格式器	Formatter	决定日志记录的最终输出格式

关系：
    日志器（logger）需要通过处理器（handler）将日志信息输出到目标位置，如：文件,sys.stdout,网络等
    不同的处理器（handler）可以将日志输出到不同的位置
    日志器（logger）可以设置多个处理器（handler）将同一条日志记录输出到不同的位置
    每个处理器（handler）都可以设置自己的过滤器（filter）实现日志过滤，从而只保留感兴趣的日志
    每个处理器（handler）都可以设置自己的格式器（formatter）实现同一条日志以不同的格式输出到不同的地方
简单地说就是：日志器（logger）是入口，真正干活的是处理器（handler），处理器（handler）还可以通过过滤器（filter）
和格式器（formatter）对要输出的日志内容做过滤和格式化处理操作。

Logger类：
Logger对象有3个任务要做：
    1.向应用程序代码暴露几个方法，使应用程序可以在运行时记录日志消息
    2.基于日志严重等级（默认的过滤设施）或filter对象来决定要对哪些日志进行后续处理
    3.将日志信息传送给所有感兴趣的日志handlers
Logger对象常用的方法分为两类：配置方法和消息发送方法
    常用的配置方法如下：
    方法	描述
    Logger.setLevel()	设置日志器将会处理的日志消息的最低严重级别
    Logger.addHandler() 和 Logger.removeHandler()	为该logger对象添加 和 移除一个handler对象
    Logger.addFilter() 和 Logger.removeFilter()	为该logger对象添加 和 移除一个filter对象
ogger对象配置完成后，可以使用下面的方法来创建日志记录：

方法	                                                   描述
Logger.debug(), Logger.info(), Logger.warning(),       创建一个与它们的方法名对应等级的日志记录
Logger.error(), Logger.critical()	
Logger.exception()	                                    创建一个类似于Logger.error()的日志消息
Logger.log()	                                        需要获取一个明确的日志level参数来创建一个日志记录

说明：
    Logger.exception()与Logger.error()的区别在于：Logger.exception()将会输出堆栈追踪信息，
    另外通常只是在一个exception handler中调用该方法。
    Logger.log()与Logger.debug()、Logger.info()等方法相比，虽然需要多传一个level参数，
    显得不是那么方便，但是当需要记录自定义level的日志时还是需要该方法来完成。

怎样得到一个Logger对象了？一种方式是通过Logger类的实例化方法创建一个Logger类的实例，但通常使用第二种方法
logging.getLogger()方法
logging.getLogger()方法有一个可选参数name，该参数表示将要返回的日志器的名称，如果不提供该参数，则其值为'root'。
若以相同的name参数值多次调用getLogger()方法，将会返回指向同一个logger对象的引用。

关于logger的层级结构与有效等级的说明：

logger的名称是一个以'.'分割的层级结构，每个'.'后面的logger都是'.'前面的logger的children，
例如，有一个名称为 foo 的logger，其它名称分别为 foo.bar, foo.bar.baz 和 foo.bam都是 foo 的后代。

logger有一个"有效等级（effective level）"的概念。如果一个logger上没有被明确设置一个level，
那么该logger就是使用它parent的level;如果它的parent也没有明确设置level则继续向上查找parent的parent的有效level，依次类推，
直到找到个一个明确设置了level的祖先为止。需要说明的是，root logger总是会有一个明确的level设置（默认为 WARNING）。
当决定是否去处理一个已发生的事件时，logger的有效等级将会被用来决定是否将该事件传递给该logger的handlers进行处理。

child loggers在完成对日志消息的处理后，默认会将日志消息传递给与它们的祖先loggers相关的handlers。
因此，我们不必为一个应用程序中所使用的所有loggers定义和配置handlers，只需要为一个顶层的logger配置handlers，
然后按照需要创建child loggers就可足够了。我们也可以通过将一个logger的propagate属性设置为False来关闭这种传递机制。

Handler类
Handler对象的作用是（基于日志消息的level）将消息分发到handler指定位置（文件，网络，邮件等）。Logger对象可以通过addHandler（）方法为自己添加0个或者多个handler对象。
比如，一个应用程序可能想要实现以下几个日志需求：
    1.把所有日志都发送到一个日志文件中；
    2.把所有严重级别大于等于error的日志发送到stdout（标准输出）
    3.把所有严重级别为critical的日志发送到一个email邮件弟子
这三种场景就需要3个不同的handlers，每个handlers复杂发送一个特定严重级别的日志到一个特定位置
一个handler中只有非常少数的方法是需要应用开发人员去关心的。对于使用内建handler对象的应用开发人员来说，
似乎唯一相关的handler方法就是下面这几个配置方法    
方法                                                  描述
Handler.setLevel()	                                设置handler将会处理的日志消息的最低严重级别
Handler.setFormatter()	                            为handler设置一个格式器对象
Handler.addFilter() 和 Handler.removeFilter()	    为handler添加 和 删除一个过滤器对象
需要说明的是，应用程序代码不应该直接实例化和使用Handler实例。因为Handler是一个基类，它只定义了所有handlers都应该有的接口，
同时提供了一些子类可以直接使用或覆盖的默认行为。下面是一些常用的Handler：

Handler	                                    描述
logging.StreamHandler	                    将日志消息发送到输出到Stream，如std.out, std.err或任何file-like对象。
logging.FileHandler	                        将日志消息发送到磁盘文件，默认情况下文件大小会无限增长
logging.handlers.RotatingFileHandler	    将日志消息发送到磁盘文件，并支持日志文件按大小切割
logging.hanlders.TimedRotatingFileHandler	将日志消息发送到磁盘文件，并支持日志文件按时间切割
logging.handlers.HTTPHandler	            将日志消息以GET或POST的方式发送给一个HTTP服务器
logging.handlers.SMTPHandler	            将日志消息发送给一个指定的email地址
logging.NullHandler	                        该Handler实例会忽略error messages，通常被想使用logging的library开发者使用来避免'No handlers could be found for logger XXX'信息的出现。

Formater类
Formater对象用于配置日志信息的最终顺序、结构和内容。与logging.Handler基类不同的是，应用代码可以直接实例化Formatter类。另外，如果你的应用程序需要一些特殊的处理行为，也可以实现一个Formatter的子类来完成。

Formatter类的构造方法定义如下：
logging.Formatter.__init__(fmt=None, datefmt=None, style='%')
可见，该构造方法接收3个可选参数：

fmt：指定消息格式化字符串，如果不指定该参数则默认使用message的原始值
datefmt：指定日期格式字符串，如果不指定该参数则默认使用"%Y-%m-%d %H:%M:%S"
style：Python 3.2新增的参数，可取值为 '%', '{'和 '$'，如果不指定该参数则默认使用'%'

Filter类
Filter可以被Handler和Logger用来做比level更细粒度的、更复杂的过滤功能。Filter是一个过滤器基类，它只允许某个logger层级下的日志事件通过过滤。该类定义如下：
class logging.Filter(name='')
    filter(record)
比如，一个filter实例化时传递的name参数值为'A.B'，那么该filter实例将只允许名称为类似如下规则的loggers产生的日志记录通过过滤：'A.B'，'A.B,C'，'A.B.C.D'，'A.B.D'，而名称为'A.BB', 'B.A.B'的loggers产生的日志则会被过滤掉。如果name的值为空字符串，则允许所有的日志事件通过过滤。

filter方法用于具体控制传递的record记录是否能通过过滤，如果该方法返回值为0表示不能通过过滤，返回值为非0表示可以通过过滤。

说明：

如果有需要，也可以在filter(record)方法内部改变该record，比如添加、删除或修改一些属性。
我们还可以通过filter做一些统计工作，比如可以计算下被一个特殊的logger或handler所处理的record数量等。
'''
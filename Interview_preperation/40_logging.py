'''Logging in Python is a way to track events that happen during runtime, helping 
    you debug and monitor the execution of your programs. The Python standard library
    provides the `logging` module to facilitate this.
'''
### Key Components of Logging

'''
1. **Loggers**: The primary entry point for logging messages. You can create multiple 
    loggers for different parts of your application.
2. **Handlers**: Send log messages to their destination, such as the console, a file,
     or a remote server.
3. **Formatters**: Define the layout of log messages.
4. **Log Levels**: Determine the severity of the events being logged. Python defines several
     log levels: DEBUG, INFO, WARNING, ERROR, and CRITICAL.
'''

### Basic Usage

#### 1. Simple Logging to Console

# **Example**:
import logging

# Configure the basic settings for logging
logging.basicConfig(level=logging.DEBUG)

# Create a logger object
logger = logging.getLogger()

# Log messages of various severity levels
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")

# **Output**:
'''
DEBUG:root:This is a debug message
INFO:root:This is an info message
WARNING:root:This is a warning message
ERROR:root:This is an error message
CRITICAL:root:This is a critical message
'''

#### 2. Logging to a File

# **Example**:
import logging

# Configure logging to write messages to a file
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger()

# Log messages
logger.debug("Debug message in file")
logger.info("Info message in file")

'''
**File (`app.log`) Output**:
2024-07-20 12:34:56,789 - DEBUG - Debug message in file
2024-07-20 12:34:56,790 - INFO - Info message in file
'''
#### 3. Customizing Log Format

# **Example**:
import logging

# Create a custom logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Create a file handler
file_handler = logging.FileHandler('custom.log')
file_handler.setLevel(logging.DEBUG)

# Create a custom formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# Log messages
logger.info("This is an info message with custom format")

'''
**File (`custom.log`) Output**:
2024-07-20 12:34:56,789 - root - INFO - This is an info message with custom format
'''

#### 4. Logging Exceptions

# **Example**:
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Configure console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

try:
    x = 1 / 0
except ZeroDivisionError:
    logger.exception("An error occurred")

'''
**Output**:
2024-07-20 12:34:56,789 - ERROR - An error occurred
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
ZeroDivisionError: division by zero
'''

### Advanced Usage

#### 1. Multiple Handlers and Levels

# **Example**:
import logging

logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

# File handler
file_handler = logging.FileHandler('advanced.log')
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")

#### 2. Logging Configuration Using Config Files

'''
You can configure logging using a configuration file, which allows for more complex setups.
'''

# **Example (`logging.conf`)**:
'''
[loggers]
keys=root,sampleLogger

[handlers]
keys=consoleHandler,fileHandler

[formatters]
keys=defaultFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_sampleLogger]
level=DEBUG
handlers=fileHandler
qualname=sampleLogger

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=defaultFormatter
args=(sys.stdout,)

[handler_fileHandler]
class=FileHandler
level=DEBUG
formatter=defaultFormatter
args=('conf.log', 'a')

[formatter_defaultFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=%Y-%m-%d %H:%M:%S
'''

# **Python Code to Load Config**:
import logging
import logging.config
import sys

logging.config.fileConfig('logging.conf')

logger = logging.getLogger('sampleLogger')
logger.debug("Debug message from sampleLogger")

### Summary

'''
- **Basic Logging**: Use `logging.basicConfig()` for simple logging to the console or a file.
- **Custom Logging**: Create and configure `Logger`, `Handler`, and `Formatter` objects
     for more control.
- **Advanced Features**: Configure logging using files and handle multiple logging
     destinations and formats.
'''
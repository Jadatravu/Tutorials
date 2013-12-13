1.Update LOGGING section in settings.py with logger,handler,formatter fields
  Logger which specifies the handler, in this case it is file
 'loggers': {
        'logapp':{
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
  File handler specifies the filename "logapp.log", also specifies theformatter in this case it is simple.
  'handlers': {
        'file':{
            'level':'DEBUG',
            'class':'logging.FileHandler',
            'filename':'logapp.log',
            'formatter':'simple'
        },
    }
  Formatter specifies the formatter in this case it is 'simple'.
 'formatters':{
        'simple':{
           'format':'%(levelname)s %(message)s'
        }
    },
2. import logging modules and add the logger message lines whereever it is required to have log message.

    logger.debug("This is debug message")
    logger.error("This is error message")

3. log messages will be printed in the log file in this case "logapp.log"
   http://127.0.0.1:8000/logproject/

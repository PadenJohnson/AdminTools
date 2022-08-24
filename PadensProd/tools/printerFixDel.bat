net stop spooler
del %systemroot%\System32\spool\printers\* /Q f/s
net start spooler
import os
import shutil
os.mkdir('pythonception')
with open('pythonception/pythonception.py', 'w') as f:
      f.close()
   
shutil.copyfile('pythonception.py', 'pythonception/pythonception.py')

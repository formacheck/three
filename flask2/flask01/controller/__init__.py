# __all__=["user_controller","product_controller"]
  # oR
import os
import glob
__all__=[os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__)+ "/*.py")]
# this lines of code automatically import all the files in this directory. so you don't need  to
# import is manaully.
# Roldan-Gomez-Juan
import rrdtool
import os
rrdtool.dump(os.path.join(os.getcwd(), "Databases", "localhost.rrd"), os.path.join(os.getcwd(), "Databases", "localhost.xml"))

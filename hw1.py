import mujoco as mj
import dm_control.mujoco as dm
import mujoco_viewer
from mujoco import viewer

m = mj.MjModel.from_xml_path("hw1.xml")
viewer.launch(m)
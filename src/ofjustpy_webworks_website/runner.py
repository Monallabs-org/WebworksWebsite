import logging
from pathlib import Path
Path("ofjustpy_webworks_monallabs_in.log").unlink(missing_ok=True)


FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(filename="ofjustpy_webworks_monallabs_in.log",
                    level=logging.DEBUG, format=FORMAT)


import macropy.activate
import ofjustpy as oj
from . import overview_revised
#from . import about_section_sbs
#from . import techstack_and_demo_page
# best to mount them 
from . import hyperui_component_library_showcase
from . import shadcnui_component_library_showcase
from . import skeletonui_component_library_showcase
from demos import demo_advanced_components

app = oj.load_app()


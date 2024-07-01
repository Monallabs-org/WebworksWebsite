from py_tailwind_utils import *
from html_writer.macro_module import macros, writer_ctx
import ofjustpy as oj
from ofjustpy_plugins import format_code
from ofjustpy_components.component_mouseover_slideshow import SlideShow

from .overview_ofjustpy_webapp_stack import about_ofjustpy_webapp_stack
from .about_ofjustpy_demos import about_ofjustpy_demos





with writer_ctx:
    with HCCMutable_Div(classes="space-y-4 w-2/3") as about_box:

        pass

about_box.childs.append(about_ofjustpy_webapp_stack)
about_box.childs.append(about_ofjustpy_demos)

about_panel = oj.HCCMutable.Subsection("About Ofjustpy Framework", about_box)



            

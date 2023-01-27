import logging
import os
from starlette.staticfiles import StaticFiles

if os:
    try:
        os.remove("ofjustpy_webworks_monallabs_in.log")
    except:
        pass

import sys
if sys:
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(filename="ofjustpy_webworks_monallabs_in.log",
                        level=logging.DEBUG, format=FORMAT)
    
import ofjustpy as oj

from addict_tracking_changes import Dict

logging.debug("load app webworks")
app = oj.load_app()

def page_builder(key, childs, **kwargs):
    return oj.Mutable.WebPage(
        key=key,
        childs=childs,
        cookie_state_attr_names=oj.aci.the_starlette_app.cookie_state_attr_names,
        template_file="production_hosting.html", 
        **kwargs,
    )

with oj.PageBuilderCtx(page_builder):
    from  webworks_website.index import wp_index
    from demos.demo_advanced_components import  wp_demo_advanced_components
    from demos.demo_basic_components import  wp_demo_basic_components
    from demos.demo_render_markdown_formatted import wp_demo_markdown_formatting
    from demos.demo_pycode_formatting import wp_demo_pycode_formatting
    import mount_examples


# app.mount("/addict-tracking-changes",
#           StaticFiles(directory='./addict_tracking_changes_doc_html'),
#           name = "addict_docs"
#           )
oj.add_jproute("/", wp_index)  #
oj.add_jproute("/demo_basic_capabilities", wp_demo_basic_components)
oj.add_jproute("/demo_advanced_capabilities", wp_demo_advanced_components)

oj.add_jproute("/demo_markdown_formatting", wp_demo_markdown_formatting)

oj.add_jproute("/demo_pycode_formatting", wp_demo_pycode_formatting)

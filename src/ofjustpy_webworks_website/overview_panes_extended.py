from py_tailwind_utils import *

import ofjustpy as oj
import twsty
app = oj.load_app()
from html_writer.macro_module import macros, writer_ctx

oj.set_style("un")

# ======================== Performant: Scalable and effficient =======================
with writer_ctx:
    with Details(classes="group", extra_classes="[&_summary::-webkit-details-marker]:hidden") as feature_scalable_efficient_infobox:
        with Summary(classes="flex cursor-pointer items-center justify-between gap-1.5 bg-pink-50 p-4 text-gray-900"):
            with Div(classes="flex-1 flex justify-center"):
                with H2(classes="font-medium", text="📌 Lean, efficient and scalable"):
                    pass
            with Icon_Plus():
                pass
        with Div(classes="bg-pink-50/50 border border-gray-200 p-2") as desc:
            with Ul(classes="ml-4 mt-4 p-2 space-y-2"):
                with Li(classes="flex space-x-2"):
                    with Icon_RightArrow():
                        pass
                    with Span(text="Space efficiency: app runtime has only a single copy for  non-mutable static components", classes="text-gray-700"):
                        pass

                with Li(classes="flex space-x-2"):
                    with Icon_RightArrow():
                        pass
                    with Span(text="Space efficiency: for mutable components only the mutable attributes have their own private copy per connection -- non-mutable attributes are shared across connections", classes="text-gray-700"):
                        pass

                with Li(classes="flex space-x-2"):
                    with Icon_RightArrow():
                        pass
                    with Span(text="Runtime efficiency: As far as possible Ofjustpy minimizes copying of component data from one data structure other.", classes="text-gray-700"):
                        pass
                    
                    
                with Li(classes="flex space-x-2"):
                    with Icon_RightArrow():
                        pass
                    with Span(text="Communication efficiency: Ofjustpy maintains state of mutable components. Only the changes for components are transported to frontend", classes="text-gray-700"):
                        pass

                with Li(classes="flex space-x-2"):
                    with Icon_RightArrow():
                        pass
                    with Span(text="Efficient Concurrency: Ofjustpy is fully asynchronous thanks to the underlying ASGI webserver -- Starlette. Asnchronous computation allows Ofjustpy to exploit concurrency even on single core machines", classes="text-gray-700"):
                        pass
                    

                    
with writer_ctx:
    with Details(classes="group", extra_classes="[&_summary::-webkit-details-marker]:hidden") as feature_uictx_programmability_infobox:
        with Summary(classes="flex cursor-pointer items-center justify-between gap-1.5 bg-pink-50 p-4 text-gray-900"):
            with Div(classes="flex-1 flex justify-center"):
                with H2(classes="font-medium", text="📌 Modular reusable codes using uictx namespaces "):
                    pass
            with Icon_Plus():
                pass
        with Div(classes="bg-pink-50/50 border border-gray-200 p-2") as desc:
            with Ul(classes="ml-4 mt-4 space-y-2"):
                with Li(classes="ml-2 flex gap-2"):
                    with Icon_RightArrow():
                        pass
                    with Span(text="Define hierarchy of namespaces", classes="text-gray-700"):
                        pass
                with Li(classes="ml-2 flex gap-2"):
                    with Icon_RightArrow():
                        pass
                    with Span(text="Every active/mutable components  gets an access path within this hierarchy", classes="text-gray-700"):
                        pass                                        

                with Li(classes="ml-2 flex gap-2"):
                    with Icon_RightArrow():
                        pass
                    with Span(text="Avoids circular name dependency issues in event handlers", classes="text-gray-700"):
                        pass
                    
                with Li(classes="ml-2 flex gap-2"):
                    with Icon_RightArrow():
                        pass
                    with Span(text="Facilitates code-reuse, modularity", classes="text-gray-700"):
                        pass                                        

            with Div(classes="text-left mt-4 ml-4"):
                with H2(text="Code Demo: Using uictx namespace to construct a hierarchy over components", classes="font-medium text-gray-900"):
                    pass
            with Div(classes="mt-2 w-full flex justify-center text-sm overflow-auto") as code_block_container:
                pass

            with Div(classes="text-left mt-4 ml-4"):
                with H2(text="Code Demo: Access components globally via uictx hierarchy", classes="font-medium text-gray-900"):
                    pass
            with Div(classes="mt-2 w-full flex justify-center text-sm overflow-auto") as code_block_event_handler_container:
                pass

            
from ofjustpy_plugins import format_code
code = """
with oj.uictx("mywp") as mywp:
   with oj.uictx("header") as headerctx:
      homelink = oj.AD.A(key="Home", target="http://www.mywebsite/Home", text="Home Page")
      deplink = oj.AD.A(key="Departments", target="http://www.mywebsite/DepartmentList")
      navlinks = oj.PD.StackH(childs = [homelink, deplink])
      header_panel = oj.PD.Subsection("Navigation Panel", childs=[navlinks])

   with oj.uictx("body") as bodyctx:
      bodytext = oj.PD.Prose(text="The body content of the webpage. This is placeholder.")
      body_panel = oj.PD.Subsection("Navigation Panel", cgens=[bodytext])
	  
   with oj.uictx("footer") as footerctx:
      content = oj.Mutable.Span(key="content", text="This is a placeholder for footer")
      footer_panel = oj.PD.Subsection(cgens=[content])
"""
fct = format_code(code)

code_block_container.components.append(fct)

code="""
   footer_content = mywp.footer.content.target
   footer_content.text = "Changed footer status"
"""

fct = format_code(code)
code_block_event_handler_container.components.append(fct)



# ============================ Ui library ============================

with writer_ctx:
    with Details(classes="group", extra_classes="[&_summary::-webkit-details-marker]:hidden") as ui_library_infobox:
        with Summary(classes="flex cursor-pointer items-center justify-between gap-1.5 bg-pink-50 p-4 text-gray-900"):
            with Div(classes="flex-1 flex justify-center"):
                with H2(classes="font-medium", text="Supported UI-toolkits: HyperUI, Skeleton UI, and MeltUI"):
                    pass
            with Icon_Plus():
                pass
        with Div(classes="bg-pink-50/50 border border-gray-200 p-2") as desc:
            with Ul(classes="ml-4 mt-4 space-y-2"):
                with Li(classes="ml-2 flex gap-2"):
                    with Icon_RightArrow():
                        pass
                    with Span(text="HyperUI", classes="text-gray-700"):
                        pass
                with Li(classes="ml-2 flex gap-2"):
                    with Icon_RightArrow():
                        pass
                    with Span(text="Skeleton UI", classes="text-gray-700"):
                        pass

                with Li(classes="ml-2 flex gap-2"):
                    with Icon_RightArrow():
                        pass
                    with Span(text="Melt UI", classes="text-gray-700"):
                        pass                                             

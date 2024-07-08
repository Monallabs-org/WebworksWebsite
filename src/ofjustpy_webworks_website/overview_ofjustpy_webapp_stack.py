from py_tailwind_utils import *
from html_writer.macro_module import macros, writer_ctx
import ofjustpy as oj
from ofjustpy_plugins import format_code
from ofjustpy_components.component_mouseover_slideshow import SlideShow
oj.set_style("un")
# ============================ Ui library ============================
slide_labels = ["python",
                "starlette",
                "websockets",
                "svelte",
                "tailwind",
                "deployment",
                
    ]
slide_info = {"python": ("Python",
                             oj.PC.Prose(text="Ofjustpy enables all aspects of webdevelopment through Python.")
                             ),
              "starlette": ("Async Processing",
                                oj.PC.Prose(text="The underlying engine powering Ofjustpy is Starlette. Being an async runtime, it enables building responsive and efficient webapp")
                                ),
              "websockets": ("Websocket",
                             oj.PC.Prose(text="All communication between webserver and the UI takes place via websockets.")
                             ),
              "svelte": ("Svelte at frontend",
                         oj.PC.Prose(text="All Ofjustpy directives to frontend are processed by Svelte runtime.")
                         ),
              "tailwind": ("Tailwind Styling",
                               oj.PC.Prose(text="Tailwind CSS is used to control the layout and style the components of the webpage")
                               ),
              "deployment": ("Nginx and Unit",
                                oj.PC.Prose(text="App written with Ofjustpy, can be deploy with Nginx/Unit server")
                                ),
              }

techstack_slideshow = SlideShow("slideshow_techstack",
                                slide_labels,
                                slide_info,
                                "starlette")

# techstack_panel = oj.HCCMutable.Subsection("Ofjustpy tech stack",
#                                            techstack_slideshow
#                                            )


with writer_ctx:
    with HCCMutable_Details(classes="group", extra_classes="[&_summary::-webkit-details-marker]:hidden") as about_ofjustpy_webapp_stack:
        with Summary(classes="flex cursor-pointer items-center justify-between gap-1.5 bg-pink-100 p-4 text-gray-900 rounded-t-lg"):

            with Div(classes="flex-1 flex justify-center"):

                with H2(classes="font-medium", text="📌 Ofjustpy webapp technology stack"):
                    pass
            with FontAwesomeIcon(label="faPlus", classes="w-5 h-5"):
                pass
            
            pass
        with HCCMutable_Div(classes="bg-pink-50/50 border border-gray-200 rounded-b-lg p-2") as content_area:
            pass

        pass

    pass


content_area.childs.append(techstack_slideshow)

            

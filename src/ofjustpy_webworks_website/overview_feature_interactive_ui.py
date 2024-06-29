from py_tailwind_utils import *
from html_writer.macro_module import macros, writer_ctx
import ofjustpy as oj
from ofjustpy_plugins import format_code
oj.set_style("un")


with writer_ctx:
    with Details(classes="group", extra_classes="[&_summary::-webkit-details-marker]:hidden") as feature_interactive_ui_infobox:
        with Summary(classes="flex cursor-pointer items-center justify-between gap-1.5 bg-pink-100 p-4 text-gray-900 rounded-t-lg"):
            with Div(classes="flex-1 flex justify-center"):
                with H2(classes="font-medium", text="📌 Easy Interactive UI "):
                    pass
            with FontAwesomeIcon(label="faPlus", classes="w-5 h-5"):
                pass
        with Div(classes="bg-pink-50/50 border border-gray-200 rounded-b-lg") as desc:
            with Div(classes="text-center"):

                with H2(text="Change UI state using simple python expressions", classes="font-bold tracking-tight text-2xl"):
                    pass

            with Div(classes="flex justify-center mt-8"):
                with Ul(classes="space-y-2 text-balance text-lg text-slate-700 tracking-tight") as desc_box:
                    with Li(classes="flex items-center gap-1"):
                        with FontAwesomeIcon(label="faArrowRight", classes="w-5 h-5"):
                            pass
                        with Span(text="Tailwind utility classes are first class objects", classes=""):
                            pass
                    with Li(classes="flex items-center gap-1"):
                        with FontAwesomeIcon(label="faArrowRight", classes="w-5 h-5"):
                            pass
                        with Span(text="Allows semantics based update and merge over tailwind classes", classes=""):
                            pass
                    with Li(classes="flex items-center gap-1"):
                        with FontAwesomeIcon(label="faArrowRight", classes="w-5 h-5"):
                            pass
                        with Span(text="Updated classes are transparently shipped to frontend to update the UI", classes=""):
                            pass
                    

            with Div(classes="mt-8 space-y-2"):
                with Div(classes="text-center"):
                    with H2(text="Code Demo: Interactive UI via simple expressions", classes="text-xl tracking-tight"):
                            pass
                with Div(classes="flex justify-center mt-2 font-bold text-sm tracking-tight overflow-auto") as code_block_container:
                    pass


code = """def on_click(dbref, msg, to_ms):
    ms_dbref = to_ms(dbref)
    # change background color to green-500 and font size to text-xl
    ms_dbref.add_twsty_tags(bg/green/5, fz.xl)
    pass
"""   
fct = format_code(code)
code_block_container.components.append(fct)

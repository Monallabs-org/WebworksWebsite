from py_tailwind_utils import *
from html_writer.macro_module import macros, writer_ctx
import ofjustpy as oj
from ofjustpy_plugins import format_code
oj.set_style("un")

with writer_ctx:
    with Details(classes="group", extra_classes="[&_summary::-webkit-details-marker]:hidden") as feature_event_handling_infobox:
        with Summary(classes="flex cursor-pointer items-center justify-between gap-1.5 bg-pink-100 p-4 text-gray-900 rounded-t-lg"):
            with Div(classes="flex-1 flex justify-center"):
                with H2(classes="font-medium", text="📌 Straightforward event handling"):
                    pass
            with FontAwesomeIcon(label="faPlus", classes="w-5 h-5"):
                pass
        with Div(classes="bg-pink-50/50 border border-gray-200 rounded-b-lg") as desc:
            with Div(classes="text-center"):

                with H2(text="Browser event are handled from within Python", classes="font-bold tracking-tight text-2xl"):
                    pass

            with Div(classes="flex flex-col justify-center mt-8"):
                with H2(text="Code Demo: handling browser events", classes="text-balance text-center text-lg text-slate-700"):
                        pass
                with Div(classes="flex justify-center mt-2 font-bold text-sm tracking-tight overflow-auto") as code_block_container:
                    pass


code = """def on_click(dbref, msg, to_ms):
   \"\"\"
   handle click event on component dbref
   \"\"\"
   pass
with writer_ctx:
   with Div():
       with Button(key="mybtn", on_click=on_click):
            pass

"""   
fct = format_code(code)
code_block_container.components.append(fct)

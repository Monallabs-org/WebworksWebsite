from py_tailwind_utils import *
from html_writer.macro_module import macros, writer_ctx
import ofjustpy as oj
from ofjustpy_plugins import format_code
oj.set_style("un")


# ======================== Performant: Scalable and effficient =======================
with writer_ctx:
    with Details(classes="group", extra_classes="[&_summary::-webkit-details-marker]:hidden") as feature_scalable_efficient_infobox:
        with Summary(classes="flex cursor-pointer items-center justify-between gap-1.5 bg-pink-100 p-4 text-gray-900 rounded-t-lg"):
            with Div(classes="flex-1 flex justify-center"):
                with H2(classes="font-medium", text="📌 Lean, efficient and scalable"):
                    pass
            with FontAwesomeIcon(label="faPlus", classes="w-5 h-5"):
                pass
        with Div(classes="bg-pink-50/50 border border-gray-200 rounded-b-lg") as desc:
            with Div(classes="text-center"):
                with H2(text="Incorporates several space and runtime optimizations", classes="font-bold tracking-tight text-2xl"):
                    pass
            with Div(classes="flex items-center mt-8"):
                with Ul(classes="ml-8 space-y-2 text-balance text-lg text-slate-700 tracking-tight"):
                    with Li(classes="flex items-center gap-1"):
                        with FontAwesomeIcon(label="faArrowRight", classes="w-5 h-5"):
                            pass
                        with Span(text="Space efficiency: runtime has only a single copy for static components", classes=""):
                            pass


                    with Li(classes="flex items-center gap-1"):
                        with FontAwesomeIcon(label="faArrowRight", classes="w-5 h-5"):
                            pass
                        with Span(text="Runtime efficiency: Ofjustpy minimizes data movement and copying.", classes=""):
                            pass


                    with Li(classes="flex items-center gap-1"):
                        with FontAwesomeIcon(label="faArrowRight", classes="w-5 h-5"):
                            pass
                        with Span(text="Communication efficiency: For interactive UI, Ofjustpy sends only UI changes to the frontend", classes=""):
                            pass

                    with Li(classes="flex items-center gap-1"):
                        with FontAwesomeIcon(label="faArrowRight", classes="w-5 h-5"):
                            pass
                        with Span(text="Efficient Concurrency: Ofjustpy utilizes  ASGI web server, for full asynchronous operation. This enables concurrency even on single-core machines", classes=""):
                            pass

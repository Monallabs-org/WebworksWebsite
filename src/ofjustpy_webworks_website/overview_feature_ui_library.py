from py_tailwind_utils import *
from html_writer.macro_module import macros, writer_ctx
import ofjustpy as oj
from ofjustpy_plugins import format_code
oj.set_style("un")
# ============================ Ui library ============================

with writer_ctx:
    with Details(classes="group", extra_classes="[&_summary::-webkit-details-marker]:hidden") as feature_ui_library_infobox:
        with Summary(classes="flex cursor-pointer items-center justify-between gap-1.5 bg-pink-100 p-4 text-gray-900 rounded-t-lg"):
            with Div(classes="flex-1 flex justify-center"):
                with H2(classes="font-medium", text="📌 Supported UI libraries: HyperUI, Skeleton UI, and ShadcnUI"):
                    pass
            with FontAwesomeIcon(label="faPlus", classes="w-5 h-5"):
                pass
        with Div(classes="bg-pink-50/50 border border-gray-200 rounded-b-lg") as desc:
            with Div(classes="flex justify-center mt-4 space-x-4 mb-4"):
                with SKHUI.button_wideWithIcon(href="/skeletonUI", text="SkeletonUI") :
                    pass

                with SKHUI.button_wideWithIcon(href="/hyperui", text="HyperUI"):
                    pass
                
                with SKHUI.button_wideWithIcon(href="/shadcnui", text="ShadcnUI") :
                    pass


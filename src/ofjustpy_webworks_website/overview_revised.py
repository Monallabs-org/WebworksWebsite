from hyperui_plugin.marketing.faqs import  (BackgroundAccentBorder,
                                              )
from py_tailwind_utils import *

import ofjustpy as oj
oj.set_style("un")
app = oj.load_app()
from html_writer.macro_module import macros, writer_ctx

# """Effortless HTML with Ofjustpy: No-Templates, No-Boilerplate, Just Clean Pythonic Code:


# Author HTML inline within Python code, 
# """

# "eliminating the need for additional templates, using Pythonic custom DSL.  Resulting html code is clean and readable, free from boilerplate, facilitating ease of maintenance. An example HTML written in Ofjustpy Python DSL"
from ofjustpy_plugins import format_code
code = """
with Article(classes="overflow-hidden rounded-lg shadow transition hover:shadow-lg") as comp_box:
    with Img(src=image_url, alt="Office", classes="h-56 w-full object-cover"):
        pass

    with Div(classes="bg-white p-4 sm:p-6"):
        with Time(classes="block text-xs text-gray-500", datetime=date, text=date):
            pass

        with A(href=link):
            with H3(classes="mt-0.5 text-lg text-gray-900", text=title):
                pass

        with P(classes="mt-2 line-clamp-3 text-sm/relaxed text-gray-500", text=content):
            pass
"""
fct = format_code(code)


with writer_ctx:
    with Div(classes="space-y-4") as overview_box:

        pass

# ============================= feature 1 ============================
with writer_ctx:
    with Details(classes="group", extra_classes="[&_summary::-webkit-details-marker]:hidden") as feature_inline_html_infobox:

        with Summary(classes="rounded-full  flex cursor-pointer items-center justify-between gap-1.5 rounded-lg bg-pink-50 p-4 text-gray-900"):
            with Div(classes="flex"):

                with H2(classes="font-medium", text="📌 Effortless HTML: No-Templates, No-Boilerplate, Just Clean Pythonic Code"):
                    pass
            with Icon_Plus():
                pass
        with Div(classes="rounded-2xl border border-gray-200 p-6 sm:px-8 lg:p-12") as desc:
            with Div(classes="text-left ml-2"):

                with H2(text="Author HTML inline within Python code", classes="text-lg font-medium text-gray-900"):
                    pass


            with Ul(classes="ml-4 mt-4 space-y-2") as desc_box:
                with Li(classes="flex items-center gap-1"):
                    with Icon_RightArrow():
                        pass
                    with Span(text="Eliminates need for templates ", classes="text-gray-700"):
                        pass
                with Li(classes="flex items-center gap-1"):
                    with Icon_RightArrow():
                        pass
                    with Span(text="Low boilerplate crud", classes="text-gray-700"):
                        pass

                with Li(classes="flex items-center gap-1"):
                    with Icon_RightArrow():
                        pass
                    with Span(text="Easy to read and maintain", classes="text-gray-700"):
                        pass                                        

            with Div(classes="text-left mt-4 ml-4"):
                with H2(text="Code Demo: A sample html using ofjustpy", classes="font-medium text-gray-900"):
                    pass
            with Div(classes="mt-2 text-xs overflow-auto") as code_block_container:
                pass
                
                
code_block_container.components.append(fct)
overview_box.components.append(feature_inline_html_infobox)

# ================================ end ===============================

# ============================= feature 2 ============================
with writer_ctx:
    with Details(classes="group", extra_classes="[&_summary::-webkit-details-marker]:hidden") as feature_event_handling_infobox:
        with Summary(classes="rounded-full  flex cursor-pointer items-center justify-between gap-1.5 rounded-lg bg-pink-50 p-4 text-gray-900"):
            with Div(classes="flex"):
                with H2(classes="font-medium", text="📌 Straightforward event handling"):
                    pass
            with Icon_Plus():
                pass
        with Div(classes="rounded-2xl border border-gray-200 p-6 sm:px-8 lg:p-12") as desc:
            with Div(classes="text-left ml-2"):

                with H2(text="Browser event are handled from within Python", classes="text-lg font-medium text-gray-900"):
                    pass

            with Div(classes="text-left mt-4 ml-4"):
                with H2(text="Code Demo: handling browser events", classes="font-medium text-gray-900"):
                        pass
                with Div(classes="mt-2 text-xs overflow-auto") as code_block_container:
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

endpoint = oj.create_endpoint("event_handling",
                              childs = [comp_box]
                              ),
                              title="Event handling"
                              )
oj.add_jproute("/", endpoint)
"""   
fct = format_code(code)
code_block_container.components.append(fct)
overview_box.components.append(feature_event_handling_infobox)

# ================================ end ===============================

# ============================= feature 3 ============================
with writer_ctx:
    with Details(classes="group", extra_classes="[&_summary::-webkit-details-marker]:hidden") as feature_interactive_ui_infobox:
        with Summary(classes="rounded-full  flex cursor-pointer items-center justify-between gap-1.5 rounded-lg bg-pink-50 p-4 text-gray-900"):
            with Div(classes="flex"):
                with H2(classes="font-medium", text="📌 Easy and Efficient Interactive UI "):
                    pass
            with Icon_Plus():
                pass
        with Div(classes="rounded-2xl border border-gray-200 p-6 sm:px-8 lg:p-12") as desc:
            with Div(classes="text-left ml-2"):

                with H2(text="Efficiently change UI state using simple python expressions", classes="text-lg font-medium text-gray-900"):
                    pass

            with Ul(classes="ml-4 mt-4 space-y-2") as desc_box:
                with Li(classes="flex items-center gap-1"):
                    with Icon_RightArrow():
                        pass
                    with Span(text="Ofjustpy maintains ui-state of mutable objects ", classes="text-gray-700"):
                        pass
                with Li(classes="flex items-center gap-1"):
                    with Icon_RightArrow():
                        pass
                    with Span(text="Computes the changes in the states ", classes="text-gray-700"):
                        pass
                with Li(classes="flex items-center gap-1"):
                    with Icon_RightArrow():
                        pass
                    with Span(text="Only states of components with changed states are shipped to browser", classes="text-gray-700"):
                        pass
                    

            with Div(classes="text-left mt-4 ml-4"):
                with H2(text="Code Demo: Interactive UI -- Efficient and effortless", classes="font-medium text-gray-900"):
                        pass
                with Div(classes="mt-2 text-xs overflow-auto") as code_block_container:
                    pass


code = """def on_click(dbref, msg, to_ms):
    ms_dbref = to_ms(dbref)
    # change background color to green-500 and font size to text-xl
    ms_dbref.add_twsty_tags(bg/green/5, fz.xl)
    pass

with writer_ctx:
    with HCCMutable_Div(classes="bg-green-100") as comp_box:
        with Mutable_Button(key="abtn", classes="bg-green-100", text="Click Me", on_click=on_click):
            pass


endpoint = oj.create_endpoint("event_handling",
                              childs = [comp_box]
                              ),
                              title="Event handling"
                              )
oj.add_jproute("/", endpoint)
"""   
fct = format_code(code)
code_block_container.components.append(fct)
overview_box.components.append(feature_interactive_ui_infobox)

# ================================ end ===============================
# TODO: in the overview page --> provide hyperlink to user_manual
# writer context should support for loop
# Points for later
# talk about oj.uictx
# talk about stackD, hirerachy navigator
# talk about writer_ctx
# does stackD.bring_to_front works on key or id (i.e. fully qualified name)
# TODO: style is not passed; progress.py is not available. --> test if style is being passed through
# TODO: radio is not available; radiogroups is not availabe.
# TODO: list, name, id is not passed to browser: Detailist select is not available
# TODO: sideMenu: Items are listed from below; needs fixing
# TODO: tables: header is not aligned with body rows.
# TODO: select doesn't support selected option
# TODO: convert tabs/pills to proper component with event hooks/etc
# TODO: need to be able to mutate svg elements: for toggle with icon as to work
# data-uncheked-icon, data-checked-icon
# TODO: Toggles is messed up
# TODO: when performing encode_twsty we are getting the same sm:sm:sm: error
# vertical menu mg_container is not working
# TODO: sm:sm:sm stuff is probably messing up ecomCards
# TODO: collection cards are not working: something about relative
# TODO: for quatity input -- add handlers/hook to actually increment/decrement
# TODO: quantity-input: figure out how not to strecth the div
# TODO: buttons bottom, top not working
# TODO: pricings is missing details
# for testimonials we need slider-- some combination of tailwind and svelte
# &mdash isn't working for html

# -->
# for and if block in writer_ctx is coming soon.
# AttributeError: 'WebPage_MutableShell' object has no attribute 'remove_twsty_tags'
# WebPage object should work like proper compoment

# In  state-changed based programming
# if an action is hooked to a access-path
# then don't change the access-path in the action

# put padding on slider
#. buttons: msg.value doesn't work. --> 

#. /home/kabiraatmonallabs/to_githubcodes/org-ofjustpy/page-style-editor/src/page_style_editor/styeditor_sbs.py: color selector spacing, alignment is messed up

endpoint = oj.create_endpoint("overview",
                              childs = [oj.PC.Container(childs=[overview_box
                                                                ],
                                                        twsty_tags=[mr/x/auto]
                                                        )

                                        ],
                              title="Overview"
                              )
oj.add_jproute("/", endpoint)



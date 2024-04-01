from hyperui_plugin.marketing.faqs import  (BackgroundAccentBorder,
                                              )
from py_tailwind_utils import *

import ofjustpy as oj
import twsty

from overview_panes_extended import feature_scalable_efficient_infobox, feature_uictx_programmability_infobox
app = oj.load_app()
from html_writer.macro_module import macros, writer_ctx

# ============================ top matter ============================
with oj.TwStyCtx(twsty):
    with oj.uictx("topmatter"):
        title = oj.PC.StackV(childs = [oj.PD.Title("Ofjustpy", twsty_tags=[fc/rose/5]),
                                       oj.PD.SubTitle("An easy-to-use yet full-featured web framework in Python",
                                                      twsty_tags=[fc/pink/3]
                                                      )
                                       ]
                             )

        # Its not possible to give an overview that will do justice

        # overview = oj.PC.Subsection("Overview",
        #                             oj.PC.Halign(oj.PC.Prose(text="Ofjustpy is a Python based webframework to seamlessly construct web-based applications and websites with ease. Leveraging Python's powerful language constructs and various libraries and utilities, this framework offers an extensive array of tools and APIs that dramatically simplify the process of developing sophisticated webpages.",
        #                                    twsty_tags=[max/W/"prose", fz.xl]
        #                                    )
        #                             )
        #                     )


        divider = oj.PC.Hr(twsty_tags=[mr/sb/4])

        top_panel = oj.PC.StackV(childs=[title, divider])

    

# """Effortless HTML with Ofjustpy: No-Templates, No-Boilerplate, Just Clean Pythonic Code:


# Author HTML inline within Python code, 
# """

# "eliminating the need for additional templates, using Pythonic custom DSL.  Resulting html code is clean and readable, free from boilerplate, facilitating ease of maintenance. An example HTML written in Ofjustpy Python DSL"
oj.set_style("un")

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
    with Div(classes="space-y-4 w-full") as overview_box:

        pass

# ============================= feature 1 ============================
with writer_ctx:
    with Details(classes="group", extra_classes="[&_summary::-webkit-details-marker]:hidden") as feature_inline_html_infobox:

        with Summary(classes="flex cursor-pointer items-center justify-between gap-1.5 bg-pink-50 p-4 text-gray-900"):
            with Div(classes="flex-1 flex justify-center"):

                with H2(classes="font-medium", text="📌 Effortless HTML: No-Templates, No-Boilerplate, Just Clean Pythonic Code"):
                    pass
            with Icon_Plus():
                pass
        with Div(classes="bg-pink-50/50 border border-gray-200 p-2") as desc:
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
            with Div(classes="flex justify-center mt-2 text-sm overflow-auto") as code_block_container:
                pass
                
                
code_block_container.components.append(fct)
overview_box.components.append(feature_inline_html_infobox)

# ================================ end ===============================

# ============================= feature 2 ============================
with writer_ctx:
    with Details(classes="group", extra_classes="[&_summary::-webkit-details-marker]:hidden") as feature_event_handling_infobox:
        with Summary(classes="flex cursor-pointer items-center justify-between gap-1.5 bg-pink-50 p-4 text-gray-900"):
            with Div(classes="flex-1 flex justify-center"):
                with H2(classes="font-medium", text="📌 Straightforward event handling"):
                    pass
            with Icon_Plus():
                pass
        with Div(classes="bg-pink-50/50 border border-gray-200 p-2") as desc:
            with Div(classes="text-left ml-2"):

                with H2(text="Browser event are handled from within Python", classes="text-lg font-medium text-gray-900"):
                    pass

            with Div(classes="text-left mt-4 ml-4"):
                with H2(text="Code Demo: handling browser events", classes="font-medium text-gray-900"):
                        pass
                with Div(classes="flex justify-center mt-2 text-xm overflow-auto") as code_block_container:
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
        with Summary(classes="flex cursor-pointer items-center justify-between gap-1.5 bg-pink-50 p-4 text-gray-900"):
            with Div(classes="flex-1 flex justify-center"):
                with H2(classes="font-medium", text="📌 Easy Interactive UI "):
                    pass
            with Icon_Plus():
                pass
        with Div(classes="bg-pink-50/50 border border-gray-200 p-2") as desc:
            with Div(classes="text-left ml-2"):

                with H2(text="Change UI state using simple python expressions", classes="text-lg font-medium text-gray-900"):
                    pass

            with Ul(classes="ml-4 mt-4 space-y-2") as desc_box:
                with Li(classes="flex items-center gap-1"):
                    with Icon_RightArrow():
                        pass
                    with Span(text="Tailwind utility classes are first class objects", classes="text-gray-700"):
                        pass
                with Li(classes="flex items-center gap-1"):
                    with Icon_RightArrow():
                        pass
                    with Span(text="Allows semantics based update and merge over tailwind classes", classes="text-gray-700"):
                        pass
                with Li(classes="flex items-center gap-1"):
                    with Icon_RightArrow():
                        pass
                    with Span(text="Updated classes are transparently shipped to frontend to update the UI", classes="text-gray-700"):
                        pass
                    

            with Div(classes="text-left mt-4 ml-4"):
                with H2(text="Code Demo: Interactive UI -- Low boilerplate; no explicit client-server communication directive required", classes="font-medium text-gray-900"):
                        pass
                with Div(classes="flex justify-center mt-2 text-sm overflow-auto") as code_block_container:
                    pass


code = """def on_click(dbref, msg, to_ms):
    ms_dbref = to_ms(dbref)
    # change background color to green-500 and font size to text-xl
    ms_dbref.add_twsty_tags(bg/green/5, fz.xl)
    pass
"""   
fct = format_code(code)
code_block_container.components.append(fct)
overview_box.components.append(feature_interactive_ui_infobox)
overview_box.components.append(feature_scalable_efficient_infobox)
overview_box.components.append(feature_uictx_programmability_infobox) 
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

#  we need to pass cookie_state_attr_names to create_endpoint for cookies to get registered. This mechanism is not too clear.

# find a proper way to pass SECRET_KEY

# ofjustpy_webworks_website/overview_panes_extended.py: Itemized Ul/Li totally screwed up.

# All the py_tailwind_utils.dsearch usage is incorrect. dsearch returns an iterator which will always
# evaluate to true.

# dsearch has bugs. need to be tested througly

#.Firefox will not show emoticons

#. need test case for inner_html and self.htmlRender_body.append(self.domDict["inner_html"])

#. resumed the ability to run javascript

#. talk about how from a event handler we can access stubStore.


#. /home/kabiraatmonallabs/Development/Ofjustpy/ofjustpy-skeletonui-plugin/devel/td_chips.py: we really need to emphasize on use of noop/tw-tag. Othersiwe update and remove twsty_tags will not work

#. try to see if we can use ofjustpy-react framework can help with group update: /home/kabiraatmonallabs/Development/Ofjustpy/ofjustpy-skeletonui-plugin/devel/td_chips.py

#. need Ally and ARIA stuff for handlers

#. when importing Skeleton component like AppBar do dependent class get loaded automatically:
# app-bar-row-main app-bar-row-headline

#   <svelte:element this=TabGroup active="border-b-4 border-surface-50-900-token">
#      {console.log("now rendering tabgroup")}
#   </svelte:element> : this produces wierd html as <tabgroup ...> while it should be <div>
  
overview_panel = oj.PD.Subsection("Key Features", overview_box)
endpoint = oj.create_endpoint("overview",
                              childs = [oj.PC.Container(childs=[top_panel, overview_panel
                                                                ],
                                                        twsty_tags=[mr/x/auto]
                                                        )

                                        ],
                              title="Overview"
                              )
oj.add_jproute("/", endpoint)



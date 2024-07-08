from hyperui_plugin.marketing.faqs import  (BackgroundAccentBorder,
                                              )
from py_tailwind_utils import *

import ofjustpy as oj
from . import twsty

import hyperui_plugin as HyUI
from ofjustpy_plugins import format_code
app = oj.load_app()
from html_writer.macro_module import macros, writer_ctx

start_btn = HyUI.button_simpleAndRevealOffsetBorderOnHover(text="Start")
from .overview_feature_inline_html import feature_inline_html_infobox
from .overview_feature_event_handling import feature_event_handling_infobox
from .overview_feature_interactive_ui import feature_interactive_ui_infobox
from .overview_feature_scalable_efficient import feature_scalable_efficient_infobox

from .overview_feature_uictx_programmability import feature_uictx_programmability_infobox

from .overview_feature_ui_library import feature_ui_library_infobox
from .overview_ofjustpy_webapp_stack import about_ofjustpy_webapp_stack

# ============================ top matter ============================
with oj.TwStyCtx(twsty):
    with oj.uictx("topmatter"):
        title = oj.PC.StackV(childs = [oj.PD.Title("Ofjustpy", twsty_tags=[fc/rose/500]),
                                       oj.PD.SubTitle("An easy-to-use yet full-featured web framework in Python",
                                                      twsty_tags=[fc/pink/300]
                                                      )
                                       ]
                             )

        divider = oj.PC.Hr(twsty_tags=[mr/sb/4])

        top_panel = oj.PC.StackV(childs=[title, divider])

    


with writer_ctx:
    with Div(classes="space-y-4 w-5/6") as overview_box:

        pass
overview_box.components.append(feature_inline_html_infobox)
overview_box.components.append(feature_event_handling_infobox)
overview_box.components.append(feature_interactive_ui_infobox)
overview_box.components.append(feature_scalable_efficient_infobox)
overview_box.components.append(feature_uictx_programmability_infobox)
overview_box.components.append(feature_ui_library_infobox)
# overview_box.childs.append(about_ofjustpy_webapp_stack)

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
# SKUI.Ratings should clear fully
#. SKUI.toggle bg/active doesn't work
#. SKUI.Listbox doesn't work
#. SKDUI.Accordion is not working
#. Be very mindful about StackD and hieght anchor. basically the use of relative, absolute ..wasted half a day on it.  
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

#   centering of optmizing of overview not happening

# In hyperui.stats chartup and chartdown has been removed with questionmark...needs to use materialui to bring it back

# <ol><li></li></ol> when rendering from bundler is introducing ::marker -- while when when using css.tailwind.com src doens't
# using ul for now.

# unable to control width of a component using max-w-screen-md, xl, etc.

#. twmax, twmin do not use as last keywork twmax/W/twmax

# tailwind tags sm, md, xl, should belong to same class
overview_panel = oj.PD.Subsection("Key Features", overview_box)

from .panel_oj_about import about_panel

def on_page_ready(dbref, msg, to_ms):
    # reset the slideshows
    # grab hold of the slideshow component
    target = msg.page.session_manager.stubStore.about_components.demo_slideshow.target
    slide_deck_ms = to_ms(target.staticCore.slide_deck)
    slide_deck_ms.bring_to_front("/about_components/slide_demo")

    target = msg.page.session_manager.stubStore.slideshow_techstack.target
    slide_deck_ms = to_ms(target.staticCore.slide_deck)
    slide_deck_ms.bring_to_front("/slide_python")

    pass

endpoint = oj.create_endpoint("overview",
                              childs = [oj.HCCMutable.Container(childs=[top_panel,
                                                                        overview_panel,
                                                                        about_panel
                                                                ],
                                                        twsty_tags=[mr/x/auto, space/y/4]
                                                        )

                                        ],
                              body_classes="font-geist",
                              title="Overview",
                              skeleton_data_theme="seafoam",
                              #rendering_type="SSR"
                              csr_bundle_dir="overview_revised",
                              page_ready = on_page_ready,
                              head_html="""<link rel="preload" src="/static/hyperui/bundle.iife.js" as="script"></script>
                              <link rel="preload" src="/static/shadcnui/bundle.iife.js" as="script"></script>
                              <link rel="preload src="/static/skeletonui/bundle.iife.js" as="script"></script>
"""
                              
                              )
oj.add_jproute("/", endpoint)


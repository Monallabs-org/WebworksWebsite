import logging
import macropy.activate
from py_tailwind_utils import *
import ofjustpy as oj

logger = logging.getLogger(__name__)

oj.set_style("un")

from skeletonui_components.hyperui import sideMenu

# ===================== skeleton theme select bar ====================
import skeletonui_components as SKUI

async def on_theme_select(dbref, msg, to_ms):
    await msg.page.run_javascript(f"""
    console.log("start setting ");
    const body = document.querySelector('body');
    console.log(body);
    body.setAttribute('data-theme', '{msg.value}');
    console.log("Done setting ");
    """)
    pass

select_theme_box  = SKUI.hyperui.Base("theme-selector",
                                      "Select Theme",
                                      classes="mt-4 mr-4 mb-4",
                                      on_change=on_theme_select)
select_theme_box.add_option('skeleton', 'skeleton')
select_theme_box.add_option('modern', 'modern')
select_theme_box.add_option('wintry', 'wintry')
select_theme_box.add_option('rocket', 'rocket')
select_theme_box.add_option('seafoam', 'seafoam')
select_theme_box.add_option('vintage', 'vintage')
select_theme_box.add_option('sahara', 'sahara')
select_theme_box.add_option('crimsom', 'crimson')

# control the layout of the theme selector
# select_theme_frame =  oj.PD.Div(childs=[select_theme_box],
#                                 twsty_tags=[W/full,
#                                             db.f,
#                                             jc.center
#                                             ]
#                                 )

top_bar = oj.PD.Div(twsty_tags=[W/full,
                                db.f,
                                jc.end,
                                space/x/4,
                               
                                ],
                    extra_classes=" bg-gradient-to-br variant-gradient-tertiary-primary",
                    childs=[select_theme_box]
                    )

from skeletonui_components_demo import (stepper_box,
                                        listbox_box,
                                        ratings_box,
                                        slidetoggle_box,
                                        lists_box,
                                        chips_box,
                                        cards_box,
                                        buttons_box,
                                        crumbs_box,
                                        badges_box,
                                        tabgroup_box
                                        )

app = oj.load_app()

sideMenu = sideMenu.Simple("Skeleton components")

with oj.uictx("SKUI_tlc") as tlctx:
    def on_selected(dbref, msg, to_ms):
        """
        action when component is selected
        """
        comp_deck_box_ms = to_ms(tlctx.comp_deck_box)
        comp_deck_box_ms.bring_to_front(f"/{dbref.value}")
        pass
    async def on_page_ready(dbref, msg, to_ms):
        # wp is already mutableShell Page
        wp = msg.page
        # ms_infobox = ms_target_func(infobox)
        # num_clicks = wp.get_cookie('num_clicks')
        # ms_infobox.text =f'Number of Click Events: {num_clicks}'
        #print("SkeletonUI: page ready called")
        comp_deck_box_ms = to_ms(tlctx.comp_deck_box)
        # there is some bug in rendering vertical menu button
        # this is a work around to reset it on page_reload
        #comp_deck_box_ms.bring_to_front("/SKUI_tlc/nobody")
        comp_deck_box_ms.bring_to_front("/Stepper")


        pass

    sideMenu.add_flat_item("stepper",
                           "Stepper",
                           value="Stepper",
                           on_click=on_selected
                           )

    sideMenu.add_flat_item("listbox",
                           "List",
                           value="Listbox",
                           on_click=on_selected
                           )

    sideMenu.add_flat_item("ratingsbox",
                           "Ratings",
                           value="Ratingsbox",
                           on_click=on_selected
                           )

    sideMenu.add_flat_item("slidetogglebox",
                           "Slidetoggle",
                           value="Slidetogglebox",
                           on_click=on_selected
                           )
    
    sideMenu.add_flat_item("listsbox",
                           "Lists",
                           value="Listsbox",
                           on_click=on_selected
                           )

    sideMenu.add_flat_item("chipsbox",
                           "Chip",
                           value="Chipsbox",
                           on_click=on_selected
                           )
    
    sideMenu.add_flat_item("cardsbox",
                           "Card",
                           value="Cardsbox",
                           on_click=on_selected
                           )

    sideMenu.add_flat_item("buttonsbox",
                           "Buttons",
                           value="Buttonsbox",
                           on_click=on_selected
                           )
    
    sideMenu.add_flat_item("crumbsbox",
                           "Crumbs",
                           value="Crumbsbox",
                           on_click=on_selected
                           )

    sideMenu.add_flat_item("badgesbox",
                           "Badges",
                           value="Badgesbox",
                           on_click=on_selected
                           )
    sideMenu.add_flat_item("tabgroupbox",
                           "Tabgroup",
                           value="Tabgroupbox",
                           on_click=on_selected
                           )
    

    all_components = [stepper_box,
                      listbox_box,
                      ratings_box,
                      slidetoggle_box,
                      lists_box,
                      chips_box,
                      cards_box,
                      buttons_box,
                      crumbs_box,
                      badges_box,
                      tabgroup_box
                      ]
    
    comp_deck_box = oj.Mutable.StackD(key="comp_deck_box",
                                      childs=all_components,
                                      height_anchor_key="Cardsbox",
                                      )

    logger.debug(f"skeleton showcase created stackD {id(comp_deck_box)}")
    


comp_display_box = oj.HCCMutable.Valign(
    oj.HCCMutable.Halign(comp_deck_box, twsty_tags=[W/full])

)


#comp_display_box = oj.HCCMutable.Halign(comp_deck_box)
body_box = oj.HCCMutable.StackH(childs = [sideMenu,
                                          oj.HCCMutable.Container(childs=[comp_display_box
                                                                          ],
                                                                  twsty_tags=[mr/x/auto],
                                                                  extra_classes="bg-gradient-to-br variant-gradient-primary-secondary"
                                                                  )

                                          ],
                                ) 

endpoint = oj.create_endpoint("Skeleton-ComponentUI",
                     
                              childs = [top_bar,
                                        body_box
                                        ],
                              title="Skeleton Component UI",
                              page_ready = on_page_ready,
                              csr_bundle_dir="skeletonui"
                              )

oj.add_jproute("/skeletonUI", endpoint)

# from starlette.testclient import TestClient
# client = TestClient(app)
# response = client.get('/') 

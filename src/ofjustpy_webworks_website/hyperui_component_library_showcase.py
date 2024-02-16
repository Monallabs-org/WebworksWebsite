from py_tailwind_utils import *
import ofjustpy as oj
oj.set_style("un")
from hyperui_plugin.sideMenu import  (Simple as SimpleSideMenu,
                                                )
from hyperui_component_library import (alert_box,
                                       badges_box,
                                       breadcrumbs_box,
                                       buttongroups_box,
                                       detailslist_box,
                                       dividers_box,
                                       errorpages_box,
                                       headers_box,
                                       inputs_box,
                                       loginforms_box,
                                       mediaalerts_box,
                                       pagination_box,
                                       selects_box,
                                       sideMenu_box,
                                       stats_box,
                                       steps_box,
                                       tables_box,
                                       tabs_box,
                                       textarea_box,
                                       toggles_box,
                                       verticalmenu_box,
                                       ecomcarts_box,
                                       ecomcollectionfilters_box,
                                       ecomfeaturedsections_box,
                                       ecomproductcards_box,
                                       ecomproductcollection_box,
                                       ecomquantinp_box,
                                       marketingannouncements_box,
                                       marketingbanner_box,
                                       marketingblogcards_box,
                                       buttons_box,
                                       marketingcard_box,
                                       marketingcta_box,
                                       marketingfaq_box,
                                       marketingfooter_box,
                                       marketingform_box,
                                       marketingheader_box,
                                       marketingpopus_box,
                                       marketingpricings_box,
                                       marketingsections_box,
                                       marketingtestimonial_box
                                       

                                       )
app = oj.load_app()
sideMenu = SimpleSideMenu("HyperUI components")
with oj.uictx("tlc") as tlctx:
    def on_hui_comp_selected(dbref, msg, to_ms):
        print("button clicked")
        print (dbref.value)
        comp_deck_box_ms = to_ms(tlctx.comp_deck_box)
        comp_deck_box_ms.bring_to_front(f"/{dbref.value}")
        pass

    sideMenu.add_flat_item("alerts", "Alerts", value="Alerts", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("badges", "Badges", value="Badges", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("breadcrumbs", "Breadcrumbs", value="Breadcrumbs", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("buttongroups", "Buttongroups", value="Buttongroups", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("detailslist", "Detailslist", value="Detailslist", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("dividers", "Dividers", value="Dividers", on_click=on_hui_comp_selected)
    # sideMenu.add_flat_item("dropdown", "Dropdown", value="Dropdown", on_click=on_hui_comp_selected)

    sideMenu.add_flat_item("errorpages", "Errorpages", value="Errorpages", on_click=on_hui_comp_selected)

    sideMenu.add_flat_item("headers", "Headers", value="Headers", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("inputs", "Inputs", value="Inputs", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("loginforms", "LoginForms", value="LoginForms", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("mediaalerts", "MediaAlerts", value="MediaAlerts", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("pagination", "Pagination", value="Pagination", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("selects", "Selects", value="Selects", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("sideMenu", "SideMenu", value="SideMenu", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("Stats", "Stats", value="Stats", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("Steps", "Steps", value="Steps", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("tables", "Tables", value="Tables", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("tabs", "Tabs", value="Tabs", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("textarea", "Textarea", value="Textarea", on_click=on_hui_comp_selected)

    sideMenu.add_flat_item("toggles", "Toggles", value="Toggles", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("verticalmenu", "VerticalMenu", value="VerticalMenu", on_click=on_hui_comp_selected)

    sideMenu.add_flat_item("ecomcarts", "EcomCarts", value="EcomCarts", on_click=on_hui_comp_selected)

    sideMenu.add_flat_item("EcomCollectionFilters", "EcomCollectionFilters", value="EcomCollectionFilters", on_click=on_hui_comp_selected)

    sideMenu.add_flat_item("EconFeaturedSections", "EconFeaturedSections", value="EconFeaturedSections", on_click=on_hui_comp_selected)
    
    sideMenu.add_flat_item("EcomProductCards", "EcomProductCards", value="EcomProductCards", on_click=on_hui_comp_selected)

    sideMenu.add_flat_item("EcomProductCollection", "EcomProductCollection", value="EcomProductCollection", on_click=on_hui_comp_selected)

    sideMenu.add_flat_item("EcomQuantInp", "EcomQuantInp", value="EcomQuantInp", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("MarketingAnnouncements", "MarketingAnnouncements", value="MarketingAnnouncements", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("MarketingBanner", "MarketingBanner", value="MarketingBanner", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("MarketingBlogCards", "MarketingBlogCards", value="MarketingBlogCards", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("Buttons", "Buttons", value="Buttons", on_click=on_hui_comp_selected)
    #sideMenu.add_flat_item("", "", value="", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("MarketingCards", "MarketingCards", value="MarketingCards", on_click=on_hui_comp_selected)

    sideMenu.add_flat_item("MarketingCTA", "MarketingCTA", value="MarketingCTA", on_click=on_hui_comp_selected)

    sideMenu.add_flat_item("MarketingFAQ", "MarketingFAQ", value="MarketingFAQ", on_click=on_hui_comp_selected)

    sideMenu.add_flat_item("MarketingFooter", "MarketingFooter", value="MarketingFooter", on_click=on_hui_comp_selected)

    sideMenu.add_flat_item("MarketingForm", "MarketingForm", value="MarketingForm", on_click=on_hui_comp_selected)

    sideMenu.add_flat_item("MarketingHeader", "MarketingHeader", value="MarketingHeader", on_click=on_hui_comp_selected)

    sideMenu.add_flat_item("MarketingPopups", "MarketingPopups", value="MarketingPopups", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("MarketingPricings", "MarketingPricings", value="MarketingPricings", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("MarketingSections", "MarketingSections", value="MarketingSections", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("MarketingTestimonal", "MarketingTestimonal", value="MarketingTestimonal", on_click=on_hui_comp_selected)
    


    

    



    comp_deck_box = oj.Mutable.StackD(key="comp_deck_box", childs=[alert_box,
                                                                   badges_box,
                                                                   breadcrumbs_box,
                                                                   buttongroups_box,
                                                                   detailslist_box,
                                                                   dividers_box,
                                                                   errorpages_box,
                                                                   headers_box,
                                                                   inputs_box,
                                                                   loginforms_box,
                                                                   mediaalerts_box,
                                                                   pagination_box,
                                                                   selects_box,
                                                                   sideMenu_box,
                                                                   stats_box,
                                                                   steps_box,
                                                                   tables_box,
                                                                   tabs_box,
                                                                   textarea_box,
                                                                   toggles_box,
                                                                   verticalmenu_box,
                                                                   ecomcarts_box,
                                                                   ecomcollectionfilters_box,
                                                                   ecomfeaturedsections_box,
                                                                   ecomproductcards_box,
                                                                   ecomproductcollection_box,
                                                                   ecomquantinp_box,
                                                                   marketingannouncements_box,
                                                                   marketingbanner_box,
                                                                   marketingblogcards_box,
                                                                   buttons_box,
                                                                   marketingcard_box,
                                                                   marketingcta_box,
                                                                   marketingfaq_box,
                                                                   marketingfooter_box,
                                                                   marketingform_box ,
                                                                   marketingheader_box,
                                                                   marketingpopus_box,
                                                                   marketingpricings_box,
                                                                   marketingsections_box,
                                                                   marketingtestimonial_box
                                                                   ],
                      height_anchor_key="Alerts",

                      )

comp_display_box = oj.HCCMutable.Halign(comp_deck_box)




endpoint = oj.create_endpoint("Interactive_Webpage",
                     
         childs = [oj.HCCMutable.StackH(childs = [sideMenu,
                                          oj.HCCMutable.Container(childs=[comp_display_box
                                                                          ],
                                                        twsty_tags=[mr/x/auto]
                                                        )

                                        ],
                                )
                   ],
                              title="Interactive Webpage"
                              )

oj.add_jproute("/", endpoint)

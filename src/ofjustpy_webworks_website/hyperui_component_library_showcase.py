from py_tailwind_utils import *
import ofjustpy as oj
oj.set_style("un")
from hyperui_plugin.sideMenu import  (Simple as SimpleSideMenu,
                                                )
from .hyperui_component_library import (alert_box,
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
    # sideMenu.add_flat_item("breadcrumbs", "Breadcrumbs", value="Breadcrumbs", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("buttongroups", "Buttongroups", value="Buttongroups", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("detailslist", "Detailslist", value="Detailslist", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("dividers", "Dividers", value="Dividers", on_click=on_hui_comp_selected)
    # sideMenu.add_flat_item("dropdown", "Dropdown", value="Dropdown", on_click=on_hui_comp_selected)

    sideMenu.add_flat_item("errorpages", "Errorpages", value="Errorpages", on_click=on_hui_comp_selected)

    sideMenu.add_flat_item("headers", "Headers", value="Headers", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("inputs", "Inputs", value="Inputs", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("loginforms", "LoginForms", value="LoginForms", on_click=on_hui_comp_selected)
    # sideMenu.add_flat_item("mediaalerts", "MediaAlerts", value="MediaAlerts", on_click=on_hui_comp_selected)
    # sideMenu.add_flat_item("pagination", "Pagination", value="Pagination", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("selects", "Selects", value="Selects", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("sideMenu", "SideMenu", value="SideMenu", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("Stats", "Stats", value="Stats", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("Steps", "Steps", value="Steps", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("tables", "Tables", value="Tables", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("tabs", "Tabs", value="Tabs", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("textarea", "Textarea", value="Textarea", on_click=on_hui_comp_selected)

    # sideMenu.add_flat_item("toggles", "Toggles", value="Toggles", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("verticalmenu", "VerticalMenu", value="VerticalMenu", on_click=on_hui_comp_selected)

    ecom_menu_group = sideMenu.add_group_item("eCommerce")
    
    ecom_menu_group.add_flat_item("ecomcarts", "Carts", value="EcomCarts", on_click=on_hui_comp_selected)

    ecom_menu_group.add_flat_item("EcomCollectionFilters", "Collection Filters", value="EcomCollectionFilters", on_click=on_hui_comp_selected)

    ecom_menu_group.add_flat_item("EconFeaturedSections", "Featured Sections", value="EconFeaturedSections", on_click=on_hui_comp_selected)
    
    ecom_menu_group.add_flat_item("EcomProductCards", "Product Cards", value="EcomProductCards", on_click=on_hui_comp_selected)

    ecom_menu_group.add_flat_item("EcomProductCollection", "Product Collection", value="EcomProductCollection", on_click=on_hui_comp_selected)

    ecom_menu_group.add_flat_item("EcomQuantInp", "Quant Inp", value="EcomQuantInp", on_click=on_hui_comp_selected)
    marketing_menu_group = sideMenu.add_group_item("Marketing")
    marketing_menu_group.add_flat_item("MarketingAnnouncements", "Announcements", value="MarketingAnnouncements", on_click=on_hui_comp_selected)
    marketing_menu_group.add_flat_item("MarketingBanner", "Banner", value="MarketingBanner", on_click=on_hui_comp_selected)
    marketing_menu_group.add_flat_item("MarketingBlogCards", "BlogCards", value="MarketingBlogCards", on_click=on_hui_comp_selected)
    marketing_menu_group.add_flat_item("Buttons", "Buttons", value="Buttons", on_click=on_hui_comp_selected)
    #marketing_menu_group.add_flat_item("", "", value="", on_click=on_hui_comp_selected)
    marketing_menu_group.add_flat_item("MarketingCards", "Cards", value="MarketingCards", on_click=on_hui_comp_selected)

    marketing_menu_group.add_flat_item("MarketingCTA", "CTA", value="MarketingCTA", on_click=on_hui_comp_selected)

    marketing_menu_group.add_flat_item("MarketingFAQ", "FAQ", value="MarketingFAQ", on_click=on_hui_comp_selected)

    marketing_menu_group.add_flat_item("MarketingFooter", "Footer", value="MarketingFooter", on_click=on_hui_comp_selected)

    marketing_menu_group.add_flat_item("MarketingForm", "Form", value="MarketingForm", on_click=on_hui_comp_selected)

    marketing_menu_group.add_flat_item("MarketingHeader", "Header", value="MarketingHeader", on_click=on_hui_comp_selected)

    # marketing_menu_group.add_flat_item("MarketingPopups", "Popups", value="MarketingPopups", on_click=on_hui_comp_selected)
    marketing_menu_group.add_flat_item("MarketingPricings", "MarketingPricings", value="MarketingPricings", on_click=on_hui_comp_selected)
    marketing_menu_group.add_flat_item("MarketingSections", "Sections", value="MarketingSections", on_click=on_hui_comp_selected)
    marketing_menu_group.add_flat_item("MarketingTestimonal", "Testimonal", value="MarketingTestimonal", on_click=on_hui_comp_selected)
    


    

    



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


comp_display_box = oj.HCCMutable.Valign(
    oj.HCCMutable.Halign(comp_deck_box,
                         twsty_tags=[W/full]
                         )

)



endpoint = oj.create_endpoint("hyperui_component_ui_library",
                     
         childs = [oj.HCCMutable.StackH(childs = [sideMenu,
                                                  oj.HCCMutable.Container(childs=[comp_display_box
                                                                                  ],
                                                                          twsty_tags=[mr/x/auto]
                                                                          )

                                                  ],
                                        )
                   ],
                              title="HyperUI component library",
                              body_classes="font-geist",
                              #rendering_type="SSR"
                              )

oj.add_jproute("/hyperui", endpoint)

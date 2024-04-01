from py_tailwind_utils import *
import ofjustpy as oj
oj.set_style("un")
from hyperui_plugin.sideMenu import  (Simple as SimpleSideMenu,
                                                )
from shadcnui_component_library import (alert_box,
                                        accordion_box,
                                        alertdialog_box,
                                        avatar_box,
                                        breadcrumb_box,
                                        calendar_box,
                                        checkbox_box,
                                        collapsible_box,
                                        carousel_box,
                                        collapsible_box,
                                        dialog_box,
                                        drawer_box,
                                        dropdownmenu_box,
                                        hovercard_box,
                                        input_box,
                                        menubar_box,
                                        resizable_box,
                                        scrollarea_box,
                                        select_box,
                                        separator_box,
                                        sheet_box,
                                        skeleton_box,
                                        slider_box,
                                        switch_box,
                                        table_box,
                                        textarea_box,
                                        tooltip_box
                                        )


app = oj.load_app()
sideMenu = SimpleSideMenu("ShadcnUI components")
with oj.uictx("tlc") as tlctx:
    def on_hui_comp_selected(dbref, msg, to_ms):
        comp_deck_box_ms = to_ms(tlctx.comp_deck_box)
        comp_deck_box_ms.bring_to_front(f"/{dbref.value}")
        pass
    sideMenu.add_flat_item("alerts", "Alerts", value="Alerts", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("accordion", "Accordion", value="Accordion", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("alertdialog", "AlertDialog", value="AlertDialog", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("avatar", "Avatar", value="Avatar", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("breadcrumb", "Breadcrumb", value="Breadcrumb", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("calendar", "Calendar", value="Calendar", on_click=on_hui_comp_selected)

    sideMenu.add_flat_item("carousel", "Carousel", value="Carousel", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("checkbox", "Checkbox", value="Checkbox", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("collapsible", "Collapsible", value="Collapsible", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("dialog", "Dialog", value="Dialog", on_click=on_hui_comp_selected)

    sideMenu.add_flat_item("drawer", "Drawer", value="Drawer", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("dropdownmenu", "DropdownMenu", value="DropdownMenu", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("hovercard", "HoverCard", value="HoverCard", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("input", "Input", value="Input", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("menubar", "MenuBar", value="MenuBar", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("resizable", "Resizable", value="Resizable", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("scrollarea", "ScrollArea", value="ScrollArea", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("select", "Select", value="Select", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("separator", "Separator", value="Separator", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("sheet", "Sheet", value="Sheet", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("skeleton", "Skeleton", value="Skeleton", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("slider", "Slider", value="Slider", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("switch", "Switch", value="Switch", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("table", "Table", value="Table", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("textarea", "TextArea", value="TextArea", on_click=on_hui_comp_selected)
    sideMenu.add_flat_item("tooltip", "Tooltip", value="Tooltip", on_click=on_hui_comp_selected)
    comp_deck_box = oj.Mutable.StackD(key="comp_deck_box", childs=[alert_box,
                                                                   accordion_box,
                                                                   alertdialog_box,
                                                                   avatar_box,
                                                                   breadcrumb_box,
                                                                   calendar_box,
                                                                   carousel_box,
                                                                   checkbox_box,
                                                                   collapsible_box,
                                                                   dialog_box,
                                                                   drawer_box,
                                                                   dropdownmenu_box,
                                                                   hovercard_box,
                                                                   input_box,
                                                                   menubar_box,
                                                                   resizable_box,
                                                                   scrollarea_box,
                                                                   select_box,
                                                                   separator_box,
                                                                   sheet_box,
                                                                   skeleton_box,
                                                                   #slider_box,
                                                                   switch_box,
                                                                   table_box,
                                                                   textarea_box,
                                                                   tooltip_box
                                                                   ],
                                      height_anchor_key="Alerts",
                                      )
    
comp_display_box = oj.HCCMutable.Halign(comp_deck_box)

endpoint = oj.create_endpoint("Shadcn",
                     
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
    

import ofjustpy as oj
from shadcnui_components.dsl  import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
from ofjustpy.icons import FontAwesomeIcon
oj.set_style("un")

with writer_ctx:
    with SCUI.Alert() as alert_box:
        with SCUI.Alert.Title(twsty_tags=[db.f, space/x/4]):
            with FontAwesomeIcon(label="faTerminal", classes="w-5 h-5"):
                pass
            
            with oj.PD.Prose(text="Heads up!"):
                pass
            pass

        with SCUI.Alert.Description():
            with oj.PD.Prose(text="You can add components to your app using the cli."):
                pass

alert_box = oj.HCCStatic.Div(key="Alerts", childs=[alert_box
                                                   ], twsty_tags=[space/y/4])            


with writer_ctx:
    with SCUI.Accordion() as accordion_box:
        
        with SCUI.Accordion.Item(value="item-1"):
            
            with SCUI.Accordion.Trigger():
                with oj.PD.Prose(text="Is it accessible?"):
                    pass
            
            with SCUI.Accordion.Content():
                with oj.PD.Prose(text="Yes. It adheres to the WAI-ARIA design pattern."):
                    pass

                
accordion_box = oj.HCCStatic.Div(key="Accordion", childs=[accordion_box
                                                   ], twsty_tags=[space/y/4])            


with writer_ctx:
    with SCUI.AlertDialog() as alertdialog_box:
        
        with SCUI.AlertDialog.Trigger():
            with SCUI.Button(key="open", text="Open", variant="outline"):
                pass
        
        with SCUI.AlertDialog.Content():
            
            with SCUI.AlertDialog.Header():
                
                with SCUI.AlertDialog.Title():
                    with oj.PD.Prose(text="Are you absolutely sure?"):
                        pass
                
                with SCUI.AlertDialog.Description():
                    with oj.PD.Prose(text="This action cannot be undone. This will permanently delete your account and remove your data from our servers."):
                        pass
            
            with SCUI.AlertDialog.Footer():
                
                with SCUI.AlertDialog.Cancel():
                    with oj.PD.Prose(text="Cancel"):
                        pass
                
                with SCUI.AlertDialog.Action():
                    with oj.PD.Prose(text="Continue"):
                        pass
alertdialog_box = oj.HCCStatic.Div(key="AlertDialog",
                                           childs=[alertdialog_box],
                                           twsty_tags=[space/y/4]
                                           )




with writer_ctx:
    with SCUI.Avatar() as avatar_box:
        with SCUI.Avatar.Image(src="https://t4.ftcdn.net/jpg/03/32/59/65/360_F_332596535_lAdLhf6KzbW6PWXBWeIFTovTii1drkbT.jpg", alt="@shadcn"):
            pass
        # with SCUI.Avatar.Fallback(text="CN"):
        #     pass

avatar_box = oj.HCCStatic.Div(
    key="Avatar",
    childs=[avatar_box],
    twsty_tags=[space/y/4]
)

with writer_ctx:
    with SCUI.Breadcrumb() as breadcrumb_box:
        with SCUI.Breadcrumb.List():
            with SCUI.Breadcrumb.Item():
                with SCUI.Breadcrumb.Link(href="/"):
                    with oj.PD.Prose(text="Home"):
                        pass
            
            # with SCUI.Breadcrumb.Separator():
            #     pass
            with FontAwesomeIcon(label="faChevronRight", classes="w-5 h-5"):
                pass
            with SCUI.Breadcrumb.Item():
                with SCUI.Breadcrumb.Link(href="/components"):
                    with oj.PD.Prose(text="Components"):
                        pass
            
            # with SCUI.Breadcrumb.Separator():
            #     pass
            
            with FontAwesomeIcon(label="faChevronRight", classes="w-5 h-5"):
                pass
            
            with SCUI.Breadcrumb.Item():
                with SCUI.Breadcrumb.Page():
                    with oj.PD.Prose(text="Breadcrumb"):
                        pass

breadcrumb_box = oj.HCCStatic.Div(
    key="Breadcrumb",
    childs=[breadcrumb_box],
    twsty_tags=[space/y/4]
)


                    
calendar = SCUI.Calendar()
calendar_box = oj.HCCStatic.Div(key="Calendar",
                                childs = [calendar],
                                )


with writer_ctx:
    with SCUI.Carousel(classes="w-full max-w-xs") as carousel_box:
        with SCUI.Carousel.Content():
            with SCUI.Carousel.Item():
                with oj.PD.Div(classes="p-1"):
                    with SCUI.Card():
                        with SCUI.Card.Content(classes="flex aspect-square items-center justify-center p-6"):
                            with oj.PD.Span(classes="text-4xl font-semibold"):
                                with oj.PD.Prose(text=f"1"):
                                    pass

            with SCUI.Carousel.Item():
                with oj.PD.Div(classes="p-1"):
                    with SCUI.Card():
                        with SCUI.Card.Content(classes="flex aspect-square items-center justify-center p-6"):
                            with oj.PD.Span(classes="text-4xl font-semibold"):
                                with oj.PD.Prose(text=f"2"):
                                    pass                                

            with SCUI.Carousel.Item():
                with oj.PD.Div(classes="p-1"):
                    with SCUI.Card():
                        with SCUI.Card.Content(classes="flex aspect-square items-center justify-center p-6"):
                            with oj.PD.Span(classes="text-4xl font-semibold"):
                                with oj.PD.Prose(text=f"3"):
                                    pass

            with SCUI.Carousel.Item():
                with oj.PD.Div(classes="p-1"):
                    with SCUI.Card():
                        with SCUI.Card.Content(classes="flex aspect-square items-center justify-center p-6"):
                            with oj.PD.Span(classes="text-4xl font-semibold"):
                                with oj.PD.Prose(text=f"4"):
                                    pass
                                
        with SCUI.Carousel.Previous():
            pass
        
        with SCUI.Carousel.Next():
            pass
        

carousel_box = oj.HCCStatic.Div(key="Carousel",
                                childs = [carousel_box],
                                )

# ============================= checkbox =============================
checkbox = SCUI.Checkbox(key="terms")
label = SCUI.Label(for_="/terms", text="Accept terms and conditions",
              classes="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70")


label_box = oj.PD.Div(classes="flex items-center space-x-2",
          childs = [checkbox, label

              ]
          )

checkbox_box = oj.HCCStatic.Div(key="Checkbox",
                                childs = [label_box],
                                )

# ============================ collapsible ===========================
with writer_ctx:
    with SCUI.Collapsible() as collapsible_box:
        with oj.PD.Div(classes="flex items-center justify-between space-x-4 px-4"):
            with oj.PD.H4(classes="text-sm font-semibold"):
                with oj.PD.Prose(text="Can I use this in my project?"):
                    pass
                pass
            with SCUI.Collapsible.Trigger():
                with SCUI.Button(key="updown",
                                 variant="ghost",
                                 classes="w-9 p-0"):
                    with FontAwesomeIcon(label="faUpDown", classes="w-5 h-5"):
                        pass
                    pass

                pass
        
        
        with SCUI.Collapsible.Content():
            with oj.PD.Prose(text="Yes. Free to use for personal and commercial projects. No attribution required."):
                pass
            
collapsible_box = oj.HCCStatic.Div(key="Collapsible",
                                childs = [collapsible_box],
                                )

# ============================== dialog ==============================
with writer_ctx:
    with SCUI.Dialog() as dialog_box:
        
        with SCUI.Dialog.Trigger():
            with SCUI.Button(text="Open",
                             key="open",
                             variant="outline"):
                pass
        
        with SCUI.Dialog.Content():
            
            with SCUI.Dialog.Header():
                
                with SCUI.Dialog.Title():
                    with oj.PD.Prose(text="Are you absolutely sure?"):
                        pass
                
                with SCUI.Dialog.Description():
                    with oj.PD.Prose(text="This action cannot be undone. This will permanently delete your account and remove your data from our servers."):
                        pass
dialog_box = oj.HCCStatic.Div(key="Dialog",
                                childs = [dialog_box],
                                )

# ============================== drawer ==============================
with writer_ctx:
    with SCUI.Drawer() as drawer_box:
        
        with SCUI.Drawer.Trigger():
            with SCUI.Button(key="drawer", text="Open"):
                pass
        
        with SCUI.Drawer.Content():
            
            with SCUI.Drawer.Header():
                
                with SCUI.Drawer.Title():
                    with oj.PD.Prose(text="Are you absolutely sure?"):
                        pass
                
                with SCUI.Drawer.Description():
                    with oj.PD.Prose(text="This action cannot be undone."):
                        pass
            
            with SCUI.Drawer.Footer():
                
                with SCUI.Button(key="abtn"):
                    with oj.PD.Prose(text="Submit"):
                        pass
                
                with SCUI.Drawer.Close():
                    with oj.PD.Prose(text="Cancel"):
                        pass
                    
drawer_box = oj.HCCStatic.Div(
    key="Drawer",
    childs=[drawer_box],

)

# =========================== DropdownMenu ===========================

with writer_ctx:
    with SCUI.DropdownMenu() as dropdownmenu_box:
        
        with SCUI.DropdownMenu.Trigger():
            with SCUI.Button(key="dropdown", text="Open"):
                pass
        
        with SCUI.DropdownMenu.Content():
            
            with SCUI.DropdownMenu.Group():
                
                with SCUI.DropdownMenu.Label():
                    with oj.PD.Prose(text="My Account"):
                        pass
                
                with SCUI.DropdownMenu.Separator():
                    pass
                
                with SCUI.DropdownMenu.Item():
                    with oj.PD.Prose(text="Profile"):
                        pass
                
                with SCUI.DropdownMenu.Item():
                    with oj.PD.Prose(text="Billing"):
                        pass
                
                with SCUI.DropdownMenu.Item():
                    with oj.PD.Prose(text="Team"):
                        pass
                
                with SCUI.DropdownMenu.Item():
                    with oj.PD.Prose(text="Subscription"):
                        pass

dropdownmenu_box = oj.HCCStatic.Div(
    key="DropdownMenu",
    childs=[dropdownmenu_box],
)

# =============================== hover ==============================
with writer_ctx:
    with SCUI.HoverCard() as hovercard_box:
        
        with SCUI.HoverCard.Trigger():
            with oj.PD.Prose(text="Hover"):
                pass
        
        with SCUI.HoverCard.Content():
            with oj.PD.Prose(text="SvelteKit - Web development, streamlined"):
                pass

hovercard_box = oj.HCCStatic.Div(
    key="HoverCard",
    childs=[hovercard_box],
    twsty_tags=[space/y/4]
)


# =============================== input==============================

inp1 = SCUI.Input(key="inp1",
                  type="email",
                  placeholder="email",
                  classes="max-w-xs")
inp_with_label = oj.PD.Div(classes="flex w-full max-w-sm flex-col gap-1.5",
               childs=[SCUI.Label(for_="email", text="Email"),
                       SCUI.Input(key="inp1",
                                  type="email",
                                  placeholder="email",
                                  classes="max-w-xs")
                   ]
        )

inp_with_label_text = oj.PD.Div(classes="flex w-full max-w-sm flex-col gap-1.5",
               childs=[SCUI.Label(for_="email", text="Email"),
                       SCUI.Input(key="inp1", type="email", placeholder="email", classes="max-w-xs"),
                       oj.PC.Prose(text="Enter your email address.", extra_classes="text-muted-foreground")
                    
                   ]
        )

inp_with_button = oj.AD.Form(key="aform", classes="flex w-full max-w-sm items-center space-x-2",
                                 childs = [SCUI.Input(key="inp1", type="email", placeholder="email", classes="max-w-xs"),
                                           SCUI.Button(key="abtn", type_= "submit",text="Subscribe")
                                           

                                     ]
                                 )

                                 
input_box = oj.PD.StackV(childs=[inp1,
                                 inp_with_label,
                                 inp_with_label_text,
                                 inp_with_button],
             twsty_tags=[space/y/8]
             )

input_box = oj.HCCStatic.Div(
    key="Input",
    childs=[input_box],
    twsty_tags=[space/y/4]
)

# ============================== menubar =============================

with writer_ctx:
    with SCUI.Menubar() as menubar_box:
        
        with SCUI.Menubar.Menu():
            
            with SCUI.Menubar.Trigger():
                with oj.PD.Prose(text="File"):
                    pass
            
            with SCUI.Menubar.Content():
                
                with SCUI.Menubar.Item():
                    with oj.PD.Prose(text="New Tab"):
                        pass
                    with SCUI.Menubar.Shortcut():
                        with oj.PD.Prose(text="⌘T"):
                            pass
                
                with SCUI.Menubar.Item():
                    with oj.PD.Prose(text="New Window"):
                        pass
                
                with SCUI.Menubar.Separator():
                    pass
                
                with SCUI.Menubar.Item():
                    with oj.PD.Prose(text="Share"):
                        pass
                
                with SCUI.Menubar.Separator():
                    pass
                
                with SCUI.Menubar.Item():
                    with oj.PD.Prose(text="Print"):
                        pass
menubar_box = oj.HCCStatic.Div(
    key="MenuBar",
    childs=[menubar_box],
)


# ============================= resizable ============================
with writer_ctx:
    with SCUI.Resizable(direction="horizontal", extra_classes="min-h-[200px] max-w-md rounded-lg border") as resizable_box:
        with SCUI.Resizable.Pane(defaultSize=25):
            with oj.PD.Div(classes="flex h-full items-center justify-center p-6"):
                with oj.PD.Span(classes="font-semibold"):
                    with oj.PD.Prose(text="Sidebar"):
                        pass

        with SCUI.Resizable.Handle(withHandle=True):
            pass

        with SCUI.Resizable.Pane(defaultSize=75):
            with oj.PD.Div(classes="flex h-full items-center justify-center p-6"):
                with oj.PD.Span(classes="font-semibold"):
                    with oj.PD.Prose(text="Content"):
                        pass


        pass

resizable_box = oj.HCCStatic.Div(
    key="Resizable",
    childs=[resizable_box],
    twsty_tags=[space/y/4]
)


    
# ============================ scrollarea ============================
with writer_ctx:
    with SCUI.ScrollArea(classes="h-16 w-80", orientation="both") as scrollarea_box:
        with oj.PD.Prose(twtags_tags=W/"400px", text="Jokester began sneaking into the castle in the middle of the night and leaving jokes all over the place: under the king's pillow, in his soup, even    in the royal toilet. The king was furious, but he couldn't seem to stop Jokester. And then, one day, the people of the kingdom discovered that the jokes left by Jokester were so funny that they couldn't help but laugh. And    once they started laughing, they couldn't stop."):

        
            pass
    pass

scrollarea_box = oj.HCCStatic.Div(
    key="ScrollArea",
    childs=[scrollarea_box],

)


# ============================= selectbox ============================

with writer_ctx:
    with SCUI.Select() as select_box:
        with SCUI.Select.Trigger(extra_classes="w-[400px]"):
            
            with SCUI.Select.Value(placeholder="Theme"):
                pass
        
        with SCUI.Select.Content():
            
            with SCUI.Select.Item(value="light"):
                with oj.PD.Prose(text="Light"):
                    pass
            
            with SCUI.Select.Item(value="dark"):
                with oj.PD.Prose(text="Dark"):
                    pass
            
            with SCUI.Select.Item(value="system"):
                with oj.PD.Prose(text="System"):
                    pass
select_box = oj.HCCStatic.Div(
    key="Select",
    childs=[select_box],
)


# ============================= separator ============================
with writer_ctx:
    with oj.PD.Div() as separator_box:
        with oj.PD.Div(classes="space-y-1"):
            with oj.PD.H4(classes="text-sm font-medium leading-none"):
                with oj.PD.Prose(text="Radix Primitives"):
                    pass
            
            with oj.PD.P(classes="text-sm", extra_classes="text-muted-foreground"):
                with oj.PD.Prose(text="An open-source UI component library."):
                    pass
        
        with SCUI.Separator(classes="my-4"):
            pass
        
        with oj.PD.Div(classes="flex h-5 items-center space-x-4 text-sm"):
            
            with oj.PD.Div():
                with oj.PD.Prose(text="Blog"):
                    pass
            
            with SCUI.Separator(orientation="vertical"):
                pass
            
            with oj.PD.Div():
                with oj.PD.Prose(text="Docs"):
                    pass
            
            with SCUI.Separator(orientation="vertical"):
                pass
            
            with oj.PD.Div():
                with oj.PD.Prose(text="Source"):
                    pass
        
        pass
separator_box = oj.HCCStatic.Div(
    key="Separator",
    childs=[separator_box],
    twsty_tags=[space/y/4]
)



# =============================== sheet ==============================
with writer_ctx:
    with SCUI.Sheet() as sheet_box:
        
        with SCUI.Sheet.Trigger():
            with SCUI.Button(key="sheet",
                             text="Open",
                             variant="outline"):
                pass
        
        with SCUI.Sheet.Content():
            
            with SCUI.Sheet.Header():
                
                with SCUI.Sheet.Title():
                    with oj.PD.Prose(text="Are you sure absolutely sure?"):
                        pass
                
                with SCUI.Sheet.Description():
                    with oj.PD.Prose(text="This action cannot be undone. This will permanently delete your account and remove your data from our servers."):
                        pass

sheet_box = oj.HCCStatic.Div(
    key="Sheet",
    childs=[sheet_box],
)


                    
# ============================= skeleton =============================
with writer_ctx:
    with oj.PD.Div(classes="flex items-center space-x-4") as skeleton_box:
        
        with SCUI.Skeleton(classes="h-12 w-12 rounded-full"):
            pass
        
        with oj.PD.Div(classes="space-y-2"):
            
            with SCUI.Skeleton(classes="h-4 ", extra_classes="w-[400px]"):
                pass
            
            with SCUI.Skeleton(classes="h-4 ", extra_classes="w-[400px]"):
                pass
            
skeleton_box = oj.HCCStatic.Div(
    key="Skeleton",
    childs=[skeleton_box],
)

# ============================== slider ==============================
with writer_ctx:
    with SCUI.Slider(extra_classes="w-[400px]", value="[50]", max_=100, step=1) as slider_box:
        pass

slider_box = oj.HCCStatic.Div(
    key="Slider",
    childs=[slider_box],
    twsty_tags=[space/y/4]
)



# ============================== switch ==============================

with writer_ctx:
    with SCUI.Switch(extra_classes="", checked=True) as switch_box:
        pass
    

    
switch_box = oj.HCCStatic.Div(
    key="Switch",
    childs=[switch_box],
    twsty_tags=[space/y/4]
)

# =============================== table ==============================
with writer_ctx:
    with SCUI.Table() as table_box:
        
        with SCUI.Table.Caption():
            with oj.PD.Prose(text="A list of your recent invoices."):
                pass
        
        with SCUI.Table.Header():
            
            with SCUI.Table.Row():
                
                with SCUI.Table.Head(extra_classes="w-[100px]"):
                    with oj.PD.Prose(text="Invoice"):
                        pass
                
                with SCUI.Table.Head():
                    with oj.PD.Prose(text="Status"):
                        pass
                
                with SCUI.Table.Head():
                    with oj.PD.Prose(text="Method"):
                        pass
                
                with SCUI.Table.Head(classes="text-right"):
                    with oj.PD.Prose(text="Amount"):
                        pass
        
        with SCUI.Table.Body():
            
            with SCUI.Table.Row():
                
                with SCUI.Table.Cell(class_="font-medium"):
                    with oj.PD.Prose(text="INV001"):
                        pass
                
                with SCUI.Table.Cell():
                    with oj.PD.Prose(text="Paid"):
                        pass
                
                with SCUI.Table.Cell():
                    with oj.PD.Prose(text="Credit Card"):
                        pass
                
                with SCUI.Table.Cell(class_="text-right"):
                    with oj.PD.Prose(text="$250.00"):
                        pass
                    
    

table_box = oj.HCCStatic.Div(
    key="Table",
    childs=[table_box],
    twsty_tags=[space/y/4]
)


# ============================= textarea =============================

with writer_ctx:
    with oj.PD.Div(class_="grid w-full gap-2") as with_button_box:
        
        with SCUI.Textarea(placeholder="Type your message here."):
            pass
        
        with SCUI.Button(key="abtn"):
            with oj.PD.Prose(text="Send message"):
                pass


with writer_ctx:            
    with oj.PD.Div(class_="grid w-full gap-1.5") as with_text_box:
        
        with SCUI.Label():
            with oj.PD.Prose(text="Your Message"):
                pass
        
        with SCUI.Textarea(placeholder="Type your message here.", id="message-2"):
            pass
        
        with oj.PD.P(class_="text-sm text-muted-foreground"):
            with oj.PD.Prose(text="Your message will be copied to the support team."):
                pass


with writer_ctx:
    with oj.PD.Div(class_="grid w-full gap-1.5") as with_label_box:
        with SCUI.Label():
            with oj.PD.Prose(text="Your message"):
                pass
        
        with SCUI.Textarea(placeholder="Type your message here.", id="message"):
            pass


textarea_box = oj.PD.StackV(
    childs = [
        with_label_box,
        with_text_box,
        with_button_box
    ],
    twsty_tags=[space/y/4]
    )
textarea_box = oj.HCCStatic.Div(
    key="TextArea",
    childs=[textarea_box],
)


        
# ============================== tooltip =============================
with writer_ctx:
    with SCUI.Tooltip() as tooltip_box: 
        with SCUI.Tooltip.Trigger():
            with SCUI.Button(text="Hover", variant="outline", key="tooltip_btn"):
                pass
        
        with SCUI.Tooltip.Content():
            with oj.PD.P():
                with oj.PD.Prose(text="Add to library"):
                    pass
tooltip_box = oj.HCCStatic.Div(
    key="Tooltip",
    childs=[tooltip_box],
    twsty_tags=[space/y/4]
)



import ofjustpy as oj
from py_tailwind_utils import *
import ofjustpy_components as ojx

#@oj.webpage_cache
def on_btn_click(dbref, msg, target_of):
    print("circle clicked", dbref.text, msg.value)

    pass

def on_input_change(dbref, msg, target_of):
    print("on input called", msg.value)
    pass

    
def stubs():
    for tag, title, hcs in [("text",
                             "Span html component",
                             oj.PC.Span(text="The text for span")
                             ),
                            ("para",
                             "Para html component",
                             oj.PC.P(text="A long sample paragraph with more text than span element"),
                             ),
                            ("button",
                             "Button html component", 
                                oj.AC.Button(key="mybtn",
                                             value="myval",
                                             text="Click me ",
                                             pcp=[bg/blue/"100/50"],
                                             on_click =  on_btn_click
                                             )
                             ),
                            ("href",
                             "Hyperlink html component",
                             oj.AC.A(key="myA", text="Wikipedia", href="https://www.wikipedia.org/")
                             ),
                            # ("cbinput",
                            #  "Checkbox with input text",
                            #  oj.AC.CheckboxInput(key="cboxinp",
                            #                      input_attrs={'pcp':[mr/sr/1], 'text': "Check if got milk"}).event_handle(oj.change, on_input_change),
                            #  ),
                            ("labeledinput",
                             "Input box with label prefixed", 
                             oj.PC.LabelDiv(
                                       childs=[oj.PC.Span(text="Enter a value"),
                                              oj.AC.TextInput(key="linp",
                                                              placeholder="dummy value", on_change= on_input_change)
                                              ]
                                       )
                             ),
                            ("textarea",
                             "Textarea html component", 
                             oj.AC.Textarea(key="textarea",
                                            text="lets put lots of text lets put lots of text lets put lots of textlets put lots of text", on_change = on_input_change )
                             ),
                             
                            # ("keyvalue",
                            #  "Key value custom component", 
                            #  oj.KeyValue_("keyvalue", "akey", "thevalue"),
                            #  ),
                            ("select",
                             "Select html component",

                             oj.AC.Select(key="myselect",
                                          childs = [oj.PC.Option(
                                                        text=k,
                                                        value=k)
                                           for k in ['red', 'blue', 'green']
                                           ],
                                          value="red",
                                          on_change= on_input_change
                                          )

                             )
                            ]:
        hcs.add_twsty_tags(bg/pink/"100/30")
        yield oj.PC.Subsubsection(
                                title,
                                hcs
                                )
        yield oj.PC.Hr()


#comp_stack = oj.PC.Halign(oj.PC.StackV(childs=[oj.PC.Halign(stub) for stub in stubs()]))
tlc = oj.PC.Container(childs = [_ for _ in stubs()])

# wp_template = oj.Mutable.WebPage(key="static-components",
#                  childs = [tlc]
#                  )
wp_demo_basic_components = oj.create_endpoint(key="demo_basic_components",
                                              childs = [tlc],
                                              title="Demo basic components"
                                              )


import ofjustpy as oj
from py_tailwind_utils import *
from ofjustpy_plugins import format_code

code = """import ofjustpy as oj
from py_tailwind_utils import *

with oj.uictx("deckdemo") as  deckdemo:
    btn1 = oj.Mutable.Button(key="mybtn1",
                              value="/mybtn2",
                              text="Click me1 ",
                              twsty_tags=[bg/blue/"100/50"],
                              #on_click = on_btn_click
                              )

    btn2 = oj.Mutable.Button(key="mybtn2",
                              value="/mybtn1",
                              text="Click me2 ",
                              twsty_tags=[bg/blue/"100/50"],
                              #on_click = on_btn_click
                              )
            
    thedeck = oj.Mutable.StackD(key = "thedeck",
                                childs = [ btn1, btn2
                               ]
                      )
    def on_btn_click(dbref, msg, target_of):
        target = dget(deckdemo, msg.value)
        ms_thedeck = target_of(thedeck)
        ms_thedeck.bring_to_front(target_of(target).id)
        pass


    btn1.on("click", on_btn_click)
    btn2.on("click", on_btn_click)
    
    
wp_endpoint = oj.create_endpoint(key="example_008",
                                 childs = [thedeck],
                                 title="example_008"
                                 )
oj.add_jproute("/", wp_endpoint)
app = oj.load_app()
                                 """


pycode_viewer = oj.PC.Subsection("The markdown text", oj.PC.Pre(text=code,
                                                                 twsty_tags  = [H/64]
                                                                 )
                                 )

collapse_box = oj.PC.Collapsible(hide_banner_text="Sample Python code",
                                 hide_banner_classes = [min/W/"1/2", W/"2/3"],
                                 childs=[pycode_viewer],

                                 twsty_tags=[bd/gray/5, bd/1, W/full, ovf/x/auto]
                                 )

# use no extrawhitespace style
oj.set_style("un")
fct = format_code(code)
oj.set_style("snow")
rendered_viewer = oj.PC.Subsection("HTML rendered via Ofjustpy",
                                   fct)
                                   

app = oj.load_app()

wp_demo_pycode_formatting = oj.create_endpoint(key="demo_pycode_formatting",
                                         childs = [oj.PC.Container(childs = [collapse_box,
                                                                             oj.PC.Hr(),
                                                                             rendered_viewer
                                                                             ]

                                                                   )
                                                   
                                                   ],
                                               title="Demo render python code"
                                 )


#oj.add_jproute("/demo_pycode_formatting", wp_endpoint)
    

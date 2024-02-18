import ofjustpy as oj
from py_tailwind_utils import *
import mistletoe
from . import md_view_handlers
md_input = 'example_all.md'



markdown_viewer = oj.PC.Subsection("The markdown text", oj.PC.Pre(text="""# Top level heading
## Level2 heading
### Level3 heading
#### Level4 heading : Show items as a list
- list item 1
- list item 2

#### Level4 heading : Show items in a grid
###### list_view_handler:gridify
- list item 1
- list item 2

#### Level4 heading : Show images in a grid

###### list_view_handler:gridify
###### list_item_view_handler:href_image_viewer
- [Black/White Acrylic Case for Raspberry Pi 4 with 1x Cooling Fan and 4x Heat Sinks](https://rarecomponents.com/store/black-white-acrylic-case-raspberry-pi4 "A no-frills basic case for Rpi4")  
![](/static/0-2185-400x400.jpg "")

- [Black/White Acrylic Case for Raspberry Pi 4 with 1x Cooling Fan and 4x Heat Sinks](https://rarecomponents.com/store/black-white-acrylic-case-raspberry-pi4 "A no-frills basic case for Rpi4")  
![](/static/0-2185-400x400.jpg "")

- [Black/White Acrylic Case for Raspberry Pi 4 with 1x Cooling Fan and 4x Heat Sinks](https://rarecomponents.com/store/black-white-acrylic-case-raspberry-pi4 "A no-frills basic case for Rpi4")  
![](/static/0-2185-400x400.jpg "")

###### list_view_handler:None
###### list_item_view_handler:None

## Level 2 heading: reset view handler
- First List item 
- Second list item 
- Third list item 

                                 """, twsty_tags  = [H/64]
    )
                                   )

collapse_box = oj.PC.Collapsible(hide_banner_text="Markdown Text",
                                 hide_banner_classes = [min/W/"1/2", W/"2/3"],
                                 childs=[markdown_viewer],

                                 twsty_tags=[bd/gray/5, bd/1, W/full, overflowx.auto]
                                 )
# collapse_box = oj.PC.Collapsible(hide_banner_text="Expand for TextInput code",
#                                  hide_banner_classes = [min/W/"1/2", W/"2/3"],
#                                  childs=[oj.PC.Pre(text="""tifc""",


#                                                     twsty_tags=[H/64])],
#                                  twsty_tags=[bd/gray/5, bd/1, W/"2/3", ovf/x/auto]
#                                  )

with open(md_input, 'r') as fin:
    rendered = mistletoe.markdown(fin,
                                  mistletoe.OfjustpyRenderer,
                                  mditem_viewer_handlers=md_view_handlers
                                  )


rendered_viewer = oj.PC.Subsection("HTML rendered via Ofjustpy",
                                   rendered)
                                   

app = oj.load_app()
#because this uses collapsible component we have to render via svelte
#from webpage_html_rendering_cache_optimization  import create_endpoint
wp_demo_markdown_formatting = oj.create_endpoint(key="demo_render_markdown_formatted",
                                         childs = [oj.PC.Container(childs = [collapse_box,
                                                                             rendered_viewer
                                                                             ]

                                                                   ),

                                                   
                                                   ],
                                                 title="Demo render markdown formatted text"
                                 )


#oj.add_jproute("/demo_markdown_formatting", wp_endpoint)
    

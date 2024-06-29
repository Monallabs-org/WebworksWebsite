"""
cherry pick content  from index.py on techstack and demos
"""
import ofjustpy as oj
from ofjustpy_components.component_mouseover_slideshow import SlideShow
from py_tailwind_utils import *
# ============================ tech stack============================
divider = oj.PC.Hr(twsty_tags=[mr/sb/4])
slide_labels = ["python",
                "starlette",
                "websockets",
                "svelte",
                "tailwind",
                "deployment",
                
    ]
slide_info = {"python": ("Python",
                             oj.PC.Prose(text="Ofjustpy enables all aspects of webdevelopment through Python.")
                             ),
              "starlette": ("Async Processing",
                                oj.PC.Prose(text="Starlette serves as the asynchronous web server engine sitting atop the Ofjustpy framework. Using async communication enables building responsive and efficient webapp")
                                ),
              "websockets": ("Websocket communication",
                             oj.PC.Prose(text="All communication between webserver and UI takes place via websockets.")
                             ),
              "svelte": ("Svelte at frontend",
                         oj.PC.Prose(text="All Ofjustpy directives to frontend are processed by Svelte runtime.")
                         ),
              "tailwind": ("Tailwind Styling",
                               oj.PC.Prose(text="Tailwind CSS is used to control the layout and style the components of the webpage")
                               ),
              "deployment": ("Nginx and Unit",
                                oj.PC.Prose(text="App written wint Ofjustpy, can be deploy with Nginx/Unit server")
                                ),
              }

techstack_slideshow = SlideShow("techstack",
                                slide_labels,
                                slide_info,
                                "deployment")

techstack_panel = oj.HCCMutable.Subsection("Ofjustpy tech stack",
                                           techstack_slideshow
                                           )



# =========================== demo section ===========================
slide_labels = ["demo",
                "examples",
                "text_renderer",
                "schema_editor",
                "chartjs_editor",
                "theme_editor",
    ]
slide_info = {"demo": ("Basic and advanced components",
                             oj.PC.StackV(childs = [oj.AC.A(key=f"demo_basic_capabilities",
                                                      href=f"/demo_basic_capabilities",
                                                      title=f"demo_basic_capabilities",
                                                      text=f"Basic components",
                                                      twsty_tags=[boxtopo.bd, bdr.lg, bd/gray/6,
                                                                  shadow/gray/2,
                                                                  shadow.md
                                                                  ]
                                                      ),
                                              oj.AC.A(key=f"demo_advanced_capabilities",
                                                      href=f"/demo_advanced_capabilities",
                                                      title=f"demo_advanced_capabilities",
                                                      text=f"Advanced components",
                                                      twsty_tags=[boxtopo.bd, bdr.lg, bd/gray/6,
                                                                  shadow/gray/2,
                                                                  shadow.md
                                                                  ]
                                                      ),
                                                    ],
                                          twsty_tags=[space/y/2]

                                    )
                             ),

              "examples": ("Examples",
                           
                           oj.AC.A(key=f"examples",
                                   href=f"/examples_index",
                                   title=f"Example collection",
                                   text=f"Click here for example collection illustrating ofjustpy components usage",
                                   twsty_tags=[boxtopo.bd, bdr.lg, bd/gray/6,
                                               shadow/gray/2,
                                               shadow.md
                                               ]
                                   )
                           
                                ),
              "schema_editor": ("CSV Data schema editor",
                                oj.PC.Prose(text="CSV Data schema editor (TBD)")
                                ),
              "chartjs_editor": ("ChartJS editor",
                                 oj.PC.Prose(text="Visually edit ChartJS (TBD)")
                                 ),
              "theme_editor": ("Webpage Theme Editor",
                               oj.PC.Prose(text="Visually edit theme of a page (TBD)")
                               ),
              "text_renderer": ("Rendering markdown text and Python code ",
                                oj.PC.StackV(childs = [oj.AC.A(key=f"demo_markdown_formatting",
                                                      href=f"/demo_markdown_formatting",
                                                      title=f"demo markdown formatting",
                                                      text=f"Rendering markdown text using ofjustpy",
                                                      twsty_tags=[boxtopo.bd, bdr.lg, bd/gray/6,
                                                                  shadow/gray/2,
                                                                  shadow.md
                                                                  ]
                                                               ),
                                                       oj.AC.A(key=f"demo_pycode_formatting",
                                                               href=f"/demo_pycode_formatting",
                                                               title=f"demo pycode formatting",
                                                               text=f"Rendering python code using ofjustpy",
                                                               twsty_tags=[boxtopo.bd, bdr.lg, bd/gray/6,
                                                                           shadow/gray/2,
                                                                           shadow.md
                                                                           ]
                                                               )
                                                    ],
                                          twsty_tags=[space/y/2]

                                    )
                                ),
              }

demo_slideShow = SlideShow("demos",
                           slide_labels,
                           slide_info,
                           "text_renderer")

demo_panel = oj.HCCMutable.Subsection("See ofjustpy in action",
                                   demo_slideShow
                   )


tlc = oj.HCCMutable.Container(childs = [
                                           demo_panel,
                                           oj.Halign(divider),
                                           techstack_panel,
                                  ]
                        )
app = oj.load_app()
# use cached optimized html rendering for responsive static pages. 
from webpage_html_rendering_cache_optimization  import create_endpoint
wp_index = create_endpoint(key="webworks_index",
                              childs = [tlc
                                        ],
                              title="Webworks By Monallabs",
                              
                              )

oj.add_jproute("/", wp_index)

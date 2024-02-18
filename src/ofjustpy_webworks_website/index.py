import ofjustpy as oj
from ofjustpy_components.component_mouseover_slideshow import SlideShow
from py_tailwind_utils import *

with oj.uictx("topmatter"):
    title = oj.PC.StackV(childs = [oj.PC.Title("Ofjustpy", twsty_tags=[fc/rose/5]),
                                   oj.PC.SubTitle("An easy-to-use yet full-featured web framework in Python",
                                                  twsty_tags=[fc/pink/3]
                                                  )
                                   ]
                         )

    overview = oj.PC.Subsection("Overview",
                                oj.PC.Halign(oj.PC.Prose(text="Ofjustpy is a Python based webframework to seamlessly construct web-based applications and websites with ease. Leveraging Python's powerful language constructs and various libraries and utilities, this framework offers an extensive array of tools and APIs that dramatically simplify the process of developing sophisticated webpages.",
                                       twsty_tags=[max/W/"prose", fz.xl]
                                       )
                                )
                        )


    divider = oj.PC.Hr(twsty_tags=[mr/sb/4])

    top_panel = oj.PC.StackV(childs=[title, divider,  overview])


with oj.uictx("body"):    
    # ==================== slideshow panel ====================
    slide_labels = ["easy_to_use" ,
                "batteries_included",
                 "interactivity",
                 "performant",
                 "tradeoffs",
                 "misc"
                    ]

    slide_info = { "easy_to_use": ("Easy to use",
                                   oj.PC.Ul(childs=[oj.PC.Li(text="Unified Python approach - Eliminates need for multiple languages (JavaScript, Jinja2, CSS, HTML)"),
                                                    oj.PC.Li(text="Versatile Python APIs - Tackle all web development tasks, including UI events, styling, and layout"),
                                                    oj.PC.Li(text="Efficient component interaction - Easily manipulate complex elements like docking panels and hierarchical navigation")
])
                               ),
                   "batteries_included": ("Batteries included",
                                          oj.PC.Ul(childs=[oj.PC.Li(text="Session management"),
                                                           oj.PC.Li(text="Signed cookie management"),
                                                           oj.PC.Li(text="User authentication"),
                                                           oj.PC.Li(text="Database interaction hooks"),
                                                           oj.PC.Li(text="Style/theme manipulation: overwrite, merge styles")
                                          ]
                                      )
                                      ),
               "interactivity": ("Build for interactivity",
                                 oj.PC.Ul(childs=[oj.PC.Li(text="Effortlessly handle browser UI events in Python"),
                                                  oj.PC.Li(text="Dynamically modify browser UI elements from Python"),
                                                  oj.PC.Li(text="Incorporates an Elm-inspired React modeling framework")
                                      ]
                                  )
                                  ),
               "performant": ("Performant",
                              oj.PC.Ul(
                                  childs=[
                                      oj.PC.Li(text="ASGI: Concurrent sessions in a single Python thread"),
                                      oj.PC.Li(text="Svelte runtime on browser: Optimized for speed"),
                                      oj.PC.Li(text="Only single copy of static elements are maintained. Minimizes copying of elements"),
                                      oj.PC.Li(text="Only ransmits the changes (diff) of the UI to the frontend."),
                                      oj.PC.Li(text="Async processing enables concurrent processing on single core machine"),                   
                                      
                                      
                                  ]
                              )
                              ),
               "tradeoffs": ("Design tradeoffs",
                             oj.PC.Ul(
                                    childs=[
                                        oj.PC.Li(text="Prioritizes ease of use over performance"),
                                        oj.PC.Li(text="Encourages good programming practices: Readability, Reusability, Maintainability"),
                                        oj.PC.Li(text="Comprehensive: Covers all web development aspects - layout, styling, reactivity, components")
                                    ]
                                    )

                             ),
               "misc": ("Misc",

                        oj.PC.Ul(
                               childs=[
                                   oj.PC.Li(text="Comprehensive documentation: Detailed guides and resources for easy understanding"),
                                   oj.PC.Li(text="Extensive testing: Robust testing capabilities for reliable applications"),
                                   oj.PC.Li(text="Low learning curve: Designed for quick adoption and user-friendly experience"),
                                   oj.PC.Li(text="Open source: Free to use and contribute, fostering community-driven development"),
                                   oj.PC.Li(text="Easily extensible: Built-in plugin framework allows seamless integration of new features")
                               ]
                               )
                        
                        )
               
               }
    slideShow = SlideShow("features",
                          slide_labels,
                          slide_info,
                          "misc")

    overview_panel = oj.HCCMutable.Subsection("Features",
                                   slideShow
                   )


# ============================ tech stack============================

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

# ================================ end ===============================
divider = oj.PC.Hr(twsty_tags=[mr/sb/4])
def on_slider_click(dbref, msg, to_mutable_shell):
    print ("slider clicked with value ", msg.value)
    pass


tlc = oj.HCCMutable.Container(childs = [top_panel,
                                           oj.Halign(divider),

                                           overview_panel,
                                           oj.Halign(divider),
                                           demo_panel,
                                           oj.Halign(divider),
                                           techstack_panel,
                                  ]
                        )



    
# ================================ end ===============================


#wp_index = oj.create_endpoint(wp_template)
app = oj.load_app()
# use cached optimized html rendering for responsive static pages. 
from webpage_html_rendering_cache_optimization  import create_endpoint
wp_index = create_endpoint(key="webworks_index",
                              childs = [tlc
                                        ],
                              title="Webworks By Monallabs",
                              
                              )

oj.add_jproute("/", wp_index)

# from starlette.testclient import TestClient
# client = TestClient(app)
# response = client.get('/')
                           

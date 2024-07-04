import ofjustpy as oj
from py_tailwind_utils import *
from html_writer.macro_module import macros, writer_ctx
from ofjustpy_components.component_mouseover_slideshow import SlideShow
oj.set_style("un")

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

with writer_ctx:
    with HCCMutable_Details(classes="group", extra_classes="[&_summary::-webkit-details-marker]:hidden") as about_ofjustpy_demos:
        with Summary(classes="flex cursor-pointer items-center justify-between gap-1.5 bg-pink-100 p-4 text-gray-900 rounded-t-lg"):

            with Div(classes="flex-1 flex justify-center"):

                with H2(classes="font-medium", text="📌 Webapp demos using the Ofjustpy framework"):
                    pass
            with FontAwesomeIcon(label="faPlus", classes="w-5 h-5"):
                pass
            
            pass
        with HCCMutable_Div(classes="bg-pink-50/50 border border-gray-200 rounded-b-lg p-2") as content_area:
            pass

        pass

    pass


content_area.childs.append(demo_slideShow)

            

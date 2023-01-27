import sys
import importlib
import ofjustpy as oj
from py_tailwind_utils import *

import logging
app = oj.load_app()
# import os

# if os:
#     try:
#         os.remove("/tmp/launcher_v1.log")
#     except:
#         pass

# import sys
# if sys:
#     FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
#     logging.basicConfig(filename="/tmp/launcher_v1.log",
#                         level=logging.DEBUG, format=FORMAT)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# def href_builder_factory(route_name):
#     def href_updater(Acomp_ref, session_manager, route_name=route_name):
#         print(f"Find route for route name {route_name}")
#         url = session_manager.request.url_for(route_name)
#         print(f"calling href_updater for {route_name} = {url}")
#         assert url.startswith("http")
#         Acomp_ref.href = "https" + url[4:]
#     return href_updater

                 
def page_builder(edir):
    """
    We need edir to find the example directory within which the example is located.
    
    """
    def page_builder_inner(key, childs, **kwargs):
        title = kwargs.get('title')
        nav_buttons = oj.Halign(oj.PC.StackH(childs = [oj.AC.A(key="back_to_examples_index",
                                                               #href=f"/examples/index",
                                                               href_builder = oj.href_builder_factory("examples:index"),
                                                               title=f"example index",
                                                               text=f"Back to examples index",
                                                               twsty_tags=[bt.bd, bdr.lg, bd/gray/6,
                                                                           shadow/gray/2,
                                                                           shadow.md
                                                                           ]
                                                               ),
                                                       oj.PC.A(key="view_source_code",
                                                               href=f"https://github.com/ofjustpy/ofjustpy/blob/main/examples/{edir}/{title}.py",
                                                               title=title,
                                                               target='_blank',
                                                               text=f"View source code",
                                                               twsty_tags=[bt.bd, bdr.lg, bd/gray/6,
                                                                           shadow/gray/2,
                                                                           shadow.md
                                                                           ]
                                                               )
                                                       ],
                                             twsty_tags=[space/x/2]
                                             )

                                )
        

        return oj.Mutable.WebPage(key=key,
                               childs = [oj.HCCMutable.StackV(childs = [oj.HCCMutable.Div(childs=childs),
                                                                oj.PC.Hr(twsty_tags=[bg/green/1]),
                                                                nav_buttons],
                                                      twsty_tags= [space/y/8]
                                                      )
                                         ],

                               **kwargs
                               )

    return page_builder_inner


with oj.MountCtx("examples"):
    with oj.PageBuilderCtx(page_builder("static_webpages")):
        with oj.MountCtx("static_webpages"):    
            static_webpage_module = importlib.import_module("examples.static_webpages",)

    with oj.PageBuilderCtx(page_builder("input_webpages")):
        with oj.MountCtx("input_webpages"):
            input_components_module = importlib.import_module("examples.input_webpages",
                                                            )

    with oj.PageBuilderCtx(page_builder("mutable_webpages")):
        with oj.MountCtx("mutable_webpages"):
            mutable_components_module = importlib.import_module("examples.mutable_webpages",
                                                            )

    static_example_links = [oj.AC.A(key=f"example_00{idx}",

                                    #href=f"/examples/static_webpages/example_00{idx}",
                                    href_builder  = oj.href_builder_factory(f"examples:static_webpages:example_00{idx}:example_00{idx}"),
                                    title=f"example_00{idx}",
                                    text=f"example_00{idx}",
                                    twsty_tags=[bt.bd, bdr.lg, bd/gray/6,
                                                shadow/gray/2,
                                                shadow.md
                                        ]
                                    )
                            for idx in range(1,8)

             ]


    passive_components = oj.PC.Subsubsection("Passive Components", 
                                             oj.PC.StackV(childs = static_example_links,
                                                          twsty_tags = [space/y/2]

                                                          )
                                             )

    input_components_links = [oj.AC.A(key=f"example_00{idx}",

                                      #href=f"/examples/input_components/example_00{idx}",
                                      href_builder  = oj.href_builder_factory(f"examples:input_webpages:example_00{idx}:example_00{idx}"),
                                      title=f"example_00{idx}",
                                      text=f"example_00{idx}",
                                      twsty_tags=[bt.bd, bdr.lg, bd/gray/6,
                                                  shadow/gray/2,
                                                  shadow.md
                                                  ]
                                      )
                              for idx in range(1,5)

                              ]


    input_components = oj.PC.Subsubsection("Input Components", 
                                             oj.PC.StackV(childs = input_components_links,
                                                          twsty_tags = [space/y/2]

                                                          )
                                             )


    mutable_components_links = [oj.AC.A(key=f"example_00{idx}",

                                        #href=f"/examples/mutable_components/example_00{idx}",
                                        href_builder  = oj.href_builder_factory(f"examples:mutable_webpages:example_00{idx}:example_00{idx}"),
                                        title=f"example_00{idx}",
                                        text=f"example_00{idx}",
                                        twsty_tags=[bt.bd, bdr.lg, bd/gray/6,
                                                    shadow/gray/2,
                                                    shadow.md
                                                    ]
                                        )
                                for idx in range(1,9)

                                ]


    mutable_components = oj.PC.Subsubsection("Mutable Components", 
                                             oj.PC.StackV(num_cols = 2, childs = mutable_components_links,
                                                          twsty_tags = [space/y/2]

                                                          )
                                             )



    tlc = oj.PC.Container(childs = [passive_components, input_components, mutable_components],
                          twsty_tags=oj.ui_styles.sty.stackv
                          )



    endpoint_examples_index = oj.create_endpoint(key="index",
                                                 childs = [tlc],
                                                 title="Examples codes illustrating usage"
                                                 )
    oj.add_jproute("/index", endpoint_examples_index)

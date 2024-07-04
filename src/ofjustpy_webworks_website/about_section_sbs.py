import ofjustpy as oj
from py_tailwind_utils import *

from .panel_oj_about import about_panel
app = oj.load_app()

endpoint = oj.create_endpoint("overview",
                              childs = [oj.HCCMutable.Container(childs=[about_panel
                                                                ],
                                                        twsty_tags=[mr/x/auto]
                                                        )

                                        ],
                              body_classes="font-geist",
                              title="Overview",
                              skeleton_data_theme="seafoam",
                              #rendering_type="SSR"
                              )
oj.add_jproute("/", endpoint)

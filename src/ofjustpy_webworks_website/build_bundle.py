import macropy.activate
from svelte_safelist_builder import get_svelte_safelist

# twtags, fontawesome_icons = get_svelte_safelist("ofjustpy_webworks_website.runner")

# print (fontawesome_icons)
# use_shadcn = True
# use_skeleton = True

# # which components and themes to include
# skeleton_config = { 'components': [],
#                     'themes': [],

#     }

# # which font families to include
# font_families = ["Geist", "Roboto"]

# import svelte_bundler

# svelte_bundler.build_bundle(twtags,
#                             font_families=font_families,
#                             fontawesome_icons = fontawesome_icons,
#                             ui_library="skeleton-shadcn-hyper",
#                             output_dir="./"
#                             )

# ============================ skeletonui ============================
# from  svelte_bundler import  skeletonui_bundle_builder
# twtags, fontawesome_icons = get_svelte_safelist("ofjustpy_webworks_website.skeletonui_component_library_showcase")
# skeletonui_bundle_builder.build_bundle(twtags,
#                                     font_families=font_families,
#                                     fontawesome_icons = fontawesome_icons,
#                                     output_dir="./skeletonui"
#                                     )
# ================================ end ===============================


# ============================= shadcnui =============================
twtags, fontawesome_icons = get_svelte_safelist("ofjustpy_webworks_website.shadcnui_component_library_showcase")

# which font families to include
font_families = ["Geist", "Roboto"]

from  svelte_bundler import  shadcnui_bundle_builder


shadcnui_bundle_builder.build_bundle(twtags,
                                    font_families=font_families,
                                    fontawesome_icons = fontawesome_icons,
                                    output_dir="./shadcnui"
                                    )

# ================================ end ===============================



# ================================ end ===============================

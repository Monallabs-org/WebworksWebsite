import macropy.activate
from svelte_safelist_builder import get_svelte_safelist

from  svelte_bundler import  skeletonui_bundle_builder
twtags, fontawesome_icons = get_svelte_safelist("ofjustpy_webworks_website.skeletonui_component_library_showcase")
font_families = ["Geist", "Roboto"]
skeletonui_bundle_builder.build_bundle(twtags,
                                    font_families=font_families,
                                    fontawesome_icons = fontawesome_icons,
                                    output_dir="./skeletonui"
                                    )

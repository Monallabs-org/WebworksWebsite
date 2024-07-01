import macropy.activate
from svelte_safelist_builder import get_svelte_safelist
twtags, fontawesome_icons = get_svelte_safelist("ofjustpy_webworks_website.overview_revised")
print (fontawesome_icons)

# which font families to include
font_families = ["Geist", "Roboto"]

from  svelte_bundler import hyperui_bundle_builder
hyperui_bundle_builder.build_bundle(twtags,
                                    font_families=font_families,
                                    fontawesome_icons = fontawesome_icons,
                                    output_dir="./overview_revised"
                                    )

from svelte_safelist_builder import get_svelte_safelist
import macropy.activate

twtags, fontawesome_icons = get_svelte_safelist("runner")
#twtags = get_svelte_safelist("debug_encode_debug")

print ("got icons  ", fontawesome_icons)


use_shadcn = True
use_skeleton = True

# which components and themes to include
skeleton_config = { 'components': [],
                    'themes': [],

    }

# which font families to include
font_families = ["Geist", "Roboto"]

import svelte_bundler

#twtags="w-16"
svelte_bundler.build_bundle(twtags,
                            font_families=font_families,
                            fontawesome_icons = fontawesome_icons
                            )





from addict_tracking_changes import Dict
import ofjustpy as oj

request = Dict()
request.session_id  = "abc"
app = oj.load_app()
from webapp_main import *

wp_index = wp_index(request)

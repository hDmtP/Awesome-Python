from mobile.sniffer.detect import  detect_mobile_browser
from mobile.sniffer.utilities import get_user_agent

# Get HTTP_USER_AGENT from HTTP request object
ua = get_user_agent(self.request)
if ua:
    # Apply reg
    if detect_mobile_browser(ua):
        # Redirect the visitor from a web site to a mobile site
        pass
    else:
        # A regular web site visitor
        pass
else:
    # User agent header is missing from HTTP request
    return False
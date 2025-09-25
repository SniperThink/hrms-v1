from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

class ForceHTTPSMiddleware(MiddlewareMixin):
    """
    Middleware to force HTTPS URLs in responses for production
    """
    
    def process_request(self, request):
        # Force HTTPS scheme detection for Vercel
        if not settings.DEBUG and 'vercel.app' in request.get_host():
            request.is_secure = lambda: True
            request.META['wsgi.url_scheme'] = 'https'
        return None
    
    def process_response(self, request, response):
        # Ensure all Location headers use HTTPS in production
        if not settings.DEBUG and 'Location' in response:
            location = response['Location']
            if location.startswith('http://'):
                response['Location'] = location.replace('http://', 'https://', 1)
        
        return response

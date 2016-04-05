from social.apps.django_app.middleware import SocialAuthExceptionMiddleware
from social import exceptions as social_exceptions
from django.shortcuts import render

# Handle login cancel
class SocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
	"""Catch errors caused when user cancels login."""
	def process_exception(self, request, exception):
		if hasattr(social_exceptions, 'AuthCanceled'):
			return render(request, "login.html", {"cancel": 'cancelled request'})
		else:
			raise exception
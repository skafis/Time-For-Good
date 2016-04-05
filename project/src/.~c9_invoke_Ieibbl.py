from django.test import TestCase
from .pipeline import update_user_social_data
from social.strategies.django_strategy import DjangoStrategy
from social.backends.linkedin import LinkedinOAuth2 as linkedin
from social.backends.facebook import FacebookOAuth2 as facebook
from django.contrib.auth.models import User

# Create your tests here.
# Test for
class ThirdPartyLoginPipelineTest(TestCase):
    def setUp(self):
    	user_kwargs=dict({    		
    		'first_name':"name1", 
    		'last_name':"name2", 
    		})
    	user = User.objects.create_user(
    		username="name1", 
    		**user_kwargs
    		)
        self.arg1 = DjangoStrategy
        self.arg2 = ('dgdj', 'gugkl', 'ghfhj')
        self.arg3 = dict({
        	'is_new':True,
        	'username': u'name1',
        	'email': u'name1@example.com',
        	'backend': facebook,
        	'user': User.objects.get(username="name1")
        })

    def test_that_my_pipeline_works(self):
    	print "Printed arguments."
    	print self.arg1
    	print self.arg2
    	print self.arg3
    	print "End of arguments."
        result = update_user_social_data(self.arg1, *self.arg2, **self.arg3)

        self.assertTrue(result)
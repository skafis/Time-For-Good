
# python-social-auth
# Linkedin authentication key

SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '77pcykjfo9eng7'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'KURzCzu1T4TqiRBT'

# Where the page goes after an event

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/home/'
SOCIAL_AUTH_LOGIN_URL = '/'

# Backends if other logins are used

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.linkedin.LinkedinOAuth2',
    'social.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# Pipelines direct data flow for the login

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.mail.mail_validation',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',

    'src.pipeline.update_user_social_data',
)

# Field definition for data from facebook
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']


SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'

SOCIAL_AUTH_FACEBOOK_KEY = '1135371423162152'
SOCIAL_AUTH_FACEBOOK_SECRET = 'dcadeec0cf756604c5b8dc1eaf3687bb'

SOCIAL_AUTH_TWITTER_KEY = ''
SOCIAL_AUTH_TWITTER_SECRET = ''


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''

# Field definition for data from linkedin

SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE = ['r_basicprofile', 'r_emailaddress']
# These fields be requested from linkedin.
SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS = [
    'email-address',
    'picture-url',
    'headline',
    'industry',
]
SOCIAL_AUTH_LINKEDIN_OAUTH2_EXTRA_DATA = [
    ('id', 'id'),
    ('firstName', 'first_name'),
    ('lastName', 'last_name'),
    ('emailAddress', 'email_address'),
    ('pictureUrl', 'picture_url'),    
    ('headline', 'headline'),
    ('industry', 'industry'),
    ('public-profile-url', 'public_profile_url'),
]

# Storing data fields
FIELDS_STORED_IN_SESSION = ['key']
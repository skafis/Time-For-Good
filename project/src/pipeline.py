def update_user_social_data(strategy, *args, **kwargs):
    """Set the name and avatar for a user only if is new.
    """
    print 'update_user_social_data ::', strategy
    if not kwargs['is_new']:
        return

    full_name = ''
    backend = kwargs['backend']

    user = kwargs['user']

    if ( isinstance(backend, FacebookOAuth2)
    ):
        full_name = kwargs['response'].get('name')
    elif (
        isinstance(backend, LinkedinOAuth2)
    ):
        if kwargs.get('details'):
            full_name = kwargs['details'].get('fullname')

    user.full_name = full_name

    
    if isinstance(backend, FacebookOAuth2):
        fbuid = kwargs['response']['id']
        image_name = 'fb_avatar_%s.jpg' % fbuid
        image_url = 'http://graph.facebook.com/%s/picture?type=large' % fbuid
        image_stream = urlopen(image_url)

        user.avatar.save(
            image_name,
            ContentFile(image_stream.read()),
        )
    
    elif isinstance(backend, LinkedinOAuth2):
        if kwargs['response'].get('pictureUrl'):
            image_name = 'linked_avatar_%s.jpg' % full_name
            image_url = kwargs['response'].get['pictureUrl']
            image_stream = urlopen(image_url)

            user.avatar.save(
                image_name,
                ContentFile(image_stream.read()),
            )
    user.save()


    return {"user": user}

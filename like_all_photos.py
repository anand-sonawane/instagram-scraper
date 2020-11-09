from igramscraper.instagram import Instagram 

instagram = Instagram()

instagram.with_credentials('user_name', 'password')
instagram.login(two_step_verificator=True)

medias = instagram.get_medias("kevin", 5)

for index,media in enumerate(medias):
    media_id = media.identifier
    instagram.like(media_id)


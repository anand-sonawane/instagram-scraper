from igramscraper.instagram import Instagram 
import pandas as pd

"""
proxies = {
    'http': 'http://123.45.67.8:1087',
    'https': 'http://123.45.67.8:1087',
}
"""
instagram = Instagram()
#instagram.set_proxies(proxies)

medias = instagram.get_medias("sonytvofficial", 1000)

media_id = []
media_type = []
media_url= []
media_likes_count = [] 
media_caption = [] 
media_comments_count = [] 
media_video_views = []

for index,media in enumerate(medias):
    media_id.append(media.identifier)
    media_type.append(media.type)
    media_likes_count.append(media.likes_count)
    media_caption.append(media.caption)
    media_comments_count.append(media.comments_count)
    media_video_views.append(media.video_views)
    if(media.type == 'image'):
        media_url.append(media.image_standard_resolution_url)
        
    else:
        media_url.append(media.video_standard_resolution_url )
        media_video_views.append(media.video_views)

data = list(zip(media_id, media_type, media_url, media_likes_count, media_caption, media_comments_count, media_video_views))  

df = pd.DataFrame(data, columns = ['ID', 'Type','URL','Likes','Caption','Comments','Views'])  

df.to_csv("anand.csv")

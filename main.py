from api.connector import pexel

pex = pexel()
photos = pex.search_api("drawing")

for photo in photos:
  # Print photographer
  print('Photographer: ', photo.photographer)
  # Print url
  print('Photo url: ', photo.url)
  # Print original size url
  print('Photo original size: ', photo.original)
#print(return_result)

#TODO: "make a surch param not hard coded, create a web page with immages in, load the photo url in the immage tag, "
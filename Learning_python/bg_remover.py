from withoutbg import WithoutBG

img = WithoutBG.opensource()
result = img.remove_background("Learning_python/pictorial_representation_of_datascience.png")
result.save("pictorial_representation_of_datascience_without_bg.png")
import folium
import base64
from folium import IFrame
zoom_start = 6

m = folium.Map(location=[36.044667, 137.966853], 
               tiles='OpenStreetMap',
               zoom_start=zoom_start)


Kabukicho = 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Kabukicho_red_gate_and_colorful_neon_street_signs_at_night%2C_Shinjuku%2C_Tokyo%2C_Japan.jpg/1200px-Kabukicho_red_gate_and_colorful_neon_street_signs_at_night%2C_Shinjuku%2C_Tokyo%2C_Japan.jpg'
Ninja_house = 'https://ninja-trick-house.com/wp-content/uploads/2017/07/slider04.jpg'
ninja_url = 'https://ninja-trick-house.com/en/'

# Add a marker with a popup containing text and an image
Shinjuku_content = ('<div style="max-height: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Kabukicho Entertainment District</strong>'
                 '<br><span style="font-size:14px">This is a famous entertainment district with pubs, late night snack bars, robot restaurant hosts, and sci-fi dinner shows.<br><br>'
                 f'<img src="{Kabukicho}" alt="Image" style="width:450px;height:450px;"><br><br>'
                 f'<a href="{Kabukicho}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 '<strong style="font-size:20px">Ninja Trick House</strong>'
                 '<br><span style="font-size:14px">Get to see different ninja weaponry and a sword demonstration. Seems cool but also seems to be potentially geared towards kids.<br><br>'
                 f'<img src="{Ninja_house}" alt="Image" style="width:300px;height:200px;"><br><br>'
                 f'<a href="{Ninja_house}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{ninja_url}" target="_blank" style="font-size:14px" >Website</a>')

folium.Marker(
    location=[35.7006507580449, 139.70876350434693],
    tooltip="Shinjuku",
    popup = Shinjuku_content,
    icon=folium.Icon(icon="star"),
).add_to(m)

Shibuya_sky = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/SHIBUYA_SCRAMBLE_SQUARE_East_Tower.jpg/200px-SHIBUYA_SCRAMBLE_SQUARE_East_Tower.jpg'
Shibuya_url = 'https://www.shibuya-scramble-square.com.e.apy.hp.transer.com/sky/ticket/'
Silkream = 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAFwAXAMBIgACEQEDEQH/xAAbAAACAwEBAQAAAAAAAAAAAAAEBQIDBgEHAP/EADEQAAIBAwMCBQMDAwUAAAAAAAECAwAEERIhMQVBBhMiUXFhgbEUMqFCgpEjMzRicv/EABgBAAMBAQAAAAAAAAAAAAAAAAECAwQA/8QAIhEAAgICAgICAwAAAAAAAAAAAAECEQMhEjEToVKBBCIj/9oADAMBAAIRAxEAPwDQAkcE4qSsSa5qBqa4FdY1E0qwgVBSK6TRs6iSbGrJ01KKqWjreB7ldKDnvRTA0BIpJwBk0wg6bI66n9P0plZdNjg9T7tRcp9BAp0xGzMNHpkK+xq+1VluAybVXMMTtn3q2ElbgHbGKrjfZLL0hu8jKnODS2YZfJerLq4Og7ilGtzuWzQcLVgUtgZ+a6Pmh9f1qXmYrFZuoKU4qeaCEu9WxMZZFjXljimTBQxsLVruXA/YDua1FnbpCFjQb0NYQrbW6qvOKbW8QVNZ/cw/xVOkRbtg1yw81gOBVMh4q2/XSVccE4NCO+4opgFfUYtFwD2NDaWaTP8ASBTLqi6oQ3cUteXTHjO9PHJwbYfFzWyq6OVwDQseQu9ERMrMdVVMRqNc87qhVhV2KdRzXxYmq9Qr7WKxWbaJZOa0Xh/pvqFxLzjYVn7bD3Ea+5rd2aBLdQBjajB3NIXJqIVGhklVO3f4pmxAwO3FDWEeI/MPLcfFXtyv3NXk7MyKpx5kJXuRkfzSYNqk+KcDOF/8j80oK6J5FPZqMTiHUTi0YntWbLM+lRyad9Zl8uzI96QxMNa70Jdjx6LxG8LgN3FUyHLnNE3GkyLpfO1VeXue9BoKEb7HaoE12TA71FJo4/U25qCVmqKsP6TGzXsWV2zW5QkYQ7VhujXjz9UgQKAordyKQEbIGCK5px/ZE8vG+KHC4CgLsAMCosfWR/02rh1L6SOfxVTtmWNAfXvnHaq2ZmdaUaVxwRild7/y9a8OoJ+aZlMqdt9WMUh6zc+VfCHHEXmav7sUeSXY2ODnLihb4jmH6cIu7Z4FJ7Vy2M1R1bqzPIY4xnHJoC1vT5gDHeg3bNeTBHHBU9msVQSh01aYxnjFLYrwmNGLijDdId/MFMZTJqskxwtVMhV8N2ohJ/07AgVcWt7zfOlqkkbIQ8ipPZd4awerxfBr0VwGQqeCMVheh2Itr5Z/MDADitXL1CNBwT9qaK1TIZMM1LoLj6lJ0/8A0r7eEA6ZhnjsKuuruG2VZomUhioV+QAe9RtHjvbBWdcg5Uhh7Vn+sdNm0v8ApJZNDDBjLHGPaskpZMC+S9h4wySp6foYXnXPKYwwnXMT6VXfb5+vvWU8U309m0JuJDJcTqSxP9K9h+aaeHp7WNhavD5FxwNXDfBrJ+M7o3fiGdQcpBiMfYb/AM5rsMnm/pJ/Q7fglxivsVPcPKdtqkgI371EYAqQINaRHJy22GLdlbcDfINX/qWIXY8e9Al3W2OAMVIPMVXccU1iBk4HaqVtpnPpUj60zsY1b1MMmh+p3csPpj0r9qFGrHijx5yeg/w9FLb3eqVy4x+3Naee4OPTAfmsn4UZpLsySOzNjvxWpuHZm0k7fSuGXCTtLRf03q1tCpgvJ4oHdiYw7YDDbOM0XNNEwysiEe4YGst4h6fBd9OZpNQaHMiMp3zj8V5K1utz1NIHLKrtvp2NRlN30LL8eORuSdHs3WZOmLCz3N1BFIN1Osas/Qc1i5r61uZWklQ63YszEck81mrC8WO9uLS3s7SEI+kyrHqkbbuzE4+2KZNtsKMMcYtyS7OcpYUo9hUyxEEwtt7UNq3qK/uqB2kIqhObUtpUE5zCctv7VNDHoHqNCaiM1bD/ALY2pkRZ/9k='
Shibuya_crossing = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Shibuya_scramble_crossing_during_Halloween_2023%2C_actually_less_crowded_than_usual%2C_high_police_presence_2.jpg/250px-Shibuya_scramble_crossing_during_Halloween_2023%2C_actually_less_crowded_than_usual%2C_high_police_presence_2.jpg'

Shibuya_content = ('<div style="max-height: 600px; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Shibuya Sky</strong>'
                 '<br><span style="font-size:14px">Mixed use skyscraper connected to Shibuya station, with the Shibuya Sky observation deck.<br><br>'
                 f'<img src="{Shibuya_sky}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Shibuya_sky}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Shibuya_url}" target="_blank" style="font-size:14px" >Website</a><br><br>'
                 '<strong style="font-size:20px">Dolci Cafe</strong>'
                 '<br><span style="font-size:14px">Cafe with a popular stylized ice cream called silkream.<br><br>'
                 f'<img src="{Silkream}" alt="Image" style="width:300px;height:200px;"><br>'
                 f'<a href="{Silkream}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 '<strong style="font-size:20px">Shibuya Crossing</strong><br>'
                 '<span style="font-size:14px">The famous Shibuya Crossing.<br><br>'
                 f'<img src="{Shibuya_crossing}" alt="Image" style="width:450px;height:450px;"><br>.<br>'
                 f'<a href="{Shibuya_crossing}" target="_blank" style="font-size:10px" >Image Source</a>')

folium.Marker(
    location=[35.667821, 139.696370],
    tooltip="Shibuya",
    popup=Shibuya_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)

animate = 'https://ex.animate.co.jp/assets/img/shop/index/shopinfo.jpg'
animate_url = 'https://ex.animate.co.jp/shop/ikebukuro/'

Toshima_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Animate Ikebukuro</strong>'
                 '<br><span style="font-size:14px">Animate is the most popular anime retailer in Japan and the Ikebukuro flagship store is the largest anime store in the world.<br><br>'
                 f'<img src="{animate}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{animate}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{animate_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.73168042506713, 139.7111534798391],
    tooltip="Toshima City",
    popup=Toshima_content,
    icon=folium.Icon(icon="star"),
).add_to(m)


Kamishikimi =  'https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Kamishikimi_Kumanoimasu_Shrine_001.jpg/440px-Kamishikimi_Kumanoimasu_Shrine_001.jpg'
Kamishikimi_url = 'https://www.visit-kyushu.com/en/see-and-do/spots/kamishikimi-kumanoimasu-shrine/'

Kamishikimi_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px"> Kamishikimi Kumanoimasu Shrine </strong>'
                 '<br><span style="font-size:14px">While the history of this shrine in unknown, according to local legend it is dedicated to the creator gods Izanagi-no-Mikoto and Izanami-no-Mikoto. Behind the main hall of the shrine is a large sacred stone called Ugeto-iwa that is said to have been kicked by a follower of the god Takeiwatatsu-no-Mikoto, creating a 10-meter hole. It is thought that worshiping here brings success and victory.<br><br>'
                 f'<img src="{Kamishikimi}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Kamishikimi}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Kamishikimi_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[32.854152425800955, 131.15853753051738],
    tooltip="Kamishikimi Kumanoimasu",
    popup=Kamishikimi_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)

Takachiko = 'https://www.japan-guide.com/g20/8052_03.jpg'
Takachiko_url = 'https://www.japan-guide.com/e/e8052.html'

Takachiko_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px"> Takachico Gorge </strong>'
                 '<br><span style="font-size:14px">A narrow chasm cut through by the Gokaso River, volcanic basalt columns that supposedly resemble the scales of a dragon line the cliffs.<br><br>'
                 f'<img src="{Takachiko}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Takachiko}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Takachiko_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[32.71606377241934, 131.3013152628766],
    tooltip="Takachiko Gorge",
    popup=Takachiko_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)



Amanoiwato = 'https://cdn.kyushuandtokyo.org/front_assets/images_other/spot/small/amanoiwato1.jpg'
Amanoiwato_url = 'https://www.kyushuandtokyo.org/spot_27/'

Amanoiwato_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px"> Amanoiwatu Shrine </strong>'
                 '<br><span style="font-size:14px">This shrine is dedicated to the sun goddess Amaterasu and sits above a gorge containing a cave called Ama-no-Iwato which according to Japanese legend is where the goddess hid after an altercation with her brother, her hiding plunged the world into darkness until she was lured out by the spirit of merriment.<br><br>'
                 f'<img src="{Amanoiwato}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Amanoiwato}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Amanoiwato_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[32.73475850641449, 131.3507412854985],
    tooltip="Amanoiwato Shrine ",
    popup=Amanoiwato_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)



Udo_jingu = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Udo-jingu_Main_hall_001.jpg/1920px-Udo-jingu_Main_hall_001.jpg'
Udo_jingu_url = 'https://www.japan-guide.com/e/e8032.html'

Udo_Jingu_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px"> Udo Jingu Shrine </strong>'
                 '<br><span style="font-size:14px">This shrine is said to be the mythical birthplace of Emperor Jimmus father, Ugayafukiaezu. Ugayafukiaezus mother, the sea goddess Toyotamahime, build a birth-hut from the feathers of a cormorantin this location. The original story includes a tragic divorce but now the shrine is popular with young couples looking for easy childbirth and a happy marriage .<br><br>'
                 f'<img src="{Udo_jingu}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Udo_jingu}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Udo_jingu_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[31.65049729507138, 131.46668110680386],
    tooltip="Udo Jingu Shrine ",
    popup=Udo_Jingu_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)



Kuratake = 'https://kumamoto.guide/files/3d68e7ec-2983-4712-b599-d8fa51df064d_l.jpg?1658210287'
Kuratake_url = 'https://www.wowu.jp/spots/kuratake-jinja-shrine'

Kuratake_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Kuratake Shrine</strong>'
                 '<br><span style="font-size:14px">Built upon the sacred mountain Mt. Kuratake, this shrine was bult for the purpose of praying for fishermans safety.<br><br>'
                 f'<img src="{Kuratake }" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Kuratake}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Kuratake_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[32.4277120855671, 130.32731868581408],
    tooltip="Kuratake Shrine",
    popup=Kuratake_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)


Hakata = 'https://gaijinpot.scdn3.secure.raxcdn.com/app/uploads/sites/6/2023/07/iStock-1472534603.jpeg'
Hakata_url = 'https://canalcity.co.jp/english'

Hakata_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Canal City Hakata </strong>'
                 '<br><span style="font-size:14px">A large shopping and entertainment complex called the “city within the city” it features many restaurants, shops, two hotels, and a canal that runs through the complex.<br><br>'
                 f'<img src="{Hakata}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Hakata}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Hakata_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[33.58979884200171, 130.41105719877893],
    tooltip="Canal City Hakata Shopping Mall",
    popup=Hakata_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)



Oarai_isosaki = 'https://upload.wikimedia.org/wikipedia/commons/5/52/Kamiiso_torii_at_Oarai_Isosaki_Jinja.jpg'
Isosaki_url = 'https://www.japan.travel/en/spot/1459/'

Isosaki_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Oarai Isosaki Shrine</strong>'
                 '<br><span style="font-size:14px">This shrine, which worships Sukunabikona a god of alcohol and medicine, features three torii gates that lead into the ocean.<br><br>'
                 f'<img src="{Oarai_isosaki}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Oarai_isosaki}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Isosaki_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[36.31596474602882, 140.5874664673554],
    tooltip="Oarai Isosaki Shrine",
    popup=Isosaki_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)



Nara_park = 'https://cdn.cheapoguides.com/wp-content/uploads/sites/3/2017/10/Deer-and-Gate-1024x600.jpg'
Nara_url = 'https://www.visitnara.jp/destinations/area/nara-park/'

Nara_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Nara Park</strong>'
                 '<br><span style="font-size:14px">Beautiful park featuring multiple temples and free roaming deer that you can feed from your hand.<br><br>'
                 f'<img src="{Nara_park}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Nara_park}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Nara_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[34.68516166199369, 135.8430012672761],
    tooltip="Nara Park",
    popup=Nara_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)




Mozu = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/NintokuTomb_Aerial_photograph_2007.jpg/640px-NintokuTomb_Aerial_photograph_2007.jpg'
Mozu_url = 'https://whc.unesco.org/en/list/1593/'

Mozu_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Mozu Tombs</strong>'
                 '<br><span style="font-size:14px">A collection of megalithic tombs from the Kofun Period (300-538 CE).<br><br>'
                 f'<img src="{Mozu}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Mozu}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Mozu_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[34.561049856740375, 135.48557922354732],
    tooltip="Mozu",
    popup=Mozu_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)




Saruhashi = 'https://en.japantravel.com/photo/poi-680-219374/1200x630/yamanashi-saruhashi-bridge-219374.jpg'
Saruhashi_url = 'https://www.yamanashi-kankou.jp/english/uncover/saruhashi-bridge.html'

Saruhashi_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Saruhashi Bridge</strong>'
                 '<br><span style="font-size:14px">Once of Japans three “unique bridges” the Saruhashi bridge corsses over the Katsura River gorge and is the most well-known example of the hanebashi design.<br><br>'
                 f'<img src="{Saruhashi}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Saruhashi}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Saruhashi_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.61592843246593, 138.98012000779403],
    tooltip="Saruhashi Bridge",
    popup=Saruhashi_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)




Glass = 'https://img.activityjapan.com/11/16084/11000001608402_ke7T6pHb_4.jpg?version=1614855031'
Glass_url = 'https://en.activityjapan.com/publish/plan/16084'

Glass_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Glass Blowing</strong>'
                 '<br><span style="font-size:14px">Glass blowing class to make a small Mt. Fuji glass design.<br><br>'
                 f'<img src="{Glass}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Glass}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Glass_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.61194321920701, 138.9079770671458],
    tooltip="Glass Blowing",
    popup=Glass_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)




Shirakawa = 'https://www.snowmonkeyresorts.com/wp-content/uploads/2021/08/22225779_m.jpg'
Shirakawa_url = 'https://whc.unesco.org/en/list/734/'

Shirakawa_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Historic Village of Shirakawa-go</strong>'
                 '<br><span style="font-size:14px">Historic village famous for the gassho-zukuri style farmhouses.<br><br>'
                 f'<img src="{Shirakawa}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Shirakawa}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Shirakawa_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[36.258049676302846, 136.90627282720365],
    tooltip="Shirakawa-go",
    popup=Shirakawa_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)




E_car = 'https://media-cdn.tripadvisor.com/media/attractions-splice-spp-720x480/10/7e/69/28.jpg'
E_car_url = 'https://www.tripadvisor.com/AttractionProductReview-g1165976-d24046433-Cute_Fun_E_Car_tour_following_guide_around_Lake_Kawaguchiko-Fujikawaguchiko_machi.html'

E_car_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">E car tour around Lake Kawaguchiko with a view of Mt. Fuji</strong>'
                 f'<img src="{E_car}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{E_car}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{E_car_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.498291410614996, 138.768842815473],
    tooltip="E car Tour",
    popup=E_car_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)




Otagi = 'https://photos.smugmug.com/Otagi-Nenbutsu-ji-Temple/i-RLVc8Kr/0/XL/Otagi%204-XL.jpg'
Otagi_url = 'https://www.insidekyoto.com/otagi-nenbutsu-ji-temple'

Otagi_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Otagi Nenbutsu-ji Temple</strong>'
                 '<br><span style="font-size:14px">Temple featuring more than 1200 rakan, which are stone statues depicting the disciples of Buddha. Rakan tradition is to have these statues generally be humorous.<br><br>'
                 f'<img src="{Otagi}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Otagi}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Otagi_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.03121634397382, 135.66154954013518],
    tooltip="Otagi Nenbutsu-ji Temple",
    popup=Otagi_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)




Kiyomizu = 'https://upload.wikimedia.org/wikipedia/commons/3/3c/Kiyomizu.jpg'
Kiyomizu_url = 'https://www.kiyomizudera.or.jp/en/'

Kiyomizu_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Kiyomizu-Dera Temple</strong>'
                 '<br><span style="font-size:14px">Literally translated to “Pure Water Temple” this is one of the most celebrated temples of Japan. This temple features Otawa Waterfall where the water is divided into three separate streams. You are given a cup attached to a long pole to drink from them and they are supposed to each have a different benefit (longevity, prosperity, or love). Drinking from more than one is considered greedy but you can drink from others on different trips.<br><br>'
                 f'<img src="{Kiyomizu}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Kiyomizu}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Kiyomizu_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[34.99478922041335, 135.78465026729074],
    tooltip="Kiyomizu-Dera Temple",
    popup=Kiyomizu_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)




Imperial_Palace = 'https://upload.wikimedia.org/wikipedia/commons/7/72/Imperial_Palace_-_panoramio_%281%29.jpg'
Imperial_Palace_url = 'https://sankan.kunaicho.go.jp/english/guide/kyoto.html'

Imperial_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Kyoto Imperial Palace</strong>'
                 '<br><span style="font-size:14px">This is the former palace of the emperor or Japan. Since the Meiji Restoration in 1868 the Emperors have resided in the Tokyo Imperial Palace and the Kyoto Imperial Palace is now open to the public.<br><br>'
                 f'<img src="{Imperial_Palace}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Imperial_Palace}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Imperial_Palace_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.025955315850275, 135.76161320961972],
    tooltip="Kyoto Imperial Palace",
    popup=Imperial_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)




Nijo = 'https://www.japan-guide.com/g18/3918_top.jpg'
Nijo_url = 'https://www.japan-guide.com/e/e3918.html'

Nijo_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Nijo Castle</strong>'
                 '<br><span style="font-size:14px">A castle completed during the reign of Tokugawa Iemitsu with two concentric rings of fortifications, as well as many buildings, and several gardens.<br><br>'
                 f'<img src="{Nijo}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Nijo}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Nijo_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.0142489045428, 135.74838557339328],
    tooltip="Nijo Castle",
    popup=Nijo_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)




Kinkaku = 'https://www.shokoku-ji.jp/wp-content/themes/shokokuji/assets/img/kinkakuji/gallery/photo01@2x.jpg'
Kinkaku_url = 'https://www.shokoku-ji.jp/en/kinkakuji/about/'

Kinkaku_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Kinkaku-ji Temple </strong>'
                 '<br><span style="font-size:14px">The “Temple of the Golden Pavillion.” This is a Zen Buddhist temple that is designates as a National Special Historic Site.<br><br>'
                 f'<img src="{Kinkaku}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Kinkaku}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Kinkaku_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.03947531441024, 135.72924307349902],
    tooltip="Kinkaku-ji Temple",
    popup=Kinkaku_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)



Heian = 'https://www.japan-guide.com/g18/3904_top.jpg'
Heian_url = 'https://www.japan-guide.com/e/e3904.html'

Heian_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Heian Shrine </strong>'
                 '<br><span style="font-size:14px">The Heian Shrine was built in 1895 on the occasion of the 1100th anniversary of when Kyoto was made the capital of Japan (which lasted from 794-1868). The shrine is dedicated to the spirits of the first and last emperors who reigned from the city, Emperor Kammu (737-806) and Emperor Komei (1832-1867).<br><br>'
                 f'<img src="{Heian}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Heian}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Heian_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.01605256742647, 135.78239410961928],
    tooltip="Heian Shrine",
    popup=Heian_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)



Fushimi = 'https://www.japan-guide.com/g18/3915_03.jpg'
Fushimi_url = 'https://www.japan-guide.com/e/e3915.html'

Fushimi_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Fushimi Inari-taisha</strong>'
                 '<br><span style="font-size:14px"> This is the head shrine of the kami Inari, who is once of the primary gods of the Shinto and is the god of many things but primarily of rice and agriculture. This shrine includes trails up a mountain that span 4 kilometers and take roughly 2 hours to walk up. The shrine is open 24 hours and lit up all night, and has no entrance fee. This is a popular spot so many people say to get there as early as possible to avoid crowds.<br><br>'
                 f'<img src="{Fushimi}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Fushimi}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Fushimi_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[34.9678526588981, 135.77913392929406],
    tooltip="Fushimi Inari-taisha",
    popup=Fushimi_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)



Arashiyama = 'https://photos.smugmug.com/Kyoto/Kyoto-Things-To-Do/i-X4SbQPn/0/L/arashiyama-bamboo-grove-M.jpg'
Arashiyama_url = 'https://www.insidekyoto.com/arashiyama'

Arashiyama_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Arashiyama</strong>'
                 '<br><span style="font-size:14px">This district of Kyoto features many temples and shrines but most notably holds the Arashiyama Bamboo Grove. This area is also known for the Kameyaka-koen park where guests can mingle with the monkeys at the hilltop if they are out and about.<br><br>'
                 f'<img src="{Arashiyama}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Arashiyama}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Arashiyama_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.010363202971746, 135.6672021750908],
    tooltip="Arashiyama",
    popup=Arashiyama_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)



Shoes = 'https://www.spoon-tamago.com/wp-content/uploads/2022/07/tokyo-kimono-shoes-9.jpeg'
Shoes_url = 'https://tokyokimonoshoes.com/en-us'

Shoes_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Tokyo Kimono Shoes</strong>'
                 '<br><span style="font-size:14px">This store sells shoes made from recycled kimonos.<br><br>'
                 f'<img src="{Shoes}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Shoes}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Shoes_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.7148789868838, 139.80041736344924],
    tooltip="Tokyo Kimono Shoes",
    popup=Shoes_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)



Akihabara = 'https://www.japan-guide.com/g18/3003_01.jpg'
Akihabara_url = 'https://www.japan-guide.com/e/e3003.html'

Akihabara_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Akihabara Shopping District</strong>'
                 '<br><span style="font-size:14px">This is a major electronics shopping district for video games, anime, manga, electronics, and computer-related goods. This area also features things based on the “otaku” culture so the streets are lined with anime and manga style imagery and features things like maid cafes and manga conventions.<br><br>'
                 f'<img src="{Akihabara}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Akihabara}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Akihabara_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.70221999005891, 139.77445799188317],
    tooltip="Akihabara",
    popup=Akihabara_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)



Meiji = 'https://cdn.cheapoguides.com/wp-content/uploads/sites/2/2020/05/meiji-jingu-iStock-499807771-1024x600.jpg'
Meiji_url = 'https://www.meijijingu.or.jp/en/'

Meiji_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Meiji Shrine</strong>'
                 '<br><span style="font-size:14px">This is a shrine dedicated to the deified sprits of Emperor Meiji and his wife, Empress Shoken. Emperor Meiji had a large role as the Emperor during the Meiji restoration (also known as the Honorable Restoration) which restored practical imperial rule to Japan in 1868.<br><br>'
                 f'<img src="{Meiji}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Meiji}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Meiji_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.676467294871635, 139.69931516732393],
    tooltip="Meiji Shrine",
    popup=Meiji_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)




Ghibli = 'https://www.japantimes.co.jp/uploads/imported_images/uploads/2022/10/np_file_187804.jpeg'
Ghibli_url = 'https://www.ghibli-museum.jp/en/tickets/'

Ghibli_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Studio Ghibli Museum</strong>'
                 '<br><span style="font-size:14px">This museum showcases the works of Studio Ghibli. This museum includes models of characters, a mock-up of an animation studio that shows the creative process of animating, as well as a theater for exclusive Ghibli short films.<br><br>'
                 f'<img src="{Ghibli}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Ghibli}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Ghibli_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.69632510375401, 139.57041023848853],
    tooltip="Studio Ghibli Museum",
    popup=Ghibli_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)




Bunkyo = 'https://www.japanistry.com/wp-content/uploads/2017/09/Hakusan-Hydrangea-v03.jpg'
Bunkyo_url = 'https://tokyocheapo.com/events/bunkyo-ajisai-festival/'

Bunkyo_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Bunkyo Hydrangea Festival</strong>'
                 '<br><span style="font-size:14px">This is a yearly festival for the beautiful hydrangea flowers in Bunkyo city. It will be taking place around June 11-18. There is more information on specific events on the website.<br><br>'
                 f'<img src="{Bunkyo}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Bunkyo}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Bunkyo_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.7218813345068, 139.7505984961623],
    tooltip="Bunkyo Hydrangea Festival",
    popup=Bunkyo_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)




Daisen = 'https://upload.wikimedia.org/wikipedia/commons/5/5a/Mt_Daisen_Full_View.jpg'
Daisen_url = 'https://www.japan-guide.com/e/e8150.html'

Daisen_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Mount Daisen</strong>'
                 '<br><span style="font-size:14px">Mount Daisen is a dormant stratovolcano that is part of the Daisen volcanic belt, which is a part of the Southwestern Honshu volcanic belt where the Phillipine Sea Plate is subducting under the Amurian Plate. The mountain features multiple temples and shrines as well as hiking routes.<br><br>'
                 f'<img src="{Daisen}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Daisen}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Daisen_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.378743857238675, 133.54943804552232],
    tooltip="Mount Daisen",
    popup=Daisen_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)




Tottori = 'https://www.japan-guide.com/g20/8103_03.jpg'
Tottori_url = 'https://www.japan-guide.com/e/e8103.html'

Tottori_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Tottori Castle Ruins</strong>'
                 '<br><span style="font-size:14px">This castle was originally built during the Sengoku period as a Yamashiro (which is a castle built into the mountain itself. This castle has changed owners on multiple occasions and following the Meiji restoration it was given to the Ministry of the Army who decided to dismantle it. However, during the dismantling the Tottori prefecture was reestablished and the dismantling stopped. Now all that remains are minor remnants and parts of the stone wall and one gate featuring iron spikes on the outside.<br><br>'
                 f'<img src="{Tottori}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Tottori}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Tottori_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.51029913765167, 134.24094661584886],
    tooltip="Tottori Castle Ruins",
    popup=Tottori_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)




Sand = 'https://media.cnn.com/api/v1/images/stellar/prod/230609110029-01-tottori-desert-japan-dunes.jpg?c=original&q=h_618,c_fill'
Sand_url = 'https://www.japan-guide.com/e/e8102.html'

Sand_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Tottori Sand Dunes</strong>'
                 '<br><span style="font-size:14px">Sand dunes formed from sediment carried from the Chugoku Mountains by the Sendai River. These sand dunes have been shaped over the span of 100,000 years.<br><br>'
                 f'<img src="{Sand}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Sand}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Sand_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.541754079688, 134.2277340093325],
    tooltip="Tottori Sand Dunes",
    popup=Sand_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)




Kannonin = 'https://www.japan-guide.com/g20/8104_01.jpg'
Kannonin_url = 'https://www.japan-guide.com/e/e8104.html'

Kannonin_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Kannon-in Temple</strong>'
                 '<br><span style="font-size:14px">This temple which used to be known as Fudarakusan Jigen-ji Kannon-in was built during the Edo period and is noted for its Edo-style garden. It was originally built for the Ikeda clan but is now just considered a Place of Scenic Beauty by the Japanese government.<br><br>'
                 f'<img src="{Kannonin}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Kannonin}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Kannonin_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.496207791805034, 134.24160064033285],
    tooltip="Kannon-in Temple",
    popup=Kannonin_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)




Osaka_castle = 'https://www.japan-guide.com/g18/4000_top.jpg'
Osaka_castle_url = 'https://www.japan-guide.com/e/e4000.html'

Osaka_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Osaka Castle</strong>'
                 '<br><span style="font-size:14px">This castle was built starting in 1583 by Toyotomi Hideyoshi. He was building this castle with the purpose of mirroring the Azuchi Castle which was the headquarters of Oda Nobunaga but he wanted to surpass it in every way.<br><br>'
                 f'<img src="{Osaka_castle}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Osaka_castle}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Osaka_castle_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[34.68734938288166, 135.52585999101004],
    tooltip="Osaka Castle ",
    popup=Osaka_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)


Namba = 'https://www.japan-guide.com/g21/4001_01.jpg'
Namba_url = 'https://www.japan-guide.com/e/e4001.html'

Namba_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Minami (Namba Station)</strong>'
                 '<br><span style="font-size:14px">Minami (“South”) is one of Osakas two major city centers. It is a famous entertainment district and features a large variety of options for shopping, and dining. It is also highly accessible because it is located at the Namba Station.<br><br>'
                 f'<img src="{Namba}" alt="Image" style="width:832px;height:468px;"><br>'
                 f'<a href="{Namba}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Namba_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[34.66306796925686, 135.5010840671321],
    tooltip="Minami (Namba Station)",
    popup=Namba_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)


Sumiyoshi = 'https://d1wv60jaas5mse.cloudfront.net/images/uploads/production/post_images/fb82770f8773b8_umiyoshi%20taisha%20Shrine%20in%20Osaka.jpeg'
Sumiyoshi_url = 'https://www.sumiyoshitaisha.net/en/'

Sumiyoshi_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Sumiyoshi Taisha</strong>'
                 '<br><span style="font-size:14px">Sumiyoshi Taisha is one of Japans oldest shrines. It was founded in the 3rd century before the introduction of Buddhism. The shrine displays a distinct shrine architecture style called Sumiyoshi-zukuri which is one of three architecture styles that are considered purely Japanese.<br><br>'
                 f'<img src="{Sumiyoshi}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Sumiyoshi}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Sumiyoshi_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[34.61257983251477, 135.49367534266986],
    tooltip="Sumiyoshi Taisha",
    popup=Sumiyoshi_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)


Minoo = 'https://www.japan-experience.com/sites/default/files/images/content_images/minoo-park-guide-1.jpg'
Minoo_url = 'https://www.japan.travel/en/spot/1080/'

Minoo_content = ('<div style="max-height: 100%; max-width: 100%; overflow-y: auto;">'
                 '<strong style="font-size:20px">Minoo Park</strong>'
                 '<br><span style="font-size:14px">Minoo Park is a forested valley on the outskirts of Osaka that features a beautiful waterfall.<br><br>'
                 f'<img src="{Minoo}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Minoo}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Minoo_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[34.84722025674175, 135.4724000403016],
    tooltip="Minoo Park",
    popup=Minoo_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)



Nintendo = 'https://www.travelandleisure.com/thmb/vAMCaJQNMWjjtWCUiVvkyq45Wcs=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/nintendoworld-NEWPARKS1220-08e70fa0a1b44e1db33298581ebebd1f.jpg'
Nintendo_url = 'https://www.usj.co.jp/web/en/us/areas/super-nintendo-world'

Nintendo_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Super Nintendo World</strong>'
                 '<br><span style="font-size:14px">Its Super Nintendo World.<br><br>'
                 f'<img src="{Nintendo}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Nintendo}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Nintendo_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[34.66809331589012, 135.43056709515471],
    tooltip="Super Nintendo World",
    popup=Nintendo_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)



Mt_togakushi = 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/161009_Kagami-ike_Togakushi_Nagano_Japan01s3.jpg/1200px-161009_Kagami-ike_Togakushi_Nagano_Japan01s3.jpg'
Mt_togakushi_hiking = 'https://upload.wikimedia.org/wikipedia/commons/f/ff/Togakusi_houkousya.jpg'
Mt_url = 'http://www.travel-around-japan.com/k42-11-mount-togakushi.html'

Togakushi_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Mount Togakushi</strong>'
                 '<br><span style="font-size:14px">The name Togakushi means “hiding door” and it is named based on the story from the Amanoiwato Shrine where the sun goddess Amaterasu hid bringing darkness to the world. This mountain features many shrines and  beautiful hiking areas.<br><br>'
                 f'<img src="{Mt_togakushi}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Mt_togakushi}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Mt_togakushi_hiking}" target="_blank" style="font-size:14px" >Hiking info</a><br><br>'
                 f'<a href="{Mt_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[36.770553760857894, 138.05467687731584],
    tooltip="Mount Togakushi",
    popup=Togakushi_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)



Takayama = 'https://japanrailandtravel.com/wp-content/uploads/2019/02/1121125150125-e1551941745646.jpg'
Takayama_url = 'https://voyapon.com/takayama-traditional-japan/'
Hida = 'https://cdn.visitgifu.com/wp/2020/02/bfd8d05a-specials-hida-beef_list.jpg'
Hida_url = 'https://www.hida.jp/english/localspeciality/food/4000195.html'
Ramen = 'https://www.kitchenbyannak.com/wp-content/uploads/2021/08/IMG_10378-Takayama-ramen-profile.jpg'
Ramen_url = 'https://shockinjapan.com/article/takayama-ramen/'


Takayama_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                '<strong style="font-size:20px">Takayama</strong>'
                '<br><span style="font-size:14px">Takayama is known for its historic district that features Edo-period style merchant houses with latticed bay windows and wooden trellises. The area is also known for its famous Hida beef and Takayama style Ramen<br><br>'
                f'<img src="{Takayama}" alt="Image" style="width:450px;height:450px;"><br>'
                f'<a href="{Takayama}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                f'<a href="{Takayama_url}" target="_blank" style="font-size:14px" >Website</a><br><br>'
  	            f'<img src="{Hida}" alt="Image" style="width:450px;height:450px;"><br>'
                f'<a href="{Hida}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                f'<a href="{Hida_url}" target="_blank" style="font-size:14px" >Website</a><br><br>'
                f'<img src="{Ramen}" alt="Image" style="width:450px;height:450px;"><br>'
                f'<a href="{Ramen}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                f'<a href="{Ramen_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')


folium.Marker(
    location=[36.139769433886094, 137.2587832343377],
    tooltip="Takayama",
    popup=Takayama_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)



Hotsprings = 'https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcRLmc0itpp1nXEovB3ghA1QMcyc6ndmvLGnH9jpUxf0V40D2GAGjpFO4LQU6Gs51VWjSQFolOe9HUdOmZNfAl2qlgIOX2YqC90Wsl8kSw'
Hotsprings_url = 'https://hakone-japan.com/things-to-do/onsen/'

Hotsprings_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Hakone Hot Springs</strong>'
                 '<br><span style="font-size:14px"> Hakone is famous for its many natural hot springs.<br><br>'
                 f'<img src="{Hotsprings}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Hotsprings}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Hotsprings_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[34.66809331589012, 135.43056709515471],
    tooltip="Hakone Hot Springs",
    popup=Hotsprings_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)



Hakone_shrine = 'https://www.japan-guide.com/g18/5204_01.jpg'
Hakone_shrine_url = 'https://www.hakonenavi.jp/international/en/spot/523'

Hakone_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Hakone Shrine</strong>'
'<br><span style="font-size:14px">Hakone Shrine was founded in 757 during the reign of Emperor Kosho. It was later burned down in 1590 during the battle of Odawara and reconstructed by Tokugawa Ieyasu, the founder and first member of the Tokugawa shogunate.<br><br>'
                 f'<img src="{Hakone_shrine}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Hakone_shrine}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Hakone_shrine_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.204896404654534, 139.02537819613715],
    tooltip="Hakone Shrine",
    popup=Hotsprings_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)



Choanji = 'https://www.kyototourism.org/wp/wp-content/uploads/2021/01/Sea-Wood_Choanji-Temple-03.jpg'
Choanji_url = 'https://www.japan-guide.com/e/e5219.html'

Choanji_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Choanji Temple</strong>'
                 '<br><span style="font-size:14px">This is a temple of the Soto school of Zen Buddhism. It features over 200 statues of rakan (disciples of Buddha) scattered around the temple grounds.<br><br>'
                 f'<img src="{Choanji}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Choanji}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Choanji_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.27366108145382, 139.01282307894115],
    tooltip="Choanji Temple",
    popup=Choanji_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)



Ropeway = 'https://a.travel-assets.com/findyours-php/viewfinder/images/res70/491000/491569-hakone-komagatake-ropeway.jpg'
Ropeway_url = 'https://www.hakonenavi.jp/international/en/transportation/hakone-ropeway'

Ropeway_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Hakone Ropeway</strong>'
                 '<br><span style="font-size:14px">This ropeway is roughly 130m off the ground and offers great views of sulfuric hot springs, Owakudani Valley, Mt. Fuji, and Lake Ashinoko.<br><br>'
                 f'<img src="{Ropeway}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Ropeway}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Ropeway_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.24456746805675, 139.01505202497546],
    tooltip="Hakone Ropeway",
    popup=Ropeway_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)



Kanazawa_castle = 'https://www.jcastle.info/images/a/a4/Kanazawa123.jpg'
Kanazawa_castle_url = 'https://www.japan.travel/en/spot/1402/'

Kanazawa_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Kanazawa Castle Ruins</strong>'
                 '<br><span style="font-size:14px">This area and castle were created when the Ikko-ikki followers of the teaching of the priest Rennyo displaces the official governors of the Kaga Province, then established a theocratic republic called "The Peasants Kingdom". In 1580 this was conquered by Odu Nobunagas general Sakuma Morimasa who was awarded the province. It became a national historic site in 2008.<br><br>'
                 f'<img src="{Kanazawa_castle}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Kanazawa_castle}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Kanazawa_castle_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[36.56500542464256, 136.65823680469612],
    tooltip="Kanazawa Castle Ruins",
    popup=Kanazawa_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)



Kenroku_en = 'https://visitkanazawa.jp/lsc/upfile/spot/0001/0106/10106_1_l.jpg?1671008655'
Kenroku_en_url = 'https://visitkanazawa.jp/en/attractions/detail_10106.html'

Kenroku_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Kenroku-en Garden</strong>'
'<br><span style="font-size:14px">This is a strolling style garden constructed during the Edo period by the Maeda clan. The name Kenrokuen means “having six factors”, representing the attributes which bring out the garden’s stunning beauty: spaciousness, tranquility, artifice, antiquity, water sources and magnificent views.<br><br>'
                 f'<img src="{Kenroku_en}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Kenroku_en}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Kenroku_en_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[36.56221305665595, 136.66271950742274],
    tooltip="Kenroku-en Garden",
    popup=Kenroku_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)



Higashi_chaya = 'https://cdn.hokurikuandtokyo.org/front_assets/images_other/spot/middle/higashi-cha4.jpg'
Higashi_chaya_url = 'https://visitkanazawa.jp/en/attractions/detail_10212.html'

Higashi_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Higashi Chaya District</strong>'
'<br><span style="font-size:14px">This district houses many Chaya which are restaurants where the guests are entertained by geisha who perform songs and dances. During the Edo Period Chaya were designated to specific entertainment districts outside of city limits and some cities today still have preserved Chaya districts. Kanazawa has three Chaya Districts and Higashi Chaya District is the largest of the three.<br><br>'
                 f'<img src="{Higashi_chaya}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Higashi_chaya}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Higashi_chaya_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[36.57251785002059, 136.6669278298269],
    tooltip="Higashi Chaya District",
    popup=Higashi_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)



Nikko_park = 'https://media.tacdn.com/media/attractions-splice-spp-674x446/0b/27/5a/b7.jpg'
Nikko_park_url = 'https://www.japan.travel/national-parks/parks/nikko/'

Nikko_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Nikko Park</strong>'
'<br><span style="font-size:14px">Just a beautiful national park with hiking and nice plants and animals.<br><br>'
                 f'<img src="{Nikko_park}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Nikko_park}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Nikko_park_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[36.893750997746686, 139.63438910971158],
    tooltip="Nikko Park",
    popup=Nikko_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)



Shinkyo = 'https://www.japan-guide.com/g19/3814_top.jpg'
Shinkyo_url = 'https://www.japan-guide.com/e/e3814.html'

Shinkyo_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Shinkyo Bridge</strong>'
'<br><span style="font-size:14px">The Shinkyo sacred bridge is the entrance to Nikkos shrines and temples. It is ranked as one of Japans three finest bridges.<br><br>'
                 f'<img src="{Shinkyo}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Shinkyo}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Shinkyo_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[36.75355049105212, 139.6039604808683],
    tooltip="Shinkyo Bridge",
    popup=Shinkyo_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)



Kegon = 'https://japandeluxetours.com/uploads/2022/04/20220404160358_624b795e37a08.jpg'
Kegon_url = 'https://www.japan.travel/en/japans-local-treasures/kegon-falls/'

Kegon_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Kegon Waterfall</strong>'
'<br><span style="font-size:14px">An almost 100 meter tall waterfall. The most famous waterfall in Nikko.<br><br>'
                 f'<img src="{Kegon}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Kegon}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Kegon_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[36.73811539754062, 139.50191869200248],
    tooltip="Kegon Waterfall",
    popup=Kegon_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)



Toshogu = 'https://images.ctfassets.net/2tgq3wsc42ke/6Q59UFFGp6Xejk3qYO1lfq/8149b9c77af45d5fb1162d66f8ee429a/img_dis_his-cul_02.jpg?q=70'
Toshogu_url = 'https://www.visitnikko.jp/en/spots/nikko-toshogu-shrine/'

Toshogu_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Nikko Toshogu</strong>'
'<br><span style="font-size:14px">Nikko Toshogu is a shrine dedicated as a memorial to Tokugawa Ieyasu, the founder of the Tokugawa Shogunate which ruled Japan for 250 years in the Edo period<br><br>'
                 f'<img src="{Toshogu}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Toshogu}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Toshogu_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[36.75817372835505, 139.59872513854128],
    tooltip="Nikko Toshogu",
    popup=Toshogu_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)



Tsujikawayama = 'https://s3.ap-northeast-1.amazonaws.com/production.guidoor.jp/images/ABh6if332uBniR2FKCsXfrtZmGGcPORe4xOp6awa.jpeg'
Tsujikawayama_url = 'https://www.guidoor.jp/en/places/6065'

Tsujikawayama_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Tsujikawayama Park</strong>'
'<br><span style="font-size:14px">This area is the ebirthplace of a famous Japanese scholar and folklorist named Yanagita Kunio. In his study of regional lore he showed particular interest in yokai, or supernatural creatures. Because of this the area is covered with statues of yokai including two moving statues that ascend from a lake or fly out of a tower.<br><br>'
                 f'<img src="{Tsujikawayama}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Tsujikawayama}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Tsujikawayama_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[34.96632978335983, 134.76746594597606],
    tooltip="Tsujikawayama Park",
    popup=Tsujikawayama_content,
    icon=folium.Icon(icon="star")
    ).add_to(m)



K_house = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/2/20147/25.jpg'
K_house_url = 'https://www.hostelworld.com/st/hostels/p/20147/k-s-house-mt-fuji/'

K_House_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">K House Mt. Fuji</strong><br>'
                 f'<img src="{K_house}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{K_house}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{K_house_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.50576408172466, 138.76069396390284],
    tooltip="K House Mt. Fuji",
    popup=K_House_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Plat_asakusa = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/2/289672/t4yr3d4tivgyusceb1nm'
Plat_asakusa_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/plat-hostel-keikyu-asakusa-station/Tokyo/289672?from=2024-06-08&to=2024-06-12&guests=2'

Plat_asakusa_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Plat hostel Keikyu Asakusa station</strong><br>'
                 f'<img src="{Plat_asakusa}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Plat_asakusa}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Plat_asakusa_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.713376835121814, 139.79036386332407],
    tooltip="Plat hostel Asakusa station",
    popup=Plat_asakusa_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Ace = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/2/20457/jjeirkspoclgcrjpnwtj'
Ace_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/Ace-Inn-Shinjuku/Tokyo/20457?from=2024-06-08&to=2024-06-12&guests=2'

Ace_inn_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Ace Inn Shinjuku</strong><br>'
                 f'<img src="{Ace}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Ace}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Ace_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.69252995150616, 139.72430870655933],
    tooltip="Ace Inn Shinjuku",
    popup=Ace_inn_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Little_japan = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/2/277898/5.jpg'
Little_japan_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/Little-Japan/Tokyo/277898?from=2024-06-08&to=2024-06-12&guests=2'
Little_Japan_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Little Japan</strong><br>'
                 f'<img src="{Little_japan}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Little_japan}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Little_japan_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.701407435055415, 139.78447710295643],
    tooltip="Little Japan",
    popup=Little_Japan_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Plat_haneda = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/3/304903/quwwuxhc39zwzlkn3sqb'
Plat_haneda_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/plat-hostel-keikyu-haneda-home/Tokyo/304903?from=2024-06-08&to=2024-06-12&guests=2'

Plat_haneda_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Plat Hostel Keikyu Haneda Home</strong><br>'
                 f'<img src="{Plat_haneda}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Plat_haneda}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Plat_haneda_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.547897859015464, 139.74875356903587],
    tooltip="Plat Hostel Keikyu Haneda Home",
    popup=Plat_haneda_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Sakura_hostel = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/1/15725/xuodpahs35holpkeiyku'
Sakura_hostel_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/Sakura-Hostel-Asakusa/Tokyo/15725?from=2024-06-08&to=2024-06-12&guests=2'

Sakura_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Sakura Hostel Asakusa</strong>'
'<br><span style="font-size:14px">This hostel offers subway tickets that you can buy at the hostel.<br><br>'
                 f'<img src="{Sakura_hostel}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Sakura_hostel}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Sakura_hostel_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.71602950560572, 139.7948278118537],
    tooltip="Sakura Hostel Asakusa",
    popup=Sakura_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Wise_owl = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/2/275924/oxi4ajjdvkbat14ownpt'
Wise_owl_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/Wise-Owl-Hostels-Shibuya/Tokyo/275924?from=2024-06-08&to=2024-06-12&guests=2'

Wise_owl_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Wise Owl Hostel Shibuya</strong><br>'
                 f'<img src="{Wise_owl}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Wise_owl}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Wise_owl_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.65373749417893, 139.68979070418052],
    tooltip="Wise Owl Hostel Shibuya",
    popup=Wise_owl_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Kagelow = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/9/98359/504.jpg'
Kagelow_url = 'https://www.hostelworld.com/st/hostels/p/98359/kagelow-mt-fuji-hostel-kawaguchiko/'

Kagelow_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Kagelow Mt. Fuji Hostel Kawaguchiko</strong><br>'
                 f'<img src="{Kagelow}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Kagelow}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Kagelow_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.49585168638704, 138.7653016177795],
    tooltip="Kagelow Mt. Fuji Hostel Kawaguchiko",
    popup=Kagelow_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Dot = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/3/302315/oc9ljj4mijijy29q5rl5'
Dot_url = 'https://www.hostelworld.com/st/hostels/p/302315/dot-hostel-and-bar/'

Dot_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Dot Hostel and Bar</strong><br>'
                 f'<img src="{Dot}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Dot}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Dot_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.523629668467464, 138.74384122498913],
    tooltip="Dot Hostel and Bar",
    popup=Dot_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Nishinomiyaso = 'https://image.jimcdn.com/app/cms/image/transf/dimension=1220x10000:format=jpg/path/sc271ef78301d00c9/image/i1fe32c809bcc6fbe/version/1601435773/%E8%A5%BF%E5%AE%AE%E8%8D%98-%E5%A4%96%E8%A6%B3.jpg'
Nishinomiyaso_url = 'https://www.nisimiyasou.com/'

Nishinomiyaso_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Nishinomiyaso</strong><br>'
                 f'<img src="{Nishinomiyaso}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Nishinomiyaso}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Nishinomiyaso_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.510534758876666, 138.74649574288017],
    tooltip="Nishinomiyaso",
    popup=Nishinomiyaso_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Four = 'https://cdn.r-corona.jp/prd.jln.r-corona.jp/assets/site_files/1a7bmyp7/232116/w733_bw1200h600.jpg'
Four_url = 'http://www.fujisan3776.asia/'

Four_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Four Seasons Inn</strong><br>'
                 f'<img src="{Four}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Four}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Four_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.507125495678544, 138.76195580080483],
    tooltip="Four Seasons Inn",
    popup=Four_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Otsuki_inn = 'https://www.toyoko-inn.com/content/gallery/101/00329/329_%E5%A4%96%E8%A6%B3%E6%A8%AA1.jpg'
Otsuki_inn_url = 'https://www.toyoko-inn.com/search/detail/00329?utm_source=google&utm_medium=mybusiness&utm_campaign=gt_web329'

Otsuki_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Tokyo Inn Fujisan Otsuki-eki</strong><br>'
                 f'<img src="{Otsuki_inn}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Otsuki_inn}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Otsuki_inn_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.614807257064314, 138.94459923848456],
    tooltip="Tokyo Inn Fujisan Otsuki-eki",
    popup=Otsuki_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Otsuki_inn = 'https://www.toyoko-inn.com/content/gallery/101/00329/329_%E5%A4%96%E8%A6%B3%E6%A8%AA1.jpg'
Otsuki_inn_url = 'https://www.toyoko-inn.com/search/detail/00329?utm_source=google&utm_medium=mybusiness&utm_campaign=gt_web329'

Otsuki_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Tokyo Inn Fujisan Otsuki-eki</strong><br>'
                 f'<img src="{Otsuki_inn}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Otsuki_inn}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Otsuki_inn_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.614807257064314, 138.94459923848456],
    tooltip="Tokyo Inn Fujisan Otsuki-eki",
    popup=Otsuki_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Resort_fuyo = 'https://fuyo-hs.jp/wp/wp-content/themes/fuyo/img/home/slider/mv2.webp'
Resort_fuyo_url = 'https://www.fuyo-hs.jp/'

Resort_fuyo_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Resort Inn Fuyo Kawaguchiko (Business Hotel)</strong><br>'
                 f'<img src="{Resort_fuyo}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Resort_fuyo}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Resort_fuyo_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.47883945443055, 138.784665073643],
    tooltip="Resort Inn Fuyo Kawaguchiko (Business Hotel)",
    popup=Resort_fuyo_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Daiwa = 'https://www.daiwaroynet.jp/datas/cache/images/2023/10/09/1760x790_ea1e9d427fb5664c32c517a73e421e58_3ef3924937eec8e9f12c5c022580660b1ea69453.jpg'
Daiwa_url = 'https://www.daiwaroynet.jp/yotsubashi/'

Daiwa_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Daiwa Roynet Hotel Yotsubashi</strong><br>'
                 f'<img src="{Daiwa}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Daiwa}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Daiwa_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[34.6779143260082, 135.49600920960296],
    tooltip="Daiwa Roynet Hotel Yotsubashi",
    popup=Daiwa_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



R_hostel = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/3/301006/fei5nlok2mv4o6q2i9bg'
R_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/R-Hostel-Namba-South/Osaka/301006?from=2024-07-10&to=2024-07-12&guests=2'

R_hostel_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">R Hostel Namba South</strong><br>'
                 f'<img src="{R_hostel}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{R_hostel}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{R_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[34.64800988148607, 135.50199092216357],
    tooltip="R Hostel Namba South",
    popup=R_hostel_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Imano_osaka = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/2/294059/rhocayryl2owcfuqxeqp'
Imano_osaka_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/Imano-Osaka-Shinsaibashi-Hostel/Osaka/294059?from=2024-07-10&to=2024-07-12&guests=2'

Imano_osaka_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Imano Osaka Shinsaibashi Hostel</strong><br>'
                 f'<img src="{Imano_osaka}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Imano_osaka}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Imano_osaka_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[34.673137009674555, 135.4951453670818],
    tooltip="Imano Osaka Shinsaibashi Hostel",
    popup=Imano_osaka_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Shinsaibashi = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1025,h_444,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/2/299208/yrutkbp4nlgc6z62yv22'
Shinsaibashi_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/The-Stay-Osaka-Shinsaibashi/Osaka/299208?from=2024-07-10&to=2024-07-12&guests=2'

Shinsaibashi_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">The Stay Osaka Shinsaibashi</strong><br>'
                 f'<img src="{Shinsaibashi}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Shinsaibashi}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Shinsaibashi_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[34.67351114008674, 135.5077548355803],
    tooltip="The Stay Osaka Shinsaibashi",
    popup=Shinsaibashi_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



And_and = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/3/303126/b7rawemjfqexmjauvtge'
And_and_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/-And-Hostel-Shinsaibashi-East/Osaka/303126?from=2024-07-10&to=2024-07-12&guests=2'

And_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">&And Hostel Shinsaibashi East</strong><br>'
                 f'<img src="{And_and}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{And_and}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{And_and_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[34.678992272814405, 135.5124627536984],
    tooltip="&And Hostel Shinsaibashi East",
    popup=And_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Hostel_q = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/8/82301/33.jpg'
Hostel_q_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/Hostel-Q/Osaka/82301?from=2024-07-10&to=2024-07-12&guests=2'

Hostel_q_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Hostel Q</strong><br>'
                 f'<img src="{Hostel_q}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Hostel_q}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Hostel_q_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[34.669362735919215, 135.49861759602553],
    tooltip="Hostel Q",
    popup=Hostel_q_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Picnic_Hostel = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/2/273231/10.jpg'
Picnic_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/Picnic-Hostel-Osaka/Osaka/273231?from=2024-07-10&to=2024-07-12&guests=2'

Picnic_hostel_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Picnic Hostel Osaka</strong><br>'
                 f'<img src="{Picnic_Hostel}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Picnic_Hostel}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Picnic_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[34.66966067552112, 135.4876486275075],
    tooltip="Picnic Hostel Osaka",
    popup=Picnic_hostel_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Backpackers_Hostel = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/5/5536/46.jpg'
Backpackers_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/Backpackers-Hostel-K-s-House-Kyoto/Kyoto/5536?from=2024-07-10&to=2024-07-12&guests=2'

Backpackers_hostel_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Backpackers Hostel Ks House Kyoto</strong><br>'
                 f'<img src="{Backpackers_Hostel}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Backpackers_Hostel}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Backpackers_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[34.98982862694386, 135.76481423337734],
    tooltip="Backpackers Hostel K's House Kyoto",
    popup=Backpackers_hostel_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Niniroom_Hostel = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/2/287080/38.jpg'
Niniroom_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/Hostel-Niniroom/Kyoto/287080?from=2024-07-10&to=2024-07-12&guests=2'

Niniroom_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Hostel Niniroom</strong><br>'
                 f'<img src="{Niniroom_Hostel}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Niniroom_Hostel}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Niniroom_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.018088892339485, 135.7751137672064],
    tooltip="Hostel Niniroom",
    popup=Niniroom_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Alohadays = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/3/323585/uvoxjzyeomn52rf8sxp7'
Alohadays_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/ALOHADAYS-Kyoto/Kyoto/323585?from=2024-07-10&to=2024-07-12&guests=2'

Alohadays_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Alohadays Kyoto</strong><br>'
                 f'<img src="{Alohadays}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Alohadays}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Alohadays_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.02722557278513, 135.74261405535356],
    tooltip="Alohadays Kyoto",
    popup=Alohadays_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Piece_hostel = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/7/71823/mmtkhzuhkuxilu0qcxk0'
Piece_hostel_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/Piece-Hostel-Kyoto/Kyoto/71823?from=2024-07-10&to=2024-07-12&guests=2'

Piece_hostel_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Piece Hostel Kyoto</strong><br>'
                 f'<img src="{Piece_hostel}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Piece_hostel}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Piece_hostel_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[34.983646133930414, 135.7620881095323],
    tooltip="Piece Hostel Kyoto",
    popup=Piece_hostel_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Yuzan_hostel = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/9/97423/18.jpg'
Yuzan_hostel_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/Yuzan-Guesthouse/Nara/97423?from=2024-07-10&to=2024-07-12&guests=2'

Yuzan_hostel_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Yuzan Guesthouse </strong><br>'
                 f'<img src="{Yuzan_hostel}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Yuzan_hostel}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Yuzan_hostel_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[34.983646133930414, 135.7620881095323],
    tooltip="Yuzan Guesthouse",
    popup=Yuzan_hostel_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Yuzan_hostel = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/9/97423/18.jpg'
Yuzan_hostel_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/Yuzan-Guesthouse/Nara/97423?from=2024-07-10&to=2024-07-12&guests=2'

Yuzan_hostel_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Yuzan Guesthouse </strong><br>'
                 f'<img src="{Yuzan_hostel}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Yuzan_hostel}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Yuzan_hostel_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[34.684476374180804, 135.82358717402624],
    tooltip="Yuzan Guesthouse",
    popup=Yuzan_hostel_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Nara_kamunabi = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/2/273689/8.jpg'
Nara_kamunabi_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/Nara-Guesthouse-Kamunabi/Nara/273689?from=2024-07-10&to=2024-07-12&guests=2'

Nara_kamunabi_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Nara Guesthouse Kamunabi </strong><br>'
                 f'<img src="{Nara_kamunabi}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Nara_kamunabi}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Nara_kamunabi_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[34.677082921392106, 135.8355476555754],
    tooltip="Nara Guesthouse Kamunabi",
    popup=Nara_kamunabi_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Hotel_wisteria_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/Nara-Guesthouse-Kamunabi/Nara/273689?from=2024-07-10&to=2024-07-12&guests=2'

Hotel_wisteria_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Hotel Wisteria</strong><br>'
                 f'<a href="{Hotel_wisteria_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[34.68461563693405, 135.8213312216786],
    tooltip="Hotel Wisteria",
    popup=Hotel_wisteria_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Linnas_kanazawa = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/2/283396/99.jpg'
Linnas_kanazawa_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/LINNAS-Kanazawa/Kanazawa/283396?from=2024-07-11&to=2024-07-12&guests=2'

Linnas_kanazawa_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Linnas Kanazawa </strong><br>'
                 f'<img src="{Linnas_kanazawa}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Linnas_kanazawa}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Linnas_kanazawa_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[36.570779710039204, 136.65980584867765],
    tooltip="Linnas Kanazawa",
    popup=Linnas_kanazawa_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Torifito_pod = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/3/317369/umv638otn3jygjr71vpt'
Torifito_pod_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/Torifito-Hotel-Pod-Kanazawa/Kanazawa/317369?from=2024-07-11&to=2024-07-12&guests=2'

Torifito_pod_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Torifito Hotel and Pod Kanazawa</strong><br>'
                 f'<img src="{Torifito_pod}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Torifito_pod}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Torifito_pod_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[36.56868307219864, 136.6541691249557],
    tooltip="Torifito Hotel and Pod Kanazawa",
    popup=Torifito_pod_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Tsudoh_stay = 'https://assets.pclncdn.com/bstatic/xdata/images/hotel/112885567.jpg?k=2e05b19e909c634618a2b11be3e6c234c654c377f3897a6d93e8a822da35e2ae&o=&undefined&dpr=2&format=jpg&opto&auto=avif,webp&crop=1:1&width=300&dpr=2'
Tsudoh_stay_url = 'https://www.priceline.com/relax/at/74778204/from/20240710/to/20240711/rooms/1?meta-id=us5we5gM01Adp3elmYiPQ1dASXOAAEoNyqhvwuNyU8PIIHGyJf9Iw6_HQiwh2Kykt4R0R0w9Q4rxF2_6IkaS3uG2XMKyHnAEjqaJiepWJ5h6X4YafHH1PzTbT3A4I7AGjwxwJRSscYntNhv_9OTWFuMZxRu6dV_wy60GoHqtLrE7exDpdUhMNcldmhzIr_M4yHLyuUJIKCusIqnq3CnCZqV2gVr7Xn1u7GKBeAx7XhYK32t5Ojdc1OZOqU1ne5rgte8-TIaHjRk7wosa1HKrSQ&pclnId=8F9C61BFD29439EDCC54CA9F256E826C84B689E3F796AE0034D7C889BA81181C520E49A1B95CDF890D7D9EAA03270FBC792A98FF5C87F1EB83520BE009A2ECB226C925414139A63A&gid=2331&cityId=5000479134&cur=USD&backlink-id=kpqcu1n68ie&taxDisplayMode=BP&qdp=34'

Tsudoh_stay_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Tsudoh Stay 101</strong><br>'
                 f'<img src="{Tsudoh_stay}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Tsudoh_stay}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Tsudoh_stay_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[36.57843518493326, 136.6605112897353],
    tooltip="Tsudoh Stay 101",
    popup=Tsudoh_stay_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Vista_kanazawa ='https://assets.pclncdn.com/bstatic/xdata/images/hotel/209993586.jpg?k=8732044645c0e46aacf1b87324f6d1c973c2618456ef3a8686a821f7a9916de3&o=&undefined&dpr=2&format=jpg&opto&auto=avif,webp&crop=1.5:1&width=300&dpr=2'
Vista_kanazawa_url = 'https://www.priceline.com/relax/at/112978804/from/20240710/to/20240711/rooms/1?pclnId=AF4985F4327703EA5AD828EFDC150F10FECAE9A66C91AF29AC3A50F9FEDEC3D7F1D967A53AD3BC9270487BE36F33E0E80A14BDEBECD4829A3C7CDBFB3BE4E2D8DAEE1D0554ACEBFC4EEB3644B49C0B37CE0B34AC88E15C68EC8D876EB71E9060A1F76B5DF95551F5E5D5E973A5E41E08363FE93C5DDD443CAC56EC349A20FDFE1366E050A6B0ED6E&gid=5168&cityId=5000479134&cur=USD&backlink-id=wp5qi31bov&taxDisplayMode=BP&qdp=35'

Vista_kanazawa_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Hotel Vista Kanazawa</strong><br>'
                 f'<img src="{Vista_kanazawa}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Vista_kanazawa}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Vista_kanazawa_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[36.58025954393444, 136.64326672198743],
    tooltip="Hotel Vista Kanazawa",
    popup=Vista_kanazawa_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Amanek_kanazawa = 'https://assets.pclncdn.com/agodastatic/hotelImages/8210986/-1/3a6a738731116976e4461e5389f5c31d.jpg?undefined&dpr=2&format=jpg&opto&auto=avif,webp'
Amanek_kanazawa_url = 'https://www.priceline.com/relax/at/82706703/from/20240710/to/20240711/rooms/1?pclnId=D5621CCB8E1B3C77D109A3A2BF6B07F52A716A1C346A59C6869799404CB9B21E0E31CA463BDC3DE592C3AD3B16226F380C82BE243DBC5C5F892B679607C0F6727A9B4D06F244B514E0C22A745588B88FAE2F21694781C06A42401A523F5550C752399D5D9684D9DA70463E85A0A75C9224850993765CB4C2571D06D53BF692158E6EDFF93D5ABE92&gid=5123&cityId=5000479134&cur=USD&backlink-id=wp5qi31bov&taxDisplayMode=BP&qdp=34'

Amanek_kanazawa_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Hotel Amanek Kanazawa</strong><br>'
                 f'<img src="{Amanek_kanazawa}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Amanek_kanazawa}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Amanek_kanazawa_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[36.560655499563325, 136.65063307450083],
    tooltip="Hotel Amanek Kanazawa",
    popup=Amanek_kanazawa_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Togakushi_kogen = 'https://cf.bstatic.com/xdata/images/hotel/max1280x900/19963033.jpg?k=0f742ae348f3ec702cf49b283c8853c18f5ee955ccb7db3ae75f8e710edcca8f&o=&hp=1'
Togakushi_kogen_url = 'https://www.booking.com/hotel/jp/togakushi-kogen-minsyuku-rindo.html?aid=2127489&label=metagha-link-MRUS-hotel-630507_dev-desktop_los-1_bw-28_dow-Tuesday_defdate-1_room-0_gstadt-2_rateid-public_aud-0_gacid-_mcid-50_ppa-0_clrid-0_ad-0_gstkid-0_checkin-20240423_ppt-B&sid=16819b199391e7ad666df2983a6a32fd&all_sr_blocks=63050702_369067396_2_34_0&checkin=2024-04-23&checkout=2024-04-24&dest_id=-237683&dest_type=city&dist=0&group_adults=2&group_children=0&hapos=1&highlighted_blocks=63050702_369067396_2_34_0&hpos=1&matching_block_id=63050702_369067396_2_34_0&no_rooms=1&req_adults=2&req_children=0&room1=A%2CA&sb_price_type=total&sr_order=popularity&sr_pri_blocks=63050702_369067396_2_34_0__990000&srepoch=1711398802&srpvid=39149084e18c00bc&type=total&ucfs=1&activeTab=main'

Togakushi_kogen_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Togakushi Kogen Minshuku Rindo</strong><br>'
                 f'<img src="{Togakushi_kogen}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Togakushi_kogen}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Togakushi_kogen_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[36.740744153359955, 138.09005546168027],
    tooltip="Togakushi – Kogen Minshuku Rindo",
    popup=Togakushi_kogen_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Oarai_hotel_url = 'https://reserve.489ban.net/client/oarai-hotel/0/detail/sn/696254?date=2024-04-23%2000%3A00%3A00&adult=2&children=0&FromChannelCode=SN&FromChannelName=STAYNAVI&FromChannelAgentCode=Google&FromChannelHash=c0a286b42dffb6b13c5675b3c865e24a'

Oarai_hotel_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Oarai Hotel</strong><br>'
                 f'<a href="{Oarai_hotel_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[36.31327323260233, 140.58705858420493],
    tooltip="Oarai Hotel",
    popup=Oarai_hotel_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Nikko_park_lodge = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/4/42720/4.jpg'
Nikko_park_lodge_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/Nikko-Park-Lodge-Tobu-Nikko-Station-/Nikko/42720?from=2024-07-11&to=2024-07-12&guests=2'

Nikko_park_lodge_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Nikko Park Lodge (Tobu Nikko Station)</strong><br>'
                 f'<img src="{Nikko_park_lodge}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Nikko_park_lodge}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Nikko_park_lodge_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[36.747130047037174, 139.61912888052257],
    tooltip="Nikko Park Lodge (Tobu Nikko Station)",
    popup=Nikko_park_lodge_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Hotel_famitec = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/2/287005/30.jpg'
Hotel_famitec_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/Hotel-Famitec-Nikko-Station/Nikko/287005?from=2024-07-11&to=2024-07-12&guests=2'

Hotel_famitec_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Hotel Famitec Nikko Station</strong><br>'
                 f'<img src="{Hotel_famitec}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Hotel_famitec}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Hotel_famitec_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[36.74780973030845, 139.61694404004243],
    tooltip="Hotel Famitec Nikko Station",
    popup=Hotel_famitec_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Nikko_guesthouse = 'https://cf.bstatic.com/xdata/images/hotel/max1280x900/351119057.jpg?k=9f5337d831bee8af76f146e739cc3d7cd0e0e75e87349012a20c983f63d1eb0f&o=&hp=1'
Nikko_guesthouse_url = 'https://www.booking.com/hotel/jp/nikko-guesthouse-sumica.html?aid=356929&label=metagha-link-MRUS-hotel-424682_dev-desktop_los-1_bw-52_dow-Friday_defdate-0_room-0_gstadt-2_rateid-public_aud-0_gacid-6623578701_mcid-50_ppa-0_clrid-0_ad-1_gstkid-0_checkin-20240517_ppt-B_lp-2840_r-10583637854885021424&sid=16819b199391e7ad666df2983a6a32fd&all_sr_blocks=42468202_364418892_1_0_0%2C42468202_364418892_1_0_0&checkin=2024-05-17&checkout=2024-05-18&dest_id=-238790&dest_type=city&dist=0&group_adults=2&group_children=0&hapos=1&highlighted_blocks=42468202_364418892_1_0_0%2C42468202_364418892_1_0_0&hpos=1&matching_block_id=42468202_364418892_1_0_0&no_rooms=2&req_adults=2&req_children=0&room1=A&room2=A&sb_price_type=total&sr_order=popularity&sr_pri_blocks=42468202_364418892_1_0_0__360000%2C42468202_364418892_1_0_0__360000&srepoch=1711400844&srpvid=a205948361ce068c&type=total&ucfs=1&activeTab=main'

Nikko_guesthouse_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Nikko Guesthouse Sumica</strong><br>'
                 f'<img src="{Nikko_guesthouse}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Nikko_guesthouse}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Nikko_guesthouse_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[36.74727488733935, 139.61937697545042],
    tooltip="Nikko Guesthouse Sumica",
    popup=Nikko_guesthouse_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Guesthouse_ouka = 'https://cf.bstatic.com/xdata/images/hotel/max1024x768/163921184.webp?k=dadcdbd7ad99b9a058312765ab3d3a83baf698c768e8f71d4a60a79511f4d128&o='
Guesthouse_ouka_url = 'https://www.booking.com/hotel/jp/guest-house-ouka.html?aid=356929&label=metagha-link-MRUS-hotel-1420831_dev-desktop_los-1_bw-28_dow-Tuesday_defdate-1_room-0_gstadt-2_rateid-public_aud-0_gacid-6623578701_mcid-50_ppa-0_clrid-0_ad-1_gstkid-0_checkin-20240423_ppt-B_lp-2840_r-6456438535938861595&sid=16819b199391e7ad666df2983a6a32fd&all_sr_blocks=142083101_338792938_0_0_0%2C142083101_338792938_0_0_0&checkin=2024-04-23&checkout=2024-04-24&dest_id=-245205&dest_type=city&dist=0&group_adults=2&group_children=0&hapos=1&highlighted_blocks=142083101_338792938_0_0_0%2C142083101_338792938_0_0_0&hpos=1&matching_block_id=142083101_338792938_0_0_0&no_rooms=2&req_adults=2&req_children=0&room1=A&room2=A&sb_price_type=total&sr_order=popularity&sr_pri_blocks=142083101_338792938_0_0_0__315000%2C142083101_338792938_0_0_0__315000&srepoch=1711401307&srpvid=b896956b45990118&type=total&ucfs=1&activeTab=main'

Guesthouse_ouka_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Guesthouse Ouka</strong><br>'
                 f'<img src="{Guesthouse_ouka}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Guesthouse_ouka}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Guesthouse_ouka_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[36.14699585679748, 137.25157098975785],
    tooltip="Guesthouse Ouka",
    popup=Guesthouse_ouka_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Guesthouse_tomaru = 'https://cf.bstatic.com/xdata/images/hotel/max1280x900/534133766.jpg?k=774f71b2fbe70a3a0e1a17fd808b3e50ab31e379f014aa87394bf131e6c2ad90&o=&hp=1'
Guesthouse_tomaru_url = 'https://www.booking.com/hotel/jp/hidatakayama-guest-house-tomaru.html?aid=356929&label=metagha-link-MRUS-hotel-1420831_dev-desktop_los-1_bw-28_dow-Tuesday_defdate-1_room-0_gstadt-2_rateid-public_aud-0_gacid-6623578701_mcid-50_ppa-0_clrid-0_ad-1_gstkid-0_checkin-20240423_ppt-B_lp-2840_r-6456438535938861595&sid=16819b199391e7ad666df2983a6a32fd&all_sr_blocks=37444401_368011499_0_0_0%2C37444401_368011499_0_0_0&checkin=2024-04-23&checkout=2024-04-24&dest_id=-245205&dest_type=city&dist=0&group_adults=2&group_children=0&hapos=4&highlighted_blocks=37444401_368011499_0_0_0%2C37444401_368011499_0_0_0&hpos=4&matching_block_id=37444401_368011499_0_0_0&no_rooms=2&req_adults=2&req_children=0&room1=A&room2=A&sb_price_type=total&sr_order=popularity&sr_pri_blocks=37444401_368011499_0_0_0__315000%2C37444401_368011499_0_0_0__315000&srepoch=1711401313&srpvid=b896956b45990118&type=total&ucfs=1&activeTab=main'

Guesthouse_tomaru_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Guesthouse Tomaru</strong><br>'
                 f'<img src="{Guesthouse_tomaru}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Guesthouse_tomaru}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Guesthouse_tomaru_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[36.1419461574299, 137.25313509583643],
    tooltip="Guesthouse Tomaru",
    popup=Guesthouse_tomaru_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Guesthouse_Sakura = 'https://cf.bstatic.com/xdata/images/hotel/max1280x900/98506285.jpg?k=fa6ab92e9c3e7711fbf84b82dae0aad3f69f38feb1d00531626684842c7e0cf3&o=&hp=1'
Guesthouse_Sakura_url = 'https://www.booking.com/hotel/jp/sakura-guest-house.html?aid=356929&label=metagha-link-MRUS-hotel-1420831_dev-desktop_los-1_bw-28_dow-Tuesday_defdate-1_room-0_gstadt-2_rateid-public_aud-0_gacid-6623578701_mcid-50_ppa-0_clrid-0_ad-1_gstkid-0_checkin-20240423_ppt-B_lp-2840_r-6456438535938861595&sid=16819b199391e7ad666df2983a6a32fd&all_sr_blocks=34539103_221727557_0_0_0%2C34539103_221727557_0_0_0&checkin=2024-04-23&checkout=2024-04-24&dest_id=-245205&dest_type=city&dist=0&group_adults=2&group_children=0&hapos=6&highlighted_blocks=34539103_221727557_0_0_0%2C34539103_221727557_0_0_0&hpos=6&matching_block_id=34539103_221727557_0_0_0&no_rooms=2&req_adults=2&req_children=0&room1=A&room2=A&sb_price_type=total&sr_order=popularity&sr_pri_blocks=34539103_221727557_0_0_0__306000%2C34539103_221727557_0_0_0__306000&srepoch=1711401313&srpvid=b896956b45990118&type=total&ucfs=1&activeTab=main'

Guesthouse_Sakura_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Guesthouse Sakura</strong><br>'
                 f'<img src="{Guesthouse_Sakura}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Guesthouse_Sakura}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Guesthouse_Sakura_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[36.13583039116946, 137.2415393688495],
    tooltip="Guesthouse Sakura",
    popup=Guesthouse_Sakura_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Guesthouse_shirakawa = 'https://cf.bstatic.com/xdata/images/hotel/max1280x900/358833061.jpg?k=459c0e23c70e38f31b449bd0db949298586d1a27387e1149ce479058f297c846&o=&hp=1'
Guesthouse_shirakawa_url = 'https://www.booking.com/hotel/jp/shirakawa-go-inn-qi-fu-xian-da-ye-jun-bai-chuan-cun.html?aid=356929&label=metagha-link-MRUS-hotel-4499531_dev-desktop_los-1_bw-28_dow-Tuesday_defdate-1_room-0_gstadt-2_rateid-0_aud-0_gacid-6623578701_mcid-50_ppa-0_clrid-0_ad-1_gstkid-0_checkin-20240423_ppt-_lp-2840_r-7874774531553695386&sid=16819b199391e7ad666df2983a6a32fd&all_sr_blocks=449953109_380296350_2_0_0&checkin=2024-04-23&checkout=2024-04-24&dest_id=900049766&dest_type=city&dist=0&group_adults=2&group_children=0&hapos=1&highlighted_blocks=449953109_380296350_2_0_0&hpos=1&matching_block_id=449953109_380296350_2_0_0&no_rooms=1&req_adults=2&req_children=0&room1=A%2CA&sb_price_type=total&sr_order=popularity&sr_pri_blocks=449953109_380296350_2_0_0__990000&srepoch=1711402011&srpvid=deb596cbff6c0319&type=total&ucfs=1&activeTab=main'

Guesthouse_shirakawa_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Guesthouse Shirakawa-Go Inn</strong><br>'
                 f'<img src="{Guesthouse_shirakawa}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Guesthouse_shirakawa}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Guesthouse_shirakawa_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[36.27186577116688, 136.89937313632268],
    tooltip="Guesthouse Shirakawa-Go Inn",
    popup=Guesthouse_shirakawa_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Green_rich = 'https://cf.bstatic.com/xdata/images/hotel/max1280x900/220985805.jpg?k=a85635f05b76e9b4667392e7cc5cde003bf05f4f8fc5e1e45b3e4fb5b0b9d55d&o=&hp=1'
Green_rich_url = 'https://www.booking.com/hotel/jp/green-rich-hotel-tottori-ekimae.html?aid=356929&label=metagha-link-MRUS-hotel-4499531_dev-desktop_los-1_bw-28_dow-Tuesday_defdate-1_room-0_gstadt-2_rateid-0_aud-0_gacid-6623578701_mcid-50_ppa-0_clrid-0_ad-1_gstkid-0_checkin-20240423_ppt-_lp-2840_r-7874774531553695386&sid=16819b199391e7ad666df2983a6a32fd&all_sr_blocks=517358502_0_2_0_0&checkin=2024-04-23&checkout=2024-04-24&dest_id=-246571&dest_type=city&dist=0&group_adults=2&group_children=0&hapos=1&highlighted_blocks=517358502_0_2_0_0&hpos=1&matching_block_id=517358502_0_2_0_0&no_rooms=1&req_adults=2&req_children=0&room1=A%2CA&sb_price_type=total&sr_order=popularity&sr_pri_blocks=517358502_0_2_0_0__873621&srepoch=1711402651&srpvid=b8eb980c67f30150&type=total&ucfs=1&activeTab=main'

Green_rich_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Green Rich Hotel Tottori Ekimae</strong><br>'
                 f'<img src="{Green_rich}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Green_rich}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Green_rich_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.49526550513466, 134.22818365397933],
    tooltip="Green rich Hotel Tottori Ekimae",
    popup=Green_rich_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Super_hotel = 'https://cf.bstatic.com/xdata/images/hotel/max1280x900/208848231.jpg?k=82dc0d9d0c5e42df3eaa3b87f1b138935095d17104c434dcd16fcf70083da727&o=&hp=1'
Super_hotel_url = 'https://www.booking.com/hotel/jp/super-tottori-ekimae.html?aid=356929&label=metagha-link-MRUS-hotel-4499531_dev-desktop_los-1_bw-28_dow-Tuesday_defdate-1_room-0_gstadt-2_rateid-0_aud-0_gacid-6623578701_mcid-50_ppa-0_clrid-0_ad-1_gstkid-0_checkin-20240423_ppt-_lp-2840_r-7874774531553695386&sid=16819b199391e7ad666df2983a6a32fd&all_sr_blocks=306785705_262388470_0_1_0&checkin=2024-04-23&checkout=2024-04-24&dest_id=-246571&dest_type=city&dist=0&group_adults=2&group_children=0&hapos=3&highlighted_blocks=306785705_262388470_0_1_0&hpos=3&matching_block_id=306785705_262388470_0_1_0&no_rooms=1&req_adults=2&req_children=0&room1=A%2CA&sb_price_type=total&sr_order=popularity&sr_pri_blocks=306785705_262388470_0_1_0__1041300&srepoch=1711402707&srpvid=b8eb980c67f30150&type=total&ucfs=1&activeTab=main'

Super_hotel_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Super Hotel Tottori Ekimae</strong><br>'
                 f'<img src="{Super_hotel}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Super_hotel}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Super_hotel_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[35.49272984928826, 134.22596440174482],
    tooltip="Super Hotel Tottori Ekimae",
    popup=Super_hotel_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Guesthouse_iwato = 'https://cf.bstatic.com/xdata/images/hotel/max1280x900/427654206.jpg?k=0e32cc3491da793620adc434dcb1223af8b642d1b6bec175eae180ad0a10a647&o=&hp=1'
Guesthouse_iwato_url = 'https://www.booking.com/hotel/jp/gesutohausuiwato.html?aid=356929&label=metagha-link-MRUS-hotel-5612843_dev-desktop_los-1_bw-28_dow-Tuesday_defdate-1_room-0_gstadt-2_rateid-public_aud-0_gacid-6623578701_mcid-10_ppa-0_clrid-0_ad-1_gstkid-0_checkin-20240423_ppt-_lp-2840_r-11471770942725840875&sid=16819b199391e7ad666df2983a6a32fd&all_sr_blocks=277388107_270925082_2_0_0&checkin=2024-04-23&checkout=2024-04-24&dest_id=900051135&dest_type=city&dist=0&group_adults=2&group_children=0&hapos=2&highlighted_blocks=277388107_270925082_2_0_0&hpos=2&matching_block_id=277388107_270925082_2_0_0&no_rooms=1&req_adults=2&req_children=0&room1=A%2CA&sb_price_type=total&sr_order=popularity&sr_pri_blocks=277388107_270925082_2_0_0__648000&srepoch=1711403193&srpvid=6b06991ad510012d&type=total&ucfs=1&activeTab=main'

Guesthouse_iwato_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Guesthouse Iwato</strong><br>'
                 f'<img src="{Guesthouse_iwato}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Guesthouse_iwato}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Guesthouse_iwato_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[32.731903449300695, 131.34754243801467],
    tooltip="Guesthouse Iwato",
    popup=Guesthouse_iwato_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Guesthouse_shizuho = 'https://cf.bstatic.com/xdata/images/hotel/max1280x900/220603024.jpg?k=2f77900f26b457ce2b8b8eb6d638504ae376eabc98d4c3f03ad8815be2a42879&o=&hp=1'
Guesthouse_shizuho_url = 'https://www.booking.com/hotel/jp/guest-house-shizuho.html?aid=356929&label=metagha-link-MRUS-hotel-5612843_dev-desktop_los-1_bw-28_dow-Tuesday_defdate-1_room-0_gstadt-2_rateid-public_aud-0_gacid-6623578701_mcid-10_ppa-0_clrid-0_ad-1_gstkid-0_checkin-20240423_ppt-_lp-2840_r-11471770942725840875&sid=16819b199391e7ad666df2983a6a32fd&all_sr_blocks=561284302_332796015_2_0_0&checkin=2024-04-23&checkout=2024-04-24&dest_id=900051135&dest_type=city&dist=0&group_adults=2&group_children=0&hapos=1&highlighted_blocks=561284302_332796015_2_0_0&hpos=1&matching_block_id=561284302_332796015_2_0_0&no_rooms=1&req_adults=2&req_children=0&room1=A%2CA&sb_price_type=total&sr_order=popularity&sr_pri_blocks=561284302_332796015_2_0_0__860000&srepoch=1711403193&srpvid=6b06991ad510012d&type=total&ucfs=1&activeTab=main'

Guesthouse_shizuho_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Guesthouse Shizuho</strong><br>'
                 f'<img src="{Guesthouse_shizuho}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Guesthouse_shizuho}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Guesthouse_shizuho_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[32.70855540575582, 131.3090964507013],
    tooltip="Guesthouse Shizuho",
    popup=Guesthouse_shizuho_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Guesthouse_aki = 'https://cf.bstatic.com/xdata/images/hotel/max1280x900/236198885.jpg?k=58770c5f2125fd300b433fe8d522c32368aa25c0347c0aa4af5afbbfb2f0248a&o=&hp=1'
Guesthouse_aki_url = 'https://www.booking.com/hotel/jp/gesutohausu-aki.html?aid=356929&label=metagha-link-MRUS-hotel-2559489_dev-desktop_los-1_bw-28_dow-Tuesday_defdate-1_room-0_gstadt-2_rateid-public_aud-0_gacid-6623578701_mcid-10_ppa-0_clrid-0_ad-1_gstkid-0_checkin-20240423_ppt-_lp-2840_r-11353739058638648501&sid=16819b199391e7ad666df2983a6a32fd&all_sr_blocks=255948901_214730487_2_0_0&checkin=2024-04-23&checkout=2024-04-24&dest_id=-238668&dest_type=city&dist=0&group_adults=2&group_children=0&hapos=1&highlighted_blocks=255948901_214730487_2_0_0&hpos=1&matching_block_id=255948901_214730487_2_0_0&no_rooms=1&req_adults=2&req_children=0&room1=A%2CA&sb_price_type=total&sr_order=popularity&sr_pri_blocks=255948901_214730487_2_0_0__700000&srepoch=1711405937&srpvid=1d269e7694bb0114&type=total&ucfs=1&activeTab=main'

Guesthouse_aki_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Guesthouse Aki</strong><br>'
                 f'<img src="{Guesthouse_aki}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Guesthouse_aki}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Guesthouse_aki_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[31.588907565883268, 131.39678876436372],
    tooltip="Guesthouse Aki",
    popup=Guesthouse_aki_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Hostel_marika = 'https://cf.bstatic.com/xdata/images/hotel/max1280x900/188872740.jpg?k=4fcac057efb89b11e46eb9e2a64f31b235629073d3e8fa2bf302323dba262dda&o=&hp=1'
Hostel_marika_url = 'https://www.booking.com/hotel/jp/hostel-marika-hosuterumarika.html?aid=356929&label=metagha-link-MRUS-hotel-2559489_dev-desktop_los-1_bw-28_dow-Tuesday_defdate-1_room-0_gstadt-2_rateid-public_aud-0_gacid-6623578701_mcid-10_ppa-0_clrid-0_ad-1_gstkid-0_checkin-20240423_ppt-_lp-2840_r-11353739058638648501&sid=16819b199391e7ad666df2983a6a32fd&all_sr_blocks=448000202_143461712_2_0_0&checkin=2024-04-23&checkout=2024-04-24&dest_id=-238668&dest_type=city&dist=0&group_adults=2&group_children=0&hapos=2&highlighted_blocks=448000202_143461712_2_0_0&hpos=2&matching_block_id=448000202_143461712_2_0_0&no_rooms=1&req_adults=2&req_children=0&room1=A%2CA&sb_price_type=total&sr_order=popularity&sr_pri_blocks=448000202_143461712_2_0_0__600000&srepoch=1711405937&srpvid=1d269e7694bb0114&type=total&ucfs=1&activeTab=main'

Hostel_marika_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Hostel Marika</strong><br>'
                 f'<img src="{Hostel_marika}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Hostel_marika}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Hostel_marika_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[31.625096194386867, 131.3546153956401],
    tooltip="Hostel Marika",
    popup=Hostel_marika_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Guesthouse_nichinan = 'https://cf.bstatic.com/xdata/images/hotel/max1280x900/368968542.jpg?k=c855538791a8b7af0c09082c4ee8335c9e3eab3d108a4deb33e02be1c5cd2725&o=&hp=1'
Guesthouse_nichinan_url = 'https://www.booking.com/hotel/jp/guesthouse-nichinan-vacation-stay-82905v.html?aid=356929&label=metagha-link-MRUS-hotel-2559489_dev-desktop_los-1_bw-28_dow-Tuesday_defdate-1_room-0_gstadt-2_rateid-public_aud-0_gacid-6623578701_mcid-10_ppa-0_clrid-0_ad-1_gstkid-0_checkin-20240423_ppt-_lp-2840_r-11353739058638648501&sid=16819b199391e7ad666df2983a6a32fd&all_sr_blocks=869349302_356165678_2_0_0&checkin=2024-04-23&checkout=2024-04-24&dest_id=-238668&dest_type=city&dist=0&group_adults=2&group_children=0&hapos=3&highlighted_blocks=869349302_356165678_2_0_0&hpos=3&matching_block_id=869349302_356165678_2_0_0&no_rooms=1&req_adults=2&req_children=0&room1=A%2CA&sb_price_type=total&sr_order=popularity&sr_pri_blocks=869349302_356165678_2_0_0__497430&srepoch=1711405944&srpvid=1d269e7694bb0114&type=total&ucfs=1&activeTab=main'

Guesthouse_nichinan_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Guesthouse Nichinan</strong><br>'
                 f'<img src="{Guesthouse_nichinan}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Guesthouse_nichinan}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Guesthouse_nichinan_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[31.59153684086511, 131.40967547170573],
    tooltip="Guesthouse Nichinan",
    popup=Guesthouse_nichinan_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Ryokan_ariakeso = 'https://res.klook.com/klook-hotel/image/upload/fl_lossy.progressive,c_fill,f_auto,q_65/s28rt/yvXL/4mPwZVb7.jpg'
Ryokan_ariakeso_url = 'https://guest.klook.com/hotels/detail/1262422-ryokan-ariakeso/?hotelid=1262422&check_in=2024-04-23&check_out=2024-04-24&aid=28539&campaignid=17745516846&adult_num=2&lead_time=27&child_num=0&childages=&room_num=1&google_site=mapresults&length_of_stay=1&partner_currency=USD&click_type=hotel&click_price_total=56.80&price_tax=9.43&rate_key=1-32-0381228L1178777&user_country=US&click_currency=USD&_currency=USD&device=desktop&partner_hotelid=1262422&language=en&audience_list=&verification=false&booking_source=cpc&isPromoted=0&utm_source=MSE&utm_medium=Google&utm_campaign=28539&utm_term=1262422&utm_content=USD&isAdClick=1&arrival_fees=0&m_clickid=1711477121'

Ryokan_ariakeso_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Ryokan Ariakeso</strong><br>'
                 f'<img src="{Ryokan_ariakeso}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Ryokan_ariakeso}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Ryokan_ariakeso_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[32.407167278486355, 130.34000969197973],
    tooltip="Ryokan Ariakeso",
    popup=Ryokan_ariakeso_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Unplan_fukuoka = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/3/310474/bq1jaszshfss7qtpvije'
Unplan_fukuoka_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/UNPLAN-Fukuoka/Fukuoka/310474?from=2024-07-11&to=2024-07-12&guests=2'

Unplan_fukuoka_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Unplan Fukuoka</strong><br>'
                 f'<img src="{Unplan_fukuoka}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Unplan_fukuoka}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Unplan_fukuoka_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[33.590392677697295, 130.38003795701616],
    tooltip="Unplan Fukuoka",
    popup=Unplan_fukuoka_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



Webase_hakata = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/2/279321/pev3b010lrtvapky6jjs'
Webase_hakata_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/WeBase-HAKATA/Fukuoka/279321?from=2024-07-11&to=2024-07-12&guests=2'

Webase_hakata_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">WeBase Hakata</strong><br>'
                 f'<img src="{Webase_hakata}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Webase_hakata}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Webase_hakata_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[33.59569116317847, 130.40819856688705],
    tooltip="WeBase Hakata",
    popup=Webase_hakata_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)


Hostel_toki = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/2/286150/oynfxqryvayzkx9wruhz'
Hostel_toki_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/Hostel-TOKI/Fukuoka/286150?from=2024-07-11&to=2024-07-12&guests=2'

Hostel_toki_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Hostel Toki</strong><br>'
                 f'<img src="{Hostel_toki}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Hostel_toki}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Hostel_toki_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[33.58048792653956, 130.41870553989955],
    tooltip="Hostel Toki",
    popup=Hostel_toki_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)


Fukuoka_hana = 'https://a.hwstatic.com/image/upload/f_auto,q_auto,w_1900,h_823,c_limit,e_sharpen,e_improve,e_vibrance:60/v1/propertyimages/2/286150/oynfxqryvayzkx9wruhz'
Fukuoka_hana_url = 'https://www.hostelworld.com/pwa/hosteldetails.php/Hostel-TOKI/Fukuoka/286150?from=2024-07-11&to=2024-07-12&guests=2'

Fukuoka_hana_content = ('<div style="max-height: 500px; max-width: 600px; overflow-y: auto;">'
                 '<strong style="font-size:20px">Fukuoka Hana Hostel</strong><br>'
                 f'<img src="{Fukuoka_hana}" alt="Image" style="width:450px;height:450px;"><br>'
                 f'<a href="{Fukuoka_hana}" target="_blank" style="font-size:10px" >Image Source</a><br><br>'
                 f'<a href="{Fukuoka_hana_url}" target="_blank" style="font-size:14px" >Website</a><br><br>')

folium.Marker(
    location=[33.59264054163918, 130.40994992997832],
    tooltip="Fukuoka Hana Hostel",
    popup=Fukuoka_hana_content,
    icon=folium.Icon(color="green", icon="home")
    ).add_to(m)



m.save("index.html")
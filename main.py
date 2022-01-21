import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import requests
import json
import random
import asyncio
from replit import db
from keepalive import keep_alive

client = discord.Client()
myid = [
  '<@933873862356107286>'
]

#Word lists

number_list = [
  "1",
  "2",
  "3",
  "4",
  "5",
  "6",
  "7",
  "8",
  "9",
  "10",
]

d4_words = [
  "roll a d4",
  "roll a 4",
  "roll d4",
  "roll 4",
]

d6_words = [
  "roll a d6",
  "roll a 6",
  "roll d6",
  "roll 6",
]

d8_words = [
  "roll a d8",
  "roll an 8",
  "roll a 8",
  "roll d8",
  "roll 8",
]

d10_words = [
  "roll a d10",
  "roll a 10",
  "roll d10",
  "roll 10",
]

d12_words = [
  "roll a d12",
  "roll a 12",
  "roll d12",
  "roll 12",
]

d20_words = [
  "roll a d20",
  "roll a 20",
  "roll d20",
  "roll 20",
]

coin_words = [
  "coinflip",
  "coin flip",
  "flip a coin",
]

insults = [
  "isn't that great ngl",
  "deserves to die in a hole, preferably at the bottom of a mass grave",
  "feels the need to have a bot insult them... how sad",
  "is a sad, limp, and soggy noodle of a human",
  "brought opposing forces into this",
  "******",
  "deserves to get their teeth nail clipped",
  "got all ball no cock",
  "is scott",
  "fuck",
  "deserves to have their body parts swapped around",
  "looks good with a ball chin; as in having balls stapled to your chin",
  "needs balls in their jaw",
  "is dreamgender",
  "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
  ":)",
  "doesn't know which is smaller, their IQ or their dick.",
  "thinks 9+10 is 21",
  "thinks 9+10 is 19",
  "likely uses uwu on a daily basis",
  "doesn't know what a stritch is (unpog)",
  "isn't my little pogchamp",
  "needs to be rearranged",
  "is going to heaven (bad ending)",
  "sex?",
  "is uhm uhhh uh uhm u h h uhmuhhhhh......",
  "listens to kids bop avidly",
  "skibbidy bops your mm da da",
  "believes american propaganda",
  "is british",
  "doesn't listen to Will Wood and the Tapeworms",
  "voted :thumbsdown:",
  "thinks emojis are better than emoticons",
  "uses tell me bs for inspiration",
  "posts porn in general",
  "mains sniper",
  "is so awkward in social situations that they can never form meaningful relationships with anyone, especially those that they have a possible romantic or sexual interest in",
  "lmao",
  "has a neo protogen fursona they keep secret from everyone",
  "is the sussy imposter (holy shit)",
  "should learn that subsituting real social interation for digital social interaction over the internet as opposed to physical is a one way track to spiralling down an ever-sinking hole of depression and mental instability",
  "gatekeeps weirdo by radiohead",
  "was (and maybe still is) a weezer fanboy in their teenage years",
  "uses the localised names of stands",
]

#Responses
coin_flip = [
  "you flipped **heads**",
  "you flipped **tails**",
]

d4 = [
   "you rolled a *1*",
  "you rolled a **2**",
  "you rolled a **3**",
  "you rolled a ***4***",
]

d6 = [
  "you rolled a *1*",
  "you rolled a **2**",
  "you rolled a **3**",
  "you rolled a **4**",
  "you rolled a **5**",
  "you rolled a ***6***",
]

d8 = [
  "you rolled a *1*",
  "you rolled a **2**",
  "you rolled a **3**",
  "you rolled a **4**",
  "you rolled a **5**",
  "you rolled a **6**",
  "you rolled a **7**",
  "you rolled a ***8***",
]

d10 = [
  "you rolled a *1*",
  "you rolled a **2**",
  "you rolled a **3**",
  "you rolled a **4**",
  "you rolled a **5**",
  "you rolled a **6**",
  "you rolled a **7**",
  "you rolled a **8**",
  "you rolled a **9**",
  "you rolled a ***10***",
]

d12 = [
  "you rolled a *1*",
  "you rolled a **2**",
  "you rolled a **3**",
  "you rolled a **4**",
  "you rolled a **5**",
  "you rolled a **6**",
  "you rolled a **7**",
  "you rolled a **8**",
  "you rolled a **9**",
  "you rolled a **10**",
  "you rolled a **11**",
  "you rolled a ***12***",
]

d20 = [
  "you rolled a *1*",
  "you rolled a **2**",
  "you rolled a **3**",
  "you rolled a **4**",
  "you rolled a **5**",
  "you rolled a **6**",
  "you rolled a **7**",
  "you rolled a **8**",
  "you rolled a **9**",
  "you rolled a **10**",
  "you rolled a **11**",
  "you rolled a **12**",
  "you rolled a **13**",
  "you rolled a **14**",
  "you rolled a **15**",
  "you rolled a **16**",
  "you rolled a **17**",
  "you rolled a **18**",
  "you rolled a **19**",
  "you rolled a ***20***",
]

avatar_words = [
  "avatar",
  "pfp",
  "profile picture",
  "user",
]

wisdom = [
  "if you have to look it up you're doing something wrong and should stop",
  "i don't care if they're 1000 years old they look like a child and thus are a child",
  "furries say that animals are ok to fuck as long as they walk on two legs",
  "sometimes, you just need a little less gun",
  "just use a gun, and if that don't work, use more gun",
  "Medic from the hit game TF2 is not officially a doctor, yet pioneers the medical industry with their revolutionary design dubbed 'the Medigun.' this just goes to show that not having a title, degree, official certification does not mean you are worth less",
  "everyone would be better off when money is abolished",
  "it's not fan fiction if you created the fiction it's based off of",
  "embed messages are WAY more effort than they're worth to code in discord.py",
  "if you need help, it's best to ask those around you. if there's no one around who can help you, random people on the internet are the next best thing",
  "batman is a furry",
  "categories like 'soup,' 'stew,' and 'cereal,' are all intentionally vague to allow for new creations to easily fit within the established labels. this also opens up the possibility of something being two things at the same time, which is completely intentional",
  "the internet is a pretty shitty place if you look in the wrong places, just like real life",
  "wisdom and advice are just words that someone spoke or typed that are intended to mean something meaningful, but often the best way to accrue advice or wisdom is through experience and/or random chance",
  "i am a glorified fortune cookie",
]

porn = [
  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTd6vvayqcPUQo-gKQ0o4o5Cs2eOZ2TyyBIBmi3qaoubGgyEPSI36bG52vxPVQi2Weixd4&usqp=CAU",
  "https://media.discordapp.net/attachments/882010619115626526/882010663185178644/sample_4e74640dccfba914fd094f659bff604c.png?width=305&height=431",
  "https://media.discordapp.net/attachments/882009502013087814/882017860409524224/image0.png",
  "https://media.discordapp.net/attachments/882009502013087814/882017753123401728/image0.png",
  "https://images-ext-1.discordapp.net/external/vXQ0MpUK8pit1FxRtaFn1kKV-kNYiCU_aRqrDoRTT3I/https/pbs.twimg.com/media/Dy6EqboUUAA8U4I.jpg%3Alarge?width=400&height=225",
  "https://media.discordapp.net/attachments/882009502013087814/882018194255147038/cxfrom5u5zs61.png",
  "https://media.discordapp.net/attachments/882009502013087814/882017428677218304/image0.png",
  "https://media.discordapp.net/attachments/882009502013087814/882018369899991100/batdosd0omy41.png",
  "https://images-ext-2.discordapp.net/external/t3E3KZd6bA0xVdioq_Qu64CDTD11cC6D2vOze_R6SQM/https/images-ext-2.discordapp.net/external/pLphUXyKoexRNR8lhNXqWHfz7hrAHeAA8D2L06JhR7I/https/us.rule34.xxx/images/3046/cacc3b66fe5355280841be6468da02f2.jpeg?width=530&height=432",
  "https://media.discordapp.net/attachments/882009502013087814/882018473562230854/image0.png",
  "https://media.discordapp.net/attachments/882009502013087814/882018544521445416/image0.png",
  "https://media.discordapp.net/attachments/882009502013087814/882018614004305930/image1.png",
  "https://media.discordapp.net/attachments/882009502013087814/882018672581943326/image0.png",
  "https://media.discordapp.net/attachments/766821369273909259/882086236049768488/image2.png?width=824&height=512",
  "https://media.discordapp.net/attachments/766821369273909259/882084113203462164/image4.png?width=397&height=512",
  "https://media.discordapp.net/attachments/766821369273909259/882084112863727676/image3.png?width=362&height=511",
  "https://media.discordapp.net/attachments/766821369273909259/882084112435904512/image2.png?width=364&height=512",
  "https://media.discordapp.net/attachments/766821369273909259/882084100268245012/image1.png?width=729&height=512",
  "https://media.discordapp.net/attachments/766821369273909259/882084099865608302/image0.png?width=289&height=512",
  "https://media.discordapp.net/attachments/766821369273909259/882086235391266897/image0.png?width=586&height=512",
  "https://media.discordapp.net/attachments/882009502013087814/882090585895350292/image0.jpg?width=357&height=511",
  "https://media.discordapp.net/attachments/882009502013087814/882089671620972585/image0.png?width=327&height=511",
  "https://media.discordapp.net/attachments/882009502013087814/882089640155308092/image0.png?width=512&height=512",
  "https://media.discordapp.net/attachments/882009502013087814/882089599118221362/image0.png",
  "https://cdn.discordapp.com/attachments/882009502013087814/882090507965186118/video0.mp4",
  "https://media.discordapp.net/attachments/762051401139879956/889672515335639040/59abs7.png",
  "https://media.discordapp.net/attachments/882009502013087814/889649299217055785/image0.png",
  "https://media.discordapp.net/attachments/766821369273909259/882015323992231966/image0.jpg?width=688&height=512",
  "https://media.discordapp.net/attachments/766821369273909259/882016313143337090/image0.jpg?width=509&height=512",
  "https://media.discordapp.net/attachments/766821369273909259/882084101119676416/image3.png?width=340&height=512",
  "https://media.discordapp.net/attachments/766821369273909259/882084111773233222/image0.png?width=335&height=512",
  "https://media.discordapp.net/attachments/766821369273909259/882086236414677012/image3.png?width=539&height=512",
  "https://media.discordapp.net/attachments/702139507700662312/884263092932980756/image0.png?width=420&height=512",
  "https://media.discordapp.net/attachments/702139507700662312/883889625943396372/image0.jpg?width=708&height=512",
  "https://media.discordapp.net/attachments/702139507700662312/869418602636406784/fabc8814-caac-4d8e-a312-cbc8fa9ab7bf.png?width=512&height=512",
  "https://media.discordapp.net/attachments/702139507700662312/862751053375471687/image0.jpg?width=542&height=512",
  "https://media.discordapp.net/attachments/702139507700662312/861472303703130112/image0.jpg?width=566&height=512",
  "https://tenor.com/view/troll-face-creepy-smile-gif-18297390",
  "https://tenor.com/view/tuga-numeiro-gif-18302117",
  "https://media.discordapp.net/attachments/803669036508381234/867017819873607680/LKKXhqiw.gif",
  "https://media.discordapp.net/attachments/872345001261170738/872349006288814131/dc2bb2da71c9f703a6e5050448b3b5f9.png?width=709&height=512",
  "https://media.discordapp.net/attachments/872345001261170738/872346329156833310/SPOILER_726440_spikedmauler_kobold-design.png?width=392&height=511",
  "https://media.discordapp.net/attachments/882010619115626526/891851600337981440/image0.jpg?width=362&height=512",
  "https://media.discordapp.net/attachments/882010619115626526/891851074707787886/image0.jpg?width=384&height=512",
  "https://media.discordapp.net/attachments/882010619115626526/882066860227579985/image0.jpg?width=306&height=512",
  "https://media.discordapp.net/attachments/882010619115626526/882066593595674664/image0.jpg?width=361&height=511",
  "https://media.discordapp.net/attachments/882010619115626526/882066079634042940/image0.jpg?width=362&height=511",
  "https://media.discordapp.net/attachments/882010619115626526/882064612730753064/image0.jpg?width=375&height=511",
  "https://media.discordapp.net/attachments/882010619115626526/891854479845117992/image0.jpg?width=363&height=512",
  "https://cdn.discordapp.com/attachments/882010619115626526/895541568239443968/video0.mp4",
  "https://media.discordapp.net/attachments/882010619115626526/895541768471339058/image0.png?width=682&height=765",
 "https://media.discordapp.net/attachments/882010619115626526/903992151770288168/IMG_4016.jpg",
 "https://media.discordapp.net/attachments/882010619115626526/903992867066884146/image0.jpg?width=451&height=765",
 "https://media.discordapp.net/attachments/882010619115626526/903993145413476362/image0.jpg?width=494&height=765",
 "https://media.discordapp.net/attachments/882010619115626526/907866857892093992/image0.jpg?width=541&height=765", 
 "https://media.discordapp.net/attachments/872345001261170738/881885794778873916/image0.jpg?width=485&height=765",
 "https://cdn.discordapp.com/attachments/828753545792061500/910756807977365554/IMG_4299.jpg",
 "https://cdn.discordapp.com/attachments/828753545792061500/910756840613228574/IMG_4291.jpg",
 "https://cdn.discordapp.com/attachments/828753545792061500/910756989792043018/IMG_4272.jpg",
 "https://cdn.discordapp.com/attachments/626912799670534154/910756960138301460/IMG_4278.mp4",
 "https://cdn.discordapp.com/attachments/626912799670534154/910756911979327508/IMG_4294.mp4",
 "https://cdn.discordapp.com/attachments/626912799670534154/910756903511027752/IMG_4296.mp4",
 "https://cdn.discordapp.com/attachments/882010619115626526/910758521165987870/image0.jpg",
 "https://cdn.discordapp.com/attachments/882010619115626526/910759276958584862/image0.jpg",
 "https://cdn.discordapp.com/attachments/882010619115626526/910759202560020480/image0.jpg",
 "https://cdn.discordapp.com/attachments/882010619115626526/910760069925314580/image0.jpg",
  "https://cdn.discordapp.com/attachments/882010619115626526/910760406748901406/image0.jpg",
 "https://cdn.discordapp.com/attachments/882010619115626526/910768966186721330/image0.jpg",
  "https://tenor.com/view/tf2-gay-heavy-medic-kiss-gif-23550226",
  "https://media.discordapp.net/attachments/882010619115626526/913569067049299998/image0.jpg?width=868&height=614",
  "https://media.discordapp.net/attachments/882010619115626526/914413145211142154/IMG_4458.png?width=425&height=614",
  "https://media.discordapp.net/attachments/828753545792061500/914413543061868554/IMG_4442.jpg",
  "https://media.discordapp.net/attachments/828753545792061500/914413557091819530/IMG_4436.png?width=345&height=613",
  "https://media.discordapp.net/attachments/828753545792061500/914413587001397298/IMG_4425.jpg?width=615&height=614",
  "https://media.discordapp.net/attachments/828753545792061500/914413608321032202/IMG_4419.jpg?width=460&height=614",
  "https://media.discordapp.net/attachments/828753545792061500/914413613928808458/IMG_4415.jpg?width=1092&height=614",
  "https://cdn.discordapp.com/attachments/882010619115626526/914293777101905940/IMG_4454.mp4",
  "https://cdn.discordapp.com/attachments/882010619115626526/914412427297292338/IMG_4450.mp4",
]

#When the bot starts
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Team Fortress 2'))
    print('We have logged in as {0.user}, bot is ready'.format(client))

#Message Events
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    #If staring word
    if any(word in msg for word in coin_words):
        await message.channel.send(random.choice(coin_flip))
    if any(word in msg for word in d20_words):
        await message.channel.send(random.choice(d20))
    if any(word in msg for word in d12_words):
        await message.channel.send(random.choice(d12))
    if any(word in msg for word in d10_words):
        await message.channel.send(random.choice(d10))
    if any(word in msg for word in d8_words):
        await message.channel.send(random.choice(d8))
    if any(word in msg for word in d6_words):
        await message.channel.send(random.choice(d6))
    if any(word in msg for word in d4_words):
        await message.channel.send(random.choice(d4))
    if any(word in msg for word in avatar_words):
        async def avatar(ctx, *, member: discord.Member = None):
            if not member:
                member = ctx.message.author
            em = discord.Embed(title=str(member), color=0xAE0808)
            em.set_image(url=member.avatar_url)
            await ctx.send(embed=em)
    if msg.startswith('horny'):
        await message.channel.send('https://www.nhentai.net/')
    if msg.startswith('hrony'):
        await message.channel.send('lmao mfer cant spell horny')
        #hepl
    if msg.startswith('post porn'):
        await message.channel.send("you made me do this (it's in <#702190721259536405>)")
        nsfw_channel = client.get_channel(702190721259536405)
        await nsfw_channel.send(random.choice(porn))
    if msg.startswith('post pron'):
        await message.channel.send("lmao mfer cant spell porn")
        nsfw_channel_2 = client.get_channel(913339106778546186)
        await nsfw_channel_2.send(random.choice(porn))
    if msg.startswith('wisdom'):
        await message.channel.send(random.choice(wisdom))
    if msg.startswith('hepl'):
        await message.channel.send("__you called? keep note that **all responses** ***must*** **be in lowercase** for the bot to work cuz im lazy.__\n**hepl**: show this message (obviously)\n**cool words**: when you say specially selected words, i respond\n**insult**: say 'insult' in chat and i will personally tear you apart\n**wisdom**: i will tell you actually useful and insightful wisdom\n**shameless promotion**: Get 25% your first month on your server with Bisect Server Hosting when you use code 'tazzan' at checkout! Not limited to Minecraft servers but thats what it mainly is :P https://bisecthosting.com/tazzan\n**post porn**: i will... most likely memes tho (uncensored, use at own risk)\n**coin flip**: flips a virtual coin, will you get heads or tails?\n**roll a d#**: specify a kind of die to roll (4,6,8,10,12,20)\n**>repl**: visit the bot's replit.com site, where it's being hosted")
    if msg.startswith('insult'):
        await message.channel.send(f'alright then,\n{message.author.mention} {random.choice(insults)}')
    if msg.startswith('>repl'):
        await message.channel.send("visit my replit.com page! https://a-very-cool-bot.tazzan2.repl.co")
        return "i know you're here"
    
#Finishing up
keep_alive()
client.run(os.getenv('TOKEN'))
#필요한 모듈 임포트!
import discord#pip
import asyncio#pip
import random
from discord.utils import get
from discord.ext import commands
import json
import os
import math
import asyncio
import requests#pip
from tabulate import tabulate #pip


#이것이 접두사입니다

bot = commands.Bot(command_prefix = '천사야 ', help_command = None)


#봇의 토큰
token=("ODIzOTA5NzU1NTAwMTAxNjUy.YFnrwQ.kYusyaa_mhKTG2BFmVzZ0AMUPOc")

@bot.event
async def on_ready():
    print(f'로그인 성공: {bot.user.name}!')
    game = discord.Game("천사야 도움을 입력해주세요|냥이 찬양하기!.") 
    await bot.change_presence(status=discord.Status.online, activity=game)


@bot.command()
async def 안녕 (ctx):
    await ctx.channel.send("안녕하세요!")


@bot.command()
async def 잘있어 (ctx):
    await ctx.channel.send("안녕히가세요~")


@bot.command()
async def 꿀꿀 (ctx):
    await ctx.channel.send("친구왔는감?")
 





@bot.command(name='청소')
async def meassage_clear(ctx, *, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'총 {amount}개의 메세지를 삭제 했습니다. *{ctx.author.name}*님')
    


@bot.command(name="킥", pass_context=True)
async def 킥(ctx, *, user_name: discord.Member, reason=None):
    await user_name.kick(reason=reason)
    await ctx.send(str(user_name)+"을(를) 추방하였습니다.")






@bot.command(name="밴", pass_context=True)
async def _ban(ctx, *, user_name: discord.Member):
    await user_name.ban()
    await ctx.send(str(user_name)+"을(를) 영원히 매장시켰습니다.")



@bot.command(name="뮤트", pass_context=True)
async def _mute(ctx, member: discord.Member=None):
    member = member or ctx.message.author
    await member.add_roles(get(ctx.guild.roles, name="Muted"))
    await ctx.send(str(member)+"의 입을 막았습니다.")



@bot.command(name="언뮤트", pass_context=True)
async def _unmute(ctx, member: discord.Member=None):
    member = member or ctx.message.author
    await member.remove_roles(get(ctx.guild.roles, name='Muted'))
    await ctx.send(str(member)+"의 입을 풀었습니다.")


@bot.command(name="멤버", pass_context=True)
async def _mute(ctx, member: discord.Member=None):
    member = member or ctx.message.author
    await member.add_roles(get(ctx.guild.roles, name="human"))
    await ctx.send(str(member)+"멤버 지급완료.")

@bot.command()
async def 도움(ctx):
        embed=discord.Embed(title="도움말", description="안녕하세요?천사입니다.", color=0x2EFEF7)
        embed.set_author(name="명령어 목록", url="https://search.pstatic.net/common/?src=http%3A%2F%2Fhttps://search.pstatic.net/common/?src=http%3A%2F%2Fhttps://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20200722_255%2F1595392266349rkALF_JPEG%2F4fx8d0g_202072103855810966.jpg&type=sc960_832")
        embed.set_thumbnail(url="https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20200722_255%2F1595392266349rkALF_JPEG%2F4fx8d0g_202072103855810966.jpg&type=sc960_832")
        embed.add_field(name="청소.", value="메세지를 삭제하는 기능입니다..", inline=True)
        embed.add_field(name="안녕.", value="돼지와 인사하는 명령어 입니다.", inline=True)
        embed.add_field(name="킥(관리자 전용).", value="멤버를 추방시킬수 있습니다.", inline=True)
        embed.add_field(name="뮤트.", value="멤버를 뮤트하는 명령어 입니다.", inline=True)
        embed.add_field(name="기타등등.", value="명령어 추천좀요.", inline=True)
        embed.set_footer(text="(기본지급 재산은 3000 이다돼지야 환전 (숫자)지갑에서 은행으로 돈을 옮기는 명령어이다.저축:환전에서 거꾸로돼지야 입금 @ 사람 (숫자)다른 유저에게 선물하는 명령어 이다.")
        await ctx.channel.send(embed=embed)




@bot.command(pass_context=True)
async def 입금 (ctx,member: discord.Member, amount =None):
    await open_account(ctx.author)
    await open_account(member)
    if amount == None:
        await ctx.send("**량을 정해주세요**")
        return

    bal = await update_bank(ctx.author)

    if amount == "모두":
        amount = bal[0]




    amount = int(amount)

    if amount>bal[1]:
        await ctx.send("**돈이 부족합니다!!**")
        return
    if amount<0:
        await ctx.send("**가능한 양을 입력해주세요.**")
        return

    await update_bank(ctx.author,-1*amount,"bank")
    await update_bank(member,amount,"bank")

    await ctx.send(f"**당신이 {amount} 만큼 입금했습니다**")






@bot.command(pass_context=True)
async def 지갑(ctx):
    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]

    bank_amt = users[str(user.id)]["bank"]

    embed = discord.Embed(title=f"{ctx.author.name}님의 지갑", color=0x2EFEF7)

    embed.add_field(name= "통장", value= wallet_amt,inline = False)
    embed.add_field(name= "현금", value= bank_amt,inline = False)

    await ctx.send(embed = embed)




@bot.command(pass_context=True)
async def 일하기(ctx):
    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()

    


    earnings = random.randrange(99999)

    await ctx.send(f"**돼지가 당신에게 {earnings} 만큼 입금했다!!**")

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json", "w") as f:
        json.dump(users,f)























@bot.command(pass_context=True)
async def 저축(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("**량을 정해주세요.**")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount>bal[1]:
        await ctx.send("**돈이 부족합니다!!**")
        return
    if amount<0:
        await ctx.send("**량을 제데로 설정해주세요**")
        return

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,"bank")

    await ctx.send(f"**당신이 {amount} 만큼 저축했습니다!**")

@bot.command(pass_context=True)
async def 환전(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("**량을 정해주세요. **")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount>bal[0]:
        await ctx.send("**돈이 부족합니다!!**")
        return
    if amount<0:
        await ctx.send("**Amount must be positive**")
        return

    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,"bank")

    await ctx.send(f"**당신이 {amount} 만큼 환전했습니다!**")


@bot.command(pass_context=True)
async def 훔치기(ctx,member: discord.Member):
    await open_account(ctx.author)
    await open_account(member)
   
    bal = await update_bank(member)

    
    if bal[0]<100:
        await ctx.send("그자는 돈이 부족합니다.")
        return

    earnings = random.randrange(0, bal[0])
  

    await update_bank(ctx.author,earnings)
    await update_bank(member,-1*earnings)

    await ctx.send(f"당신이 훔쳐서 {earnings}을 얻었습니다")


@bot.command(pass_context=True)
async def 도박(ctx, amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("얼마나 거실지 포함해서 말씀해주세요.1~3")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount>bal[0]:
        await ctx.send("돈이 부족합니다.")
        return
    if amount<0:
        await ctx.send("1~3까지 가능합니다")
        return

    final = []
    for i in range(3):
        a = random.choice([":poop:", ":smile:", ":cherry_blossom:"])

        final.append(a)

    await ctx.send(str(final))

    if final[0] == final[1] or final[0] == final[2] or final[2] == final[1]:
         await update_bank(ctx.author,2*amount)
         await ctx.send("**당신이 이겼습니다.**")


    else:
        await update_bank(ctx.author,-1*amount)
        await ctx.send("**이돈은 이제 제껍니다**")


async def open_account(user):

    users = await get_bank_data()
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open("mainbank.json", "w") as f:
        json.dump(users,f)
    return True


async def get_bank_data():
    with open("mainbank.json", "r") as f:
        users = json.load(f)

    return users



async def update_bank(user, change=0,mode = 'wallet'):

    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("mainbank.json", "w") as f:
        json.dump(users,f)

    bal = users[str(user.id)]["wallet"],users[str(user.id)]["bank"]





    return bal




bot.run(token)
import requests
from bs4 import BeautifulSoup

#____________________________________________________________________________________________________
#Scrape for Team Names and  their URLs
#____________________________________________________________________________________________________

urlteams = "https://en.as.com/resultados/futbol/primera/equipos/"#URL to be scraped
pageteams = requests.get(urlteams)#HTML request from the page to get DOM

# print(page.text)

soupteam = BeautifulSoup(pageteams.content, "html.parser")#Parse results into object
teamresults = soupteam.find_all("span", class_="escudo")

scrapeTeams = []

for s_team in teamresults:
    # print(team.text.strip())
    scrapeTeams.append(s_team.text.strip())

# print(scrapeTeams)

teamurlresults = soupteam.find_all("ul", class_="arrow-list2 col-md-6 col-sm-6 col-xs-6 content-links-equipo")
scrapeTeamURLs = []

for teamcard in teamurlresults:
    # print(teamcard)
    teamurl = teamcard.find_all("a")[3]["href"]
    # print(teamurl)
    scrapeTeamURLs.append("https://en.as.com" + teamurl)

#____________________________________________________________________________________________________
#Scrape for players
#____________________________________________________________________________________________________

teamindex = 0
for teamurl in scrapeTeamURLs:
    urlplayers = teamurl#Team URL to be scraped
    pageplayers = requests.get(urlplayers)#HTML request from the page to get DOM

    soupplayers = BeautifulSoup(pageplayers.content, "html.parser")#Parse results into object
    playerresults = soupplayers.find_all("div", class_="cnt-data")

    playernames = []
    playernums = []
    playerpositions = []

    for playercontainer in playerresults:
        # print(playercontainer)
        playernamespan = playercontainer.find_all("span", class_="ellipsis nom-jugador")
        for playername in playernamespan:
            # print(playername.text)
            playernames.append(playername.text)

        playerposandnum = playercontainer.find_all("p", class_="s-block cf")
        for playerinfo in playerposandnum:
            playerpos = playerinfo.find_all("span", class_="info-team s-left")
            for playerp in playerpos:
                # print(playerp.text)
                playerpositions.append(playerp.text)
            playernum = playerinfo.find_all("strong", class_="info-team dorsal s-left s-tcenter")
            for playern in playernum:
                # print(playern.text)
                playernums.append(playern.text)
    # print(playernames)
    # print(playerpositions)
    # print(playernums)
    print(f"_______________{scrapeTeams[teamindex]}___________________")
    for x in range(len(playernames)):
        print(playernames[x]+" "+playerpositions[x]+" "+playernums[x])

    teamindex += 1 

#____________________________________________________________________________________________________
#Scrape for Team Odds
#____________________________________________________________________________________________________

# urlods = "https://www.oddsportal.com/soccer/spain/laliga/outrights/"#URL to be scraped
# pageods = requests.get(urlods)#HTML request from the page to get DOM

# soupods = BeautifulSoup(pageods.content, "html.parser")#Parse results into object
# odsresults = soupods.find_all("span", class_="escudo")
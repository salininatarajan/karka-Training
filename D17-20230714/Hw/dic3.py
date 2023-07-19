cricket=[{"country":"india",
          "name":"yuvaraj singh",
          "century":17,
          "half century":71,
          "wickets":148,
          "hat trick wickets":0,
          "top bating score" :[169,256,182]},
          {"country":"Australia",
          "name":"michael hussey",
          "century":22,
          "half century":72,
          "wickets":9,
          "hat trick wickets":0,
          "top bating score" :[195,348,299]},
          {"country":"england",
          "name":"sir alastair cook",
          "century":38,
          "half century":76,
          "wickets":1,
          "hat trick wickets":0,
          "top bating score" :[294,232,314]},
          {"country":"sri lanka",
          "name":"mahela jeyawardene ",
          "century":54,
          "half century":136,
          "wickets":14,
          "hat trick wickets":6,
          "top bating score" :[374,184,192]},
          {"country":"south africa",
          "name":"graeme smith",
          "century":37,
          "half century":90,
          "wickets":26,
          "hat trick wickets":0,
          "top bating score" :[277,212,238]}]
# # 1
def cricket_details():
    n=0
    for i in cricket:
        if i["century"]>10:
            n=n+1
        if i["hat trick wickets"]>5:
            name =i["name"]
            country=i["country"]
        top_score=0
        for one in i["top bating score"]:
          if one>top_score:
                top_score=one
                name=i["name"]
        print(f"top bating score achieved the player name is {name} and the top score is {top_score}")
    score=(f"total number of score more than 10 centuries in the list is {n}")
    print(score) 
    print(f"i have more than 5 hat trick wickets. i am {name} my country is {country}")

cricket_details()






















































    













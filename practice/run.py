players = ['mumu','soe','poe','kai','mine']
callings = ['kai','kai','mine','mine']

def solution(players, callings):
    answer = []

    rank = {player : i for i, player in enumerate(players)} # 딕셔너리에 enumerate를 이용해 랭킹과 플레이어를 추가 가능.

    for i in callings:
        idx = rank[i]

        players[idx], players[idx - 1] = players[idx - 1], players[idx]

        rank[players[idx]] = idx
        rank[players[idx-1]] = idx - 1
        
    for i in players:
        answer.append(i)        

    return answer

print(solution(players,callings))

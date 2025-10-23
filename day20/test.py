"""
Version: 1.0
Author: 李小婕
Description: 
1.SPADE, HEART, CLUB, DIAMOND定义四个枚举常量，分别对应黑桃、红心、梅花、方块，值分别为0,1,2,3
2.定义花色对应的Unicode符号♠♥♣♦
3.定义点数对应的文字：'', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'

Keyword arguments:
argument -- description
Return: return_description
"""

from enum import Enum
import random

class Suites(Enum):
    # 花色枚举
    SPADE, HEART, CLUB, DIAMOND = range(4)


class Card:
    """牌"""
    # 初始化扑克牌
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face
    
    # 初始化花色和点数
    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'
    
    # 定义牌的排序规则：先按花色，再按点数
    def __lt__(self, other):
        if self.suite.value != other.suite.value:
            return self.suite.value < other.suite.value
        return self.face < other.face


class Poker:
    """扑克牌组"""
    def __init__(self):
        self.cards = []
        self.reset()
    
    def reset(self):
        """重置牌组"""
        self.cards = []
        for suite in Suites: # 扑克牌花色
            for face in range(1, 14):  # 扑克牌点数： A ~ K
                self.cards.append(Card(suite, face))

    def shuffle(self):
        # 洗牌
        random.shuffle(self.cards)
        
    # 发牌给玩家
    def deal(self, num_players = 4, cards_per_player = 13):
        if len(self.cards) < num_players * cards_per_player:
            raise ValueError("牌不够发!")
        
        players_hands = [[] for _ in range(num_players)] #玩家存放扑克牌位置
        for i in range(cards_per_player):
            for j in range(num_players):
                if self.cards:
                    players_hands[j].append(self.cards.pop())
        return players_hands

class Player:
    def __init__(self,name):
        self.name = name
        self.hand = []
        
    def receive_card(self, cards):
        self.hand.extend(cards)
        self.sort_hand()
        
    def sort_hand(self):
        """按花色和点数排序手牌"""
        self.hand.sort()        
        
    def show_hand(self):
        print(f'{self.name}的手牌: {self.hand}')

# 测试代码
if __name__ == "__main__":
    
    # 创建扑克牌
    poker = Poker()
    print("初始牌组:", poker.cards)
    
    # 洗牌
    poker.shuffle()
    print('洗牌后:', poker.cards)
    
    # 创建玩家
    players = [Player(f"玩家{i+1}") for i in range(4)]
    # print(f"玩家: {[p.name for p in players]}")
    
    # 发牌
    players_hands = poker.deal()
    for i, hand in enumerate(players_hands):
        players[i].receive_card(hand)
        print(players[i].name, hand)

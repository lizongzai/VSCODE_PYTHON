from enum import Enum
import random

class Suite(Enum):
    """花色(枚举)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)

class Card:
    """牌"""
    
    # 初始化花色和点数
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face
    
    # 定义花色符合号和点数文字
    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'

    def __lt__(self, other):
        """定义牌的排序规则：先按花色，再按点数"""
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
        for suite in Suite:
            for face in range(1, 14):  # A~K
                self.cards.append(Card(suite, face))
    
    def shuffle(self):
        """洗牌"""
        random.shuffle(self.cards)
    
    def deal(self, num_players=4, cards_per_player=13):
        """发牌给玩家"""
        if len(self.cards) < num_players * cards_per_player:
            raise ValueError("牌不够发")
        
        # 根据玩家数量，为每个玩家创建一个空的手牌列表
        players_hands = [[] for _ in range(num_players)]
        
        # 52张牌，分13轮发牌，每轮每次发4张不同牌给不同四个玩家。之至发完所有52张牌。
        for i in range(cards_per_player):
            for j in range(num_players):
                if self.cards:
                    players_hands[j].append(self.cards.pop())
        
        return players_hands

class Player:
    """玩家"""
    
    def __init__(self, name):
        self.name = name
        self.hand = []  # 手牌
    
    def receive_cards(self, cards):
        """接收牌"""
        self.hand.extend(cards)
        self.sort_hand()
    
    def sort_hand(self):
        """按花色和点数排序手牌"""
        self.hand.sort()
    
    def show_hand(self):
        """显示手牌"""
        print(f"{self.name}的手牌: {self.hand}")

# 测试代码
if __name__ == "__main__":
    # 创建扑克牌
    poker = Poker()
    print("初始牌组:", poker.cards)
    
    # 洗牌
    poker.shuffle()
    print("\n洗牌后:", poker.cards[:10], "...")  # 只显示前10张
    
    # 创建玩家
    players = [Player(f"玩家{i+1}") for i in range(4)]
    
    # 发牌
    players_hands = poker.deal()
    for i, hand in enumerate(players_hands):
        players[i].receive_cards(hand)
    
    # 显示每个玩家的手牌
    print("\n发牌结果:")
    for player in players:
        player.show_hand()
    
    # 测试单张牌
    print("\n测试单张牌:")
    card1 = Card(Suite.SPADE, 5)
    card2 = Card(Suite.HEART, 13)
    print(card1)  # ♠5 
    print(card2)  # ♥K
    
    # 测试枚举
    print("\n测试花色枚举:")
    for suite in Suite:
        print(f'{suite}: {suite.value}')
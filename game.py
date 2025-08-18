import random
import time

# === КОНСТАНТЫ ===
SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['9', '10', 'J', 'Q', 'K', 'A']
WIN_COMBO = ['Q', 'K', 'A']

CARD_STRENGTH = {
    '9': 1,
    '10': 2,
    'J': 3,
    'Q': 4,
    'K': 5,
    'A': 6,
}

# === КЛАСС КАРТЫ ===
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def beats(self, other):
        # 9 бьёт туза
        if self.rank == '9' and other.rank == 'A':
            return True
        if self.rank == 'A' and other.rank == '9':
            return False
        return CARD_STRENGTH[self.rank] > CARD_STRENGTH[other.rank]

# === КЛАСС ИГРОКА ===
class Player:
    def __init__(self, name, is_bot=False):
        self.name = name
        self.hand = []
        self.deck = []
        self.is_bot = is_bot

    def draw_to_three(self):
        while len(self.hand) < 3 and self.deck:
            self.hand.append(self.deck.pop(0))

    def has_winning_combo(self):
        ranks = [card.rank for card in self.hand]
        suits = [card.suit for card in self.hand]
        for suit in SUITS:
            if ranks.count('Q') >= 1 and ranks.count('K') >= 1 and ranks.count('A') >= 1:
                if any(c.rank == 'Q' and c.suit == suit for c in self.hand) and \
                   any(c.rank == 'K' and c.suit == suit for c in self.hand) and \
                   any(c.rank == 'A' and c.suit == suit for c in self.hand):
                    return True
        return False

    def play_card(self, opponent_card=None):
        if self.is_bot:
            # Бот выбирает карту стратегически
            qka = [c for c in self.hand if c.rank in WIN_COMBO]
            if len(qka) == 3 and len(set(c.suit for c in qka)) == 1:
                return self._remove_card(qka[0])

            # Против сильной карты — используем девятку
            if opponent_card and opponent_card.rank == 'A':
                for card in self.hand:
                    if card.rank == '9':
                        return self._remove_card(card)

            # Иначе — карта с наибольшим шансом победы
            best_card = max(self.hand, key=lambda c: CARD_STRENGTH[c.rank])
            return self._remove_card(best_card)
        else:
            # Человек выбирает по номеру карты
            print(f"Твои карты:")
            for idx, card in enumerate(self.hand):
                print(f"{idx + 1}. {card}")

            while True:
                choice = input("Выбери номер карты: ")
                if choice.isdigit():
                    choice = int(choice)
                    if 1 <= choice <= len(self.hand):
                        return self._remove_card(self.hand[choice - 1])
                print("Неверный выбор. Попробуй снова.")

    def _remove_card(self, card):
        self.hand.remove(card)
        return card

# === КЛАСС ИГРЫ ===
class Game:
    def __init__(self):
        self.deck = self._create_deck()
        random.shuffle(self.deck)
        self.player = Player("Игрок")
        self.bot = Player("Бот", is_bot=True)
        self.round = 1
        self.current_starter = self.player  # Кто ходит первым
        self.stake = []  # Карты в ничьей

        self._deal_cards()

    def _create_deck(self):
        return [Card(rank, suit) for rank in RANKS for suit in SUITS]

    def _deal_cards(self):
        for i in range(3):
            self.player.hand.append(self.deck.pop())
            self.bot.hand.append(self.deck.pop())
        self.player.deck = [self.deck.pop() for _ in range(9)]
        self.bot.deck = [self.deck.pop() for _ in range(9)]

    def _check_winner_combo(self):
        if self.player.has_winning_combo():
            print("\nИгрок собрал QKA одной масти и выиграл игру!")
            return self.player
        if self.bot.has_winning_combo():
            print("\nБот собрал QKA одной масти и выиграл игру!")
            return self.bot
        return None

    def handle_special_cards(self, card1, card2, winner):
        # Эффект десятки
        if card1.rank == '10' and winner == self.player:
            print(f"-> Игрок проиграл с десяткой, он берет две карты.")
            self.player.draw_to_three()

        if card2.rank == '10' and winner == self.bot:
            print(f"-> Бот проиграл с десяткой, он берет две карты.")
            self.bot.draw_to_three()

        # Эффект вальта
        if card1.rank == 'J' and winner == self.player:
            print(f"-> Игрок проиграл с вальтом, он видит следующую карту.")
            print(f"-> Следующая карта у Игрока: {self.player.deck[0]}")

        if card2.rank == 'J' and winner == self.bot:
            print(f"-> Бот проиграл с вальтом, он видит следующую карту.")
            print(f"-> Следующая карта у Бота: {self.bot.deck[0]}")

    def play_round(self):
        print(f"\n=== Раунд {self.round} ===")
        self.player.draw_to_three()
        self.bot.draw_to_three()

        starter = self.current_starter
        follower = self.bot if starter == self.player else self.player

        card1 = starter.play_card()
        print(f"{starter.name} сыграл {card1}")
        time.sleep(0.5)

        card2 = follower.play_card(opponent_card=card1)
        print(f"{follower.name} ответил {card2}")
        time.sleep(0.5)

        all_cards = self.stake + [card1, card2]

        if card1.rank == card2.rank:
            print("-> Ничья! Эти карты остаются на кону.")
            self.stake = all_cards
            # Раунд повторяется, порядок не меняется
        else:
            if card1.beats(card2):
                winner = starter
            else:
                winner = follower
            print(f"-> {winner.name} выигрывает раунд и забирает карты: {[str(c) for c in all_cards]}")
            winner.deck.extend(all_cards)
            self.stake = []
            self.round += 1
            self.current_starter = follower if self.current_starter == self.player else self.player

            self.handle_special_cards(card1, card2, winner)

        winner = self._check_winner_combo()
        if winner:
            exit()

        if not self.player.hand and not self.player.deck:
            print("\nБот забрал все карты. Победа бота!")
            exit()
        if not self.bot.hand and not self.bot.deck:
            print("\nИгрок забрал все карты. Победа игрока!")
            exit()

# === ЗАПУСК ===
game = Game()
while True:
    game.play_round()
    input("Нажми Enter для следующего раунда...\n")

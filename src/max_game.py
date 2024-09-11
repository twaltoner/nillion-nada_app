from nada_dsl import *

def nada_main():
    party_alice = Party(name="Alice")
    party_bob = Party(name="Bob")
    party_charlie = Party(name="Charlie")
    party_john = Party(name="John")

    num_1 = SecretInteger(Input(name="num_1", party=party_alice))
    num_2 = SecretInteger(Input(name="num_2", party=party_bob))
    num_3 = SecretInteger(Input(name="num_2", party=party_charlie))
    
    # Generate a secret integer with the random value in the range of 0 to max
    max = 10000
    random_int = SecretInteger.random() % Integer(max+1)
    # 0 - tie
    # 1 - num1 - wins
    # 2 - num2 - wins
    # 3 - num3 - wins
    condition1 = num1 > random_int
    conditional_product1 = condition1.if_else(Integer(0), Integer(1))
    condition2 = num2 > random_int
    conditional_product2 = condition2.if_else(Integer(0), Integer(1))
    condition3 = num3 > random_int
    conditional_product3 = condition3.if_else(Integer(0), Integer(1))

    winner = (conditional_product1 == Integer(1)).if_else((num_1 > num_2).if_else((num_1 > num_3).if_else(Integer(1),Integer(0)), Integer(0))), Integer(0))
    winner = (conditional_product2 == Integer(1)).if_else((num_2 > num_1).if_else((num_1 > num_3).if_else(Integer(2),Integer(0)), Integer(0))), Integer(0))
    winner = (conditional_product3 == Integer(1)).if_else((num_3 > num_1).if_else((num_1 > num_2).if_else(Integer(3),Integer(0)), Integer(0))), Integer(0))


    winner = ((result > Integer(0)).if_else((result > Integer(1)).if_else(Integer(2), Integer(1)),Integer(0)))
  


    out = Output(winner, "winning_player_number", party_john)

    return [out]

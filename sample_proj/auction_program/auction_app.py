import pprint
import os


logo = (r'''
                                      ,
                                   ,nNN
                                ,nNNNN'
                             ,nNNNNNN;
                            ;NNNNNNNN
                           ;NNNNNNNN'
                          ;NNNNNNNN;
                         .NNNNNNNNN
                         NNNNNNNNNb.
                        ;NNNNNNNNNNNNn.
                       ,NNNNNNNNNNNNNNNNn.
                      ;NNNNNNNNN' ""YNNNNNNn.
                      NNNNNNNNN;      ""YNNNNNNn.
                      ""YNNNNNN           ""YNNNNNNn.
                          ""YN'               ""YNNNNNNn.
            /\                                    ""YNNNNNNn.
        .nNNNNNb. _______                             ""YNNNNNNn.
       dN(o)NNNNNNNNN"NNNNNNb.                            ""YNNNNNNn.
     dNNNNNNNNNNNNNP" ""NNNNNNb _                             ""cgmmP
     YNNNN"NNNNNNNN N NNNNNNNNN( )                                ""
       ""'dNNNNNNNNb. "YNNNNNNN_X_
        "YNNNNNNNNNNN N NNNNNNN
            YNNNNNN.. .dNNNNNNP
             "YNNNNNN.NNNNNNP"
                NN """"" NN
                nn       nn

''')
auction = {}

finish = False
max_bid_val = -1
max_bid_key = ''


def collect_bids():
    global finish, max_bid_val, max_bid_key

    while not finish:
        os.system('clear')
        name = input('What is your name ?\n')
        bid_val = int(input('What is your bid ?$\n'))

        if max_bid_val < bid_val:
            max_bid_val = bid_val
            max_bid_key = name

        auction.update({name : bid_val})

        game_over = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
        if game_over == 'no':
            finish = True


def calculate_max_bid():
    max_val = max(auction.items())

    return max_val


print(logo)

collect_bids()
pprint.pprint(auction)
print(f'1 - The max bid was ${max_bid_val} made by {max_bid_key}')

max_val = calculate_max_bid()
print(f'2 - The max bid was ${max_val[1]} made by {max_val[0]}')

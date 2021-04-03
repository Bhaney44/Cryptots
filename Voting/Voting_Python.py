#Copyright Cryptots 2021

#Voting Mechanism
#Pull block
def pull_block():
    print("Block")
pull_block()

#Stake rewards and vote
stake_validation = float(input("Stake:"))
stake_vote = float(input("Vote 0 for no, 1 for yes:"))

#State Transition
#Total stake
##Sum all staked tokens for block
total_stake = float(input("Total Stake:"))

#Total votes
#Sum all votes
total_votes = float(input("Total Votes:"))

#Total points
#Sum all yes votes for block
total_points = float(input("Sum Yes Votes:"))

#Consensus
#More than 50.0% yes votes
consensus = float(total_points/total_votes)

#Calculate Stake
stake_percentage = float(stake_validation/total_stake)

#Return Reward

if consensus > 0.5:
    def reward():
        print("reward")
    reward()
else:
    def new_vote():
        print("new vote")
    new_vote()
        



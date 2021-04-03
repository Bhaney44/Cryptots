#Stateful Smart Contract in PyTeal
#Copyright Cryptots 2021
#MIT Bitcoin Expo

#Import
import pyteal

#Write to state
program = App.globalPut(Bytes("Mykey"), Int(50))

#Store value in local storage
program = App.localPut(Int(0), Bytes("MyLocalKey"), Int(50))

#Read from state
program = App.globalGet(Bytes("MyGlobalKey"))

#Locate sender
program = App.localGet(Int(0), Bytes("MyLocalKey"))

#Example
get_amount_given = App.localGetEx(Int(0), Txn.application_id(), Bytes("MyAmountGiven"))
new_giver_logic = Seq([Return(Int(1))])
previous_giver_logic = Seq([Return(Int(1))]) 
program = Seq([get_amount_given, If(get_amount_given.hasValue(), previous_giver_logic, new_giver_logic)])

#Transaction Type
program = OnComplete.NoOp == Txn.on_completion()

#Call stateful stateful smart contract
is_my_parm = Seq([Return(Int(1))])
is_not_my_parm = Seq([Return(Int(1))])
program = If(Bytes("myparm") == Txn.application_args[0], is_my_parm, is_not_my_parm)

#Asset Balance
asset_balance = AssetHolding.balance(Int(0), Int(2))
program = Seq([asset_balance, If(asset_balance.hasValue(), Return(Int(1)), Return(Int(0)))])

#Opt in using global storage
program = Global.latest_timestamp() >= App.globalGet(Bytes("StartDate"))

#Boilerplate contract
from pyteal import *
def approval_system():
    handle_noop = Seq([Return(Int(1))])
    handle_optin = Seq([Return(Int(1))])
    handle_closeout = Seq([Return(Int(1))])
    handle_updateapp = Err()
    handle_deleteapp = Err()
    program = Cond(
        [Txn.on_completion() == OnComplete.NoOp, handle_noop],
        [Txn.on_completion() == OnComplete.OptIn, handle_optin],
        [Txn.on_completion() == OnComplete.CloseOut, handle_closeout],
        [Txn.on_completion() == OnComplete.UpdateApplication, handle_updateapp],
        [Txn.on_completion() == OnComplete.DeleteApplication, handle_deleteapp]
    )
    return program
## Open file to write boilerplate contract
with open('boilerplate_approval_pyteal.teal', 'w') as f:
    compiled = compileTeal(approval_program(), Mode.Application)
    f.write(compiled)



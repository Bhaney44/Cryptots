from pyteal import *
"""Escrow Account for Interest Payment and Par Value Payment"""

def EscrowAccount(mgr_add, interest_id, par_id, accepted_payment, closure, par, coupon,
                  holdup_period, begin_round, end_round, total_payment,
                  period, span):
    max_fee = Int(1000)
    lease = Bytes("base64", "NPWoaHaDbyyovXHAHoc5AnKskQwfmTm4YK+psfQutvM=")

    # for EscrowAccount to receive payments in opt-in interest token
    # arg_id = 0
    optInInterest = And(
        Txn.sender() == Txn.asset_receiver(),
        Txn.type_enum() == TxnType.AssetTransfer,
        Txn.xfer_asset() == Int(interest_id),
        Txn.asset_amount() == Int(0),
        Txn.rekey_to() == Global.zero_address(),
        Txn.asset_close_to() == Global.zero_address(),
        Txn.fee() <= max_fee
    )

    # for EscrowAccount to receive payments in opt-in par-value token
    # arg_id = 1
    optInPar = And(
        Txn.sender() == Txn.asset_receiver(),
        Txn.type_enum() == TxnType.AssetTransfer,
        Txn.xfer_asset() == Int(par_id),
        Txn.asset_amount() == Int(0),
        Txn.rekey_to() == Global.zero_address(),
        Txn.asset_close_to() == Global.zero_address(),
        Txn.fee() <= max_fee
    )

    # escrow account receives payment_id as payment
    # arg_id = 2
    optInPayment = And(
        Txn.sender() == Txn.asset_receiver(),
        Txn.type_enum() == TxnType.AssetTransfer,
        Txn.xfer_asset() == Int(accepted_payment),
        Txn.asset_amount() == Int(0),
        Txn.rekey_to() == Global.zero_address(),
        Txn.asset_close_to() == Global.zero_address(),
        Txn.fee() <= max_fee
    )

    # arg_id = 3
    claim = And(
        Txn.receiver() == Addr(mgr_add),
        Txn.type_enum() == TxnType.AssetTransfer,
        Txn.xfer_asset() == Int(accepted_payment),
        Txn.first_valid() > Int(holdup_period),
        Txn.rekey_to() == Global.zero_address(),
        Txn.asset_close_to() == Global.zero_address(),
        Txn.fee() <= max_fee
    )

    # user purchases token from escrow
    # arg_id = 4
    purchase =  And(
        Global.group_size() == Int(3),
        Gtxn[0].type_enum() == TxnType.AssetTransfer,
        Gtxn[0].xfer_asset() == Int(accepted_payment),
        Gtxn[0].asset_amount() % Int(par) == Int(0),
        Gtxn[0].first_valid() < Int(closure),
        Gtxn[1].type_enum() == TxnType.AssetTransfer,
        Gtxn[1].xfer_asset() == Int(par_id),
        Gtxn[1].asset_amount() == Gtxn[0].asset_amount() / Int(par),
        Gtxn[1].asset_receiver() == Gtxn[0].sender(),
        Gtxn[1].rekey_to() == Global.zero_address(),
        Gtxn[1].asset_close_to() == Global.zero_address(),
        Gtxn[1].fee() <= max_fee,
        Gtxn[2].type_enum() == TxnType.AssetTransfer,
        Gtxn[2].xfer_asset() == Int(interest_id),
        Gtxn[2].asset_amount() == Gtxn[1].asset_amount() * Int(total_payment),
        Gtxn[2].asset_receiver() == Gtxn[0].sender(),
        Gtxn[2].rekey_to() == Global.zero_address(),
        Gtxn[2].asset_close_to() == Global.zero_address(),
        Gtxn[2].fee() <= max_fee
    )

    # user receives interest from escrow
    # arg_id = 5
    interestPayment =  And(
        Global.group_size() == Int(3),
        Gtxn[0].type_enum() == TxnType.AssetTransfer,
        Gtxn[0].xfer_asset() == Int(interest_id),
        Gtxn[1].type_enum() == TxnType.AssetTransfer,
        Gtxn[1].sender() == Gtxn[0].sender(),
        Gtxn[1].asset_receiver() == Gtxn[0].sender(),
        Gtxn[1].xfer_asset() == Int(par_id),
        Gtxn[1].asset_amount() == Gtxn[0].asset_amount(),
        Gtxn[2].type_enum() == TxnType.AssetTransfer,
        Gtxn[2].xfer_asset() == Int(accepted_payment),
        Gtxn[2].asset_receiver() == Gtxn[0].sender(),
        Gtxn[2].first_valid() >= Int(begin_round),
        Gtxn[2].first_valid() % Int(period) == Int(0),
        Gtxn[2].last_valid() == Gtxn[1].first_valid() + Int(span),
        Gtxn[2].asset_amount() == Gtxn[0].asset_amount() * Int(coupon),
        Gtxn[2].lease() == lease,
        Gtxn[2].rekey_to() == Global.zero_address(),
        Gtxn[2].asset_close_to() == Global.zero_address(),
        Gtxn[2].fee() <= max_fee
    )

    # user receives par value from escrow
    # arg_id = 6
    parPayment = And(
        Global.group_size() == Int(2),
        Gtxn[0].type_enum() == TxnType.AssetTransfer,
        Gtxn[0].xfer_asset() == Int(par_id),
        Gtxn[1].type_enum() == TxnType.AssetTransfer,
        Gtxn[1].first_valid() > Int(end_round),
        Gtxn[1].asset_receiver() == Gtxn[0].sender(),
        Gtxn[1].xfer_asset() == Int(accepted_payment),
        Gtxn[1].asset_amount() == Gtxn[0].asset_amount() * Int(par),
        Gtxn[1].rekey_to() == Global.zero_address(),
        Gtxn[1].asset_close_to() == Global.zero_address(),
        Gtxn[1].fee() <= max_fee
    )


    program = Cond(
        [Btoi(Arg(0)) == Int(0), optInInterest],
        [Btoi(Arg(0)) == Int(1), optInPar],
        [Btoi(Arg(0)) == Int(2), optInPayment],
        [Btoi(Arg(0)) == Int(3), claim],
        [Btoi(Arg(0)) == Int(4), purchase],
        [Btoi(Arg(0)) == Int(5), interestPayment],
        [Btoi(Arg(0)) == Int(6), parPayment],
    )

    return program

def compile(mgr_add, interest_id, par_id, accepted_payment, closure, par, coupon, holdup_period, begin_round, end_round, total_payment, period, span, name):
    program = EscrowAccount(mgr_add, interest_id, par_id, accepted_payment, closure, par, coupon, holdup_period, begin_round, end_round, total_payment, period, span)
    with open("./teal/" + name + ".teal", "w") as f:
        compiled = compileTeal(program, Mode.Signature)
        f.write(compiled)

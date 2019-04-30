
class ContractMeta:

    language_code_byte_length = 4
    language_version_byte_length = 4

    init_para = ["max", "unity", "tokenDescription", "signer"]
    supersede_para = ["newIssuer", "maker"]
    issue_para = ["amount", "issuer"]
    destroy_para = ["amount", "issuer"]
    split_para = ["newUnity", "issuer"]
    send_para = ["recipient", "amount", "caller"]
    transfer_para = ["sender", "recipient", "amount"]
    deposit_para = ["sender", "smart", "amount"]
    withdraw_para = ["smart", "recipient", "amount"]
    total_supply_para = ["total"]
    max_supply_para = ["max"]
    balance_of_para = ["address", "balance"]
    get_issuer_para = ["issuer"]

    state_var_issuer = bytes([0])
    state_var_maker = bytes([1])

    public_key = bytes([1])
    address = bytes([2])
    amount = bytes([3])
    int32 = bytes([4])
    short_text = bytes([5])
    contract_account = bytes([6])
    account = bytes([7])

    gteq_zero_assert = bytes([1])
    lteq_assert = bytes([2])
    lt_int64_assert = bytes([3])
    gt_zero_assert = bytes([4])
    eq_assert =bytes([5])
    is_caller_origin_assert = bytes([6])
    is_signer_origin_assert = bytes([7])

    set_cdbv = bytes([1])

    get_cdbvr = bytes([1])

    signer_load = bytes([1])
    caller_load =bytes([2])

    assert_opc = bytes([1])
    load_opc = bytes([2])
    cdbv_opc = bytes([3])
    cdbvr_opc = bytes([4])
    tdb_opc = bytes([5])
    tdbr_opc = bytes([6])
    tdba_opc = bytes([7])
    tdbar_opc = bytes([8])
    return_opc = bytes([9])

    deposit_tdba = bytes([1])
    withdraw_tdba = bytes([2])
    transfer_tdba = bytes([3])

    balance_tdbar = bytes([1])

    new_token_tdb = bytes([1])
    split_tdb = bytes([2])

    get_tdbr = bytes([1])
    total_tdbr = bytes([2])

    init = 0
    supersede = 0
    issue = 1
    destroy = 2
    split = 3
    send = 4
    transfer = 5
    deposit = 6
    withdraw = 7
    total_supply = 8
    max_supply = 9
    balance_of = 10
    get_issuer = 11

    supersede_without_split = 0
    issue_without_split = 1
    destroy_without_split = 2
    send_without_split = 3
    transfer_without_split = 4
    deposit_without_split = 5
    withdraw_without_split = 6
    total_supply_without_split = 7
    max_supply_without_split = 8
    balance_of_without_split = 9
    get_issuer_without_split = 10

    supersede_index = bytes([0])
    issue_index = bytes([1])
    destroy_index = bytes([2])
    split_index = bytes([3])
    send_index = bytes([4])
    transfer_index = bytes([5])
    deposit_index = bytes([6])
    withdraw_index = bytes([7])
    total_supply_index = bytes([8])
    max_supply_index = bytes([9])
    balance_of_index = bytes([10])
    get_issuer_index = bytes([11])

    non_return_type = bytes('',encoding ='utf-8')
    on_init_trigger_type = 0
    public_func_type = 0

    init_input_max_index = bytes([0])
    init_input_unity_index = bytes([1])
    init_input_short_text_index = bytes([2])
    init_input_issuer_load_index = bytes([3])

    supersede_input_new_issuer_index = bytes([0])
    supersede_input_maker = bytes([1])

    split_input_new_unity_index = bytes([0])
    split_input_issuer_get_index = bytes([1])

    destroy_input_destroy_amount_index = bytes([0])
    destroy_input_issuer_get_index = bytes([1])

    issue_input_amount_index = bytes([0])
    issue_input_issuer_get_index = bytes([1])

    send_input_recipient_index = bytes([0])
    send_input_amount_index = bytes([1])
    send_input_sender_index = bytes([2])

    transfer_input_sender_index = bytes([0])
    transfer_input_recipient_index = bytes([1])
    transfer_input_amount_index = bytes([2])

    deposit_input_sender_index = bytes([0])
    deposit_input_smart_contract_index = bytes([1])
    deposit_input_amount_index = bytes([2])

    withdraw_input_smart_contract_index = bytes([0])
    withdraw_input_recipient_index = bytes([1])
    withdraw_input_amount_index = bytes([2])

    balance_of_input_account_index = bytes([0])
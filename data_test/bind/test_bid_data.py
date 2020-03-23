failed_bid = [
                {'amount': 10, 'expect': '投标金额必须为100的倍数'},
                {'amount': 100000000000000, 'expect': '投标金额大于可用金额'}
             ]

succeed_bid = {'amount': 100}